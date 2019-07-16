class TreeNode(object):

	def __init__(self,val=None):
		self.val = None
		self.left = None
		self.right = None


'''
The lowest common node of a binary tree is found
by having two nodes, then identify there lowest
common parent
Example:
			[1]
			/ \
		  [4] [6]

the lowest common node of 4 and 6 is 1

the key to understanding is to first focus on
ONE node
'''

class LowestCommonAncestor(object):

	def __init__(self,root:TreeNode):
		self.root = root

	def lca(self, x: TreeNode, y:TreeNode):
		root = self.root
		return self._lca(root,x,y)

	def _lca(self, root: TreeNode, x: TreeNode, y: TreeNode):
		if root.val == None:
			return None
		if root.val == x.val or root.val = y.val:
			return root

		leftside = self._lca(root.left,x,y)
		rightside = self._lca(root.right,x,y)

		if 
