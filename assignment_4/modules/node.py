
class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.predecessors = []
        self.successors = []
        self.start_date = None
        self.end_date = None
        
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def getPredeceddor(self):
        return self.predecessors
    
    def addPredecessor(self, constraint):
        self.predecessors.append(constraint)

    def getSucessor(self):
        return self.successors
    
    def addSuccessor(self, constraint):
        self.successors.append(constraint)
  

