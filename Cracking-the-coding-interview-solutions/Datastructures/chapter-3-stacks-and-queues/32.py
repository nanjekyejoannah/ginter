class Stack(object):
	def __init__(self):
		self.stack = []

	def pop(self):
		self.stack.pop()

	def push(self, data):
		return self.stack.append(data)

	def min(self):
		return min(self.stack)

	def min_2(self):
		items = self.stack.sort()
		return items[0]