class Vertex:
	def __init__(self, name):
		self.name = name
		self.neighbours = list()

	def add_neighbours(self, vertex):
		if vertex not in self.neighbours:
			self.neighbours.append(vertex)
			self.neighbours.sort()

class Graph:
	vertices = {}

	def add_vertex(self, vertex):
		if isInstance(vertex, Vertex) and vertex.name not in self.vertices:
			vertices["name"] = vertex.name
			return True

		else:
			return False

	def add_edge(self, n, v):
		if n in self.vertices and v in self.vertices:
			for k,  v in self.vertices.items():
				if key == u:
					value.add_neighbours(u)
				if key == v:
					value.add_neighbours(v)
			return True
		else:
			return False

	def print_graph():
		
