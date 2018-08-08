# Mike Hickey
# WIT
#
# This game allows you to play tick-tac-toe

import numpy as np
import random
import time
import os

os.chdir("dataset")


class Grid:
	def __init__(self):
		self.slots = []


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
		self.slots = []
		for i in range(9):
			self.slots.append(" ")

		return self


	def reset(self):
		self.initialize_grid()
		for i in range(9):
			self.slots[i] = " "

		return self


	def check_valid_move(self, position, h_or_d):
		the_move_is_valid = False

		# Is the move within the number of grids in the board
		if position <= 8 and position >= 0:
			# If the slot is empty. you can place a symbol there.
			if self.slots[position] == " ":
				the_move_is_valid = True
			else:
				if h_or_d == "human":
					print("Invalid Move.")
		else:
			if h_or_d == "human":
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
		# If its round nine, and no one won, then its a tie.
		if round_num == 9:
			if self.check("x") != True and self.check("o") != True:
				tie = True

		return tie

	def add_to_dataset(self, winner, dataset):

		# Change every string in a slot to an integer.
		for i in range( len(self.slots) ):
	
			if self.slots[i] == "x":
				self.slots[i] = 1

			if self.slots[i] == "o":
				self.slots[i] = 2

			# The slot was empty, so declare it as 0.
			if self.slots[i] == " ":
				self.slots[i] = 0

		# Convert the winner to an integer
		if winner == "x":
			winner = 1
		if winner == "o":
			winner = 2
		if winner == "tie":
			winner = 3

		self.slots.append(winner)
		dataset.append(self.slots)

		return dataset

	def save_dataset(self, dataset):
		# Save the dataset to a *.csv
		np_dataset = np.asarray(dataset)
		print(np_dataset)
		np.savetxt("tic_tac_toe_temp.csv", np_dataset, delimiter = ",")

		return 0


def print_round(num_round):
	print("Current Round: " + str(num_round))

	return 0


def change_player(round_num):
	if round_num % 2 == 0:
		symbol = "x"
	else:
		symbol = "o"

	return symbol


def rng_action():
	slot = random.randint(0, 9)

	return slot


def menu():
	print("tick-tac-toe")
	while True:
		choice = input("Type in \"human\" or \"dataset\": ")
		if choice == "human" or choice == "dataset":
			# Start the game.
			break	

	return choice


if __name__ == "__main__":
	try:
		# Seed the random number generator	
		random.seed(time.time())

		# Instantiate the grid.
		grid = Grid()

		# Initialize the grid to be blank
		grid.initialize_grid()

		# Display a menu, choose if humans want to play or make a dataset
		human_or_dataset = menu()

		# Empty dataset at the start
		dataset = []

		num_games = 10
		for i in range(num_games):
			# Initialize the outcome of the game to be a tie.
			winner = "tie"

			# ROUND 1, FIGHT
			round_num = 1

			# x goes first.
			symbol = "x"

			game_on = True
			while game_on:

				if human_or_dataset == "human":
					print_round(round_num)

				while True:

					if human_or_dataset == "human":
						# Print out the grid... for humans...
						grid.draw()
						
						while  True:
							try:
								# Get a move from the player
								position = int( input("Player " + symbol + " Please Pick A Slot From 0-8: ") )
								
								if isinstance(position, int):
									break
							except ValueError:
								pass

					else:
						position = rng_action()

					# Check if that move is valid.
					if grid.check_valid_move(position, human_or_dataset):
						break
					
				# Since the move is valid, set the position
				grid.set_slot(symbol, position)

				# Check for a tie
				if grid.check_tie(round_num):
					winner = grid.check_tie(round_num)
					if human_or_dataset == "human":
						print("Tie!")
					break

				# Check if anyone won
				outcome = grid.check_winner()
				if outcome == "x" or outcome == "o":
					# x or o won, end the game
					winner = grid.check_winner()
					if human_or_dataset == "human":
						print(outcome + " won!")
					break

				# Since no one won, the next player can go.
				symbol = change_player(round_num)

				# Increment the round number
				round_num += 1

			if human_or_dataset == "dataset":
				# Save the dataset
				dataset = grid.add_to_dataset(winner, dataset)
				
			# Reset the game.
			grid.reset()

		# After all the games are played, save the *.csv
		if human_or_dataset == "dataset":
			grid.save_dataset(dataset)	
	
	except KeyboardInterrupt:
		print("\nExiting Game. Thanks!")
