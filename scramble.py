import random

BLANK = '-'
WIDTH = 3
HEIGHT = 3

def scramble(pieces, WIDTH, HEIGHT):
	# take pieces and mix up the order
	# take out one piece
	blank = int(random.random() * len(pieces))
	# pieces[blank] = BLANK

	for i in range(5):
		allowed = allowed_moves(blank, WIDTH, HEIGHT)
		choice = random.choice(allowed)
		blank, pieces = make_move(pieces, blank, choice, WIDTH, HEIGHT)
		# print_puzzle(pieces, blank, WIDTH, HEIGHT)
		# print("\n")
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
def get_picture(filename):
	# open filename, return the picture
	return ""
	
def get_slices(picture):
	# array of filenames for each slice
	# or just names in this case
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
	picture = get_picture("fake")
	pieces = get_slices(picture)
	blank, puzzle = scramble(pieces, WIDTH, HEIGHT)
	print(puzzle)
	print_puzzle(puzzle, blank, WIDTH, HEIGHT)
	while not solved(puzzle):
		move = input()
		blank, puzzle = make_move(puzzle, blank, int(move), WIDTH, HEIGHT)
		print(puzzle)
		print_puzzle(puzzle, blank, WIDTH, HEIGHT)


main()

def setup():
	picture = get_picture(filename)
	pieces = get_slices(picture)
	blank, puzzle = scramble(pieces)
	return blank, puzzle

def play(puzzle, blank):
	while not solved(puzzle):
		move = get_user_input()
		make_move(puzzle, move)



