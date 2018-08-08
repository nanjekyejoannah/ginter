class Stack(object):
	def __init__(self):
		self.stack = []

	def pop(self):
		self.stack.pop()

	def push(self, data):
		return self.stack.append(data)

	def peek(self):
		return self.stack[len(slef.stack)-1]

	def size(self):
		return len(self.stack)

	def is_empty(self):
		return self.stack == []
