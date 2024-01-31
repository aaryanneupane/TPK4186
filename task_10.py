from utility.load_network import load_network
from utility.save_network import save_network


loaded_network = load_network("networks/task_9_test, 5.json")

print(loaded_network.fastest_route("1", "5", "Monday", 400))
print(loaded_network.max_min("1", "2", "Monday"))

# save_network(loaded_network)