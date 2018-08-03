
def dfs_recursive(graph, start, visited = None):
	if visited = None:
		stack = set()
		visited = [start]
	for next in graph[start] - visited:
		dfs_recursive(graph, next, visited)
	return visited


#path

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])

list(dfs_paths(graph, 'C', 'F'))
