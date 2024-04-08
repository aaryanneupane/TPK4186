import numpy as np
from .cell import Storage_Cell, Route_Cell, Loading_Cell, Unloading_Cell


class Warehouse:
    def __init__(self, height:int, length:int) -> None:
        self.height = height
        self.length = length + 1  # Add 1 to the length to account for the extra column
        self.grid = np.empty((height, length), dtype=object)  # Initialize an empty grid of objects
        self.generate_warehouse_layout()

    def add_cell(self, cell_type: str, position: tuple):
        if not self.is_valid_position(position):
            print("Invalid position for cell.")
            return False

        if cell_type == "storage":
            self.grid[position] = Storage_Cell(position)
        elif cell_type == "route":
            self.grid[position] = Route_Cell(position)
        elif cell_type == "loading":
            self.grid[position] = Loading_Cell(position)
        elif cell_type == "unloading":
            self.grid[position] = Unloading_Cell(position)
        else:
            print("Invalid cell type.")
            return False

        return True
    
    def generate_warehouse_layout(self):
    # Intialize first column to be none
        for i in range(self.height):
            self.grid[i][0] = None
    # Create loading and unloading cells
        loading_cell_pos = self.height // 2
        self.add_cell("loading", (loading_cell_pos, 0))
        self.add_cell("unloading", (loading_cell_pos + 1, 0))
    # Create storage cells on the first wall
        for i in range(1, self.length - 1):
            for j in range(self.height):
                self.add_cell("storage", (j, i))
    

    def is_valid_position(self, position: tuple) -> bool:
        x, y = position
        return 0 <= x < self.height and 0 <= y < self.length

    def print_warehouse_layout(self):
        for row in self.grid:
            for cell in row:
                print(cell or "empty", end=" ")  # Print the cell or empty space if cell is None
            print()  # Move to the next row
    
    def print_dawg(self):
        print(self.grid)

        