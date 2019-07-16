

class TreeNode(object):
	def __init__(self, val = None):
		self.val = val
		self.left = None
		self.right=None
		self.parent=None


class minHeap(object):
	"""
		A Heap is a special Tree-based data structure 
		in which the tree is a complete binary tree
	"""

	def __init__(self):
		self.heap = TreeNode()

	def insert(self, data):
		root = self.heap
		self.insertRecursive(root,data)


	def insertRecursive(self, root: TreeNode, data: int):

		if root.val:
			if data<root.val:
				if root.left is None:
					root.left = TreeNode(data)
					root.left.parent = root
					if root.left.val<root.left.parent.val:
						temp = root.left
						root.left = root.left.parent
						root.left.parent = temp
				else:
					self.insertRecursive(root.left,data)
			if data>root.val:
				if root.right is None:
					root.right = TreeNode(data)
					root.right.parent = root

				else:
					self.insertRecursive(root.right, data)
		else:
			root.val = data




if __name__ == "__main__":
	hp = Heap()
	hp.insert(0)
	hp.insert(4)


