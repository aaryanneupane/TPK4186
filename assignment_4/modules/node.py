
class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.predecessors = []
        self.successors = []
        self.startDate = 0
        self.endDate = 0
        
    def __repr__(self) -> str:
        return self.name
        
        
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def setId(self, id):
        self.id = id
    
    def getPredecessors(self):
        return self.predecessors
    
    def addPredecessor(self, constraint):
        self.predecessors.append(constraint)

    def getSuccessors(self):
        return self.successors
    
    def addSuccessor(self, constraint):
        self.successors.append(constraint)

    def setStartDate(self, startDate):
        self.startDate = startDate

    def setEndDate(self, EndDate):
        self.endDate = EndDate

    def getStartDate(self) -> int:
        return self.startDate

    def getEndDate(self) -> int:
        return self.endDate 
  

