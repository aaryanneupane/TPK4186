from utility.load_network import load_network
from utility.save_network import save_network


loaded_network = load_network("networks/3x4_test.json")
loaded_network.change_name("generator_load_save_test")
save_network(loaded_network)