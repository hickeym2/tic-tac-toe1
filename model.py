# Michael Hickey
# Neural Network Model for Tic-Tac-Toe

from keras.models import Sequential
from keras.layers import Dense
import numpy as np 
import os

os.chdir("dataset")

if __name__ == "__main__":
	# Fix the random seed so you can reproduce the sequence.
	np.random.seed(1)

	# Load a dataset.
	dataset = np.loadtxt("tic_tac_toe_dataset.csv", delimiter = ",")
	
	# We want all the rows, and only 4 columns.
	input_data = dataset[ : , 0:9]
	answer = dataset[ : , 9]

	# Define the model
	model = Sequential()

	# Add layers to the network.
	model.add(Dense(12, input_dim = 9, activation = "relu") )
	# Second Layer
	model.add(Dense(10, activation = "relu") )
	# Third Layer
	model.add(Dense(8, activation = "relu") )
	# Fourth Layer
	model.add(Dense(4, activation = "relu") )	
	# This is the output layer, notice there is one neuron for the output.
	model.add(Dense(1, activation = "linear") )

	# Compile the model.
	model.compile(loss = "mse", optimizer = "adam", metrics = ["accuracy"])

	size_of_dataset = 1000
	model.fit(input_data, answer, epochs = size_of_dataset, batch_size = 25)

	# Score the model.
	scores = model.evaluate(input_data, answer)
	print("\n%s: %.2f%%" %(model.metrics_names[1], scores[1]*100) )