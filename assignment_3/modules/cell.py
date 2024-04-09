from .shelf import Shelf


class Cell:
    def __init__(self, position: tuple, type: str) -> None:
        self.position = position
        self.type = type

    def __str__(self) -> str:
        return f"({self.type} {self.position[1]}, {self.position[0] + 1})"  # Switch in the end for the wanted format in the task


class Storage_Cell(Cell):
    def __init__(self, position: tuple, type: str = "SC") -> None:
        super().__init__(position, type)
        self.shelves = []
        for i in range(1):
            self.shelves.append(Shelf())

    def __str__(self) -> str:
        return super().__str__()


class Route_Cell(Cell):
    def __init__(self, position: tuple, type: str = "RC") -> None:
        super().__init__(position, type)
        self.position = position

    def __str__(self) -> str:
        return super().__str__()


class Loading_Cell(Cell):
    def __init__(self, position: tuple, type: str = "LC") -> None:
        super().__init__(position, type)
        self.position = position

    def __str__(self) -> str:
        return super().__str__()


class Unloading_Cell(Cell):
    def __init__(self, position: tuple, type: str = "UC") -> None:
        super().__init__(position, type)
        self.position = position

    def __str__(self) -> str:
        return super().__str__()
