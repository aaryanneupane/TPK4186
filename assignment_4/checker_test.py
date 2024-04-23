from modules.checker import Checker
from modules.projectParser import ProjectParser

parser = ProjectParser()
project = parser.parse_xml('controlSystemProject.xml')

checker = Checker(project)
checker.checkModel()