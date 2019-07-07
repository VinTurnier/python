class TreeNode(object):
	def __init__(self, key=None):
		self.key = key
		self.left = None
		self.right = None


class BinaryTree(object):

	def __init__(self):
		self.root = TreeNode()
		self.in_order = False

	def __str__(self):
		if self.in_order:
			tree_arr = self.inorder()
		else:
			tree_arr = self.preorderTraversal()
		string = "BinaryTree("+str(tree_arr)+"]"
		return string

	def __len__(self):
		return len(self.preorderTraversal())

	def add(self,key: int):
		root = self.root
		self.addRecursive(root=root,key=key)
	
	def addRecursive(self, root: TreeNode, key: int):
		if root.key:
			if key<root.key:
				if root.left is None:
					root.left = TreeNode(key=key)
				else:
					self.addRecursive(root=root.left,key=key)
			elif key>root.key:
				if root.right is None:
					root.right = TreeNode(key=key)
				else:
					self.addRecursive(root=root.right,key=key)
		else:
			root.key = key

	def preorderTraversal(self):
		root = self.root
		arr = []
		self.preorderTraversalRecursive(root, arr)
		return arr

	def preorderTraversalRecursive(self, root: TreeNode(), arr=None):
		if root:
			arr.append(root.key)
			self.preorderTraversalRecursive(root.left,arr)
			self.preorderTraversalRecursive(root.right,arr)

	
	def inorder(self):
		self.in_order = True
		root = self.root
		arr = []
		self.inorderTraversalRecursive(root,arr)
		return arr

	def inorderTraversalRecursive(self,root: TreeNode, arr=None):
		if root:
			self.inorderTraversalRecursive(root.left, arr)
			arr.append(root.key)
			self.inorderTraversalRecursive(root.right, arr)

if __name__ == "__main__":
	bt = BinaryTree()
	bt.add(5)
	bt.add(3)
	bt.add(4)
	bt.add(6)

	print(bt)
	print(len(bt))
