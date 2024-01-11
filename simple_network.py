from module.Road_Network import Road_Network

# Create a new road network
network = Road_Network("Test Network", 3, 3)

# Defining the nodes
A = network.nodes[0]
A.code = "A"

B = network.nodes[1]
B.code = "B"

C = network.nodes[2]
C.code = "C"

# Defining the edges
AB = network.edges[0]
AB.code = "AB"
AB.sourceNode = A
AB.targetNode = B
AB.length = 10

AC = network.edges[1]
AC.code = "AC"
AC.sourceNode = A
AC.targetNode = C
AC.length = 10

BC = network.edges[2]
BC.code = "BC"
BC.sourceNode = B
BC.targetNode = C
BC.edgeType = "bi"
BC.length = 10

# Update the inEdges and outEdges of the nodes
A.outEdges.append(AB)
A.outEdges.append(AC)

B.inEdges.append(AB)
B.outEdges.append(BC)

C.inEdges.append(AC)
C.inEdges.append(BC)

# Print the network stats
print(network.name)
print("Nodes:")
for node in network.nodes:
    print(node.code)
print("Edges:")
for edge in network.edges:
    print(edge.sourceNode.code, edge.targetNode.code, edge.edgeType, edge.length)

print("OutEdges of A:")
for edges in network.find_node("A").outEdges:
    print(edges.code)

print("InEdges of C:")
for edges in network.find_node("C").inEdges:
    print(edges.code)

print("OutEdges of C:")
for edges in network.find_node("C").outEdges:
    print(edges.code)

print("InEdges of B:")
for edges in network.find_node("B").inEdges:
    print(edges.code)

print("OutEdges of B:")
for edges in network.find_node("B").outEdges:
    print(edges.code)
