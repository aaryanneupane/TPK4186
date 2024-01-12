from utility.load_network import load_network

loaded_network = load_network("networks/Test Network.json")

# Print the network stats
print(loaded_network.name)
print("Nodes:")
for node in loaded_network.nodes:
    print(node.code)
print("Edges:")
for edge in loaded_network.edges:
    if edge.sourceNode and edge.targetNode:
        print(edge.sourceNode.code, edge.targetNode.code, edge.edgeType, edge.length)


print("InEdges of A:")
node_A = loaded_network.find_node("A")
if node_A and node_A.inEdges:
    for edges in node_A.inEdges:
        print(edges.code)

print("OutEdges of A:")
if node_A and node_A.outEdges:
    for edges in node_A.outEdges:
        print(edges.code)

print("InEdges of C:")
node_C = loaded_network.find_node("C")
if node_C and node_C.inEdges:
    for edges in node_C.inEdges:
        print(edges.code)

print("OutEdges of C:")
if node_C and node_C.outEdges:
    for edges in node_C.outEdges:
        print(edges.code)

print("InEdges of B:")
node_B = loaded_network.find_node("B")
if node_B and node_B.inEdges:
    for edges in node_B.inEdges:
        print(edges.code)

print("OutEdges of B:")
if node_B and node_B.outEdges:
    for edges in node_B.outEdges:
        print(edges.code)