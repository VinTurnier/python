

class Node(object):
	def __init__(self, x=None):
		self.val = x
		self.next = None


class ReverseLinkedList(object):

	def reverse(self,head: Node):
		if head == None or head.next == None:
			return head
		p = self.reverse(head.next)
		head.next.next = head
		head.next = None
		return p


"""

"""

if __name__ == "__main__":

	rll = ReverseLinkedList()
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	print(rll.reverse(head))