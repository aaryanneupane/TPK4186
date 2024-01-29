from generators.square_generator import square_generator
from utility.load_network import load_network
from utility.save_network import save_network


test_network = square_generator("task_9_test, 5")
save_network(test_network)

