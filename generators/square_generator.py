from module.Road_Network import Road_Network
from module.Edge import Edge
import numpy as np

def euclidean_distance(tuple1:tuple, tuple2:tuple):
    return round(np.linalg.norm(np.array(tuple2) - np.array(tuple1)),2)

def probability(distance) -> float:
    alpha = 0.2
    beta = 0.6
    return beta*float(np.exp((-1 * alpha)*distance))


def square_generator(name:str, n_nodes = 5) -> Road_Network:
    square_size = int(np.ceil(np.sqrt(n_nodes)) - 1) #Generate the smallest square according to the node size

    x_coords = [i for i in range(square_size + 1)]
    y_coords = [i for i in range(square_size + 1)]
    
    nodes_tuples = []

    for _ in range(n_nodes):
        point = (np.random.choice(x_coords), np.random.choice(y_coords))
        while point in nodes_tuples:
            point = (np.random.choice(x_coords), np.random.choice(y_coords))
        nodes_tuples.append(point)

    network = Road_Network(name, n_nodes)
    nodes = network.nodes

    edge_types = ["uni", "bi"]

    for i in range(n_nodes - 1):
        for j in range(i + 1, n_nodes):
            distance = euclidean_distance(nodes_tuples[i], nodes_tuples[j])
            prob = probability(distance)

            if np.random.uniform(0, 1) < prob:
                source_node = nodes[i]
                target_node = nodes[j]
                edge = Edge(f"{i + 1}-{j + 1}")
                edge.change_length(distance)
                edge.change_edgeType(np.random.choice(edge_types))
                network.add_edge(edge)
                edge.change_sourceNode(source_node)
                edge.change_targetNode(target_node)
    return network