"""
A _very_ basics symbol class showing operator overloading.
By Macarthur Inbody
AGPLv3 or Later.

"""

class Symbol:
	"""
	Symbol Class
	
	To see string representation type print(symbol_name)
	to see how to recreate the object repr(symbol_name)
	It supports +,-,/,//,* and symbol_a**<some_int>.
	"""
	
	#default variables.
	variable='x'
	constant=1
	power=1
	#we intialize the class with default values if they're not given)
	def __init__(self,constant=constant,variable=variable,power=power):
		self.variable=variable
		self.constant=constant
		self.power=power
	
	#the printable representation of this class.
	def __str__(self,other=None,operator=None):
		out=''
		if self.constant == 0:
			return '0'
		elif self.constant != 1:
			out+=str(self.constant)
		out+=self.variable
		if self.power >1:
			out+='^'+str(self.power)
		if other is None:
			return out
		out+=operator
		if other.constant > 1:
			out+=str(other.constant)
		out+=other.variable
		if other.power >1:
			out+='^'+str(other.power)
		return out

	#how to recreate this class after importing this module.
	def __repr__(self):
		return 'Symbol({!r},{!r},{!r})'.format(self.constant,self.variable,self.power)
		
	#overloaded + operator.
	def __add__(self,other_symbol):
		"""
		Adds two symbols if they're the same variable we return a new symbol.
		Otherwise we return the string representation.
		__add__(self,other_symbol)
		example:
			x^2 + x => 2x^2
			x^2 + 2 = 2x^2
			3x+3y = 3x+3y
		"""
		#if they're passing an int as the other symbol.
		if type(other_symbol).__name__ == 'int':
			#we just return a new symbol that's both constant parts added together.
			return Symbol(self.constant+other_symbol,self.variable,self.power)
		#otherwise if they're both the same symbol we add constants like normal.
		elif other_symbol.variable == self.variable:
			return Symbol(self.constant+other_symbol.constant,self.variable,self.power)
		else:
			#otherwise just print both symbols with a '+' inbetween them.
			return self.__str__(other_symbol,'+')

	#overloaded - operator.
	def __sub__(self,other_symbol):
		"""
		Subtract two symbols.
		Returns new Symbol object if variables match otherwise it returns a string.
		__sub__(self,other_symbol)
		example:
			2x^2 - x => x^2
			3x^2 - 2 = x^2
			3x-3y = 3x-3y
		"""	
		if type(other_symbol).__name__ == 'int':
			return Symbol(self.constant-other_symbol,self.variable,self.power)
		elif other_symbol.variable == self.variable:
			return Symbol(self.constant-other_symbol.constant,self.variable,self.power)
		else:
			return self.__str__(other_symbol,'-')
	
	#overloaded * operator.
	def __mul__(self,other_symbol):
		"""
		Subtract two symbols.		
		Returns new Symbol object if variables match otherwise it returns a string.		
		__mul__(self,other_symbol)
		example:
			x^2 + x => x^3
			x^2 + 2 = 2x^2
			3x*3y = 3x*3y
		"""	
		if type(other_symbol).__name__ == 'int':
			return Symbol(self.constant*other_symbol,self.variable,self.power)
		elif other_symbol.variable == self.variable:
			return Symbol(self.constant*other_symbol.constant,self.variable,self.power+other_symbol.power)
		else:
			return self.__str__(other_symbol,'*')
					
	#overloaded ** operator.
	def __pow__(self,power):
		"""
		Raise symbol1 to the power of symbol2.
		Returns new Symbol object if variables match otherwise it returns a string.		
		__pow__(self,other_symbol)
		example:
			x^2 ** x => x^3
			x^2 ** 2 => x^6
			3x ** 3y = Error not supported.
		"""	
		if type(power).__name__ == 'int':
			return Symbol(pow(self.constant,power),self.variable,self.power*power)
		else:
			return ("\nERROR: '{} ** {}' not yet supported.".format(self,power))
			
	#overloaded / operator.
	def __truediv__(self,other_symbol):
		"""
		Divide two symbols. This one returns a float if divsion isn't even.	
		Returns new Symbol object if variables match otherwise it returns a string.		
		__truediv__(self,other_symbol)
		example:
			x^2 / 2 => 0
			4x // 5 = 0
			3x // 3y = 3x // 3y
		"""	
		if type(other_symbol).__name__ == 'int':
			return Symbol(self.constant/other_symbol,self.variable,self.power)
		elif other_symbol.variable == self.variable:
			return Symbol(self.constant/other_symbol.constant,self.variable,self.power)
		else:
			return self.__str__(other_symbol,'/')


			
			
	#overloaded // operator.
	def __floordiv__(self,other_symbol):
		"""
		Divide two symbols. This one returns the floored value of the integer parts.
		Returns new Symbol object if variables match otherwise it returns a string.		
		__truediv__(self,other_symbol)
		example:
			x^2 // 2 => 0x^2
			4x / 5 = 0x
			3x // 3y = 3x // 3y
		"""	
		if type(other_symbol).__name__ == 'int':
			return Symbol(self.constant//other_symbol,self.variable,self.power)
		elif other_symbol.variable == self.variable:
			return Symbol(self.constant//other_symbol.constant,self.variable,self.power)
		else:
			return self.__str__(other_symbol,'//')
def print_tests():
	first=Symbol(1,'x',2)
	second=Symbol(2,'y',3)
	third=Symbol(1,'x',4)
	fourth=Symbol(3,'y',4)
	fifth=Symbol(2,'x',2)
	print("Note that the symbols are the default ones for math not python.")
	print("{} + {} = {}".format(first,second,first+second))
	print("{} + {} = {}".format(first,3,first+3))
	print("{} / {} = {}".format(first,4,first/4))
	print("{} // {} = {}".format(first,4,first//4))	
	print("{} - {} = {}".format(first,second,first-second))
	print("{} - {} = {}".format(first,2,first-2))
	print("{} * {} = {}".format(first,second,first*second))
	print("{} * {} = {}".format(first,2,first*2))
	print("{} * {} = {}".format(first,third,first*third))
	print("{} ** {} = {}".format(first,2,first**2))
	print("{} ** {} = {}".format(second,2,second**2))
	print("{} ** {} = {}".format(fourth,4,fourth**4))
	print("{} ** {} = {}".format(fifth,first,fifth**first))
	
if __name__ == "__main__":
	print_tests()
