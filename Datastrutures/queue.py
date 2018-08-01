class Queue:
	def __init__(self):
		self.queue = []

	def size():
		return len(self.queue)

	def is_empty(self):
		return self.size() == 0

	def enqueue(self, value):
		return self.queue.insert(0, value)

	def dequeue(self):
		if is_empty():
			return None
		else:
			return self.queue.pop()

	def peek(self):
		if is_empty():
			return None

		else:
			return self.queue[-1]