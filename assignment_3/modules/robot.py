from modules.cell import Cell

class Robot:
    def __init__(self) -> None:
        self.on_hand = () # tuple of (product, quantity)
        self.available_capacity = 40
        self.booked = False
        self.current_pos = None
        self.previous_pos = None
        self.target_cell = None
        self.route = []
        self.objective = None
    
    def move(self, next_cell: Cell):
        # Move the robot to the next cell
        if self.current_pos:
            self.previous_pos = self.current_pos
        self.current_pos = next_cell
    
    def set_current_pos(self, cell: Cell):
        self.current_pos = cell