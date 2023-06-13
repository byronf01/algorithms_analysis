import requirements
import random
import itertools
from decimal import *

from typing import TypeVar, NamedTuple, Callable
from copy import deepcopy


# Instructions
# Some test cases for the Zi[ZipTree and bin packing algorithms can be found in the main block below.
#
# Note that passing the test cases here does not necessarily mean that your zip tree or algorithms
# are correctly implemented / will pass other cases. It is a good idea to try and create different
# test cases for both.

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

class InsertType(NamedTuple):
	key: KeyType
	val: ValType
	rank: int

def create_tree_with_data(data: list[InsertType]) -> requirements.ZipZipTree:
	tree = requirements.ZipZipTree(capacity = len(data))
	ct = 0
	for item in data:
		tree.insert(item.key, item.val, item.rank)
		ct += 1
		# print(ct)

	return tree

class ProblemInstance(NamedTuple):
	items: list[float]
	assignments: list[int]
	free_space: list[float]

def is_equal(v1: list[float], v2: list[float]) -> bool:
	for a, b in zip(v1, v2):
		if abs(Decimal(a) - Decimal(b)) > 1e-6:
			return False

	return True

def test_algorithm(test: ProblemInstance, expected_result: ProblemInstance, algorithm: Callable[[list[float], list[int], list[float]], None], name: str):
	test_copy = deepcopy(test)
	algorithm(test_copy.items, test_copy.assignments, test_copy.free_space)

	if test_copy.assignments == expected_result.assignments and is_equal(test_copy.free_space, expected_result.free_space):
		print(f'Test case passed: {name}')
		print(test_copy.free_space)
		print(f'{str(sum(test_copy.free_space))} vs. correct val of {str(sum(expected_result.free_space))}')
	else:
		print(f'Test case failed: {name}')
		print(test_copy.assignments)
		print(test_copy.free_space)

def zip_tree_tests():
	print('testing ZipTree')

	
	data = [InsertType(4, 'a', requirements.Rank(0, 9)), InsertType(5, 'b', requirements.Rank(0, 9)), InsertType(2, 'c', requirements.Rank(1, 12)), InsertType(1, 'd', requirements.Rank(1, 5))]
	tree = create_tree_with_data(data)

	print(f'find(4): {tree.find(4)}, Expected: a')
	print(f'get_size(): {tree.get_size()}, Expected: 4')
	print(f'get_height(): {tree.get_height()}, Expected: 2')
	print(f'get_depth(2): {tree.get_depth(2)}, Expected: 0')
	print(f'get_depth(1): {tree.get_depth(1)}, Expected: 1')
	tree.insert(0, 'e', requirements.Rank(1, 5))
	print(f'get_size(): {tree.get_size()}, Expected: 5')
	print(f'get_height(): {tree.get_height()}, Expected: 2')
	print(f'get_depth(2): {tree.get_depth(2)}, Expected: 0')
	print(f'get_depth(1): {tree.get_depth(1)}, Expected: 2\n')

	

	data2 = [InsertType(4, 'a', requirements.Rank(2, 1)), InsertType(5, 'b', requirements.Rank(2, 2)), InsertType(2, 'c', requirements.Rank(1, 8)), InsertType(1, 'd', requirements.Rank(0, 12))]
	tree2 = create_tree_with_data(data2)
	# print(tree2)
	tree2.insert(0, 'e', requirements.Rank(1, 8))
	# print(tree2)

	print(f'find(4): {tree2.find(4)}, Expected: a')
	print(f'get_size(): {tree2.get_size()}, Expected: 5')
	print(f'get_height(): {tree2.get_height()}, Expected: 4')
	print(f'get_depth(2): {tree2.get_depth(2)}, Expected: 3')
	print(f'get_depth(1): {tree2.get_depth(1)}, Expected: 4\n')

	
	data3 = []
	keys = set()
	for i in range(0, 150000):
		x = random.randint(0, 99999999)
		while x in keys:
			x = random.randint(0, 99999999)
		keys.add(x)
		foo = InsertType(x, str(random.random()), None)
		data3.append(foo)
		
	# data3.append(InsertType(58756, 'hi', None))
	tree3 = create_tree_with_data(data3)

	
	for i in keys:
		tree3.find(i)
	
	
	# print(f'find(58756): {tree3.find(58756)}, Expected: hi')
	print(f'get_size(): {tree3.get_size()}, Expected: 150000')
	print(f'get_height(): {tree3.get_height()}, Expected: idk')
	
	for x in keys:
		tree3.remove(x)
	
	# print(f'find(58756): {tree3.find(58756)}, Expected: hi')
	print(f'get_size(): {tree3.get_size()}, Expected: a lower number')
	print(f'get_height(): {tree3.get_height()}, Expected: idk')
		
	
	data4 = []
	keys = set()
	for i in range(0, 20):
		x = random.randint(0, 1000)
		foo = InsertType(x, str(random.random()), None)
		data4.append(foo)
		keys.add(x)
	tree4 = create_tree_with_data(data4)
	print(f'get_size(): {tree4.get_size()}, Expected: 20')
	print(f'get_height(): {tree4.get_height()}, Expected: idk')

	for i in keys:
		tree4.find(i)
	

	data5 = [InsertType(21, 'a', requirements.Rank(3, 31)), InsertType(-1, 'b', requirements.Rank(3, 13)), 
	  InsertType(29, 'c', requirements.Rank(2, 20)), InsertType(-8, 'd', requirements.Rank(1, 26)), InsertType(16, 'e', requirements.Rank(1, 49)),
	  InsertType(55, 'a', requirements.Rank(1, 38)), InsertType(-19, 'b', requirements.Rank(0, 33)), InsertType(-4, 'c', requirements.Rank(0, 31)), 
	  InsertType(2, 'd', requirements.Rank(1,1)), InsertType(22, 'e', requirements.Rank(0, 21)), InsertType(52, 'a', requirements.Rank(0, 2)), 
	  InsertType(-2, 'b', requirements.Rank(0, 1)), InsertType(7, 'c', requirements.Rank(0, 46)), InsertType(5, 'd', requirements.Rank(0, 23)), 
	  InsertType(12, 'e', requirements.Rank(0, 13))]
	tree5 = create_tree_with_data(data5)
	print(f'get_size(): {tree5.get_size()}, Expected: 15')
	print(f'get_height(): {tree5.get_height()}, Expected: 5')
	print(f'get_depth(): {tree5.get_depth(5)}, Expected: 5')
	print(f'get_depth(): {tree5.get_depth(12)}, Expected: 5')
	print(f'get_depth(): {tree5.get_depth(-2)}, Expected: 4')
	print(f'get_depth(): {tree5.get_depth(-4)}, Expected: 3')
	print(f'get_depth(): {tree5.get_depth(-8)}, Expected: 2')
	print(f'get_depth(): {tree5.get_depth(21)}, Expected: 0')
	print(f'get_depth(): {tree5.get_depth(-1)}, Expected: 1')
	print(f'get_depth(): {tree5.get_depth(29)}, Expected: 1')
	print(f'get_depth(): {tree5.get_depth(55)}, Expected: 2')
	print(f'get_depth(): {tree5.get_depth(52)}, Expected: 3')
	print(f'get_depth(): {tree5.get_depth(16)}, Expected: 2')
	print(f'get_depth(): {tree5.get_depth(7)}, Expected: 4')
	
	
	print('\ntesting random geometric rank generation')
	geometric_rank_sum = 0
	num_ranks = 10000
	tree3 = requirements.ZipZipTree(capacity = num_ranks)

	for _ in range(num_ranks):
		geometric_rank_sum += tree3.get_random_rank().geometric_rank

	geometric_rank_mean = geometric_rank_sum / num_ranks

	print(f'random geometric rank mean: {geometric_rank_mean}, Expected: ~1')

	# add new tests...

def bin_packing_tests():

	print('\ntesting bin packing\ntest 1')
	items = [0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4]
	assignments = [0] * len(items)
	free_space = list()

	test1 = ProblemInstance(items = items, assignments = assignments, free_space = free_space)

	# next-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 0, 1, 1, 2, 2, 3, 3], free_space = [0.1, 0.2, 0.1, 0.0])
	test_algorithm(test1, expected_result, requirements.next_fit, 'next_fit')

	# first-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 0, 1, 1, 2, 1, 3, 3], free_space = [0.1, 0.0, 0.3, 0.0])
	test_algorithm(test1, expected_result, requirements.first_fit, 'first_fit')

	# first-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 2, 1, 0, 3], free_space = [0.0, 0.0, 0.0, 0.4])
	test_algorithm(test1, expected_result, requirements.first_fit_decreasing, 'first_fit_decreasing')

	# best-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 0, 1, 1, 2, 1, 3, 3], free_space = [0.1, 0.0, 0.3, 0.0])
	test_algorithm(test1, expected_result, requirements.best_fit, 'best_fit')

	# best-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 2, 1, 0, 3], free_space = [0.0, 0.0, 0.0, 0.4])
	test_algorithm(test1, expected_result, requirements.best_fit_decreasing, 'best_fit_decreasing')

	print('\ntest 2')
	items = [0.79, 0.88, 0.95, 0.12, 0.05, 0.46, 0.53, 0.64, 0.04, 0.38, 0.03, 0.26]
	assignments = [0] * len(items)
	free_space = list()

	test2 = ProblemInstance(items = items, assignments = assignments, free_space = free_space)

	# next-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6], free_space = [0.21, 0.12, 0.05, 0.37, 0.47, 0.32, 0.33])
	test_algorithm(test2, expected_result, requirements.next_fit, 'next_fit')

	# first-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 0, 0, 3, 3, 4, 0, 5, 1, 4], free_space = [0, 0.09, 0.05, 0.01, 0.1, 0.62])
	test_algorithm(test2, expected_result, requirements.first_fit, 'first_fit')

	# first-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 4, 4, 5, 3, 1, 0, 2, 2], free_space = [0, 0, 0.14, 0.1, 0.01, 0.62])
	test_algorithm(test2, expected_result, requirements.first_fit_decreasing, 'first_fit_decreasing')

	# best-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 1, 2, 3, 3, 4, 0, 5, 0, 4], free_space = [0.14, 0, 0, 0.01, 0.1, 0.62])
	test_algorithm(test2, expected_result, requirements.best_fit, 'best_fit')

	# best-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 4, 4, 5, 3, 1, 0, 3, 3], free_space = [0, 0, 0.21, 0.03, 0.01, 0.62])
	test_algorithm(test2, expected_result, requirements.best_fit_decreasing, 'best_fit_decreasing')

	print('\ntest 3')
	items = [0.43, 0.75, 0.25, 0.42, 0.54, 0.03, 0.64]
	assignments = [0] * len(items)
	free_space = list()

	test3 = ProblemInstance(items = items, assignments = assignments, free_space = free_space)

	# next-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 1, 2, 2, 2, 3], free_space = [0.57, 0, 0.01, 0.36])
	test_algorithm(test3, expected_result, requirements.next_fit, 'next_fit')

	# first-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 0, 2, 2, 0, 3], free_space = [0.29, 0.25, 0.04, 0.36])
	test_algorithm(test3, expected_result, requirements.first_fit, 'first_fit')

	# first-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 2, 3, 0, 1], free_space = [0, 0.33, 0.03, 0.58])
	test_algorithm(test3, expected_result, requirements.first_fit_decreasing, 'first_fit_decreasing')

	# best-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 1, 0, 2, 0, 3], free_space = [0.12, 0, 0.46, 0.36])
	test_algorithm(test3, expected_result, requirements.best_fit, 'best_fit')

	# best-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 2, 3, 0, 2], free_space = [0, 0.36, 0, 0.58])
	test_algorithm(test3, expected_result, requirements.best_fit_decreasing, 'best_fit_decreasing')

	print('\ntest 4')
	items = [0.54, 0.67, 0.46, 0.57, 0.06, 0.23, 0.83, 0.64, 0.47, 0.03, 0.53, 0.74, 0.36, 0.24, 0.07, 0.25, 0.05, 0.63, 0.43, 0.04]
	assignments = [0] * len(items)
	free_space = list()

	test4 = ProblemInstance(items = items, assignments = assignments, free_space = free_space)

	# next-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 9, 9, 9, 10, 11, 11], free_space = [0.46, 0.33, 0.54, 0.14, 0.17, 0.36, 0.5, 0.47, 0.26, 0.03, 0.37, 0.53])
	test_algorithm(test4, expected_result, requirements.next_fit, 'next_fit')

	# first-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 0, 2, 1, 1, 3, 4, 5, 1, 5, 6, 2, 4, 2, 6, 3, 7, 8, 3], free_space = [0, 0.01, 0, 0.08, 0.12, 0, 0.01, 0.37, 0.57])
	test_algorithm(test4, expected_result, requirements.first_fit, 'first_fit')

	# first-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 3, 1, 2, 4, 0, 0, 2, 0, 2], free_space = [0, 0.01, 0.01, 0, 0.14, 0, 0, 0])
	test_algorithm(test4, expected_result, requirements.first_fit_decreasing, 'first_fit_decreasing')

	# best-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 0, 2, 1, 1, 3, 4, 5, 1, 5, 6, 4, 6, 3, 2, 3, 7, 8, 3], free_space = [0, 0.01, 0.18, 0.01, 0, 0, 0.02, 0.37, 0.57])
	test_algorithm(test4, expected_result, requirements.best_fit, 'best_fit')

	# best-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 3, 1, 2, 4, 2, 4, 4, 0, 4], free_space = [0.13, 0.01, 0.02, 0, 0, 0, 0, 0])
	test_algorithm(test4, expected_result, requirements.best_fit_decreasing, 'best_fit_decreasing')

	
	# add new tests...
	print('\ntest 5')
	items = [0.4, 0.3, 0.2, 0.1]
	assignments = [0] * len(items)
	free_space = list()

	test5 = ProblemInstance(items = items, assignments = assignments, free_space = free_space)

	# next-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 0, 0, 0], free_space = [])
	test_algorithm(test5, expected_result, requirements.next_fit, 'next_fit')
	# first-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 0, 0, 0], free_space = [])
	test_algorithm(test5, expected_result, requirements.first_fit, 'first_fit')
	# first-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0, 0, 0, 0], free_space = [])
	test_algorithm(test5, expected_result, requirements.first_fit_decreasing, 'first_fit_decreasing')
	# best-fit
	expected_result = ProblemInstance(items = items, assignments = [0, 0, 0, 0], free_space = [])
	test_algorithm(test5, expected_result, requirements.best_fit, 'best_fit')
	# best-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0, 0, 0, 0], free_space = [])
	test_algorithm(test5, expected_result, requirements.best_fit_decreasing, 'best_fit_decreasing')
	
	print('\n Base test')
	items = [0.5, 0.7, 0.5, 0.2, 0.4, 0.2, 0.5, 0.1, 0.6]
	assignments = [0] * len(items)
	free_space = list()

	test6 = ProblemInstance(items = items, assignments=assignments, free_space=free_space)

	# next-fit
	expected_result = ProblemInstance(items=items, assignments=[0,1,2,2,3,3,4,4,5], free_space=[0.5,0.3,0.3,0.4,0.4,0.4])
	test_algorithm(test6, expected_result, requirements.next_fit, 'next_fit')
	# first-fit
	expected_result = ProblemInstance(items = items, assignments = [0,1,0,1,2,2,3,1,4], free_space = [0,0,0.4,0.5,0.4])
	test_algorithm(test6, expected_result, requirements.first_fit, 'first_fit')
	# first-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0,1,2,2,3,1,0,3,0], free_space = [0,0,0,0.3])
	test_algorithm(test6, expected_result, requirements.first_fit_decreasing, 'first_fit_decreasing')
	# best-fit
	expected_result = ProblemInstance(items = items, assignments = [0,1,0,1,2,2,3,1,4], free_space = [0,0,0.4,0.5,0.4])
	test_algorithm(test6, expected_result, requirements.best_fit, 'best_fit')
	# best-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0,1,2,2,3,1,0,3,0], free_space = [0,0,0,0.3])
	test_algorithm(test6, expected_result, requirements.best_fit_decreasing, 'best_fit_decreasing')
	
	print('\nItems size 1 test')
	items = [1, 1, 1]
	assignments = [0] * len(items)
	free_space = list()
	

	test7 = ProblemInstance(items = items, assignments=assignments, free_space=free_space)

	# next-fit
	expected_result = ProblemInstance(items=items, assignments=[0,1,2], free_space=[0,0,0])
	test_algorithm(test7, expected_result, requirements.next_fit, 'next_fit')
	# first-fit
	expected_result = ProblemInstance(items=items, assignments=[0,1,2], free_space=[0,0,0])
	test_algorithm(test7, expected_result, requirements.first_fit, 'first_fit')
	# first-fit decreasing
	expected_result = ProblemInstance(items=items, assignments=[0,1,2], free_space=[0,0,0])
	test_algorithm(test7, expected_result, requirements.first_fit_decreasing, 'first_fit_decreasing')
	# best-fit
	expected_result = ProblemInstance(items=items, assignments=[0,1,2], free_space=[0,0,0])
	test_algorithm(test7, expected_result, requirements.best_fit, 'best_fit')
	# best-fit decreasing
	expected_result = ProblemInstance(items=items, assignments=[0,1,2], free_space=[0,0,0])
	test_algorithm(test7, expected_result, requirements.best_fit_decreasing, 'best_fit_decreasing')
	
	print('\nLong floating points test')
	items = [0.1847536493, 0.498573641139, 0.53, 0.9385376662222, 0.22224775, 0.00000144, 0.284366141414145833314]
	assignments = [0] * len(items)
	free_space = list()

	test8 = ProblemInstance(items = items, assignments=assignments, free_space=free_space)

	# next-fit
	expected_result = ProblemInstance(items=items, assignments=[0,0,1,2,3,3,3], free_space=[0.316672709561,0.47,0.0614623337778,0.493384668585854166686])
	test_algorithm(test8, expected_result, requirements.next_fit, 'next_fit')
	# first-fit
	expected_result = ProblemInstance(items=items, assignments=[0,0,1,2,0,0,1], free_space=[0.0944235195610001,0.185633858585855,0.0614623337778])
	test_algorithm(test7, expected_result, requirements.first_fit, 'first_fit')
	# first-fit decreasing
	expected_result = ProblemInstance(items=items, assignments=[0,1,2], free_space=[0,0,0])
	test_algorithm(test7, expected_result, requirements.first_fit_decreasing, 'first_fit_decreasing')
	# best-fit
	expected_result = ProblemInstance(items=items, assignments=[0,1,2], free_space=[0,0,0])
	test_algorithm(test7, expected_result, requirements.best_fit, 'best_fit')
	# best-fit decreasing
	expected_result = ProblemInstance(items=items, assignments=[0,1,2], free_space=[0,0,0])
	test_algorithm(test7, expected_result, requirements.best_fit_decreasing, 'best_fit_decreasing')
	
	print('\nMany items test')
	items = [0.2 for i in range(0, 200)] + [0.1 for i in range(0, 100)] + [0.4 for i in range(0, 200)]
	assignments = [0] * len(items)
	free_space = list()
	
	test9 = ProblemInstance(items = items, assignments=assignments, free_space=free_space)

	# next-fit
	assignments_c = [[i]*5 for i in range(0, 40)] + [[i]*10 for i in range(40, 50)] + [[i]*2 for i in range(50, 150)]
	assignments_c = list(itertools.chain.from_iterable(assignments_c))
	free_space_c = [0]*50 + [0.2]*100
	expected_result = ProblemInstance(items=items, assignments=assignments_c, free_space=free_space_c)
	test_algorithm(test9, expected_result, requirements.next_fit, 'next_fit')

	

if __name__ == '__main__':
	# zip_tree_tests()
	bin_packing_tests()
