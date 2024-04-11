from modules.cell import Cell

class Robot:
    Robot_ID = 1

    def __init__(self) -> None:
        self.robot_id = Robot.Robot_ID
        self.on_hand = () # tuple of (product, quantity)
        self.available_capacity = 40
        self.booked = False
        self.current_pos = None
        self.previous_pos = None
        self.target_cell = None
        self.route = []
        self.route_back = []
        self.objective = None
        Robot.Robot_ID += 1

    def __str__(self) -> str:
        return f"""Robot with ID: {self.robot_id}
        On hand: {self.on_hand} 
        At cell: {self.current_pos}
        Previous cell: {self.previous_pos}
        Target cell: {self.target_cell}
        Route: {self.route}\n
        """

    # def __str__(self) -> str:  For testing the movement of the robot
    #     return f"Robot with ID: {self.robot_id} at {self.current_pos}"
    
    def move(self, next_cell: Cell):
        # Move the robot to the next cell
        if self.current_pos:
            self.previous_pos = self.current_pos
        self.current_pos = next_cell
        self.current_pos.set_occupied()
        self.previous_pos.set_unoccupied()
    
    def set_current_pos(self, cell: Cell) -> None:
        self.current_pos = cell
    
    def set_previous_pos(self, cell: Cell) -> None:
        self.previous_pos = cell

    def set_route(self, route: list[Cell]) -> None:
        self.route = route
    
    def set_route_back(self, route: list[Cell]) -> None:
        self.route_back = route

    def set_target_cell(self, cell: Cell) -> None:
        self.target_cell = cell
    