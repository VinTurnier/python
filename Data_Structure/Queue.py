from Stack import Stack


class Queue(object):

	"""
	Queue is an abstract data structure, somewhat similar to 
	Stacks. Unlike stacks, a queue is open at both its ends. 
	One end is always used to insert data (enqueue) and the 
	other is used to remove data (dequeue)
	"""

	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()

	def enQueue(self,item):
		self.stack1.push(item)

	def deQueue(self):
		if len(self.stack2)==0:
			if len(self.stack1)==0:
				return None
			while self.stack1.isEmpty() !=True:
				self.stack2.push(self.stack1.pop())
		
		return self.stack2.pop()


if __name__ == "__main__":

	q = Queue()
	q.enQueue(1)
	q.enQueue(3)
	q.enQueue(5)

	print(q.deQueue())
	print(q.deQueue())
	q.enQueue(6)
	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())