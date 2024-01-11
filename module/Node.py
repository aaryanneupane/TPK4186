class Node:
    def __init__(self, code):
        self.code = code
        self.inEdges = []
        self.outEdges = []
        self.Attributes = {}

        def add_inEdge(self, edge):
            self.inEdges.append(edge)

        def add_outEdge(self, edge):
            self.outEdges.append(edge)

        def delete_inEdge(self, edge):
            self.inEdges.remove(edge)

        def delete_outEdge(self, edge):
            self.outEdges.remove(edge)

        def add_Attribute(self, key, value):
            self.Attributes[key] = value