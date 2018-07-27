from collections import defaultdict
from copy import deepcopy
import sys
import time

## Each input grid will be a string of values from the puzzle 
## where empty entries will be 0 

grid = "000260701680070090190004500820100040004602900050003028009300074040050036703018000"
# grid1="100489006730000040000001295007120600500703008006095700914600000020000037800512004"
# grid2="020608000580009700000040000370000500600000004008000013000020000009800036000306090"
# grid3="090700006010004000000068003407000900000006052000001008260400000300620080008007000"

def change_grid(puzzle):
	"""
	Change the given puzzle into a grid 
	[[row1], [row2], ... , [row9]]
	"""
	grid = []
	for i in range(0, 9):
		grid.append([int(j) for j in list(puzzle[i*9:i*9+9])])
	return grid 

def visualize(grid):
	"""
	Visualize the grid into easily readable format
	"""
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in grid]))

def is_empty(grid, i, j):
	"""
	Determine if any of entries following row i and column j is empty. In other words,
	return the first entry whose value is 0
	"""
	for row in range(i, 9):
		for col in range(j, 9):
			if grid[row][col] == 0:
				return row,col

	for row in range(0, 9):
		for col in range(0, 9):
			if grid[row][col] == 0:
				return row, col

	return -1, -1

def candidate(grid):
	"""
	Given the grid, determine all feasible candidates for 
	every entries. Return a dictionary {entries : possible candidates} 
	"""
	# candidate = defaultdict(lambda x:defaultdict())
	candidate = {}
	for i in range(0, 9):
		col_entries = defaultdict(str)
		for j in range(0, 9):
			entry = ''
			for k in range(1,10):
				if (grid[i][j] == 0 and k not in grid[i] and k not in [grid[l][j] for l in range(0,9)] and 
					k not in [grid[m][n] for m in range(int(i/3)*3, int(i/3)*3+3) for n in range(int(j/3)*3, int(j/3)*3+3)]):
					entry += str(k)
			if len(entry) == 1:
				grid[i][j] = int(entry) ##if only one possible candidate for the entry, fill it up
			elif len(entry)!=0:
				col_entries[j] = entry
		candidate[i] = col_entries 
	return candidate	

def sudoku_solver(grid, a=0, b=0):
	"""
	Given the grid (sudoku puzzle), solve it using the idea of constraint propagation
	and backtracking
	"""
	i, j = is_empty(grid, a, b)
	if i == -1 and j==-1:
		visualize(grid)
		return True	##sudoku solved!

	else:
		init = candidate(grid)
		i, j = is_empty(grid, a, b)
		if i==-1 and j==-1:
			visualize(grid)
			return True ## This part was added since candidate function changes the grid and thus need to check again
		for k in init[i][j]:
			if (int(k) not in grid[i] and int(k) not in [grid[l][j] for l in range(0,9)] and 
				int(k) not in [grid[m][n] for m in range(int(i/3)*3, int(i/3)*3+3) for n in range(int(j/3)*3, int(j/3)*3+3)]):

				c = 0
				new_grid = deepcopy(grid)
				new_grid[i][j] = int(k)

				if b+1<9: b+=1; c+=1
				else: a+=1; b=0; c-=1

				if sudoku_solver(new_grid,a,b):
					return True
				else:
					if c==1: b-=1
					else: a-=1; b=8
			else:
				pass

	return False

if __name__=="__main__":
	grid = sys.argv[1]
	grid = change_grid(grid)
	visualize(grid)
	print('\n')
	start = time.clock()
	sudoku_solver(grid)
	end = time.clock()
	print("time elapse = ", end-start)



