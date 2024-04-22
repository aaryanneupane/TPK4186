from modules.projectParser import ProjectParser
from modules.project import Project
from modules.printer import Printer
        
            
parser = ProjectParser()
project = parser.parse_xml('controlSystemProject.xml')

printer = Printer()
printer.print_document(project)