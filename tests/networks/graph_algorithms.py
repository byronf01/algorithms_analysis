# explanations for these functions are provided in requirements.py

from graph import Graph
import random
import itertools
from decimal import Decimal

SAMPLE_RATIO = 0.3

def BFS(graph, node):
	visited = set()
	queue = []
	queue.append((node, 0))

	max_dist = 0
	max_dist_nodes = []
	# print(queue)
	while len(queue) != 0:
		# print(queue)
		
		s = queue.pop(0)
		if s[1] > max_dist: 
			max_dist = s[1]
			max_dist_nodes = [] # rest max_dist_nodes as node with greater max distance found
		max_dist_nodes.append(s[0])

		for node in graph.get_neighbors(s[0]):
			if node not in visited:
				visited.add(node)
				queue.append((node, s[1] + 1))

	return (max_dist_nodes, max_dist)

def H1(graph):
	upper = graph.get_num_nodes()
	sample = []
	for _ in range(int(SAMPLE_RATIO * upper)):
		sample.append(random.randint(0, upper-1))
	
	max_found_dist = set()
	max_d = 0
	for n in sample:
		sample, sample_max_d = BFS(graph, n)
		if sample_max_d < max_d:
			continue
		elif sample_max_d > max_d:
			max_d = sample_max_d
			max_found_dist = set() # clear old entries
		max_found_dist.update(sample)
		
	# 2nd BFS with the new nodes
	# Random sample if new nodes are at least 30% of total nodes

	"""
	while len(max_found_dist) > int(graph.get_num_nodes() * 0.4):
		target = random.sample(max_found_dist, 1)[0]
		max_found_dist.remove(target)
	"""
	if len(max_found_dist) > int(graph.get_num_nodes() * 0.4):
		max_found_dist = set(itertools.islice(max_found_dist, int(graph.get_num_nodes() * 0.4)))
	
	diameter = 0 
	for n in max_found_dist:
		_, sample_max_d = BFS(graph, n)
		if sample_max_d > diameter:
			diameter = sample_max_d

	return max(diameter, max_d)

def H2(graph):
	# Let r be a random vertex and set Dmax = 0
	r = random.randint(0, graph.get_num_nodes()-1)
	Dmax = 0
	while True:
		# Perform a BFS from r
		nodes, furthest = BFS(graph, r)
		# Select the farthest node w in the BFS
		candidate = nodes[0]
		# if distance from r to w is larger than D max set D max to this dist, let r=w and repeat the above two steps 
		if furthest > Dmax: 
			Dmax = furthest
			r = candidate
		else: break

	return Dmax

def degeneracy_list(graph: Graph) -> list:
	pass
	L = []
	L_hash = set()
	degrees = {}
	D = [set() for _ in range(graph.get_num_nodes())]
	for vertex, neighbors in graph.adj_set.items():
		degrees[vertex] = len(neighbors)
		D[len(neighbors)].add(vertex)
	Nv = {} # stores {v: set(neighbors before v) }
	k = 0

	for _ in range(graph.get_num_nodes()):
		i = 0
		while len(D[i]) == 0: 
			i += 1
		k = max(k, i)
		v = D[i].pop()
		L.append(v)
		L_hash.add(v)
		for neighbor in graph.get_neighbors(v):
			if neighbor in L_hash: continue
			D[degrees[neighbor]].remove(neighbor)
			degrees[neighbor] -= 1
			D[degrees[neighbor]].add(neighbor)
			if v not in Nv: Nv[v] = set()
			Nv[v].add(neighbor)

	return (L, Nv)

def get_diameter(graph: Graph) -> int:
	# d1 = H1(graph)
	d2 = H2(graph)
	# print(f'H1 returns: {d1}')
	# print(f'H2 returns: {d2}')
	# return max(d1, d2)
	return d2

def get_clustering_coefficient(graph: Graph) -> float:
	
	# compute a d-degeneracy ordering of the vertices
	L, Nv = degeneracy_list(graph)

	triangles = 0
	# for each vertex v
	for vertex in L:
		# for each pair u w that is adjacent to v and earlier in the ordering from the degeneracy solution
		foo = list(graph.get_neighbors(vertex))
		res = [(a, b) for i, a in enumerate(foo) for b in foo[i + 1:]]
		# see if u and w is an edge in the graph, if it is then add one to triangle count
		for u, v in res:
			if vertex in Nv and u in Nv[vertex] and v in Nv[vertex] and v in graph.get_neighbors(u):
				triangles += 1

	# and count the number of two edge paths
	two_edge_paths = Decimal(0)
	for vertex in graph.adj_set.keys():
		deg = Decimal(len(graph.get_neighbors(vertex)))
		two_edge_paths += (deg*(deg-1))/Decimal(2)

	C = Decimal(3) * Decimal(str(triangles)) / two_edge_paths
	return float(C)

def get_triangles(graph):
	# compute a d-degeneracy ordering of the vertices
	L, Nv = degeneracy_list(graph)

	triangles = 0
	# for each vertex v
	for vertex in L:
		# for each pair u w that is adjacent to v and earlier in the ordering from the degeneracy solution
		foo = list(graph.get_neighbors(vertex))
		res = [(a, b) for i, a in enumerate(foo) for b in foo[i + 1:]]
		# see if u and w is an edge in the graph, if it is then add one to triangle count
		for u, v in res:
			if vertex in Nv and u in Nv[vertex] and v in Nv[vertex] and v in graph.get_neighbors(u):
				triangles += 1
	return triangles

def get_degree_distribution(graph: Graph) -> dict[int, int]:
	H = {}
	for v in graph.adj_set.keys():
		deg = len(graph.get_neighbors(v))
		if deg not in H: H[deg] = 0
		H[deg] += 1
	return H
