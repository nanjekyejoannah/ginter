class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class Binarytree:
	def __init__(self, root):
		self.root = Node(root)

	def print_tree(self, typet):
		if typet == "preorder":
			print (self.pre_order(tree.root, ""))
		if typet == "inorder":
			print (self.in_order(tree.root, ""))
		if typet == "postorder":
			print (self.post_order(tree.root, ""))

	def pre_order(self, start, traversal):
		#Root > Left > Right
		if start:
			traversal += (str(start.value) + "-")
			traversal =  self.pre_order(start.left, traversal)
			traversal =  self.pre_order(start.right, traversal)
		return traversal

	def in_order(self, start, traversal):
		#Left > Root > Right
		if start:
			traversal =  self.in_order(start.left, traversal)
			traversal += (str(start.value) + "-")
			traversal =  self.in_order(start.right, traversal)
		return traversal

	def post_order(self, start, traversal):
		#Left > Rightt > Root
		if start:
			traversal =  self.post_order(start.left, traversal)
			traversal =  self.post_order(start.right, traversal)
			traversal += (str(start.value) + "-")
		return traversal

	def level_order(self, start):
		#Left > Rightt > Root
		if start:
			traversal =  self.post_order(start.left, traversal)
			traversal =  self.post_order(start.right, traversal)
			traversal += (str(start.value) + "-")
		return traversal


tree = Binarytree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.print_tree ("preorder")
tree.print_tree ("inorder")
tree.print_tree ("postorder")
