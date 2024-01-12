from module.Node import Node 
from module.Edge import Edge
from typing import List

class Road_Network:
    def __init__(self, name, nodes=0, edges=0):
        self.name = name
        self.nodes:List[Node] = [Node('code') for i in range(nodes)]
        self.edges:List[Edge] = [Edge('code') for i in range(edges)]

    def add_node(self, node:Node):
        self.nodes.append(node)

    def add_edge(self, edge:Edge):
        self.edges.append(edge)

    def find_node(self, node_code:str):
        for node in self.nodes:
            if node.code == node_code:
                return node
        return None

    def find_edge(self, edge_code:str):
        for edge in self.edges:
            if edge.code == edge_code:
                return edge
        return None

    def delete_node(self, nodeIndex):
        self.nodes.remove(nodeIndex)

    def delete_edge(self, edgeIndex):
        self.edges.remove(edgeIndex)


