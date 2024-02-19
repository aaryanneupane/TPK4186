class Paragraph:
    def __init__(self, text: str):
        self.text = text

    def get_text(self) -> str:
        return self.text

    def set_text(self, text: str) -> None:
        self.text = text
    
    def add_text(self, text: str) -> None:
        self.text += text

    def __str__(self) -> str:
        return self.text
