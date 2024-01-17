from module.Road_Network import Road_Network
import numpy as np

def grid_network(name:str, rows:int, columns:int) -> Road_Network:
    num_nodes = rows * columns
    num_edges = (rows - 1) * columns + (columns - 1) * rows

    edge_types = ["uni", "bi"]

    network = Road_Network(name, num_nodes, num_edges)

    # Use NumPy for efficient array operations
    nodes_array = np.array(network.nodes).reshape((rows, columns))
    edges_list = np.array(network.edges).reshape((num_edges,))

    edge_counter = 0
    
    for row in range(rows - 1):
        for col in range(columns):
            # Vertical edges
            source_node = nodes_array[row, col]
            target_node = nodes_array[row + 1, col]
            edge = edges_list[edge_counter]
            edge.change_edgeType(np.random.choice(edge_types))
            edge.change_sourceNode(source_node)
            edge.change_targetNode(target_node)
            edge.change_length(2)
            edge_counter += 1

    for row in range(rows):
        for col in range(columns - 1):
            # Horizontal edges
            source_node = nodes_array[row, col]
            target_node = nodes_array[row, col + 1]
            edge = edges_list[edge_counter]
            edge.change_edgeType(np.random.choice(edge_types))
            edge.change_sourceNode(source_node)
            edge.change_targetNode(target_node)
            edge.change_length(2)
            edge_counter += 1

    return network
