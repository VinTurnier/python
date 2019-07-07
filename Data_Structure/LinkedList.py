
# Initialize Node 
class Node(object):
	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList(object):

	def __init__(self):
		self.head = Node()

	#adds Nodes to linked List	

	def add(self, data: int):
		# initialize new Node
		node = Node(data)
		cur = self.head
		while cur.next!=None:
			cur = cur.next

		cur.next = node

	# Returns the length of the Linked List
	def __len__(self)->int:
		length = 0
		cur = self.head
		while cur.next!=None:
			length +=1
			cur = cur.next

		return length

	# Get the data from the linked list
	# given an index
	def get(self, i: int)->int:
		
		if i>=self.__len__():
				return "ERROR: Get index out of range"

		cur = self.head
		index = 0

		while cur.next!=None:
			index+=1
			cur = cur.next
			if index==i:
				return cur.data
			else:
				cur = cur.next

	# Turns the linked list to a string to visualize
	def __str__(self)->str:
		cur = self.head
		string = "LinkedList(["
		while cur.next!=None:
			if cur.data == None:
				cur = cur.next
				string+=str(cur.data)
			else:
				cur = cur.next
				string+=", "+str(cur.data)

		return string+"])"




if __name__ == "__main__":

	ll = LinkedList()
	ll.add(1)
	ll.add(8)
	ll.add(20)

	print(ll.get(3))
	print(ll)