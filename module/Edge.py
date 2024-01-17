import module.Node as nd

class Edge:
    def __init__(self, code:str, edgeType = "uni", length = 0):
        self.code = code
        self.sourceNode = None
        self.targetNode = None
        self.edgeType = edgeType
        self.length = length

    def change_code(self, new_code:str):
        self.code = new_code

    def change_length(self, length:int):
        self.length = length

    def change_edgeType(self, edgeType:str):
        self.edgeType = edgeType
    
    def change_sourceNode(self, sourceNode:nd.Node):
        if self.sourceNode:
            self.sourceNode.delete_outEdge(self)
        self.sourceNode = sourceNode
        sourceNode.add_outEdge(self)
    
    def change_targetNode(self, targetNode:nd.Node):
        if self.targetNode:
            self.targetNode.delete_inEdge(self)
        self.targetNode = targetNode
        targetNode.add_inEdge(self)
