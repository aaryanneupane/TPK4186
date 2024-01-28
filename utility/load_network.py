from module.Road_Network import Road_Network
from module.Node import Node
from module.Edge import Edge
import json

def load_network(file_path:str) -> Road_Network:
    with open(file_path, "r") as f:
        network_data = json.load(f)

    network_name = network_data["network_name"]
    node_size = network_data["node_size"]
    edge_size = network_data["edge_size"]
    node_codes = network_data["node_codes"]
    edge_codes = network_data["edge_codes"]
    edges_data = network_data["edges"]
    nodes_data = network_data["nodes"]

    loaded_network = Road_Network(network_name, nodes=node_size, edges=edge_size)

    # Replace the initiated nodes
    for node in loaded_network.nodes:
        node.code = node_codes.pop(0)

    # Replace the initiated edges
    for edge in loaded_network.edges:
        edge.code = edge_codes.pop(0)

    for edge_data in edges_data:
        edge = loaded_network.find_edge(edge_data["edge_code"])
        if edge:
            edge.sourceNode = loaded_network.find_node(edge_data["source_nodes"][0])
            edge.targetNode = loaded_network.find_node(edge_data["target_nodes"][0])
            edge.edgeType = edge_data["edge_type"]
            edge.length = edge_data["length"]
            edge.distribution.distribution = edge_data["distribution"]

    for node_data in nodes_data:
        node = loaded_network.find_node(node_data["node_code"])
        if node:
            node.inEdges = [loaded_network.find_edge(edge_code) for edge_code in node_data["in_edges"]]
            node.outEdges = [loaded_network.find_edge(edge_code) for edge_code in node_data["out_edges"]]
            node.attributes = node_data["attributes"]

    return loaded_network


        

        