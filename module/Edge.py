import module.Node as nd
class Edge:
    def __init__(self, code, edgeType = "uni", length = 0):
        self.code = code
        self.sourceNode = None
        self.targetNode = None
        self.edgeType = edgeType
        self.length = length

    def change_length(self, length):
        self.length = length

    def change_edgeType(self, edgeType):
        self.edgeType = edgeType
    
    def change_sourceNode(self, sourceNode):
        self.sourceNode = sourceNode
    
    def change_targetNode(self, targetNode):
        self.targetNode = targetNode
