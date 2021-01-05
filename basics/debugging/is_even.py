"""
The goal is to make the following functions return the following values.

format is function(input) = return_value
is_even(1) = False
is_odd(2)  = False
is_even(65535) = False
is_odd(256) = True

The code at the bottom should run and print "All tests passed".
"""

def is_even(number):
	#way to do the same with bitwise is below.
	#if number & 1 = 0
	if number % 1 = 0:
		return True
	else:
		return False

def is_odd(number):
	return not is_even(number)


"""
The code below here is completely fine. You DON'T have to touch it at all.
"""
tests = ((1,False),(2, True), (255, False), (256, True), (65535, False))
for num,result in tests:
	assert is_even(num) == result
else:
	print("All Tests passed.")
