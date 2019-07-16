class TreeNode(object):
	def __init__(self,val=None):
		self.val = val
		self.left = None
		self.right = None


class BinaryTree(object):

	def __init__(self):
		self.root = TreeNode()

	def preorderTraversal(self):
		arr = []
		root = self.root
		self.preorderTraversalRecursive(root,arr)
		return arr

	def preorderTraversalRecursive(self, root: TreeNode, arr):
		if root:
			arr.append(root.val)
			self.preorderTraversalRecursive(root.left,arr)
			self.preorderTraversalRecursive(root.right,arr)

	def insert(self, val):
		root = self.root
		self.insertRecursive(root,val)

	def insertRecursive(self,root: TreeNode,val):
		if root.val:
			if val<root.val:
				if root.left is None:
					root.left = TreeNode(val = val)
				else:
					self.insertRecursive(root.left,val)
			elif val>root.val:
				if root.right is None:
					root.right = TreeNode(val = val)
				else:
					self.insertRecursive(root.right,val)
		else:
			root.val = val

	def serialize(self):
		root = self.root
		return self._serialize(root)

	def _serialize(self,root: TreeNode):
		if root == None:
			return 'x,'

		leftSerialized = self._serialize(root.left)
		rightSerialized = self._serialize(root.right)

		return str(root.val)+','+leftSerialized+rightSerialized

	def deserialize(self):
		pass

if __name__ =="__main__":

	bt = BinaryTree()
	bt.insert(5)
	bt.insert(10)
	bt.insert(15)
	bt.insert(9)
	bt.insert(8)
	print(bt.preorderTraversal())
	print(bt.serialize())