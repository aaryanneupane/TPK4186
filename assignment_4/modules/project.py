from modules.node import Node
from modules.gate import Gate
from modules.task import Task
from modules.constraint import Constraint
from modules.lane import Lane
from modules.container import Container

class Project:
    
    def __init__(self, id, name):
        #Container.__init__(self)
        self.id = id
        self.name = name
        self.tasks = dict()
        self.constraints = []
        self.lanes = dict()
        self.gates = dict()
        
    def getName(self):
        return self.name
        
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def getNodes(self):
        return self.nodes.values()
    
    def lookForNode(self, id):
        return self.tasks.get(id, None)
        
    def newGate(self, id):
        gate = Gate(id)
        self.nodes[id] = gate
        return gate
    
    def newTask(self,id, name):
        task = Task(id,name)
        self.tasks[id] = task
        return task
    
    def getConstraints(self):
        return self.constraints
    
    def newConstraint(self, sourceNode, targetNode):
        constraint = Constraint(sourceNode, targetNode)
        self.constraints.append((sourceNode,targetNode))
        return constraint
    
    def getLanes(self):
        return self.lanes.values()
    
    def lookForLane(self, id):
        return self.lanes.get(id, None)
    
    def newLane(self, id, name):
        lane = Lane(id, name)
        self.lanes[id] = lane
        return lane
    
    def newGate(self, id, name):
        gate = Gate(id, name)
        self.gates[id] = gate
        return gate
 
    
    def getGates(self):
        return self.gates.values()
    
    def getTasks(self):
        return self.tasks.values()
    
    
    
        
    
           