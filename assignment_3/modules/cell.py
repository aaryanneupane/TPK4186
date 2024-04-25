from .shelf import Shelf
from .catalog import Catalog


class Cell:
    def __init__(self, position: tuple, type: str) -> None:
        self.position = position
        self.type = type

    def __str__(self) -> str:
        # return f"( {self.type} {self.position[1]}, {self.position[0] + 1})"  # Switch in the end for the wanted format in the task
        # return f"({self.type})"
        return f"({self.position[0]}, {self.position[1]})"  # For development purposes
        # return f"({self.position[1]}, {self.position[0] + 1})"

    def __repr__(self) -> str:
        return str(self)

    def get_position(self) -> tuple:
        return self.position

    def get_type(self) -> str:
        return self.type


class Storage_Cell(Cell):
    catalog_count = 0

    def __init__(self, position: tuple, type: str = "SC") -> None:
        super().__init__(position, type)
        self.shelves: list[Shelf] = []
        for i in range(2):
            self.shelves.append(Shelf())

    def __str__(self) -> str:
        # return super().__str__()
        return f"({self.position[0]}, {self.position[1]}) with {len(self.shelves)} shelves"  # For robot movement testing

    def populate_shelves(self, catalog: Catalog):
        for shelf in self.shelves:
            product = catalog.get_products()[Storage_Cell.catalog_count]
            if Storage_Cell.catalog_count == len(catalog.get_products()) - 1:
                Storage_Cell.catalog_count = 0
            Storage_Cell.catalog_count += 1
            if product is not None:
                while shelf.remaining_capacity() >= product.weight:
                    shelf.add_product(product)
                    # Add the same product to the other shelf in the cell
                    other_shelf_index = (self.shelves.index(shelf) + 1) % len(
                        self.shelves
                    )
                    other_shelf = self.shelves[other_shelf_index]
                    other_shelf.add_product(product)

    def get_shelves(self) -> list[Shelf]:
        return self.shelves


class Route_Cell(Cell):
    def __init__(self, position: tuple, type: str = "rc") -> None:
        super().__init__(position, type)
        self.position = position
        self.occupied = False

    def __str__(self) -> str:
        # return super().__str__()
        return f"({self.position[0]}, {self.position[1]}) with occupied status: {self.occupied}"  # For robot movement testing

    def get_status(self) -> bool:
        return self.occupied

    def set_occupied(self) -> None:
        self.occupied = True

    def set_unoccupied(self) -> None:
        self.occupied = False


class Loading_Cell(Cell):
    def __init__(self, position: tuple, type: str = "LC") -> None:
        super().__init__(position, type)
        self.position = position
        self.available_robots = []

    def __str__(self) -> str:
        # return f"({self.position[0]}, {self.position[1]}) with available robots: {len(self.available_robots)}"
        return super().__str__()

    def get_available_robots(self) -> int:
        return self.available_robots

    def add_robot(self, robot) -> None:
        self.available_robots.append(robot)

    def remove_robot(self, robot) -> None:
        self.available_robots.remove(robot)


class Unloading_Cell(Cell):
    def __init__(self, position: tuple, type: str = "UC") -> None:
        super().__init__(position, type)
        self.position = position

    def __str__(self) -> str:
        return super().__str__()


class Empty_Cell(Cell):
    def __init__(self, position: tuple, type: str = "o") -> None:
        super().__init__(position, type)
        self.position = position

    def __str__(self) -> str:
        return super().__str__()
