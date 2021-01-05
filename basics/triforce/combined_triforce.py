#!/usr/bin/env python3

string=''
j=0
character=''
numbers=10

characters='#'*64
#characters='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!-'
number_i=0

#this line is to make the text colored yellow.
print("\033[1mCan I haz triforce?! I haz triforce of \033[31;1mPower\033[39;22m,\033[34;1mWisdom\033[39;22m,a and \033[32;1mCourage\033[39;22m\033[93;1m\n")

total_characters=0
#draw top triangle.
#Also to make it centered I am shifting it to the right by 2*number_of_lines - current_line
#so that it looks like this.
"""
       #
      ###
     #####
    #######
   #       #
  ###     ###
 #####   #####
####### #######
"""
#I am doing all of the lines of characters.
for i in range(numbers+1):
	#select the chracter from the character list.
	character=characters[i]
	#make string equal to numbers*2 -i plus 1 spaces.
	#in python you can do it like this without a for/while loop. It saves you typing.
	string=' '*(((numbers*2)-i)+1)
	#then we add i*2 plus 1 characters
	string+=character*((i*2)+1)
	#print the string.
	print(string)

#then we draw the bottom two together.
for i in range(numbers):
	#make sure the string's empty.
	string=''
	#select the character.
	character=characters[i]
	#instead of having to do the calculation over and over we cache the value.
	number_i=numbers-i
	#add numbers-i spaces to the string.
	string+=' '*number_i
	#then we add i*2 plus 1 characters to the string.
	string+=character*((i*2)+1)
	#now for triangle 3 as it's inline with the second one. We add an additional space.
	string+=' '
	#then we add the number of lines -i times 2 spaces.
	#for j in range((numbers -i) *2 ):
	string+=' '*(number_i*2)
		
	#then we add i*2+1 characters to the string.
	string+='\033[93m'+character*(i*2+1)
	#quick hack to get total character counts.
	total_characters+=len(string)
	#print the generated string.
	print(string)

string=''
character=characters[i+1]
for j in range(i*2+3):
	string+=character

string+=' '

for j in range(i*2+3):
	string+=character

total_characters+=len(string)
#this line prints the stirng and also clears the formatting and turns it back into the default one.
print('{}\033[39;22m'.format(string))

