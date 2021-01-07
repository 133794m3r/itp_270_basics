"""
The goal is to make the fizzbuzz script below work and then have it print out the following info.

The 3 tests should print what they say, for the 3 test cases. And you should get an "All Tests Passed" message at the end. If you get an AssertionError then that means you have a logic error in the code.
SyntaxError means you have a syntax error.
"""
from typing import Tuple

"""
Test cases for fizz_buzz and what you should get in return.
The typing information/docstring is there to help you get documentation to help understand the function.

And it should print(next line)
function(start,end) = tuple(div_3, div_5, div_7)
fizz_buzz(1,10) = (3,1,1)
Numbers from 1,10 that are divisible by 3 = 3, 5 = 1, 7 = 1
fizz_buzz(10,50) = (13,8,6)
Numbers from 10 to 50 that are divisible by 3 = 13, 5 = 8, 7 = 6
fizz_buzz(1,500) = (166,99,71)
Numbers from 1 to 500 that are divisible by 3 = 166, 5 = 8, 7 = 71
"""

def fizz_buzz(start:int)->Tuple[int,int,int]:
	"""
	Basic FizzBuzz function.

	:param start: The integer to start with.
	:param end: The integer to count up to(non-inclusive)
	:return: A tuple containing the number of numbers divisible by 3, 5 and 7 respectively.
	"""
	
	div_3
	div_5
	div_7 
	for i in range(start,end):
		elif i % 3 = 0:
			div_3 += 1
		elif i % 5 = 0:
			div_5 += 1
		elif i % 7 = 0:
			div_7 +=1

	print("Numbers from",start,"to",end,"that are divisible by 3 =",div_3,", 5 =",div_5,", 7 =",div_7)
	return div_7, div_3, div_5


"""
Code below here doesn't need changed.
It is all correct. DO NOT CHANGE IT!
IT IS CHECKING THAT THE CODE ABOVE IS RIGHT!
Tuples are used below because the values shouldn't ever change.
Since tuples are immutable(as in can't be changed) this makes them
perfect for this case since you shouldn't ever be changing them.
Normally you'd see a list/dict but I don't want your fix to accidently modify it
then have you wonder why the tests aren't coming back properly.
"""
tests = (
	(
		(1,10), (3,1,1)
	),
	(
		(10,50), (13,8,6)
	),
	(
		(1,500),(166,99,71)
	),
)

for test,result in tests:
	s, e = test
	assert fizz_buzz(s,e) == result
else:
	print("All Tests Passed")
