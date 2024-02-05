from module.Road_Network import Road_Network
import os
import json

'''This method saves a network to a file in our chosen json format.'''

def save_network(Road_Network:Road_Network):
    directory_path = "networks"
    os.makedirs(directory_path, exist_ok=True)
    file_path = os.path.join(directory_path, Road_Network.name + ".json")

    network_data = {
        "network_name": Road_Network.name,
        "node_size": len(Road_Network.nodes),
        "edge_size": len(Road_Network.edges),
        "node_codes": [node.code for node in Road_Network.nodes],
        "edge_codes": [edge.code for edge in Road_Network.edges],
        "edges": [],
        "nodes": [],
    }

    for edge in Road_Network.edges:
        if edge.sourceNode and edge.targetNode:
            edge_data = {
                "edge_code": edge.code,
                "source_nodes": [edge.sourceNode.code],
                "target_nodes": [edge.targetNode.code],
                "edge_type": edge.edgeType,
                "length": edge.length,
                "distribution": edge.distribution.distribution,
            }
            network_data["edges"].append(edge_data)

    for node in Road_Network.nodes:
        node_data = {
            "node_code": node.code,
            "in_edges": [edge.code for edge in node.inEdges],
            "out_edges": [edge.code for edge in node.outEdges],
            "attributes": node.attributes,
        }
        network_data["nodes"].append(node_data)

    with open(file_path, "w") as f:
        json.dump(network_data, f, indent=2)
