#!/usr/bin/env python3
'''
Double nested loops.
Will print the following pattern.

By Macarthur Inbody
2020 - AGPLv3.

         0
        1
       2
      3
     4
    5
   6
  7
 8
9
9
 8
  7
   6
    5
     4
      3
       2
        1
         0




This will print out the text above if the value 10 is given for the number of elements
that we'll be doing for each half. Basially it'll show that each line is indendented
by one less space as we go down the lines for the first half until we're at one. Then we 

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
	for j in range(numbers-i):
		string+=' '
	#set j to zero again.

	#set our character to the character pointed to by i.
	character=characters[i]
	#print our output string.
	string+=character
	print(string)
	
print(characters[i+1])
#this time we're making the second half of it. So we're counting down instead of up.
while i >= 0:
	#clear the string again.
	string='';
	#set character to the character in our table pointed to by i.
	character=characters[i]
	j=(numbers - i )
	while j>0:
		string+=' '
		j-=1

	string+=character
	i-=1
	#print this new string to the terminal.
	print(string)
	
