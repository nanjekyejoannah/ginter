class Node:
	def __init__(self, value):
		self.value = value
		self.next = None #originally pointing nowhere

	def traverse(self):
		node = self
		while node != None:
			print node.value
			node = node.next

node1 = Node(12)
node2 = Node(13)
node3 = Node(14)

node1.next = node2
node2.next = node3

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None