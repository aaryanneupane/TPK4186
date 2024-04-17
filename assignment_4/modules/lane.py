from modules.container import Container

class Lane(Container):
    
#lanes are managing sets of tasks

    def _init_(self):
        Container.__init__(self,id)
        #self.id = id
        #self.name = name
        self.tasks = []
        
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
        
    def getTasks(self):
        return self.tasks
    
    def appendTasks(self, task):
        self.tasks.append(task)