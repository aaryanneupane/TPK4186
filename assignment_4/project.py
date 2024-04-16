#Table of contents, classes
#1. Nodes
#2. Gates
#3. Tasks
#4. precedenceConstraints
#5. Lanes
#6. Projects


class Node:
    def __init__(self, id):
        self.id = id
        self.inConstraints = []
        self.outConstraints = []
        
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def getInConstraints(self):
        return self.inConstraints
    
    def addInConstraint(self, constraint):
        self.inConstraints.append(constraint)

    def getOutConstraints(self):
        return self.outConstraints
    
    def addOutConstraint(self, constraint):
        self.outConstraints.append(constraint)
  

class Gate(Node):
    def __init__(self, id):
        Node.__init__(self)
    
    
class Task(Node):
    def __init__(self, id):
        Node.__init__(self,id)
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


class Constraint:
    def __init__(self, sourceNode, targetNode):
        self.sourceNode = sourceNode
        self.targetNode = targetNode
    
    def getSourceNode(self):
        return self.sourceNode
    
    def setSourceNode(self, node):
        self.sourceNode = node
    
    def getTargetNode(self):
        return self.targetNode
    
    def setTargetNode(self, node):
        self.targetNode = node
    
    
class Lane:
    
#lanes are managing sets of tasks

    def _init_(self, id):
        self.id = id
        self.tasks = []
        
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
        
    def getTasks(self):
        return self.tasks
    
    def appendTasks(self, task):
        self.tasks.append(task)
        
    
class Project:
    
    def _init_(self, id):
        self.id = id
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
    
    
        
    
           