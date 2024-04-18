from modules.projectParser import ProjectParser

class Printer:
    def print_document(self, document):
        xml_str = document.toxml()
        print(xml_str)  # You can replace this with actual printing function for physical printer

# Test the parser and printer
parser = ProjectParser()
document = parser.parse_xml('controlSystemProject.xml')

printer = Printer()
printer.print_document(document)