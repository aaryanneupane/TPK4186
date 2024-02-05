from utility.load_network import load_network
from utility.save_network import save_network

'''This is a test for the fastest_route method. It loads a network from a file and finds the fastest route between two nodes.'''

loaded_network = load_network("networks/task_9_test, 5.json")
print(loaded_network.fastest_route("1", "5", "Monday", 400))