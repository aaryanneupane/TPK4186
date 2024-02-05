from generators.square_generator import square_generator
from utility.load_network import load_network
from utility.save_network import save_network

'''This i a test for the square_generator. It creates a network with 5 nodes and saves it to a file.'''

test_network = square_generator("task_9_test, 5")
save_network(test_network)

