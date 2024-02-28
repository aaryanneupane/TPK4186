import docx
from .paragraph import Paragraph
from .list import List
from .figure import Figure

class DocxCompiler:

    def __init__ (self):
        pass

    def exportDocument(self, simplanDocument, filename):
        filename_docx = filename + ".docx"
        docxDocument = docx.Document()
        self.compileDocument(simplanDocument, docxDocument)
        docxDocument.save(filename_docx)
	
    def compileDocument(self, simplanDocument, docxDocument):
        docxDocument.add_heading(simplanDocument.get_title(), level=1)
        self.compileSections(simplanDocument, docxDocument)
	
    def compileSections(self, simplanDocument, docxDocument):
        for simplanSection in simplanDocument.get_sections():
            self.compileSection(simplanSection, docxDocument)

    def compileSection(self, simplanSection, docxDocument):
        docxDocument.add_heading(simplanSection.get_title(), level=2)
        self.compileContents(simplanSection, docxDocument)

    def compileContents(self, simplanSection, docxDocument):
        for simplanContent in simplanSection.get_contents():
            if type(simplanContent) == Paragraph:
                self.compileParagraph(simplanContent, docxDocument)
            elif type(simplanContent) == List:
                if simplanContent.list_type == "uo":
                    self.compileUnorderedList(simplanContent, docxDocument)
                elif simplanContent.list_type == "ol":
                    self.compileOrderedList(simplanContent, docxDocument)
            elif type(simplanContent) == Figure:
                self.compileFigure(simplanContent, docxDocument)

    def compileParagraph(self, simplanContent, docxDocument):
        docxDocument.add_paragraph(simplanContent.get_text())

    def compileUnorderedList(self, simplanContent, docxDocument):
        for item in simplanContent.get_items():
            docxDocument.add_paragraph(item, style='ListBullet')
    
    def compileOrderedList(self, simplanContent, docxDocument):
        for item in simplanContent.get_items():
            docxDocument.add_paragraph(item, style='ListNumber')

    def compileFigure(self, simplanContent, docxDocument):
        docxDocument.add_picture(simplanContent.get_path())
    


        

	    
    









