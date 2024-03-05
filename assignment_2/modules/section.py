from .paragraph import Paragraph
from .list import List
from .figure import Figure

class Section:
    def __init__(self, title: str):
        self.title = title
        self.contents = []

    def get_title(self) -> str:
        return self.title
    
    def set_title(self, title: str) -> None:
        self.title = title

    def get_contents(self) -> list:
        return self.contents
    
    def get_content(self, index: int) -> Paragraph:
        return self.contents[index]
    
    def delete_content(self, index: int) -> None:
        self.contents.pop(index)
    
    def add_paragraph(self, text: str) -> Paragraph:
        new_paragraph = Paragraph(text)
        self.contents.append(new_paragraph)
        return self.contents[-1]

    def add_list(self, list_type, items: list) -> List:
        new_list = List(list_type, items)
        self.contents.append(new_list)
        return self.contents[-1]
    
    def add_figure(self, path: str, name: str) -> Figure:
        new_figure = Figure(path, name)
        self.contents.append(new_figure)
        return new_figure
    
    def add_section(self, section):
        self.contents.append(section)