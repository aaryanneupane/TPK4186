import module.Node as nd
import module.Empirical_distribution as ed
from numpy import floating

class Edge:
    def __init__(self, code:str, edgeType = "uni", length = 1):
        self.code = code
        self.sourceNode = None
        self.targetNode = None
        self.edgeType = edgeType
        self.length = length
        self.distribution = {"Monday": ed.EmpiricalDistribution(self), "Tuesday": ed.EmpiricalDistribution(self), "Wednesday": ed.EmpiricalDistribution(self), "Thursday": ed.EmpiricalDistribution(self), "Friday": ed.EmpiricalDistribution(self), "Saturday": ed.EmpiricalDistribution(self), "Sunday": ed.EmpiricalDistribution(self)}

    def change_code(self, new_code:str):
        self.code = new_code

    def change_length(self, length:floating):
        self.length = length

    def change_edgeType(self, edgeType:str):
        self.edgeType = edgeType
    
    def change_sourceNode(self, sourceNode):
        if self.sourceNode:
            self.sourceNode.delete_outEdge(self)
        self.sourceNode = sourceNode
        sourceNode.add_outEdge(self)
    
    def change_targetNode(self, targetNode):
        if self.targetNode:
            self.targetNode.delete_inEdge(self)
        self.targetNode = targetNode
        targetNode.add_inEdge(self)

    