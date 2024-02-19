import re
from .document import Document

class Parser:
    def __init__(self):
        self.document = Document()
    
    def parse(self, text) -> Document:
        sections = re.split(r'\n#+\s+', text.strip())  # Split text into sections based on headers
        # Add title
        self.document.set_title(sections[0].strip())
        # Add sections
        for section_text in sections[1:]:
            lines = section_text.split('\n')
            title = lines[0].strip()
            self.document.add_section(title)
            section = self.document.get_section(len(self.document.get_sections()) - 1)  # Get the last section          
            # Add paragraphs to section
            for line in lines[1:]:
                section.add_paragraph(line.strip())
        return self.document