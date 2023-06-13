import requirements
import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import time

from collections.abc import Iterable

# Instructions
# Some test cases for the Graph class and the graph algorithms can be found in the main block below.
#
# Note that passing the test cases here does not necessarily mean that your graph class or graph
# algorithms are correctly implemented / will pass other cases. It is a good idea to try and create
# different test cases for both.

def create_and_verify_graph(num_nodes: int, edges: 'Iterable[tuple[int, int]]') -> requirements.Graph:
	print(f'\nTesting graph = ({num_nodes}, {edges})')
	graph = requirements.Graph(num_nodes, edges)
	print(f'get_num_nodes(): {graph.get_num_nodes()}, Expected: {num_nodes}')
	print(f'get_num_edges(): {graph.get_num_edges()}, Expected: {len(edges)}')

	return graph

def verify_neighbors(graph: requirements.Graph, node: int, neighbors: 'Iterable[int]'):
	print(f'get_neighbors({node}): {sorted(graph.get_neighbors(node))}, Expected: {sorted(neighbors)}')

def graph_tests():
	print('testing Graph class')

	graph = create_and_verify_graph(0, {})

	graph = create_and_verify_graph(1, {})

	graph = create_and_verify_graph(2, {})
	verify_neighbors(graph, 0, {})
	verify_neighbors(graph, 1, {})

	graph = create_and_verify_graph(2, {(0, 1)})
	verify_neighbors(graph, 0, {1})
	verify_neighbors(graph, 1, {0})

	graph = create_and_verify_graph(3, {})
	verify_neighbors(graph, 0, {})
	verify_neighbors(graph, 1, {})
	verify_neighbors(graph, 2, {})

	graph = create_and_verify_graph(3, {(0, 1), (1, 2)})
	verify_neighbors(graph, 0, {1})
	verify_neighbors(graph, 1, {0, 2})
	verify_neighbors(graph, 2, {1})

	graph = create_and_verify_graph(3, {(0, 1), (1, 2), (0, 2)})
	verify_neighbors(graph, 0, {1, 2})
	verify_neighbors(graph, 1, {0, 2})
	verify_neighbors(graph, 2, {0, 1})

def graph_algorithm_tests():
	print('\ntesting graph algorithms\n')

	
	print("Test 1")
	edges = {(0, 3), (0, 7), (1, 4), (1, 5), (1, 6), (2, 3), (2, 7), (3, 4), (3, 8), (3, 9), (4, 5), (4, 9), (5, 6), (8, 9)}
	graph = requirements.Graph(10, edges)
	print(f'get_diameter(): {requirements.get_diameter(graph)}, Expected: 5')
	print(f'get_clustering_coefficient(): {requirements.get_clustering_coefficient(graph)}, Expected: 0.4')
	print(f'get_degree_distribution(): {requirements.get_degree_distribution(graph)}, Expected: { {2: 5, 3: 3, 4: 1, 5: 1} }')
	G = nx.Graph(list(edges))
	correct = nx.clustering(G)
	print(f"CORRECT CLUSTERING: {sum(correct.values()) / len(correct)}")

	print("Test 2")
	edges = {(1, 6), (2, 6), (2, 3), (2, 7), (3, 4), (3, 8), 
				 				(8, 0), (5, 9), (9, 6), (6, 7), (7, 10), (7, 11), 
								(3, 7)}
	graph = requirements.Graph(12, edges)
	print(f'get_diameter(): {requirements.get_diameter(graph)}, Expected: 6')
	print(f'get_clustering_coefficient(): {requirements.get_clustering_coefficient(graph)}, Expected: 0.222222')
	print(f'get_degree_distribution(): {requirements.get_degree_distribution(graph)}, Expected: too lazy')
	G = nx.Graph(list(edges))
	correct = nx.clustering(G)
	print(f"CORRECT CLUSTERING: {sum(correct.values()) / len(correct)}")
	
	print("Test cc 1")

	for _ in range(0, 50):
		edges = generate_random_graph(600)
		# print(edges)
		graph = requirements.Graph(600, edges)
		G = nx.Graph()
		G.add_edges_from(edges)
		hyp = requirements.get_clustering_coefficient(graph)
		correct = nx.clustering(G)
		correct = sum(correct.values()) / len(correct)
		# print(hyp, correct)
		if abs(hyp - correct) > 1e-6:
			print(f"INCORRECT CC: {hyp}")
			print(f"CORRECT CC: {correct}")
			print(f"TRIANGLES CORRECT: {sum(nx.triangles(G).values()) / 3}")
			input()

	print("Test cc 2")

	for _ in range(0, 50):
		edges = generate_random_graph(6000)
		# print(edges)
		graph = requirements.Graph(6000, edges)
		G = nx.Graph()
		G.add_edges_from(edges)
		hyp = requirements.get_clustering_coefficient(graph)
		correct = nx.clustering(G, 0)
		print(hyp, correct)
		if abs(hyp - correct) > 1e-6:
			print(f"INCORRECT CC: {hyp}")
			print(f"CORRECT CC: {correct}")
			print(f"TRIANGLES CORRECT: {sum(nx.triangles(G).values()) / 3}")
			input()
			
	"""
	print("Test diameter")

	for _ in range(0, 20):
		edges = generate_random_graph(50)
		# print(edges)
		graph = requirements.Graph(50, edges)
		G = nx.Graph()
		G.add_edges_from(edges)
		hyp = requirements.get_diameter(graph)
		correct = nx.diameter(G)
		if hyp != correct:
			print(graph.adj_set)
			print(f"INCORRECT DIAMETER: {hyp}")
			print(f"CORRECT DIAMETER: {correct}")
			foo = nx.periphery(G)
			for i in range(0, len(foo)):
				for j in range(i+1, len(foo)):
					if correct == len(nx.shortest_path(G, source=foo[i], target=foo[j])) - 1:
						print(nx.shortest_path(G, source=foo[i], target=foo[j]))
						print(f"PATH: {foo[i]} TO {foo[j]} ")
			
			# Draw the graph
			pos = nx.spring_layout(G)  # Positions of nodes
			nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray')

			# Draw edge labels
			edge_labels = nx.get_edge_attributes(G, 'weight')
			nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

			# Show the graph
			plt.show()
	
	print("Test diameter 2")

	for _ in range(0, 50):
		edges = generate_random_graph(500)
		# print(edges)
		graph = requirements.Graph(500, edges)
		G = nx.Graph()
		G.add_edges_from(edges)
		hyp = requirements.get_diameter(graph)
		correct = nx.diameter(G)
		if hyp != correct:
			print(graph.adj_set)
			print(f"INCORRECT DIAMETER: {hyp}")
			print(f"CORRECT DIAMETER: {correct}")
			foo = nx.periphery(G)
			flag = False 
			for i in range(0, len(foo)):
				for j in range(i+1, len(foo)):
					if correct == len(nx.shortest_path(G, source=foo[i], target=foo[j])) - 1:
						print(f"PATH: {foo[i]} TO {foo[j]} ")
						print(nx.shortest_path(G, source=foo[i], target=foo[j]))
						flag = True
						break
				if flag:
					break
	
	print("Test 5")
	edges = set()
	edges = generate_random_graph(50000)
	
	graph = requirements.Graph(50000, edges)
	print(f'get_diameter(): {requirements.get_diameter(graph)}, Expected: idk')
	print(f'get_clustering_coefficient(): {requirements.get_clustering_coefficient(graph)}, Expected: erm')
	print(f'get_degree_distribution(): {requirements.get_degree_distribution(graph)}, Expected: kys')
	G = nx.Graph()
	G.add_edges_from(edges)
	correct = nx.diameter(G)
	print(f"CORRECT DIAMETER: {correct}")
	"""

	
def generate_random_graph(n):
	edges = set()

	connected = set()
	for i in range(0, n):
		for j in range(i+1, n):
			if random.random() > 0.9:
				edges.add((i, j))
				connected.add(i)
				connected.add(j)

	for i in range(n): # failsafe
		if i not in connected:
			edges.add((i, 0))		

	return edges

if __name__ == '__main__':
	# graph_tests()
	graph_algorithm_tests()
