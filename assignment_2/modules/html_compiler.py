from modules.paragraph import Paragraph
from modules.list import List
from modules.figure import Figure
from modules.document import Document

class HTMLcompiler:

    def __init__(self):
        pass

    def export(self, document: Document, filename):
        outputFile = open(filename + ".html", "w")
        self.printHTML(document, outputFile)
        outputFile.close()

    def printHTML(self, document, outputFile):
        outputFile.write("<!DOCTYPE html>\n")
        outputFile.write("<html>\n")
        outputFile.write("<head>\n")
        outputFile.write("<title>" + document.get_title() + "</title>\n")
        outputFile.write("</head>\n")
        outputFile.write("<body>\n")
        outputFile.write("<h1>" + document.get_title() + "</h1>\n")
        for section in document.get_sections():
            outputFile.write("<h2>" + section.get_title() + "</h2>\n")
            for content in section.get_contents():
                if type(content) == Paragraph:
                    outputFile.write("<p>" + content.get_text() + "</p>\n")
                elif type(content) == List:
                        if content.get_list_type() == "unordered":
                                outputFile.write("<ul>\n")
                                for item in content.get_items():
                                        outputFile.write("<li>" + item + "</li>\n")
                                outputFile.write("</ul>\n")
                        else: 
                                outputFile.write("<ol>\n")
                                for item in content.get_items():
                                        outputFile.write("<li>" + item + "</li>\n")
                                outputFile.write("</ol>\n")
                elif type(content) == Figure:
                        outputFile.write("<figure>")
                        outputFile.write("<img src=" + content.get_path() + " alt=" + content.get_name() + ">")
                        outputFile.write("</figure>")     
        outputFile.write("</body>\n")
        outputFile.write("</html>\n")
