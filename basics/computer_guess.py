def random_guess(low,high):
	import math
	#we always initalize it to the middle point of the number.
	guess=low+((high-low)//2)
	#we do a log2 of the number to figure out the binary choices to get to the value.
	#log is an inverse of exponination. So what we're looking for here is our total
	#number of guesses that we need to do. Remember it has to be base 2 because we are
	#dividing the search space after each space by 2. Thus it's a binary climbing
	#ladder style question.
	#So if our range was 0-1000. It'd take at most 9.96 guesses. We round up so that's
	#10 guesses. If we use all 10 of our guesses and still don't have answer they cheated.
	guesses=round(math.log(high-low,2))
	#we set i to zero.
	i=0
	#do this loop while i is less than our number of guesses. Because we have the first one
	#already used for our initial guess.
	while i < guesses:
		#print our guess.
		print("guess",guess)
		#print the prompt to ask whether it's less than more than or equal to.
		answer=input("is it >, < or =: ")
		#if it's greater than.
		if answer == ">":
			#set the new high to be the guess.
			high=guess
			guess=(high+low)//2			
		#if it's less than.
		elif answer == "<":
			#we set then we set the new low to the guess +1.
			low=guess+1
			guess=(high+low)//2						
		elif answer == "=":
			print("So it was",guess)
			break
		else:
			#otherwise we tell them they didn't give us a valid selection.
			print("you didn't enter a valid selection.")
			#this is to just negate their choice from the next line that increments it.
			i-=1
	
		i+=1
	#if we used all of our guesses they cheated as we were given the maximum number of guesses
	#plus it was rounded up so in reality it should never take more than that amount of guesses.
	if i <= guesses :
		print("It took",i+1,"guesses.")
	else:
		print("you Cheated. because it took",i)
	#else we say how many guesses it took.


#tell them to give us the range.
print("Enter the range")
low=int(input("Enter the lowest number: "))
high=int(input("Enter the highest number: "))
random_guess(low,high)


