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
aaaaaaaaaaaaaaaaaaaaa
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




Now it's a perfect diamond.

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
	elif numbers >63:
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
total_chars=0
#we get all values in the range of 0-10
for i in range(numbers):
	#make sure to clear the string again.
	string='';

	for j in range(numbers-i):
		string+=' '
		
	total_chars+=(j+1)
	#set j to zero again.
	j=0
	#set our character to the character pointed to by i.
	character=characters[i]
	#while j is less than or equal to i.	
	#by setting it to be less than i*2 we can make an entire diamond.
	for  j in range(i*2+1):
		#append the number i(as a string) to the string.
		string+=character

	total_chars+=(j+1)

	#print our output string.
	print(string)

#the lines below are to make it into a true diamond.
#first I clear the string.
string=''
#then I set j to be i*2 plus 2(since we have no spaces this time so we have to 
#add 2 extra characters.
j=(i*2)+2

total_chars+=(j+1)
#we set it to the next character.
character=characters[i+1]
#we loop until j becomes 0.
while j>=0:
	#we append the character j times.
	string+=character
	#decrement j.
	j-=1;

#print the string.
print(string)

#this time we're making the second half of it. So we're counting down instead of up.
while i >= 0:
	#clear the string again.
	string='';

	#set character to the character in our table pointed to by i.
	character=characters[i]
	#set j to be the amoutn of numbers minus the current i.
	j=(numbers - i )
	total_chars+=j
	#loop through it until j is 0.
	while j>0:
		#append a space to teh string.
		string+=' '
		#decrement j by 1.
		j-=1
	
	#set j to i*2 so that we can draw the bottom half of the diamond.
	j=(i*2)
	total_chars+=j+1
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

print('\nIn total we used',total_chars+(numbers*2),'characters to make our diamond.')
