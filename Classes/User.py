
# User class is very common
# any thing that you login to has a user class
# the class communicates with a database then adds
# this information to the class as needed


"""
Lets make it more interesting and bring in the 
Account class. Lets see how we can link the user
class and the account class together
"""
from Bank import Account

class User(object):

	def __init__(self,fName,lName,age,email):
		self.firstName = fName
		self.lastName = lName
		self.age = age
		self.email = email


	def getFullName(self):
		# Basically adding the strings together
		return self.firstName+ " "+self.lastName


	def createAccount(self,id):
		self.account = Account(id)


if __name__ == "__main__":

	user1 = User("vincent","turnier",22,"vincentturnier@gmail.com")

	# Lets create an account for the user

	user1.createAccount(232323)
	# look how 'self' is interesting
	print(user1.account.balance) # => 0
	# I basiccally created an account for the user 
	# and now that user has a specific account for themselves
	# lets create a second user

	user2 = User("user","example",34,"user@example.com")
	user2.createAccount(232324)
	print(user2.getFullName())
	user2.account.deposit(2300)
	# See the relationships and how elegant a class can make a code
	# makes it verry readable 
	print(user2.account.balance)