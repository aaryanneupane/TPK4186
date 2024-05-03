from modules.project import Project

class Checker:

    def __init__(self, project: Project):
        self.project = project
        
    def verifyStartNode(self):
        num_start_nodes = 0
        for task in self.project.getTasks():
            if len(task.getPredecessors()) == 0:
                return False
        for gate in self.project.getGates():
            if len(gate.getPredecessors()) == 0:
                num_start_nodes +=1
        
        if num_start_nodes != 1:
            return False
        return True

            
    def verifyEndNode(self):
        num_end_nodes = 0;
        for task in self.project.getTasks():
            if len(task.getSuccessors()) == 0:
                return False
        for gate in self.project.getGates():
            if len(gate.getSuccessors()) == 0:
                num_end_nodes +=1
        if num_end_nodes != 1:
            return False
        return True
    
    def checkModel(self):
        if self.verifyStartNode() and self.verifyEndNode():
            return print("The model has been checked, and it is verified that the model is well designed")
                  
        

            
            