import random

BLANK = '-'
WIDTH = 3
HEIGHT = 3

def scramble(pieces, WIDTH, HEIGHT):
	blank = int(random.random() * len(pieces))
	for i in range(5):
		allowed = allowed_moves(blank, WIDTH, HEIGHT)
		choice = random.choice(allowed)
		blank, pieces = make_move(pieces, blank, choice, WIDTH, HEIGHT)
	return blank, pieces

def solved(puzzle):
	# return true when the puzzle is solved
	# which means it's in order and only the last square is missing
	first = puzzle[0]
	for piece in puzzle[:-1]:
		if piece == BLANK:
			continue
		if int(piece) < int(first):
			return False
		first = int(piece)
	return True
	
def get_slices():
	return [
		str(i) for i in range(9)
	]

def get_user_input():
	# read from stdin for the move
	pass

def allowed_moves(blank, width, height):
	y = blank % width
	x = (blank - y) // width
	allowed = []
	if (y-1 >= 0):
		allowed.append(x * width + y - 1)
	if (y+1 < height):
		allowed.append(x * width + y + 1)
	if (x-1 >= 0):
		allowed.append((x-1)*width + y)
	if (x+1 < width):
		allowed.append((x+1)*width + y)
	return allowed

def make_move(puzzle, blank, move, width, height):
	# given a piece there is only one way to move it, so 
	# update puzzle to make the move happen
	if move in allowed_moves(blank, width, height):
		# swap move and blank in the puzzle
		tmp = puzzle[blank]
		puzzle[blank] = puzzle[move]
		puzzle[move] = tmp
		blank = move
	return blank, puzzle
def translate(direction, blank, width, height):
	y = blank % width
	x = (blank - y) // width
	if direction == "l":
		return x * width + y + 1
	if direction == "r":
		return x * width + y - 1
	if direction == "u":
		return (x+1)*width + y
	if direction == "d":
		return (x-1)*width + y

def print_puzzle(puzzle, blank, width, height):
	for row in range(height):
		line = ''
		for col in range(width):
			if row*width + col == blank:
				line += "- "
			else:
				line += puzzle[row*width + col] + " "
		print(line)

def main():
	pieces = get_slices()
	blank, puzzle = scramble(pieces, WIDTH, HEIGHT)
	# print(puzzle)
	print_puzzle(puzzle, blank, WIDTH, HEIGHT)
	while not solved(puzzle):
		direction = input() 
		move = translate(direction, blank, WIDTH, HEIGHT)
		blank, puzzle = make_move(puzzle, blank, int(move), WIDTH, HEIGHT)
		# print(puzzle)
		print_puzzle(puzzle, blank, WIDTH, HEIGHT)
	print("You solved it!")

main()


