class ClimbStairs(object):

	'''
		You are climbing a stair case. It takes n steps to reach to the top.
		Each time you can either climb 1 or 2 steps. In how many distinct 
		ways can you climb to the top?
		Note: Given n will be a positive integer.
	'''

	def climb(self,n):
		if n == 0:
			return 0
		elif n == 1:
			return 1
		elif n == 2:
			return 2
		else:
			return self.climb(n-1)+self.climb(n-2)

"""
	1 = 1
	2 = 2
	3 = 3
	4 = 5
	5 = 8
	6 = 13
	its basically a fibonacci sequence
	where 0 = 0
	1 = 1 
	2 = 2
	the base is 2,1,0
	3 = 2+1
	4 = 2+3



"""
