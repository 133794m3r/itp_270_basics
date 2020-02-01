#!/usr/bin/env python3

string=''
j=0;
character=''
numbers=10

characters='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!-';
total_characters=0
#draw top triangle.
for i in range(numbers+1):
	character=characters[i]
	string=' '
	for j in range((numbers*2) -i ):
		string+=' '
	for j in range(i*2+1):
		string+=character
	print(string)

#then we draw the bottom two together.
for i in range(numbers):
	string=''
	character=characters[i]

	string=''

	for j in range(numbers - i):
		string+=' '

	for j in range(i*2+1):
		string+=character

	string+=' '
	for j in range((numbers -i) *2 ):
		string+=' '

#	for j in range(numbers -i ):
#		string+=' '
	
	for j in range(i*2+1):
		string+=character
	total_characters+=len(string)
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
'''
while i>=0:
	string=''
	character=characters[i]
	j=(numbers - i )
	
	while j > 0:
		string+=' '
		j-=1
	
	j=(i*2)
	while j >=0:
		string+=character
		j-=1
	
	j=(numbers -i )*2-1
	while j >= 0:
		string+=' '
		j-=1

	j = (i*2)
	while j >=0:
		string+=character
		j-=1
	i-=1
	total_characters+=len(string)
	print(string)
'''
print("\nIn total to make the 2 triangles we used",total_characters,"to make 2 diamonds that were",(numbers*2)+1,"lines each.\nAlso we used",numbers+1,"unique characters.")
print('{0};{2};{1}'.format(total_characters,(numbers*2)+1,numbers+2))
