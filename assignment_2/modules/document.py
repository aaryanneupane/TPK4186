from .section import Section

class Document():
    def __init__(self, title="SET TITLE"):
        self.title = title
        self.sections = []
        

    def get_title(self) -> str:
        return self.title
    
    def set_title(self, title: str) -> None:
        self.title = title

    def get_sections(self) -> list:
        return self.sections
    
    def get_section(self, index: int) -> Section:
        return self.sections[index]
    
    def add_section(self, title: str) -> None:
        new_section = Section(title)
        self.sections.append(new_section)
    