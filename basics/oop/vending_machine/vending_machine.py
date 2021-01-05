class Item:
	_name = ""
	cost = 0
	def __init__(self,name,cost):
		self.name = name
		self.cost = cost
	def get_cost(self,currency):
		return "{}{:.2f}".format(currency, self.cost)
	def __str__(self):
		return "{}:{:.2f}".format(self.name,self.cost)

def get_float(prefix=''):
	while True:
		try:
			res = round(float(input(prefix))*100)/100
			break
		except ValueError:
			print("Please enter a valid number.")
	return res


def get_change(money):
	change_str = 'The machine gave you: '
	# Bonus challenge. Write a greedy algorithm to
	# Give the person the optimal change.
	# If you don't want to do it. Just copy
	# and paste the code from the greedy_change
	# function from bonus.py below here.

	quarters, money = divmod(money, 0.25)
	dimes, money = divmod(money, 0.10)
	nickels, money = divmod(money, 0.05)
	pennies = (money * 100) // 1.0

	result = []
	if quarters != 0:
		result += ["{:.0f} Quarters".format(quarters)]
	if dimes != 0:
		result += ["{:.0f} Dimes".format(dimes)]
	if nickels != 0:
		result += ["{:.0f} Nickels".format(nickels)]
	if pennies != 0:
		result += ["{:.0f} Pennies".format(pennies)]

	return change_str+", ".join(result)


class VendingMachine:
	_CURRENCY = "$"
	_COINS ={
		"quarters": 0.25,
		"dimes":0.10,
		"nickels":0.05,
		"pennies":0.01,
	}
	_items = {}
	_rows = 5
	_current_letter = 65
	_current_number = 1
	_profit = 0
	def __init__(self,items: list=None,rows=5):
		if items is None:
			items = (
		        {'item':Item("Pepsi Can", 0.50),'num':5},
				{'item':Item("Buttered Toast", 0.10),'num':6},
				{'item':Item("10x Fish Sticks", 1.25),'num':7},
		        {'item':Item("3x ABC Gum", 0.03),'num':8},
		        {'item':Item("5x Bananas",0.75),'num':2},
			)
		# This is so that we can have the items listed as "A1", "B3" etc.
		letter = 65
		number = 1
		self._rows = rows
		for item in items:
			#Get the current letter, and then the number.
			self._items[chr(letter) + str(number)] = (item['item'], item['num'])
			number += 1
			if number > rows:
				number = 0
				letter += 1
		self._current_number = number
		self._current_letter = letter

	def add_item(self,item):
		self._items[chr(self._current_letter)+str(self._current_number)] = (item['item'], item['num'])
		if self._current_number + 1 > self._rows:
			self._current_number = 0
			self._current_letter += 1
		else:
			self._current_number += 1

	def get_item(self,location:str) -> Item or False:
		"""
		Gets an item at the specified location.

		:param location: The location of the item.
		:return: The item object at the location. Or False
		"""

		location = location.upper()
		if self._items.get(location, False):
			return self._items[location][0]
		else:
			return False

	def select_item(self,location:str):
		location = location.upper()
		if self._items.get(location, False):
			slot =self._items[location]
			print("{} Quantity Remaining:{}".format(slot[0].get_cost(self._CURRENCY),slot[1]))
		else:
			print("'{}' Doesn't exist.".format(location))

	def purchase_item(self,location:str):
		location = location.upper()
		if self._items.get(location, False):
			slot = self._items[location]
			if slot[1] > 0:
				item_cost = slot[0].cost
				print('Please insert {}'.format(slot[0].get_cost()))
				money = get_float()
				if money > item_cost:
					money -= item_cost
					self._profit += item_cost
				elif money == 0:
					return False, "You didn't even input a single penny!"
				else:
					print("You didn't insert enough money.")
				return True, get_change(money)
			else:
				return False, "Item is not in stock anymore."
		else:
			print("An item doesn't exist at location {}".format(location))
			return False


	def shut_off(self):


		# TODO: Actually do the following
		# 1) Print out the remaining stock.
		# 2) Print out the total money the machine has in it's reserve.

		pass

	def print_items(self):
		current_str = ''
		print(len(self._items.items()))
		for i,location_entry in enumerate(self._items.items()):
			item, _ = location_entry[1]
			location = location_entry[0]
			current_str += "{}:{}\t".format(location,item.name)
			if i % self._rows == 0 and i > self._rows:
				print(current_str)
				current_str = ''

		print(current_str)




