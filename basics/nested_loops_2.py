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
	total_chars+=len(string)
	print(string)
string=''
character=characters[i+1]
for j in range(i*2+3):
	string+=character

string+=' '

for j in range(i*2+3):
	string+=character

total_chars+=len(string)
print(string)

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
	
	j=(numbers -i )*2
	while j >= 0:
		string+=' '
		j-=1

	j = (i*2)
	while j >=0:
		string+=character
		j-=1
	i-=1
	total_chars+=len(string)
	print(string)

print("\nIn total to make the 2 triangles we used",total_chars,"to make 2 diamonds that were",(numbers*2)+1,"lines each.\nAlso we used",numbers+1,"unique characters.")
print('{0};{2};{1}'.format(total_chars,(numbers*2)+1,numbers+2))
