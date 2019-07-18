class BinarySearch(object):

	def __init__(self, item):
		self.item = item

	def search(self,E: int):
		left, right = 0, len(self.item)-1
		while(left<=right):
			mid = (right+left)//2
			if self.item[mid]==E:
				return mid
			elif self.item[mid]>E:
				right = mid-1
			else:
				left = mid+1


if __name__=="__main__":
	arr = [1,2,5,7,9,10]
	bs = BinarySearch(arr)
	print(bs.search(10))
