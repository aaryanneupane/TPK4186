from .paragraph import Paragraph

class Section:
    def __init__(self, title: str):
        self.title = title
        self.paragraphs = []

    def get_title(self) -> str:
        return self.title
    
    def set_title(self, title: str) -> None:
        self.title = title

    def get_paragraphs(self) -> list:
        return self.paragraphs
    
    def get_paragraph(self, index: int) -> Paragraph:
        return self.paragraphs[index]
    
    def delete_paragraph(self, index: int) -> None:
        self.paragraphs.pop(index)
    
    def add_paragraph(self, text: str) -> None:
        new_paragraph = Paragraph(text)
        self.paragraphs.append(new_paragraph)

    

