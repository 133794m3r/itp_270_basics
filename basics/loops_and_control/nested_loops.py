#!/usr/bin/env python3
'''
Double nested loops.
Will print the following pattern.

By Macarthur Inbody
2020 - AGPLv3.

         0
        111
       22222
      3333333
     444444444
    55555555555
   6666666666666
  777777777777777
 88888888888888888
9999999999999999999
9999999999999999999
 88888888888888888
  777777777777777
   6666666666666
    55555555555
     444444444
      3333333
       22222
        111
         0




It's not a perfect diamond but it

'''
#our initial string.
string=''
j=0;
character=''
#here this is a varaible so that the next line can be commented out and the user 
#can speify the number to use.
numbers=10
'''
#Put a # before the line above to make the rest of this code work.
#it's completely optional.

#below is a basic try catch block so that I can control the errors shown.
#first we try the code below.
try:
	#we try and get the user's input and then make it an integer and assign it to the variable
	#numbers.
	numbers=int(input("Enter a number between 1-64: "))
	#if the value of numbers is less than or equal to zero.
	if numbers <=0:
		#we raise a value error because they didn't follow instructions.
		raise ValueError("Please enter a number greater than zero.")
	elif numbers >64:
		raise ValueError("Your number is too large.")
#our exception handler.
except ValueError as ve:
	#We print this custom message telling them it was wrong.
	print("An invalid number was provided.")
	#then we raise the error.
	raise ve
#if all went well then we continue with the program.
#place a # right before the line below to make it work properly too.
'''
#this is a bunch of printable characters so that if the user enters a number
#that is between 1 and 64 we an print all of the characters.
characters='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!-';
#we get all values in the range of 0-10
for i in range(numbers):
	#make sure to clear the string again.
	string='';
	if i <numbers:
		string=' '*(numbers -(i +1))
	#set j to zero again.
	j=0
	#set our character to the character pointed to by i.
	character=characters[i]
	#while j is less than or equal to i.	
	#by setting it to be less than i*2 we can make an entire diamond.
	while j <= (i*2) :
		#append the number i(as a string) to the string.
		string+=character
		#increment j by 1.
		j+=1
	#print our output string.
	print(string)
#this time we're making the second half of it. So we're counting down instead of up.
while i >= 0:
	#clear the string again.
	string='';
	#set j to i*2 so that we can draw the bottom half of the diamond.
	j=(i*2)
	#set character to the character in our table pointed to by i.
	character=characters[i]
	#if i is less than numbers then we add the total numbers minus i spaces
	#to the beginning of our string.
	if i <numbers:
		string=' '*(numbers -(i +1)	)
	#do this while j is greater than or equal to 0.
	while j>=0:
		#append this character to the string j times.
		string+=character
		#decrement j by 1.
		j-=1
	#do the same but this time with i.
	i-=1
	#print this new string to the terminal.
	print(string)
	
