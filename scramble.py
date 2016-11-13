import random
BLANK = '-'

class Puzzle():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.puzzle = self.get_slices()
		self.scramble()

	def scramble(self):
		self.blank = int(random.random() * len(self.puzzle))
		for i in range(5):
			allowed = self.allowed_moves()
			choice = random.choice(allowed)
			self.swap_pieces(choice)

	def solved(self):
		# return true when the puzzle is solved
		# which means it's in order and only the last square is missing
		first = self.puzzle[0]
		for piece in self.puzzle[:-1]:
			if piece == BLANK:
				continue
			if int(piece) < int(first):
				return False
			first = int(piece)
		return True
		
	def get_slices(self):
		return [
			str(i) for i in range(self.width * self.height)
		]

	def allowed_moves(self):
		y = self.blank % self.width
		x = (self.blank - y) // self.width
		allowed = []
		if (y-1 >= 0):
			allowed.append(x * self.width + y - 1)
		if (y+1 < self.height):
			allowed.append(x * self.width + y + 1)
		if (x-1 >= 0):
			allowed.append((x-1)*self.width + y)
		if (x+1 < self.width):
			allowed.append((x+1)*self.width + y)
		return allowed

	def swap_pieces(self, move):
		if move in self.allowed_moves():
			# swap move and blank in the puzzle
			tmp = self.puzzle[self.blank]
			self.puzzle[self.blank] = self.puzzle[move]
			self.puzzle[move] = tmp
			self.blank = move

	def make_move(self, direction):
		move = self.translate(direction)
		self.swap_pieces(move)
		
	def translate(self, direction):
		y = self.blank % self.width
		x = (self.blank - y) // self.width
		if direction == "l":
			return x * self.width + y + 1
		if direction == "r":
			return x * self.width + y - 1
		if direction == "u":
			return (x+1)*self.width + y
		if direction == "d":
			return (x-1)*self.width + y

	def print_puzzle(self):
		for row in range(self.height):
			line = ''
			for col in range(self.width):
				if row*self.width + col == self.blank:
					line += "- "
				else:
					line += self.puzzle[row*self.width + col] + " "
			print(line)

# def main():
# 	puzzle = Puzzle(WIDTH, HEIGHT)
# 	puzzle.print_puzzle()
# 	while not puzzle.solved():
# 		direction = input() 
# 		puzzle.make_move(direction)
# 		puzzle.print_puzzle()
# 	print("You solved it!")

# main()


