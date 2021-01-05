numbers=10
#characters='#'*64
characters='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!-'
number_i=0
#this line is to make the text colored yellow.
print("\033[93mCan I haz Triforce of Wisdom?!\033[34;1m")
for i in range(numbers+1):
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
	print(string)
