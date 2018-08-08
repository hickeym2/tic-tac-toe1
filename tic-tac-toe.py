# Mike Hickey
# WIT
#
# This game allows you to play tick-tac-toe

import numpy as np 

class grid:
	def __init__(self, slots):
		self.slots = slots

	def draw(self):
		print("     |   |   ")
		print("  " +self.slots[0]+ "  | " +self.slots[1]+ " |  " +self.slots[2] )
		print("     |   |   ")
		print("---------------")
		print("     |   |   ")
		print("  " +self.slots[3]+ "  | " +self.slots[4]+ " |  " +self.slots[5] )
		print("     |   |   ")
		print("---------------")
		print("     |   |   ")
		print("  " +self.slots[6]+ "  | " +self.slots[7]+ " |  " +self.slots[8] )
		print("     |   |   ")
		return 0

	def set_slot(self, symbol, position):
		self.slots[position] = symbol

		return self

	def set_slot_debug(self):
		for i in range(9):
			self.set_slot("x", i)

		return self

	def initialize_grid(self):
		for i in range(9):
			self.slots.append(" ")

		return self

	def reset(self):
		print("Resetting the game.")
		for i in range(9):
			self.slots[i] = " "

		return self

	def check_valid_move(self, position):
		the_move_is_valid = False

		# Is the move within the number of grids in the board
		if position <= 8 and position >= 0:
			# If the slot is empty. you can place a symbol there.
			if self.slots[position] == " ":
				the_move_is_valid = True
			else:
				print("Invalid Move.")
		else:
			print("Invalid Move.")

		return the_move_is_valid

	def check_winner(self):
		outcome = ""

		if grid.check("x"):
			outcome = "x"
		
		if grid.check("o"):
			outcome = "o"

		return outcome

	def check(self, symbol):
		# Check if x or o won.
		evaluation = False

		# Check horizontal
		if self.slots[0] == symbol and self.slots[1] == symbol and self.slots[2] == symbol:
			evaluation = True
		if self.slots[3] == symbol and self.slots[4] == symbol and self.slots[5] == symbol:
			evaluation = True
		if self.slots[6] == symbol and self.slots[7] == symbol and self.slots[8] == symbol:
			evaluation = True

		# Check vertical
		if self.slots[0] == symbol and self.slots[3] == symbol and self.slots[6] == symbol:
			evaluation = True
		if self.slots[1] == symbol and self.slots[4] == symbol and self.slots[7] == symbol:
			evaluation = True
		if self.slots[2] == symbol and self.slots[5] == symbol and self.slots[8] == symbol:
			evaluation = True

		# Check Cross
		if self.slots[0] == symbol and self.slots[4] == symbol and self.slots[8] == symbol:
			evaluation = True
		if self.slots[6] == symbol and self.slots[4] == symbol and self.slots[2] == symbol:
			evaluation = True

		return evaluation

	def check_tie(self, round_num):
		tie = False
		if round_num == 9:
			if self.check("x") != True and self.check("o") != True:
				tie = True

		return tie


def print_round(num_round):
	print("Current Round: " + str(num_round))

def change_player(round_num):
	if round_num % 2 == 0:
		symbol = "x"
	else:
		symbol = "o"
	return symbol


if __name__ == "__main__":
	print("tick-tac-toe")

	# Instantiate the grid.
	grid = grid([])

	# Initialize the grid to be blank
	grid.initialize_grid()

	num_games = 1000
	for i in range(num_games):


		round_num = 1

		# x goes first.
		symbol = "x"

		game_on = True
		while game_on:

			print_round(round_num)

			while True:
				# Print out the grid... for humans...
				grid.draw()

				# Get a move from the player
				position = input("Player " + symbol + " Please Pick A Slot From 0-8: ")
				position = int(position)
				# Check if that move is valid.
				if grid.check_valid_move(position):
					break
				
			# Since the move is valid, set the position
			grid.set_slot(symbol, position)

			# Check for a tie
			if grid.check_tie(round_num):
				print("Tie!")
				break

			# Check if anyone won
			outcome = grid.check_winner()
			if outcome == "x" or outcome == "o":
				# x or o won, end the game
				print(outcome + " won!")
				break

			# Since no one won, the next player can go.
			symbol = change_player(round_num)

			# Increment the round number
			round_num += 1

		# Reset the game.	
		grid.reset()	

