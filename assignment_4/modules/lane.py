import random
from modules.container import Container

class Lane:
    
#lanes are managing sets of tasks

    def __init__(self, id, name):
        #Container.__init__(self,id)
        #self.id = id
        #self.name = name
        self.id = id
        self.name = name
        self.tasks = []
        self.workload = 0
        
        
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
        
    def getTasks(self):
        return self.tasks
    
    def getName(self):
        return self.name
    
    def appendTasks(self, task):
        self.tasks.append(task)
    
    def setWorkload(self):
        return random.randint(0,1)
    
    def getWorkload(self):
        return self.workload
    