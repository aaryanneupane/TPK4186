
class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.predecessors = []
        self.successors = []
        self.start_date = None
        self.end_date = None
        
    def __repr__(self) -> str:
        return self.name
        
        
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def setId(self, id):
        self.id = id
    
    def getPredecessor(self):
        return self.predecessors
    
    def addPredecessor(self, constraint):
        self.predecessors.append(constraint)

    def getSuccessor(self):
        return self.successors
    
    def addSuccessor(self, constraint):
        self.successors.append(constraint)
  

