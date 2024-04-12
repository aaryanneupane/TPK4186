from modules.cell import *
from modules.product import Product

class Robot:
    Robot_ID = 1

    def __init__(self) -> None:
        self.robot_id = Robot.Robot_ID
        self.on_hand = () # tuple of (product, quantity)
        self.available_capacity = 40
        self.current_pos:Route_Cell = None
        self.previous_pos: Route_Cell = None
        self.target_cell: Storage_Cell = None
        self.route: list[Route_Cell] = []
        self.route_back: list[Route_Cell] = []
        self.objective = False
        Robot.Robot_ID += 1
        self.current_objective_time = 0
        self.global_time = 0

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
        #print(f"Robot {self.robot_id} moving to {next_cell}")
        self.objective = True
        if self.current_pos:
            self.previous_pos = self.current_pos
        # Check if the next cell is occupied
        while isinstance(next_cell, Route_Cell) and next_cell.get_status():
            print(f"Robot {self.robot_id} cannot move to {next_cell}. Cell is occupied.\n")
            self.current_objective_time += 10 

        self.current_pos = next_cell

        # Mark the current cell as occupied
        if isinstance(self.current_pos, Route_Cell):
            self.current_pos.set_occupied()
        
        # Mark the previous cell as unoccupied
        if isinstance(self.previous_pos, Route_Cell):
            self.previous_pos.set_unoccupied()
        
        self.current_objective_time += 10
        
        print(f"Robot {self.robot_id} moved to {self.current_pos}")

    def load_product(self, quantity:int):
        # Load the product from the shelf
        for shelf in self.target_cell.get_shelves():
            product = shelf.get_product()
            if product is not None:
                if product.get_weight() * quantity <= self.available_capacity:
                    self.on_hand = (product, quantity)
                    self.available_capacity -= product.get_weight() * quantity
                    shelf.remove_product(product)
                    print(f"Robot number {self.robot_id} loaded {quantity} of {product} from {self.target_cell}")
                    print(f"Robot number {self.robot_id} has now got {self.available_capacity} kg(s) of capacity left\n")
                    break
                else:
                    print(f"Robot {self.robot_id} does not have enough capacity to load {quantity} of {product}\n")
                    break
        self.current_objective_time += 120

    def unload_product(self):
        # Unload the product to the unloading cell
        product = self.on_hand[0]
        quantity = self.on_hand[1]
        self.on_hand = ()
        self.available_capacity = 40
        print(f"Robot {self.robot_id} unloaded {quantity} of {product} to the unloading cell\n")
        self.current_objective_time += 120
        self.objective = False
    
    def restock_product(self):
        # Restock the product to the shelf
        product = self.on_hand[0]
        quantity = self.on_hand[1]
        for shelf in self.target_cell.get_shelves():
            if shelf.get_product() is None or shelf.get_product() == product:
                for _ in range(quantity):
                    shelf.add_product(product)
                print(f"Robot {self.robot_id} restocked {quantity} of {product} to {self.target_cell}\n")
                break
        self.current_objective_time += 120
        self.objective = False
    
    
            
    def set_current_pos(self, cell: Cell) -> None:
        self.current_pos = cell

    def set_objective(self, status: bool) -> None:
        self.objective = status
    
    def set_previous_pos(self, cell: Cell) -> None:
        self.previous_pos = cell

    def set_route(self, route: list[Cell]) -> None:
        self.route = route
    
    def set_route_back(self, route: list[Cell]) -> None:
        self.route_back = route
    
    def set_on_hand(self, product: Product, quantity: int) -> None:
        self.on_hand = (product, quantity)

    def set_target_cell(self, cell: Cell) -> None:
        self.target_cell = cell

    def set_global_state(self) -> None:
        self.global_time +=1
        

    def get_objective_time(self) -> int:
        return self.current_objective_time
    
    def get_robot_id(self) -> int:
        return self.robot_id
    
    def get_available_capacity(self) -> int:
        return self.available_capacity
    
    def reset_objective_time(self) -> None:
        self.current_objective_time = 0