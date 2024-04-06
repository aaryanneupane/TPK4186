from shelf import Shelf

class Storage_Cell:
    def __init__(self) -> None:
        self.shelves = []
        for i in range(1):
            self.shelves.append(Shelf())