from utility.load_network import load_network
from utility.save_network import save_network

'''This is a test for the load_network method. It loads a network from a file and prints the network stats.
It also used to test the dijkstra methods.'''

loaded_network = load_network("networks/square_5_nodes.json")
loaded_network2 = load_network("networks/dijkstra_test.json")

print(loaded_network.has_path("3", "1"))
print(loaded_network.exists_any_path())

print(loaded_network.dijkstra("3", "1"))
print(loaded_network2.dijkstra("A", "F"))