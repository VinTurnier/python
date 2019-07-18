class Node(object):
	def __init__(self,val=None):
		self.val = val
		self.next = None


class LinkedList(object):

	def __init__(self,head: Node):
		self.head = head


	def hasCycle(self):
		if head == None:
			return False
		fast = head.next
		slow = head
		while(fast != None and fast.next !=None):
			if fast==slow:
				return True
			fast = fast.next.next
			
			slow = slow.next
			

		return False

if __name__ == "__main__":
	head = Node(val = 1)
	head.next = Node(val = 2)
	head.next.next = Node(val = 3)
	head.next.next.next = Node(val = 4)
	head.next.next.next.next = head.next
	ll = LinkedList(head)
	print(ll.hasCycle())