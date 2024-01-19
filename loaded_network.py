from utility.load_network import load_network
from utility.save_network import save_network


loaded_network = load_network("networks/square_3_nodes.json")
# loaded_network.change_name("square_load_save_test")

print(loaded_network.has_path("2", "1"))
print(loaded_network.exists_any_path())

loaded_network.calculate_length("1", "2")

# save_network(loaded_network)
