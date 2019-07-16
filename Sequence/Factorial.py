class Factorial(object):
	"""
	Calculate the factorial of a number
	n! = n*n-1*...*1
	"""
	def factorial(self,n:int):
		if n == 0:
			return 0
		elif n == 1:
			return 1
		else:
			return n*self.factorial(n-1)

"""
n=4
4*factorial(n-1)
|
->3 * factorial(n-1)
	  |
	  -> 2*factorial(n-1)
	  	   |
	  	   -> 1
	  |
	  -> 2 *1
|
-> 3 * 2 *1
|
-> 4 * 3 * 2 * 1 = 24

"""

if __name__ == "__main__":
	fc = Factorial()
	print(fc.factorial(4))
