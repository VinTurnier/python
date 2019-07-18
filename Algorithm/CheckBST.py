class TreeNode(object):

	def __init__(self, val=None):
		self.val = val
		self.left = None
		self.right = None



class BST(object):

	def checkBST(self,root: TreeNode):
		'''
			To check to see if a tree is a binary search tree
			all of the items to the left are less then the root
			and those to the right are greater then the root

		'''
		return self._checkBST(root,-200,200)

	def _checkBST(self, root: TreeNode, min: int, max: int):
		if root == None:
			return True
		if root.val< min or root.val >max:
			return False

		return self._checkBST(root.left,min, root.val-1) and self._checkBST(root.right,root.val+1,max)

if __name__ == "__main__":
	root = TreeNode(40)
	root.left = TreeNode(30)
	root.right = TreeNode(50)
	root.left.left = TreeNode(20)
	root.left.right = TreeNode(35)
	bst = BST()
	print(bst.checkBST(root))
