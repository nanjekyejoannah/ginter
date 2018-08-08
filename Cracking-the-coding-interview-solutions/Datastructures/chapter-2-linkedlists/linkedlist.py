class Node:

	def __init__(self, value):
		self.value = value
		self.next = None
		self.previous = None

	def get_value(self):
		return self.value

	def get_next_node(self):
		return self.next

	def set_next_node(self, newNextNode):
		self.next = newNextNode

class LinkedList(object):

	def __init__(self, head = None):
		self.head = head

	def insert(self, value):
		new_node = Node(value)
		new_node.next = head
		self.head = new_node

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next_node()
		return count

	def search(self, data):
		current = self.head
		found = False
		while current and found is False:
			if current.get_value() == data:
				found = True
			else:
				current = current.get_next_node()
		if current is None:
			return ValueError("data not in list")
		return current

	def delete(self, data):
	    current = self.head
	    previous = None
	    found = False
	    while current and found is False:
	        if current.get_data() == data:
	            found = True
	        else:
	            previous = current
	            current = current.get_next()
	    if current is None:
	        raise ValueError("Data not in list")
	    if previous is None:
	        self.head = current.get_next()
	    else:
	        previous.set_next(current.get_next())


