## Each input grid will be a string of values from the puzzle 
## where empty entries will be 0 

grid = "000260701680070090190004500820100040004602900050003028009300074040050036703018000"

def change_grid(puzzle):
	"""
	Change the given puzzle into a grid 
	[[row1], [row2], ... , [row9]]
	"""
	grid = []
	for i in range(0, 9):
		grid.append([int(j) for j in list(puzzle[i*9:i*9+10])])
	return grid 

grid = change_grid(grid)
# print grid
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
				return row,col

	return -1, -1



def entry_val(grid):
	"""
	Given a grid, represented as a string, determine 
	all possible candidates for the entries and write it in
	a string format. The output will be a dictionary that maps
	each entry to all its possible values
	"""
	digits = '123456789'
	values = []
	for i in range(len(grid)):
		if grid[i] == '0':
			values.append(digits)
		else:
			values.append(grid[i])
	return dict(zip(range(1, 82), values))

# for i in range(1,10): 
	
	# if i%9!=0: col_peers = [j if i!=9 else j+9 for j in range(i%9, (i%9)+81, 9) if j!=i]
	# else: col_peers = [j+9 for j in range(i%9, (i%9)+81, 9) if j+9!=i]# print entry_val(grid)

def peers(grid):
	"""
	Given a grid, determine peers of each entries for row, 
	column, and square. Represent it in the form of a dictionary
	{entry:[row_peers, col_peers, square_peers]}
	"""
	for i in range(1, len(grid)+1):
		#constructing row_peers, col_peers, square_peers 
		row_peers = [j if i%9!=0 else j-9 for j in range((i/9)*9+1, (i/9)*9+10)]
		col_peers = [j if i%9!=0 else j+9 for j in range(i%9, (i%9)+81, 9)]
		row_peers.remove(i), col_peers.remove(i), square_peers.remove(i)




def eliminate(grid):
	"""
	Given a grid, eliminate any infeasbile candidates that could fill up each 
	entry, determined by examining the corresponding row, column, and square. 
	Only eliminate when one of the entries in either row, column, or the square 
	is completely determined
	"""
	return

def fib(max):
	a,b=0,1
	while a<max:
		yield a
		a, b, = b, a+b

a = fib(5)
print len(a)