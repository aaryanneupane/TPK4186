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

    #Got help from chatGPT
    def has_path(self, start_node_code: str, end_node_code: str) -> bool:
        start_node = self.find_node(start_node_code)
        end_node = self.find_node(end_node_code)

        if not start_node or not end_node:
            return False

        visited = set()

        def dfs(current_node):
            if current_node == end_node:
                return True
            visited.add(current_node)

            for edge in current_node.outEdges:
                neighbor = edge.targetNode
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(start_node)
    
    def exists_any_path(self) -> bool:
        all_nodes = self.nodes
        for start_node in all_nodes:
            for end_node in all_nodes:
                if start_node != end_node:
                    if not self.has_path(start_node.code, end_node.code):
                        return False
        return True