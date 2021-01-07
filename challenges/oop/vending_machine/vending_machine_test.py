from completed.vending_machine import VendingMachine, Item
"""
None of the code below needs to be modified. It is just a test of the class to
make sure that the class wasn't broke when you added your method. As long as
you didn't break something and the main script you wrote worked this should work
too. Only the shut_off method might be different.

What I did was to literally use the same exact code from the list_items method of 
VendingMachine class in the print_items. Then I simply had it return the profit in
the string specified, and the result of list items basically. All I had to do was
add the quantity remaining bit.
"""
def run_test():
	tests_passed = 0
	total_tests = 0
	machine = VendingMachine()
	machine.add_item({"item":Item("Ball Bat",100),"num":100})
	machine.add_item({"item": Item("Fruit Candy", 25), "num": 5})

	#Item Selection Test
	item_selection_test = (
		("Z5",(False,"\r\nLocation 'Z5' doesn't exist.")),
		("A0",(True,"\r\nCost:$0.50 Quantity Remaining:5")),
		("B2",(True,"\r\nCost:$25.00 Quantity Remaining:5"))
	)

	for i,test in enumerate(item_selection_test):
		total_tests += 1
		prompt, expected_result = test
		test_result = machine.select_item(prompt)
		if test_result == expected_result:
			print(f"Item Selection Test #{i} Passed")
			tests_passed+=1
		else:
			print(f"Item Selection Test #{i} Failed!")
			print(f"Expected '{expected_result}'\r\nBut we got '{test_result}'")


	#Machine List Method Test
	machine_list_items = 'A0:Pepsi Can           \tA1:Buttered Toast      \tA2:10x Fish Sticks     \t\r\nA3:3x ABC Gum          \tB0:5x Bananas          \tB1:Ball Bat            \t\r\nB2:Fruit Candy         \t'
	test_result = machine.list_items()
	if test_result == machine_list_items:
		print(f"Item List Test Passed!")
		tests_passed += 1
	else:
		print(f"Item List Test Failed!\r\nExpected '{machine_list_items}'.\r\nBut we got '{test_result}'")

	#Item Purchase Test
	item_purchase_test = (
		(
			("Z5",False),
		    (False,"\r\nAn item doesn't exist at location Z5")),
		(
			("A0",1),
		    (True,"\r\nYou purchased Pepsi Can. Then the machine gave you back: 2 Quarters")),
		(
			("A0",0.25),
		    (False,"\r\nYou didn't insert enough money! Then the machine gave you back: 1 Quarters")),
		(
			("B0",1.42),
		    (True,"\r\nYou purchased 5x Bananas. Then the machine gave you back: 2 Quarters, 1 Dimes, 1 Nickels, 1 Pennies")
		 )
	)

	for i,test in enumerate(item_purchase_test):
		total_tests += 1
		selection_item, expected_result = test
		location, amt = selection_item
		test_result = machine.purchase_item(location,amt)
		if test_result == expected_result:
			print(f"Item Purchase Test #{i} Passed")
			tests_passed+=1
		else:
			print(f"Item Purchase Test #{i} Failed!")
			print(f"Expected '{expected_result}'\r\nBut we got '{test_result}'")



	#Machine Shutoff Test
	machine_shutoff_no_deduct = (
		'A0:Pepsi Can has 5 remaining\tA1:Buttered Toast has 6 remaining\tA2:10x Fish Sticks has 7 remaining\t\r\nA3:3x ABC Gum has 8 remaining\tB0:5x Bananas has 2 remaining\tB1:Ball Bat has 100 remaining\t\r\nB2:Fruit Candy has 5 remaining\t', 'The machine made $1.25')
	machine_shutoff_deduct = (
		'A0:Pepsi Can has 4 remaining\tA1:Buttered Toast has 6 remaining\tA2:10x Fish Sticks has 7 remaining\t\r\nA3:3x ABC Gum has 8 remaining\tB0:5x Bananas has 1 remaining\tB1:Ball Bat has 100 remaining\t\r\nB2:Fruit Candy has 5 remaining\t',
		'The machine made $1.25')
	test_result = machine.shut_off()
	if test_result == machine_shutoff_no_deduct or test_result == machine_shutoff_deduct:
		print(f"Shutdown test Passed!")
		if test_result == machine_shutoff_no_deduct:
			print("They didn't implement deduction.")
		else:
			print("They implemented deduction.")
		tests_passed += 1
	else:
		print(f"Shutdown test Failed!\r\nExpected '{machine_shutoff_no_deduct}' or '{machine_shutoff_deduct}'.\r\nBut we got '{test_result}'")
	total_tests += 2

	if total_tests != tests_passed:
		print("NOT ALL TESTS PASSED!")
	print(f"{tests_passed}/{total_tests} passed or {round(tests_passed/total_tests*100,2)} %")
run_test()
