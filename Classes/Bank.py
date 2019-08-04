# Classic Bank example
# I say classic because you find a lot of videos on this

# Lets create an account class


# Always capitalize the new of a class, thats a standard
class Account(object):
	# The reason why (object) is in the parantheses is because
	# we want it to inherit from the object class
	# which is the base class.

	# Now within a class you have methods 
	# the method __init__ is to initialize the class 
	# in JAVA its called a constructor (basically to construct the class)
	def __init__(self,id):
		# the varial self is used to class the function or the id
		# it makes it a perminat variable in the class
		# so later i can call it.
		self.id = id
		# Here we initialize balance to zero
		self.balance = 0

	def deposit(self,amount):
		# because balance is initialized with self
		# I can call it within other functions
		self.balance +=amount
		print("Current Balance: ",self.balance)

	def withdraw(self,amount):
		# here if the amount is too large we can display a warning
		if amount>self.balance:
			print("Not sufficient funds")
		else:
			self.balance-=amount
			print("Current Balance: ",self.balance)


#  Now that we have created the class lets test it 

# The following lines only works in the script 

if __name__ == "__main__":

	# Lets initialize the Account and give it an ID
	account1 = Account(34234)

	# lets get the ID:
	# Thats where the self variable is important
	# account1 is equal to self
	print(account1.id)
	print(account1.balance)

	# Now lets add some money to account1
	account1.deposit(20000)

	# Now lets withdraw from the account
	account1.withdraw(5000)

	# Now lets try and withdraw a lot more 
	account1.withdraw(30000)








