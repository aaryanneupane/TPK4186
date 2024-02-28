class Figure:
    def __init__(self, path, name):
        self.name = name
        self.path = path

    def get_path(self) -> str:
        return self.path
    
    def get_name(self) -> str:
        return self.name