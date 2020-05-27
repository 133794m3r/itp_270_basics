#!/usr/bin/env python3

"""
This is a Full Shift Cipher that prompts the user for a string, key, and mode and then carries out encryption or decryption on the string.

Author: Ritchie Deel
Unit tests/Complexifying by Macarthur Inbody.
Version 1.1
Now with unit tests and functions.
There's one gigantic function that'll run through all possible keys and test them all too now.

Version 1.2
Now it does the full "printable" ASCII characterset.
Version 1.3
Now it encipher function is a generic one that takes any symbol set or length of symbols. Also there's some 
docstrings included for each function making it showup with help(<FUNCTION_NAME>) or if it's called like <FUNCTION_NAME>.__doc__
"""


#The behavior below of defining global variables isn't recommended but since this is a global module it's fine for right now.

#this is the sorted version. I believe it's correct.
SYMBOLS=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

#cache this value as it's never going to change after startup.
TOTAL_SYMBOLS=len(SYMBOLS);

#this is the main function that's run.
def main():
	"""The main function.
	Keyword Arguments: None
	
	This is the main function that'll prompt the user interactively to get their string to be encrypted/decrypted.
	
	Return:
	Just zero because I'm a C programmer.
	"""
	
	# The string to be encrypted/decrypted is input here:
	message = input("Enter the message to be encrypted here: ")

	# The encryption/decryption key:
	key = int(input("Enter the encryption key: "))
	
	#if the key is larger than our total symbols or less than zeor
	if key >= TOTAL_SYMBOLS or key < 0:
		#we have to clamp it down to a value between 0 and TOTAL_SYMBOLS-1
		#so that it's a valid key to use for your program to utilize below.
		key = key % TOTAL_SYMBOLS

	# Whether the program will encrypt or decrypt the string:
	mode = input('Enter the mode (encrypt or decrypt): ')
	"""
	Then we pass our arguments to the program so that it can then encrypt/decrypt it for us.
	We pass the message, the key, the SYMBOLS we're using and also the TOTAL_SYMBOLS
	This way if we want to re-use the program below for plain-old Ceaser(A-Za-z) we can pass it the new
	symbols and the total length of those and it'll work just fine w/o any extra work.
	All the end user has to do is modify the SYMBOLS variable at the top of this function and
	it'll work with any characterset.
	"""
	translated=encipher(message,key,mode,SYMBOLS,TOTAL_SYMBOLS)
	# Output the translated string:
	print(translated)
	
	return 0
	
#here's our encrypter/decrypter program.
def encipher(message,key,mode,SYMBOLS,TOTAL_SYMBOLS=0):
	"""Translate a string using the key, and symbols in the mode given.
	Keyword arguments:
	message -- the string to be encoded.
	key -- an integer between 0-(len(SYMBOLS)-1)
	SYMBOLS -- The table of symbols we're going to utilize for translation.
	TOTAL_SYMBOLS -- The number of symbols we're going to utilize. If omitted it will be calculated.

	Return:
	translated (String) -- The Translated string.
	This program will take the input and then convert it using a basic shift cipher with the symbols given.\n
	Only those given will be translated and the rest will be left alone.
	"""
	#this is here in case they don't provide us with the length.
	#so that it's simpler on them.
	if TOTAL_SYMBOLS == 0:
		TOTAL_SYMBOLS=len(SYMBOLS)

	# Stores the encrypted/decrypted form of the message:
	translated = ''
	#get each symbol from the message.
	for symbol in message:
		#if the symbol we found is in our encrypted symbols.
		if symbol in SYMBOLS:
			#find the index of it.
			symbolIndex = SYMBOLS.find(symbol)
			
			# Perform encryption/decryption
			if mode == 'encrypt':
				translatedIndex = symbolIndex + key
			elif mode == 'decrypt':
				translatedIndex = symbolIndex - key
		   
		   # Handle wrap-around, if needed:
			if translatedIndex >= TOTAL_SYMBOLS:
				#if it's greater than the maximum item. Take the index minus the item size.
				translatedIndex = translatedIndex - TOTAL_SYMBOLS
			elif translatedIndex < 0:
				#If it's less than 0 as in it's underflowed. Take the translated index
				#and add it to the total number of symbols to get the new index.
				translatedIndex = translatedIndex + TOTAL_SYMBOLS
			#get this new character and add it to the translated string.
			translated = translated + SYMBOLS[translatedIndex]
		#otherwise it's not in the translation string so we just pass it along.
		else:
			# Append the symbol without encrypting/decrypting:
			translated = translated + symbol

	#return the translated string.
	return translated

"""
The folllowing function just does the enciphering/deciphering in one loop all at once.
This is another way to write your tests.
"""
def test_gauntlet(symbols=None,total=None):
	if symbols is None:
		symbols=SYMBOLS
	if total is None:
		total=TOTAL_SYMBOLS
	"""Test Gauntlet function.
	Keyword Arguments
	symbols -- The symbols to utilize. (Default is None causing it to be set as global SYMBOLS variable.)
	total -- The total number of symbols. (Default is None causing it to be set as global TOTAL_SYMBOLS variable.)
	This function will run through every possible key. Encrypting some plain-text. Then it decrypts it using the same key. It will then verify that the output of the decryption is the same string as the original string given. If they are not the same it will raise an error with the following information:
 	Key,Cipher Text,Plain Text
 	
 	Return -- Nothing.
 	Thus alerting you to the issue. If it runs fine the program reports back that everything is OK.
	"""
	#our original plain text we're going to compare against.
	#plain_text='Some see Ouroboros, I see recursive Python.'
	plain_text="What Is the Airspeed Velocity of an Unladen Swallow?"
	original_text=plain_text
	cipher_text=""
	i=95
	#tell the user what wer'e doing.
	print("Running encipher module test.")
	#also saying this here too to explain what's taking so long.
	print("Testing all possible keys....")
	#while i is greater than or equal to zero continue.
	while i>=0:
		#encipher the original text with the current key.
		cipher_text=encipher(original_text,i,"encrypt",symbols,total)
		#decipher the cipher text with our current key.
		plain_text=encipher(cipher_text,i,"decrypt",symbols,total)
		#check that the plain text we got back and our original text are not the same.
		if plain_text != original_text:
			#if they're not. We throw this little message.
			print("Key {} : Passed:[ ] Failed:[X]".format(i))		
			"""
			Then we raise an assertion error because our code failed.
			First the format paramters are positional. {0} = first argument, {1} = second etc.
			Then we add it to our string.
			And we make sure that the key string we insert is padded to two characters. This is the new
			and "PEP8" way of doing it. % is the old way.
			"""
			raise AssertionError("Your code's broke with the key:{:>2}. We got back {0} but expected {1} and the cipher text is '{3}'".format(plain_text,original_text,i,cipher_text))
		#otherwise it worked.
		else:
			#same thing here but this time we're formatting it to add a padding character if the number is less than 2 digits.
			#we print that it passed.		
			print("\nKey {:>2} : Passed:[X] Failed:[ ]".format(i))
			print("CT: {} \nPT: {}\n".format(cipher_text,plain_text))
		#decrease the value of i by one number.
		i-=1
	#print the following string that all passed. Because the error will cause the script to stop.
	print("All tests have passed!")

#if it's run as a script we instantly run the main function.
if __name__ == "__main__":
	test_gauntlet()
#	main()

