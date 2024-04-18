from modules.projectParser import ProjectParser
from modules.project import Project
"""""
class Printer:
    def print_document(self, document):
        xml_str = document.toxml()
        print(xml_str)  # You can replace this with actual printing function for physical printer

# Test the parser and printer
parser = ProjectParser()
text = parser.parse_xml('controlSystemProject.xml')

printer = Printer()
printer.print_document(text)
"""

class Printer:
    def print_document(self, project: Project):
        print('Project name is: ' + project.getName())
        print(project.getLanes())
        for lane in project.getLanes():
            print('Lane name is: ' + lane.getName())
            
        for gate in project.getGates():
            print('Gate name is: ' + gate.getName())
            
        for constraint in project.getConstraints():
            print(constraint)

        for task in project.getTasks():
            print('Tasks name is: ' + str(task.getName()))
            print('Max-duration: ' + str(task.getMaximumDuration()))
        
            
        
        

# Test the parser and printer
parser = ProjectParser()
project = parser.parse_xml('controlSystemProject.xml')

printer = Printer()
printer.print_document(project)