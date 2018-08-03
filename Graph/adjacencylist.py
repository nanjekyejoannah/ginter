class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}

	def add_neighbour(self, node, weight=None):
		return self.connectedTo[node] = weight

	def get_connections(self):
		return self.connectedTo.keys()

	def get_id(self):
		return self.id

	def get_weight(self, node):
		return self.connectedTo[nbr]


class Graph:
	def __init__(self):
		vertexList = {}
		numOfVertexes = 0

	def add_Vertex(self, key):
		numOfVertexes = numOfVertexes + 1
		newVertex = Vertex(key)
		vertexList[key] = newVertex
		return newVertex

	def get_vertex(self, id):
		if is in self.vertexList:
			return self.vertexList[id]
		else:
			return None

	def __contains__(self, id):
		return id in self.vertexList

	def add_edge(self, fr, to, weight):
		if fr not in self.vertexList:
			nv = self.add_Vertex(fr)
		if to not in self.vertexList:
			nv = self.add_Vertex(to)
		return self.vertexList[f].add_neighbour(self.vertexList[t], weight)

	def get_vertices(self):
		return self.vertexList.keys()

	def __iter__(self):
		return iter(self.vertexList.values())



from pythonds import Graph

#undirected graph
def add_both_edges(g, key1, key2):
	g.add_edge(key1, key2)
	g.add_edge(key2, key1)

g = Graph
g.add_both_edges('a', 'f')
g.add_both_edges('b', 'g')
g.add_vertex(r)

for from_id in g.getVertices():
	t = tuple (v.id for v in g.getVertices(from_id).connectedTo.keys())
	print ("{0} to {t}", from_id, t)




