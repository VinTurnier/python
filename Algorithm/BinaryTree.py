from collections import deque

class TreeNode(object):

	def __init__(self,val=None):
		self.val = val
		self.left = None
		self.right = None

class BinaryTree(object):

	def __init__(self,root):
		self.root = root

	def serialize(self):
		root = self.root
		return self._serialize(root)

	def _serialize(self, root: TreeNode):
		if root == None:
			return 'x,'

		left = self._serialize(root.left)
		right = self._serialize(root.right)
		return str(root.val)+','+left+right

	def deserialize(self, s: str):
		queue = deque(s.split(','))
		self.root = self._deserialize(queue)

	def _deserialize(self,queue: deque):
		value = queue.popleft()
		if value == 'x':
			return TreeNode(val=None)
		node = TreeNode(int(value))
		node.left = self._deserialize(queue)
		node.right = self._deserialize(queue)

		return node

	def preorderTraversal(self):
		arr = []
		root = self.root
		self._preorderTraversal(root,arr)
		return arr

	def _preorderTraversal(self,root,arr):
		if root:
			arr.append(root.val)
			self._preorderTraversal(root.left,arr)
			self._preorderTraversal(root.right,arr)


if __name__ == "__main__":
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.right.left = TreeNode(4)
	root.right.right = TreeNode(5)
	bt = BinaryTree(root)
	print(bt.preorderTraversal())
	print(bt.serialize())
	bt.deserialize(bt.serialize())
	print(bt.preorderTraversal())



