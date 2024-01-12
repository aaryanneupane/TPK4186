from module.Road_Network import Road_Network

# Create a new road network
simple_network = Road_Network("Test Network", 3, 3)

# Defining the nodes
A = simple_network.nodes[0]
A.change_code('A')

B = simple_network.nodes[1]
B.code = "B"

C = simple_network.nodes[2]
C.code = "C"

# Defining the edges
AB = simple_network.edges[0]
AB.change_code("AB")
AB.change_sourceNode(A)
AB.change_targetNode(B)
AB.change_length(10)

AC = simple_network.edges[1]
AC.change_code("AC")
AC.change_sourceNode(A)
AC.change_targetNode(C)
AC.change_length(10)

BC = simple_network.edges[2]
BC.change_code("BC")
BC.change_sourceNode(B)
BC.change_targetNode(C)
BC.change_edgeType("bi")
BC.change_length(10)

# Update the inEdges and outEdges of the nodes
A.add_outEdge(AB)
A.add_outEdge(AC)

B.add_inEdge(AB)
B.add_inEdge(BC)
B.add_outEdge(BC)


C.add_inEdge(AC)
C.add_inEdge(BC)
C.add_outEdge(BC)

# Print the network stats
print(simple_network.name)
print("Nodes:")
for node in simple_network.nodes:
    print(node.code)
print("Edges:")
for edge in simple_network.edges:
    if edge.sourceNode and edge.targetNode:
        print(edge.sourceNode.code, edge.targetNode.code, edge.edgeType, edge.length)

print("OutEdges of A:")
node_A = simple_network.find_node("A")
if node_A and node_A.outEdges:
    for edges in node_A.outEdges:
        print(edges.code)

print("InEdges of C:")
node_C = simple_network.find_node("C")
if node_C and node_C.inEdges:
    for edges in node_C.inEdges:
        print(edges.code)

print("OutEdges of C:")
if node_C and node_C.outEdges:
    for edges in node_C.outEdges:
        print(edges.code)

print("InEdges of B:")
node_B = simple_network.find_node("B")
if node_B and node_B.inEdges:
    for edges in node_B.inEdges:
        print(edges.code)

print("OutEdges of B:")
if node_B and node_B.outEdges:
    for edges in node_B.outEdges:
        print(edges.code)

from utility.save_network import save_network

save_network(simple_network)
