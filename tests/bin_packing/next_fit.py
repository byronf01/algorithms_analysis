# Example file: next_fit.py

# explanations for member functions are provided in requirements.py

# from Cfloat import CFloat
from decimal import *

def next_fit(items: list[float], assignment: list[int], free_space: list[float]):
	space_left = Decimal(1)
	current_bin = 0
	i = 0
	while i < len(items):
		cur = Decimal(str(items[i]))
		if cur <= space_left: # Add to this bin
			space_left -= cur
			assignment[i] = current_bin
			i += 1
		else: # Make new bin and try again with this item
			free_space.append(float(space_left))
			space_left = Decimal(1)
			current_bin += 1
	free_space.append(float(space_left))