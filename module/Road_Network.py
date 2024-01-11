from module.Node import Node
from module.Edge import Edge

class Road_Network:
    def __init__(self, name, nodes=0, edges=0):
        self.name = name
        self.nodes = [Node('code') for i in range(nodes)]
        self.edges = [Edge('code') for i in range(edges)]

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def find_node(self, nodeCode):
        for node in self.nodes:
            if node.code == nodeCode:
                return node

    def find_edge(self, edgeIndex):
        return self.edges.index(edgeIndex)

    def delete_node(self, nodeIndex):
        self.nodes.remove(nodeIndex)

    def delete_edge(self, edgeIndex):
        self.edges.remove(edgeIndex)


