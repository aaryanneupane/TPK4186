from modules.node import Node
from modules.gate import Gate
from modules.task import Task
from modules.constraint import Constraint
from modules.lane import Lane
from modules.container import Container

class Project(Container):
    
    def _init_(self):
        Container.__init__(self,id)
        #self.id = id
        #self.name = name
        self.nodes = dict()
        self.constraints = []
        self.lanes = dict()
        
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def getNodes(self):
        return self.nodes.values()
    
    def lookForNode(self, id):
        return self.nodes.get(id, None)
        
    def newGate(self, id):
        gate = Gate(id)
        self.nodes[id] = gate
        return gate
    
    def newTask(self, id):
        task = Task(id)
        self.nodes[id] = task
        return task
    
    def getConstraints(self):
        return self.constraints
    
    def newConstraint(self, sourceNode, targetNode):
        constraint = Constraint(sourceNode, targetNode)
        self.constraints.append(constraint)
        return constraint
    
    def getLanes(self):
        return self.lanes.values()
    
    def lookForLane(self, id):
        return self.lanes.get(id, None)
    
    def newLane(self, id):
        lane = Lane(id)
        self.lanes[id] = lane
        return lane
    
    
        
    
           