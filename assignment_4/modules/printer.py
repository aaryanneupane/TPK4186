from modules.projectParser import ProjectParser
from modules.project import Project

class Printer:
    def print_document(self, project: Project):
        print('Project name is: ' + project.getName())
       
        for lane in project.getLanes():
            print('Lane name is: ' + lane.getName())
            
        for gate in project.getGates():
            print('Gate name is: ' + gate.getName())
            

        for task in project.getTasks():
            print('Tasks name is: ' + str(task.getName()))
            print('Max-duration: ' + str(task.getMaximumDuration()))


        for constraint in project.getConstraints():
            print(constraint)
            
        for task in project.getTasks():
            if task.getName() == "DesignDocumentation":
                print(task.getPredecessors())
                print(task.getSuccessors())
        
            