numbers=10
#characters='#'*64
characters='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!-';
number_i=0
print("\033[93mCan I haz Trifroce of Courage?!\033[32;1m")
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
	string+=' '*((i*2)+1)
	#now for triangle 3 as it's inline with the second one. We add an additional space.
	string+=' '
	#then we add the number of lines -i times 2 spaces.
	#for j in range((numbers -i) *2 ):
	string+=' '*(number_i*2)
		
	#then we add i*2+1 characters to the string.
	string+=character*(i*2+1)
	#print the generated string.
	print(string)
	
print("\033[0m")
