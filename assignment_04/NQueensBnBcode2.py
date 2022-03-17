"""N Queen Problem using Branch and Bound """

N = int(input("Enter value of N-"))

"""To print solution of N Queens problem"""
def printSolution(board):
	print("NQueen solution-")
	for i in range(N):
		for j in range(N):
			print (board[i][j], end = " ")
		print()

""" A Optimized function to check if a queen can be placed on board[row][col] """
def isSafe(row, col, diagonal1, diagonal2,
						rowLookup, diagonal1Lookup,
						diagonal2Lookup):
	if (diagonal1Lookup[diagonal1[row][col]] or
		diagonal2Lookup[diagonal2[row][col]] or
		rowLookup[row]):
		return False
	return True

""" A recursive utility function
to solve N Queen problem """
def solveNQueensUtil(board, col, diagonal1, diagonal2,
						rowLookup, diagonal1Lookup,
						diagonal2Lookup):
						
	""" base case: If all queens are
	placed then return True """
	if(col >= N):
		return True
	for i in range(N):
		if(isSafe(i, col, diagonal1, diagonal2,
						rowLookup, diagonal1Lookup,
						diagonal2Lookup)):
					
			""" Place this queen in board[i][col] """
			board[i][col] = 1
			rowLookup[i] = True
			diagonal1Lookup[diagonal1[i][col]] = True
			diagonal2Lookup[diagonal2[i][col]] = True
			
			""" recur to place rest of the queens """
			if(solveNQueensUtil(board, col + 1,
								diagonal1, diagonal2,
						rowLookup, diagonal1Lookup,
						diagonal2Lookup)):
				return True
			
			""" If placing queen in board[i][col]
			doesn't lead to a solution,then backtrack """
			
			""" Remove queen from board[i][col] """
			board[i][col] = 0
			rowLookup[i] = False
			diagonal1Lookup[diagonal1[i][col]] = False
			diagonal2Lookup[diagonal2[i][col]] = False
			
	""" If queen can not be place in any row in
	this column col then return False """
	return False

def solveNQueens():
	board = [[0 for i in range(N)]
				for j in range(N)]
	
	# helper matrices
	diagonal1 = [[0 for i in range(N)]
					for j in range(N)]
	diagonal2 = [[0 for i in range(N)]
						for j in range(N)]
	
	# arrays to tell us which rows are occupied
	rowLookup = [False] * N
	
	# keep two arrays to tell us
	# which diagonals are occupied
	x = 2 * N - 1
	diagonal1Lookup = [False] * x
	diagonal2Lookup = [False] * x
	
	# initialize helper matrices
	for rr in range(N):
		for cc in range(N):
			diagonal1[rr][cc] = rr + cc
			diagonal2[rr][cc] = rr - cc + (N-1)
	
	if(solveNQueensUtil(board, 0, diagonal1, diagonal2,
						rowLookup, diagonal1Lookup,
						diagonal2Lookup) == False):
		print("Solution does not exist for N ={}".format(N))
		return False
		
	# solution found
	printSolution(board)
	return True

# Driver Cde
solveNQueens()
