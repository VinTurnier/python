
class Fibonacci(object):
	# 0, 1
	# 0+1 = 1
	# 1+1 = 2
	# 2+1 = 3
	# 3+2 = 5
	# Where n>= 2 because we cannot have n-2 in the sequence
	# first Identify n1 and n0
	# n0 = 0, n1 = 1

	def sequence1(self, num):
		arr = []
		if num==0:
			return [0]
		if num==1:
			return [0,1]

		arr = [0,1]
		self.recursion(len(arr)-1,len(arr)-2,0,num,arr)
		return arr[num]

	def recursion(self,n1,n2,curent_num,num,arr):
		if curent_num<=num-2:
			arr+=[arr[n1]+arr[n2]]
			curent_num+=1
			self.recursion(len(arr)-1,len(arr)-2,curent_num,num,arr)

	def sequence2(self,n):
		if n<0:
			return "ERROR: Entry must be > 0"
		if n==1:
			return 0
		elif n==2:
			return 1
		else:
			return self.sequence2(n-1)+self.sequence2(n-2)


	def sequence3(self,n, arr):
		if n<0:
			return "ERROR: Entry must be > 0"
		elif n == 1:
			return 0
		elif n == 2:
			return 1
		else:
			arr[n] = self.sequence3(n-1,arr)+self.sequence3(n-2,arr)
		return arr[n]


# let n = 4
# sequence2(4-1) + sequence2(4-2) 
# |				   |	
# |				   -> 1
# -> sequence2(3-1) + sequence(3-2)
#    |                |
#    |                -> 0
#    -> 1
#	1+0 = 1
# 1+1 =2

if __name__ == "__main__":
	fb = Fibonacci()
	print(fb.sequence1(20))
	print(fb.sequence2(4))
	arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	print(fb.sequence3(20,arr))