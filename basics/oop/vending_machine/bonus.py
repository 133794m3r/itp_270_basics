# Greedy Change Algorithm
# this one doesn't use the divmod function in python.

def greedy_change(money):
	quarters = money // 0.25
	money -= quarters * 0.25
	dimes = money // 0.10
	money -= dimes * 0.10
	nickels = money // 0.05
	money -= nickels * 0.05
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

	return ", ".join(result)


# as you can see the one with divmod is much cleaner.
def greedy_change(money):
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

	return ", ".join(result)

