import sys, os, time
import concurrent.futures
import socket, ipaddress
import scapy.all as scapy
from argparse import ArgumentParser

class CustomParser(ArgumentParser):
	def print_help(self,file=None):
		super().print_help(file)
		if file is sys.stderr:
			sys.exit(2)
		else:
			sys.exit(0)
	def error(self,message):
		sys.stderr.write(f"error: {message}\n\n")
		self.print_help(sys.stderr)

#must be root for any scapy related items.
def find_hosts(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast_ether = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
	answered, unanswered = scapy.srp(broadcast_ether/arp_request,timeout=1,verbose=False)
	live_hosts = []
	live_ips = []
	for response in answered:
		live_hosts.append((response[1].psrc, response[1].src))
		live_ips.append(response[1].src)

	return live_ips

def scan_port(opts):
	dst_ip, port, timeout = opts
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.settimeout(timeout)
	res = sock.connect_ex((dst_ip, port))
	if res == 0:
		return port, True
	else:
		return port, False

def scan_futures(ip_ports,threat_level):
	results = {}
	# We do 2x the number of CPUs that are reported to us multiplied by the threat level.
	# Ex. TL4 on a 6 core system. 6 * (2 << 4) => 6 * 32 => 224 worker threads.
	workers = os.cpu_count()* (2 << threat_level)
	with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
		future_to_opts = {executor.submit(scan_port, opt): opt[0] for opt in ip_ports}
		for future in concurrent.futures.as_completed(future_to_opts):
			future_res = future.result()
			if results.get(future_to_opts[future], False):
				if future_res[1] is True:
					results[future_to_opts[future]].append(future_res[0])
			else:
				results[future_to_opts[future]] = [future_res[0]]

		return results

def start_fast_scan(dst_ips):
	try:
		live_ips = find_hosts(dst_ips)
	except PermissionError:
		print("Make sure it's being run with elevated privileges.")

	return live_ips

def main():
	import regex
	parser = CustomParser(description="""
Network Scanner that lets you either map the network or do port scanning. Root/System is required to do stealth scans. Only required argument is the ip-address to scan.
Example: ./pyscanner.py "192.168.1.1"
""")
	parser.add_argument("-p",
	                    metavar="{PORT(S)}|-",
	                    type=str,
	                    help="A port or ports we should scan. '-' means all ports. Single or range e.g. 1-80, or 80.",
	                    required=False,
	                    default="1-1024")
	parser.add_argument("-T",
	                    metavar="{THREAT_LEVEL}",
	                    type=int,
	                    choices=[1,2,3,4],
	                    help="The threat level from 1-4. Higher increases the number of threads we make and also how fast we scan.",
	                    required=False,
	                    default=1,
	                    )
	parser.add_argument("-s", metavar="{SCAN_TYPE}",
	                    type=str,
	                    default="",
	                    required=False,
	                    help="Scan type: U(UDP), S(Stealth), T(TCP). Stealth scan requires root/Admin privileges. Can be combined. Ex: -sTU")

	if len(sys.argv) == 1:
		parser.print_help(sys.stderr)
	else:
		options, extra = parser.parse_known_args()
		if len(extra) == 0:
			if "h" in options:
				parser.print_help(sys.stdout)
			else:
				parser.print_help(sys.stderr)
		else:
			if regex.match("[0-9]{1,3}\-[0-9]{1,3}",options.p):
				start, end = map(int, options.p.split('-'))
			elif options.p[0] == "-":
				start, end = 0, 1024
			else:
				print(f"Option {options.p} was not a valid option.")
				parser.print_help(sys.stderr)
			if len(options.s) <= 3:
				if "S" in options.s:
					stealth_scan = True
				if "T" in options.s:
					tcp_scan = True
				if "U" in options.s:
					udp_scan = True
			else:
				print(f"{options.s} was too large.")
				parser.print_help(sys.stderr)
			threat_level = options.T

	dst_ip_addr = extra[0]
	#match an IP address in CIDR notation or normal
	if not regex.match("^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}(\/[0-9]{1,2})?$", dst_ip_addr):
		print("Not a valid IP Address. Only non-numbered arguments must be the IP Address to scan!")
		parser.print_help(sys.stderr)
		sys.exit(1)

	dst_ports = range(start,end)

	current_os = sys.platform
	if current_os == "Windows":
		print("Dont' know if this'll work or not but let's find out.")
		uid = 0  # just assume it works on windows I guess.
	else:
		uid = os.geteuid()

	if uid != 0:
		try:
			to_scan_ips = [str(ip) for ip in ipaddress.ip_network(dst_ip_addr)]
		except ValueError:
			print("Host bits set! Make sure you're giving a correct network address.\n")
			parser.print_help(sys.stderr)
	else:
		to_scan_ips = start_fast_scan(dst_ip_addr)

	opts = []
	if '/' in dst_ip_addr:
		to_scan_ips = to_scan_ips[1:-1]

	#default timeout is between 0.25-2s.
	timeout = 2 / ( 1 << (threat_level -1 ))

	#only get the usuable ip-addresses
	for dst_ip in to_scan_ips:
		for port in dst_ports:
			opts.append( (dst_ip, port, timeout))

	start = time.time()
	res = scan_futures(opts,threat_level)
	print(res)
	end = time.time()
	print('futures time', str(end-start))


if __name__ == "__main__":
	main()



