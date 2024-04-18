from modules.node import Node

class Gate(Node):
    def __init__(self, id, name):
        Node.__init__(self, id)
        self.id = id
        self.name = name
       # self.name = name
        
       
    def getName(self):
        return self.name
    
