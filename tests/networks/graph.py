# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.

from collections.abc import Iterable

class Graph:
	def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
		# Add nodes to adjacency set
		self.adj_set = {}
		self.node_ct = 0
		self.edge_ct = 0
		for i in range(0, num_nodes):
			self.adj_set[i] = set()
			self.node_ct += 1
		
		# Add edges
		for e in edges:
			self.adj_set[e[0]].add(e[1])
			self.adj_set[e[1]].add(e[0])
			self.edge_ct += 1

	def get_num_nodes(self) -> int:
		return self.node_ct

	def get_num_edges(self) -> int:
		return self.edge_ct

	def get_neighbors(self, node: int) -> Iterable[int]:
		return self.adj_set[node]

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
