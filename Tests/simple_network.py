from Road_Networks import Road_Network;

# Create a new road network
network = Road_Network("Test Network", 3, 3);

# Defining the nodes
A = network.nodes[0]
A.code = 'A'

B = network.nodes[1]
B.code = 'B'

C = network.nodes[2]
C.code = 'C'

# Defining the edges
AB = network.edges[0]
AB.sourceNode = A
AB.targetNode = B
AB.length = 10

AC = network.edges[1]
AC.sourceNode = A
AC.targetNode = C
AC.length = 10

BC = network.edges[2]
BC.sourceNode = B
BC.targetNode = C
BC.edgeType = 'bi'
BC.length = 10

# Print the network
print(network.name)
print("Nodes:")
for node in network.nodes:
    print(node.code)
print("Edges:")
for edge in network.edges:
    print(edge.sourceNode.code, edge.targetNode.code, edge.edgeType, edge.length)