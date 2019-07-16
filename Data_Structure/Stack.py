
class Stack(object):

	"""
	Stack is a linear data structure which follows 
	a particular order in which the operations are 
	performed. The order may be LIFO(Last In First Out) 
	or FILO(First In Last Out)
	"""
	def __init__(self):
		self.stack = []


	def __len__(self):
		return len(self.stack)

	def push(self,item):
		# add items to the stack
		# add an item at the end of a stack
		
		self.stack.append(item)
		

	def pop(self):
		# removes the last item in the stack
		if self.isEmpty():
			return None
		
		return self.stack.pop(len(self.stack)-1)

	def peek(self):
		if self.isEmpty():
			return None
		return self.stack[len(self.stack)-1]

	def isEmpty(self):
		if self.stack == []:
			return True
		else:
			return False

		


if __name__ == "__main__":
	s = Stack()
	s.push(2)
	s.push(5)
	s.push(3)
	print(s.peek())
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.pop())