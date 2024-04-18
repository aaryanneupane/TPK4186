from modules.node import Node

class Task(Node):
    def __init__(self, id, name):
        Node.__init__(self,id)
        self.name = name
        self.minimumDuration = 0
        self.maximumDuration = 0
        self.expectedDuration = 0
        
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

    def getName(self):
        return self.name
