class GeometricProgression(object):
	"""
	n mathematics, a geometric progression, also known as a geometric sequence, 
	is a sequence of numbers where each term after the first is found 
	by multiplying the previous one by a fixed, non-zero number 
	called the common ratio
	"""

	def sequence1(self, n):
		if n<0:
			return "Error: Sequence input must be > 0"
		elif n==1:
			return 3

		else:
			return 2* self.sequence1(n-1)

# let sequence(4)
# 2 * sequence(4-1)
# 	  |
#	  -> 2 * sequence(3-1)
#			 |
#			 -> 2 * sequence(2-1)
#					|
#					-> 3
# 2 * 3 = 6
# 2 * 6 = 12
# 2 *12 = 24

if __name__ == "__main__":
	gp = GeometricProgression()
	print(gp.sequence1(4))