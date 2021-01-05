#!/bin/env python3
from vending_machine import VendingMachine

"""
Challenge is as follows.
1) Print all items in the vending machine.
2) Write a menu where the person is able to select an item to purchase.
3) If the user enters the location "off" turn the machine off and call the "turn_off" method of the vending machine. 
	3a) This method should print the number of items left in the vending machine along with the amount of money the machine made. This should then break the loop.
4) Let the user select an item to purchase, and call the proper method of the vending machine.
5) Add your own items to the vending machine(setting all proper parameters). 
	5a) This should be at least 2 items.
6) If the person is able to purchase the item print out the string "You have purchase ITEM." and say they received CHANGE as change.
	6a) The change string should be printed if the change string isn't empty and the result was True.
7) Actually reduce the quanity of each item after someone purchases a single one.
BONUSES
1) Make it so that the screen is cleared between each printing of the menu.


"""

def main():
	machine = VendingMachine
	pass


if __name__ == "__main__":
	main()