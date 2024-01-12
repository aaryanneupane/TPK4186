import module.Edge as ed

class Node:
    def __init__(self, code):
        self.code = code
        self.inEdges = []
        self.outEdges= []
        self.attributes = {}

    def change_code(self, new_code):
        self.code = new_code

    def add_inEdge(self, edge: ed.Edge):
        self.inEdges.append(edge)
        if edge.edgeType == "bi":
            self.outEdges.append(edge)

    def add_outEdge(self, edge: ed.Edge):
        self.outEdges.append(edge)
        if edge.edgeType == "bi":
            self.inEdges.append(edge)

    def delete_inEdge(self, edge: ed.Edge):
        self.inEdges.remove(edge)
        if edge.edgeType == "bi":
            self.outEdges.remove(edge)

    def delete_outEdge(self, edge: ed.Edge):
        self.outEdges.remove(edge)
        if edge.edgeType == "bi":
            self.inEdges.remove(edge)

    def add_Attribute(self, key, value):
        self.attributes[key] = value
