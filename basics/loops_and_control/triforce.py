#!/usr/bin/env python3

string=''
j=0;
character=''
numbers=20
characters='#'*64
#characters='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!-';
print("Can I haz triforce?!")
total_characters=0
#draw top triangle.
for i in range(numbers+1):
	#select the chracter from the character list.
	character=characters[i]
	#make sure there's one extra space.
	string=' '
	#make numbers*2 -i be appened to string.
	for j in range((numbers*2) -i ):
		string+=' '
	#then we add i*2 plus 1 characters be appeneded to the string.
	for j in range(i*2+1):
		string+=character
	#print the string.
	print(string)

#then we draw the bottom two together.
for i in range(numbers):
	#make sure the string's empty.
	string=''
	#select the character.
	character=characters[i]
	#add numbers-i spaces to the string.
	for j in range(numbers - i):
		string+=' '
	#then we add i*2 plus 1 characters to the string.
	for j in range(i*2+1):
		string+=character
	#now for triangle 3 as it's inline with the second one. We add an additional space.
	string+=' '
	#then we add the number of lines -i times 2 spaces.
	for j in range((numbers -i) *2 ):
		string+=' '
		
	#then we add i*2+1 characters to the string.
	for j in range(i*2+1):
		string+=character
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
print(string)


print("\nIn total to make the triforce we used",total_characters,"to make 2 diamonds that were",(numbers*2)+1,"lines each.\nAlso we used",numbers+1,"unique characters.")
print('{0};{2};{1}'.format(total_characters,(numbers*2)+1,numbers+2))
