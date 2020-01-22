#!/usr/bin/env python3

'''
This is a Full Shift Cipher that prompts the user for a string, key, and mode and then carries out encryption or decryption on the string.

Author: Ritchie Deel
Unit tests/Complexifying by Macarthur Inbody.
Version 1.1
Now with unit tests and functions.
There's one gigantic function that'll run through all possible keys and test them all too now.

Version 1.2
Now it does the full "printable" ASCII characterset.

'''
#this is the main function that's run.
def main():
	# The string to be encrypted/decrypted is input here:
	message = input("Enter the message to be encrypted here: ")

	# The encryption/decryption key:
	key = int(input("Enter the encryption key: "))
	
	if key >=100 or key<=-1:
		key = key % 100
	# Whether the program will encrypt or decrypt the string:
	mode = input('Enter the mode (encrypt or decrypt): ')
	translated=encipher(message,key,mode)
	# Output the translated string:
	print(translated)
	
#here's our encrypter/decrypter program.
def encipher(message,key,mode):
	# Every possible symbol that is allowed to be encrypted:
	#SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
	#SYMBOLS='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
	#this is the sorted version. I believe it's correct.
	SYMBOLS=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

	#cache this value as it's never going to change after startup.
	TOTAL_SYMBOLS=len(SYMBOLS);

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
				translatedIndex = translatedIndex - len(SYMBOLS)
			elif translatedIndex < 0:
				translatedIndex = translatedIndex + len(SYMBOLS)
	
			translated = translated + SYMBOLS[translatedIndex]
		else:
			# Append the symbol without encrypting/decrypting:
			translated = translated + symbol

	#return the translated string.
	return translated

'''
The folllowing function just does the enciphering/deciphering in one loop all at once.
This is another way to write your tests.
'''
def test_gauntlet():
	#our original plain text we're going to compare against.
	#plain_text='Some see Ouroboros, I see recursive Python.'
	plain_text="What Is the Airspeed Velocity of an Unladen Swallow?"
	original_text=plain_text
	cipher_text=""
	i=95
	#tell the user what wer'e doing.
	print("Running encipher module test.")
	print("Testing all possible keys....")
	#while i is greater than or equal to zero continue.
	while i>=0:
		#encipher the original text with the current key.
		cipher_text=encipher(original_text,i,"encrypt")
		#decipher the cipher text with our current key.
		plain_text=encipher(cipher_text,i,"decrypt")
		#check that the plain text we got back and our original text are not the same.
		if plain_text != original_text:
			#if they're not. We throw this little message.
			print("Key {} : Passed:[ ] Failed:[X]".format(i))		
			'''
			Then we raise an assertion error because our code failed.
			First the format paramters are positional. {0} = first argument, {1} = second etc.
			Then we add it to our string.
			And we make sure that the key string we insert is padded to two characters. This is the new
			and "PEP8" way of doing it. % is the old way.
			'''
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

