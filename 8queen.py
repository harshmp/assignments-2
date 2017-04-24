#load data from JSON
import json
inf = open("8queen.json")
board = json.loads(inf.read())
board = board["matrix"]

#display initial board configuration
for i in board:
	print i

#check if the postion is safe (not attacked by a queen)
def isSafe(row, col):
	for i in range(8):
		for j in range(8):
			if board[i][j] == 1:
				if row == i:
					return False
				if col == j:
					return False
				if abs(row-i) == abs(col-j):
					return False
	return True

#recursively place queens if safe
def placeQueen(col):
	if col >= 8:
		print "Scanned all columns."
		return True

	for i in range(8):
		if isSafe(i, col):
			board[i][col] = 1
			if placeQueen(col+1):
				return True
			board[i][col] = 0
	return False

#start with first column
if placeQueen(1):
	print "Solution found!"
else:
	print "Solution not found!"

#display the final board
for i in board:
	print i
