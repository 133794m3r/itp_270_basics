#!/usr/bin/env python3
'''
FizzBuzz Program
By Macarthur Inbody
2020- AGPLv3
Teaches the basics of a loop and also multiple conditionals.
'''
#ask the user for what number we should start counting from.
start=input("Enter a number to start counting from(press enter for 0): ")
#if they hit enter and we have no result assume they didn't want to specify one.
if start == '':
#so we set it to zero as we said it'd be.
	start=0
#otherwise.
else:
	#we convert their input into an int.
	start=int(start)
#prompt them for a maximum number.
maximum=int(input("Enter a number to count up to: "))
#intialize some variables.
divisible_by_30=0
divisible_by_5=0
divisible_by_3=0
divisible_by_2=0
'''
this is a for loop.
What it'll do is the following.
Python will generate a list of numbers that are between start and maximum+1
e.g. range(0,10) will give you a range object that contains all of these values.
It'll be a "list" of numbers(note not a real list). Of the values 0,1,2,3,4,6,7,8,9

Then here's what python does next.
It gets each of the items from the range and uses it below.
If you didn't make it maximum+1 then it'd only count upto that value not including it
because python like most languages starts at zero(unless told otherwise).

We set maximum to one more than what we were given because otherwise it counts up to that
number without including it. And most people who are told to count to 10 count up to 10
and include 10 in their counting. they don't stop at 9(as python would 
if you're counting from  1 to 10 and set the maximum to 10 it'd stop at 9.
'''
maximum=maximum+1

for number in range(start,maximum):
	'''
	the % operator is called the modulus operator. 
	It'll return the remainder of any division operation.
	For example 5 % 3 = 2. Because 3 goes into 5 1 time. With a remainder of 2.
'''
	#if the number is divisible by 30 evenly.
	if number % 30 == 0:
		#print Foo.
		print("Foo")
		#increment this variable 1.
		divisible_by_30+=1
		#same as above but this time with the number 5.
	elif number % 5 == 0:
		print("Bar")
		divisible_by_5+=1
	elif number % 3 == 0:
		print("Fizz")
		divisible_by_3+=1
	elif number % 2 == 0:
		print("Buzz")
		divisible_by_2+=1
	#if none of the other tests pass we print Bazz.
	else:
		print("Bazz")
#now we print the values and our totals.
print("In total all numbers up to your number {}.".format(number))
print("Had {} numbers that were divisible by 30.".format(divisible_by_30))
print("Had {}  numbers that were divisible by 5.".format(divisible_by_5))
print("Had {} numbers that were divisible by 3.".format(divisible_by_5))
print("Finally it had {} numbers that were divisible by 2.".format(divisible_by_2))
