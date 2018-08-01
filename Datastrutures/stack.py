class Stack:
	def _init__(self):
		self.stack = []

	def size():
		return len(self.stack)

	def is_empty(self):
		return self.size() == 0

	def pop(self):
		if is_empty():
			return None
		else:
			return self.stack.pop()

	def push(self, value):
		return self.stack.append(value)

	def peak(self):
		if is_empty():
			return None
		else:
			return self.stack[-1]