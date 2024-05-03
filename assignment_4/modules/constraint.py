from  modules.node import Node

class Constraint:
    def __init__(self, sourceNode: Node, targetNode: Node):
        self.sourceNode = sourceNode
        self.targetNode = targetNode
        
    def __repr__(self) -> str:
        return f"{self.sourceNode} -> {self.targetNode}"
    
    def addSuccessor(self):
        self.sourceNode.addSuccessor(self)

    def addPredecessor(self):
        self.targetNode.addPredecessor(self)
    
    def getSourceNode(self):
        return self.sourceNode
    
    def setSourceNode(self, node):
        self.sourceNode = node
    
    def getTargetNode(self):
        return self.targetNode
    
    def setTargetNode(self, node):
        self.targetNode = node
    