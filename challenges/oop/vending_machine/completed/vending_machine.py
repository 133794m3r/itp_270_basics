from typing import Tuple
"""
Vending Machine Module

This python file includes the vending machine class, and also the Item class along with utility functions.
"""

def get_money(prefix=''):
	while True:
		try:
			res = round(float(input(prefix))*100)/100
			break
		except ValueError:
			print("Please enter a valid number.")
	return res


def get_change(money:float)-> str:
	"""
	Returns the amount of change the person gets in quarters, dimes, nickels and pennies.

	:param money: The amount of money we need to make change out of.
	:return: A string representing teh amount of money the person gets.
	"""
	change_str = 'Then the machine gave you back: '
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
	if len(result) != 0:
		return change_str+", ".join(result)
	else:
		return ""


class Item:
	_name = ""
	cost = 1

	def __init__(self, name, cost):
		self.name = name
		self.cost = cost

	def get_cost(self, currency:str ="$") ->str:
		"""
		Gets the item's cost and formats it to 2 digits.

		:param currency: The currency symbol to utilize.
		:return: A string showing the price to 2 digits with currency symbol.
		"""
		return "{}{:.02f}".format(currency, self.cost)

	def __str__(self):
		return "{}:{:.02f}".format(self.name, self.cost)


class VendingMachine:
	_CURRENCY = "$"

	_items = {}
	_rows = 3
	_current_letter = 65
	_current_number = 0
	_profit = 0
	def __init__(self,items: list=None,rows=_rows):
		if items is None:
			items = (
		        {'item':Item("Pepsi Can", 0.50),'num':5},
				{'item':Item("Buttered Toast", 0.10),'num':6},
				{'item':Item("10x Fish Sticks", 1.25),'num':7},
		        {'item':Item("3x ABC Gum", 0.03),'num':8},
		        {'item':Item("5x Bananas",0.75),'num':2},
			)
		# This is so that we can have the items listed as "A1", "B3" etc.
		self._rows = rows
		letter = self._current_letter
		number = self._current_number
		for item in items:
			#Get the current letter, and then the number.
			self._items[chr(letter) + str(number)] = {'item':item['item'], 'quantity':item['num']}
			number += 1
			if number > rows:
				number = 0
				letter += 1
		self._current_number = number
		self._current_letter = letter


	def add_item(self,item:dict):
		"""
		Adds an item to the vending machine

		:param item: The item to add.
		:return: Nothing
		"""

		self._items[chr(self._current_letter)+str(self._current_number)] = {'item':item['item'], 'quantity':item['num']}
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


	def select_item(self,location:str) -> Tuple[bool, str]:
		"""
		Selects an item if it exists and returns item description along with result code.

		:param location: The location of the item.
		:return: The result(true or false), and a string message.
		"""

		location = location.upper()
		if self._items.get(location, False):
			slot =self._items[location]
			return True,"\r\nCost:{} Quantity Remaining:{}".format(slot['item'].get_cost(self._CURRENCY),slot['quantity'])
		else:
			return False, "\r\nLocation '{}' doesn't exist.".format(location)


	def purchase_item(self,location:str,amt=None)-> Tuple[bool, str]:
		"""
		This method allows you to purchase an item.

		:param location: The location of the item we want to purchase.
		:param amt: This parameter is _only_ used during testing!
		:return:
		"""

		location = location.upper()
		result_str = ""
		purchase_result = False
		if self._items.get(location, False):
			slot = self._items[location]
			if slot['quantity'] > 0:
				item_cost = slot['item'].cost
				if amt is None:
					print('Please insert at least {}'.format(slot['item'].get_cost(self._CURRENCY)))
					money = get_money(self._CURRENCY)
				else:
					money = round(amt*100)/100
				if money >= item_cost:
					money -= item_cost
					self._profit += item_cost
					result_str = "You purchased {}. ".format(slot['item'].name)+ get_change(money)
					purchase_result = True
					#decreased the number of items by 1.
					self._items[location]['quantity'] -= 1
				elif money == 0:
					result_str = "You didn't even input a single penny!"
					purchase_result = False
				else:
					result_str = "You didn't insert enough money! " + get_change(money)
					purchase_result = False
				return purchase_result, "\r\n"+result_str

			else:
				return False, "\r\nItem '{}' is not in stock anymore.".format(slot['item'].name)
		else:
			return False, "\r\nAn item doesn't exist at location {}".format(location)


	def shut_off(self) -> Tuple[str,str]:
		"""
		Shut off method.

		:return: The two strings that we're going to print out.
		"""

		quantity_str = ''
		for i,location_entry in enumerate(self._items.items()):
			slot = location_entry[1]
			location = location_entry[0]
			if i % self._rows == 0 and i >= self._rows:
				quantity_str += "\r\n"
			quantity_str += "{}:{} has {} remaining\t".format(location, slot['item'].name, slot['quantity'])


		profit_str = f"The machine made {self._CURRENCY}{self._profit}"
		return quantity_str, profit_str


	def list_items(self) -> str:
		"""
		Returns a string containing all items from the machine.

		:return: A string containing all items formatted in a known way.
		"""

		current_str = ''
		for i,location_entry in enumerate(self._items.items()):
			slot = location_entry[1]
			location = location_entry[0]
			if i % self._rows == 0 and i >= self._rows:
				current_str+='\r\n'

			current_str += "{}:{:20}\t".format(location,slot['item'].name)
		return current_str




