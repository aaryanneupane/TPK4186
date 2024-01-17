from module.Node import Node 
from module.Edge import Edge
from typing import List

class Road_Network:
    def __init__(self, name:str, nodes=0, edges=0):
        self.name = name
        self.nodes:List[Node] = [Node(str(i+1)) for i in range(nodes)]
        self.edges:List[Edge] = [Edge(str(i+1)) for i in range(edges)]

    def change_name(self, name:str):
        self.name = name   

    def add_node(self, node:Node):
        self.nodes.append(node)

    def add_edge(self, edge:Edge):
        self.edges.append(edge)

    def find_node(self, node_code:str) -> Node | None:
        for node in self.nodes:
            if node.code == node_code:
                return node

    def find_edge(self, edge_code:str) -> Edge | None:
        for edge in self.edges:
            if edge.code == edge_code:
                return edge

    def delete_node(self, nodeIndex):
        self.nodes.remove(nodeIndex)

    def delete_edge(self, edgeIndex):
        self.edges.remove(edgeIndex)


