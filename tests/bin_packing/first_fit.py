from decimal import *

from zipzip_tree import ZipZipTree
from zipzip_tree import Node
from merge_sort import merge_sort

def find_largest_child(node: Node):
	left_max, right_max = (0, 0)
	if node.left != None:
		left_max = max(find_largest_child(node.left), Decimal(1) - Decimal(str(sum(node.left.val["contents"]))))
		node.val["left"] = left_max
	if node.right != None:
		right_max = max(find_largest_child(node.right), Decimal(1) - Decimal(str(sum(node.right.val["contents"]))))
		node.val["right"] = right_max
	return max(left_max, right_max)

def insert_target(cur, target, assignment, i):
	# Insert here 
	if target + Decimal(str(sum(cur.val["contents"]))) <= Decimal(1) and (cur.left == None or target > cur.val["left"]):
		cur.val["contents"].append(target)
		assignment[i] = cur.key
		# print(f'{target} was inserted to bin {cur.key}')
	# Insert in child
	elif cur.left != None and target <= cur.val["left"]:
		largest_space_after_insert = insert_target(cur.left, target, assignment, i)
		# update left/right child's space left depending on which one you inserted it into
		cur.val["left"] = largest_space_after_insert
	elif cur.right != None and target <= cur.val["right"]:
		largest_space_after_insert = insert_target(cur.right, target, assignment, i)
		cur.val["right"] = largest_space_after_insert
	else: 
		print(cur.val["left"], target)
		raise ValueError("bin not found")

	# return greatest space avail in child after insert i think, which is max of space of cur bin, space in left/right branches
	return max(cur.val["left"], cur.val["right"], ( Decimal(1) - Decimal(str(sum(cur.val["contents"]))) ))

def update_parents(cur, target):
	if cur.key == target:
		return cur
	elif cur.key < target:
		node = update_parents(cur.right, target)
		cur.val["right"] = Decimal(1)
		return node
	elif cur.key > target:
		node = update_parents(cur.left, target)
		cur.val["right"] = Decimal(1)
		return node
	else: raise ValueError("unknown error")


def first_fit(items: list[float], assignment: list[int], free_space: list[float]):
    
	# new zip zip tree
	tree = ZipZipTree(len(items))

	# while i is less than items.len:
	i = 0
	bin = -1
	while i < len(items):
        
		target = Decimal(str(items[i]))
		cur = tree.root
		# if traversal of zip tree finds no bins that can be entered into:
		if tree.get_size() == 0 or (cur.val["left"] < target and cur.val["right"] < target and target + Decimal(str(sum(cur.val["contents"]))) > 1):
			# Insrt new bin with correct index
			bin += 1
			tree.insert(bin, {"contents": [], "left": -1, "right": -1})

			"""
			# keep update parent nodes as necessary - do this by keeping track of a "trail" of parents before you get to the new bin
			path = []
			
			# print(str(tree))
			cur = tree.root
			while cur.key != bin:
				if cur.key > bin:
					path.append((cur, 0))
					cur = cur.left
				else:
					path.append((cur, 1))
					cur = cur.right

			for node in path:
				if node[1] == 0:
					node[0].val["left"] = Decimal(1)
				else:
					node[0].val["right"] = Decimal(1)
			"""
			target = update_parents(tree.root, bin)

			# update both childrens of the new bin
			find_largest_child(target)

			# print("tree updated to " + str(tree))

		# else there is a bin that can fit the item:
		else:
			
			insert_target(tree.root, target, assignment, i)
			i += 1
			
		
	#print(bin)
	# get the free spaces of the bins
	foo = [None]*(bin+1)
	# print(foo)
	#print(len(foo))
	j = 0
	while j < len(foo):
		if foo[j] != None: 
			j += 1
			continue
		
		cur = tree.root 
		# look for the bin and it's free space, filling up free spaces of bins we find along the way
		
		while cur.key != j:
			foo[j] = float(Decimal(1) - Decimal(sum(cur.val["contents"])))
			if j > cur.key:
				cur = cur.right
			else:
				cur = cur.left
		foo[j] = float(Decimal(1) - Decimal(sum(cur.val["contents"])))
		j += 1

	for i in foo:
		free_space.append(i)	


def first_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    
    merge_sort(items, reverse=True)
    first_fit(items, assignment, free_space)
	