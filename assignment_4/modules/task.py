from modules.node import Node

class Task(Node):
    def __init__(self, id, name):
        Node.__init__(self,id, name)
        self.minimumDuration = 0
        self.maximumDuration = 0
        self.expectedDuration = 0
        self.actualDuration = 0
        
    
        
    def getMinimumDuration(self):
        return self.minimumDuration
    
    def setMinimumDuration(self, duration):
        self.minimumDuration = duration
    
    def getMaximumDuration(self):
        return self.maximumDuration
    
    def setMaximumDuration(self, duration):
        self.maximumDuration = duration
    
    def getExpectedDuration(self):
        return self.expectedDuration
    
    def setExpectedDuration(self, duration):
        self.expectedDuration = duration

    def getActualDuration(self) ->int:
        return self.actualDuration
    
    def setActualDuration(self, duration):
        self.actualDuration = duration

   