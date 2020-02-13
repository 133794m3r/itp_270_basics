numbers=10
#characters='#'*64
characters='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!-';
number_i=0

#this line is to make the text colored yellow.
print("\033[93mCan I haz Triforce of Power?!\033[31;1m")

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

print("\033[0m");
