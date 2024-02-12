from generators.grid_generator import grid_generator
from utility.save_network import save_network
from generators.square_generator import square_generator

'''This is a test for the grid_generator. It creates a network with 3x4 nodes and saves it to a file.'''

test_grid = grid_generator("3x4_test", 3, 4)
# save_network(test_grid)


# complex_grid = grid_network('5x5_grid', 5, 5)
# save_network(complex_grid)
