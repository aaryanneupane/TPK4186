import module.Edge as ed
from typing import List

'''This class represents a node in a road network.'''

class Node:
    def __init__(self, code:str):
        self.code = code
        self.inEdges = []
        self.outEdges= []
        self.attributes = {}

    def change_code(self, new_code:str):
        self.code = new_code

    def add_inEdge(self, edge):
        self.inEdges.append(edge)
        if edge.edgeType == "bi":
            self.outEdges.append(edge)

    def add_outEdge(self, edge):
        self.outEdges.append(edge)
        if edge.edgeType == "bi":
            self.inEdges.append(edge)

    def delete_inEdge(self, edge):
        self.inEdges.remove(edge)
        if edge.edgeType == "bi":
            self.outEdges.remove(edge)

    def delete_outEdge(self, edge):
        self.outEdges.remove(edge)
        if edge.edgeType == "bi":
            self.inEdges.remove(edge)

    def add_Attribute(self, key:str, value:str):
        self.attributes[key] = value

    def get_targets_length(self):
        nodes = {}
        for edge in self.outEdges:
            if edge.edgeType == "bi" and self is not edge.sourceNode:
                nodes[edge.sourceNode.code] =  edge.length
            else:
                nodes[edge.targetNode.code] =  edge.length
        return nodes
    
    def get_targets_time(self, day:str, time: int):
        nodes = {}
        for edge in self.outEdges:
            if edge.edgeType == "bi" and self is not edge.sourceNode:
                nodes[edge.sourceNode.code] =  edge.distribution.interpolate(day, time)
            else:
                nodes[edge.targetNode.code] =  edge.distribution.interpolate(day, time)
        return nodes
    
    
