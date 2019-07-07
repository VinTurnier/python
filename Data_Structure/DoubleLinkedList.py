# create node type
class Node(object):
	def __init__(self, data=None):
		self.data = data
		self.next = None
		self.previous = None


# create Double Linked 
class DoubleLinkedList(object):
	def __init__(self):
		self.head = Node()





if __name__=="__main__":
	dll = DoubleLinkedList()
	dll.add(1)
	dll.add(10)
	dll.add(40)