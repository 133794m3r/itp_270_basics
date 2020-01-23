#!/bin/python3
'''
Full ASCII Shift Cipher
By Macarthur Inbody AGPLv3
'''
"""
get_input
the following function handles getting the user's input string and also the shift we want to use.
Then it returns the result as a tuple. This is to reduce reused/wasted code.
"""
def get_input(operand):
	#ask the user for their input string.
	input_string=input("Enter the string to {}: ".format(operand))
	#ask them for the shift we want to use.
	#here I am doing a loop to give them as many chances as it takes.
	while True:
		#I'm wrapping it in try except so that I can capture the errors.
		try:
			#we try to read their input and cast it to an integer.
			shift=int(input("Enter the shift to use: "))
			shift = shift % 96
			#then we break from the loop.
			break;
		#otherwise it doesn't work and we raise this error.
		except ValueError:
			print("You need to enter a whole number for this to work. Please try again.")
	#OK everything worked let's return the values.
	return (input_string,shift)
	
'''
The encryption function.
This will shift the user's input string by some set of characters in the printable ASCII
character set. It'll also handle bound checking for us for any values. It's faster
to not use modulus but I am here so that I always end up with the difference from the printable set.
'''
def encrypt(input_string,shift):
	#initialize the output string.
	output_string="";
	#same thing with our code point.
	code_point=0;
	'''
	This for loop goes through each character of the string and does all of the code below.
	This will get each character seperately as it's own item. This also works for lists.
	'''
	for char in input_string:
		#we set our codepoint to the ordinal(ASCII) value of that character and the shift value.	
		code_point=ord(char)
		#if it's not the normal printable ASCII we just leave it be.
		if code_point >126 or code_point < 32:
			pass
		else:
			code_point+=shift
			#uh-oh we overflowed from printable characters.
			if code_point > 126:
				#OK so we need to get the distance from printable we need to use to wrap around.
				#Basically it'll return a value between 32 to 126
				code_point = 32 + (code_point - 126);

		#append the value of the character to the output.
		output_string+=chr(code_point)
	#return this string.
	return output_string

"""
Decryption function. This'll decrypt the string and handle wrap-around.
"""
def decrypt(input_string,shift):

	#initialize the output string.
	output_string=""
	#same thing for code point.
	code_point = 0;
	#for each character of the input string.
	for char in input_string:
		code_point=ord(char)
		#if it's not the normal printable ASCII we just leave it be.
		if code_point >126 or code_point < 32:
			pass
		else:	
			#get the code point and subtract the shift from it.
			code_point-=shift
			#if it's less than 32(space character) we have to wrap around.
			if code_point <32:
				'''
				set the code point as 126(maximum ascii value) minus 32(minium) - 
				our current code point. Then subtract that value from 126.
				'''			
				code_point = 126 - ( 32 - code_point)
		#append the current character pointed to by the code point to the output string.
		output_string+=chr(code_point)
	#return the string.
	return output_string
	

def main():
	#print our menu.
	print('''Shift Cipher encoder/decoder.
1) Encrypt
2) Decrypt
''')
	result="";
	#while loop to make sure they give us valid input.
	while True:
		#prompt them for the mode.
		mode=input("Enter selection(1 or 2): ")
		#if it's equal to the string value 1
		if mode == "1":
			#it means we encrypt it and set returned value to result.
			input_string,shift=get_input('encrypt');			
			result=encrypt(input_string,shift)
			#break out of the loop.
			break;
		#otherwise if it's equal to 2 we do this.
		elif mode =="2":
			#same thing but this time with the decryption function.
			input_string,shift=get_input('decrypt');			
			result=decrypt(input_string,shift)
			#same break
			break;
		#otherwise they didn't enter a valid selection.
		else:
			print("Not a valid input. Select 1 or 2.\n")
	#print the result.
	print(result)
	
def full_shift_test_all():
	i=95
	original_text="What Is the Airspeed Velocity of an Unladen Swallow?"
	plain_text=""
	cipher_text=""
	while i>=0:
		cipher_text=encrypt(original_text,i)
		plain_text=decrypt(cipher_text,i)
		if plain_text != original_text:
			#if they're not. We throw this little message.
			print("Key {} : Passed:[ ] Failed:[X]".format(i))		
			'''
			Then we raise an assertion error because our code failed.
			First the format paramters are positional. {0} = first argument, {1} = second etc.
			Then we add it to our string.
			And we make sure that the key string we insert is padded to two characters. This is the new
			and "PEP8" way of doing it. % is the old way.
			'''
			raise AssertionError("Your code's broke with the key:{:>2}. We got back {0} but expected {1} and the cipher text is '{3}'".format(plain_text,original_text,i,cipher_text))
		#otherwise it worked.
		else:
			#same thing here but this time we're formatting it to add a padding character if the number is less than 2 digits.
			#we print that it passed.
			print("\nKey {:>2} : Passed:[X] Failed:[ ]".format(i))
			print("CT:{1} \nPT:{0}\n".format(plain_text,cipher_text))
		i-=1
	print("All tests have passed!")		
	
if __name__ == "__main__":
	full_shift_test_all()
#	main()
