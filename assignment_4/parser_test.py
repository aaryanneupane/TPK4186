from modules.projectParser import ProjectParser
import xml.etree.ElementTree as ET

new_parser = ProjectParser()

file = "controlSystemProject.xml"

print(new_parser.parse_xml('controlSystemProject.xml'))