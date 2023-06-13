# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file

from __future__ import annotations
from random import random, randint
from math import log2


from typing import TypeVar
from dataclasses import dataclass

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

@dataclass
class Rank:
	def __init__(self, x=None, y=None):
		self.geometric_rank = x
		self.uniform_rank = y

	def __eq__(self, x):
		try:
			if self.geometric_rank == x.geometric_rank and self.uniform_rank == x.uniform_rank:
				return True
			else:
				return False
		except AttributeError as err: # x is None
			return False 

	def __lt__(self, x):
		if x == None:
			return False
		if self.geometric_rank < x.geometric_rank:
			return True
		elif self.geometric_rank > x.geometric_rank:
			return False
		else:
			if self.uniform_rank < x.uniform_rank:
				return True
			elif self.uniform_rank > x.uniform_rank:
				return False
			else:
				return False
			
	def __gt__(self, x):
		if x == None:
			return False
		return self.__lt__(x)
	
	def __le__(self, x):
		if x == None:
			return False
		return self.__lt__(x) or self.__eq__(x)
	
	def __ge__(self, x):
		if x == None:
			return False
		return x.__lt__(self) or self.__eq__(x)
			
	def __str__(self):
		return str({"geometric": self.geometric_rank, "uniform": self.uniform_rank})
	
	def toString(self):
		return "{Geometric: " + str(self.geometric_rank) + ", Uniform: " + str(self.uniform_rank) + "}"
		
class Node:
	def __init__(self, key, val, rank: Rank, left: Node = None, right: Node = None):
		self.key = key
		self.val = val
		self.rank = rank
		self.left = left
		self.right = right
	
	def __str__(self):
		return str({"Key": self.key, "Value": self.val, "Rank": self.rank.toString(), 
	      "Left Child": str(self.left), "Right Child": str(self.right)})
	
	def toString(self):
		return '{Key: ' + str(self.key) +  ', Value: ' + str(self.val) + ', Rank: ' + self.rank.toString() + ", Left Child: " + self.left.toString() + ", Right Child: " + self.right.toString() + '}'


class ZipZipTree:
	def __init__(self, capacity: int):
		
		self.__capacity = capacity
		self.root = None
		
		
	def get_random_rank(self) -> Rank:
		
		gm = 0
		x = random()
		while x >= 0.5:
			gm += 1
			x = random()

		upper = log2(self.__capacity) ** 3 - 1
		uni = randint(1, int(upper))

		return Rank(gm, uni)
		

	def insert(self, key: KeyType, val: ValType, rank: Rank = None):
		DEBUG = False
		
		new_rank = self.get_random_rank() if rank == None else rank
		x = Node(key, val, new_rank, None, None)
		
		cur = self.root
		while cur != None and (x.rank < cur.rank or (x.rank == cur.rank and x.key > cur.key)):
			# print("inf1")
			prev = cur
			if x.key < cur.key: cur = cur.left 
			else: cur = cur.right
			if DEBUG: 
				print("Cur: " + str(cur))
				print("Prev: " + str(prev))
		if DEBUG: print("out")
				
		
		
		if cur == self.root: 
			self.root = x
		elif x.key < prev.key:
			prev.left = x
		else: 
			prev.right = x

		if DEBUG: 
			print(self.__str__())
			print(x)
			print(prev)
		
		if cur == None: 
			x.left, x.right = (None, None) 
			return
		if x.key < cur.key:
			x.right = cur
		else:
			x.left = cur
		prev = x
		
		while cur != None:
			# print("inf2")
			fix = prev
			if cur.key < x.key:
				while True:
					# print("inf3")
					prev = cur
					cur = cur.right
					if cur == None or cur.key > key:
						break
			else:
				while True:
					# print("inf4")
					prev = cur
					cur = cur.left
					if cur == None or cur.key < key:
						break
			
			if fix.key > x.key or (fix == x and prev.key > x.key): fix.left = cur
			else: fix.right = cur


	def remove(self, key: KeyType):
		cur = self.root
		
		while key != cur.key:
			prev = cur
			cur = cur.left if key < cur.key else cur.right
		
		left, right = (cur.left, cur.right)

		if left == None: cur = right
		elif right == None: cur = left
		elif left.rank >= right.rank: cur = left
		else: cur = right

		if self.root.key == key: self.root = cur
		elif key < prev.key: prev.left = cur
		else: prev.right = cur

		while left != None and right != None:
			if left.rank >= right.rank:
				while True:
					prev = left
					left = left.right
					if left == None or left.rank < right.rank:
						break
				prev.right = right
			else:
				while True:
					prev = right
					right = right.left
					if right == None or left.rank >= right.rank:
						break
				prev.left = left
		

	def find(self, key: KeyType) -> ValType:
		cur = self.root
		while cur != None:
			if key < cur.key: 
				cur = cur.left
			elif key > cur.key:
				cur = cur.right
			else:
				return cur.val
			
		raise ValueError(f'Key {key} not found') # key not found

	def get_size(self) -> int:
		return self.size(self.root)

	def get_height(self) -> int:

		return self.height(self.root)
	
	def height(self, cur) -> int:

		if cur == None:
			return -1
		return 1 + max(self.height(cur.left), self.height(cur.right))
	
	def size(self, cur) -> int:
		if cur == None:
			return 0
		return 1 + self.size(cur.left) + self.size(cur.right)


	def get_depth(self, key: KeyType):
		depth = 0
		cur = self.root
		while cur != None:
			if key < cur.key: 
				cur = cur.left
				depth += 1
			elif key > cur.key:
				cur = cur.right
				depth += 1
			else:
				return depth
			
		return None # key not found
	
	def __str__(self):
		return str(self.root) + '\n'

	
	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
