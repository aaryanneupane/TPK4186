import numpy as np
from .cell import Storage_Cell, Route_Cell, Loading_Cell, Unloading_Cell, Empty_Cell


class Warehouse:
    def __init__(self, ally_number:int, ally_size:int) -> None:
        self.height = ally_size * 2 + 4
        self.length = ally_number * 6 + 1  # Add 1 to the length to account for the extra column
        self.grid = np.empty((self.height, self.length), dtype=object)  # Initialize an empty grid of objects
        self.generate_warehouse()
        

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
            self.grid[i][0] = Empty_Cell((i, 0))
    # Create loading and unloading cells
        loading_cell_pos = self.height // 2 
        self.add_cell("loading", (loading_cell_pos - 1, 0))
        self.add_cell("unloading", (loading_cell_pos, 0))
    # Create storage cells on the first and last wall
        for i in range(loading_cell_pos - 2):
            self.add_cell("storage", (i, 1))
            self.add_cell("storage", (self.height - i-1, 1))
            self.add_cell("storage", (i, self.length - 1))
            self.add_cell("storage", (self.height - i-1, self.length - 1))    

    # Create storage cells in the middle
        skip_columns = 4
        storage_columns = 2
        column_spacing = skip_columns + storage_columns
        
        for i in range(loading_cell_pos - 2):
            for j in range(skip_columns + 1, self.length - 2, column_spacing):
                for k in range(storage_columns):
                    self.add_cell("storage", (i, j + k + 1))
                    self.add_cell("storage", (self.height - i - 1, j + k + 1))

    # Create route cells
        for i in range(self.height):
            for j in range(self.length):
                if self.grid[i][j] is None:
                    self.add_cell("route", (i, j))


    def is_valid_position(self, position: tuple) -> bool:
        x, y = position
        return 0 <= x < self.height and 0 <= y < self.length 

    def print_warehouse_layout(self):
        for row in self.grid:
            for cell in row:
                print(cell or "empty", end=" ")  # Print the cell or empty space if cell is None
            print()  # Move to the next row
    
    def generate_warehouse(self):
        self.generate_warehouse_layout()
        


        