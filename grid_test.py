from generators.grid_generator import grid_network
from utility.save_network import save_network

test_grid = grid_network('3x4_test', 3, 4)
save_network(test_grid)


complex_grid = grid_network('5x5_grid', 5, 5)
save_network(complex_grid)