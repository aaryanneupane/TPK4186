import numpy as np
from .cell import Cell, Storage_Cell, Route_Cell, Loading_Cell, Unloading_Cell, Empty_Cell
from .catalog import Catalog
from .product import Product
from .robot import Robot
from .order import Order
from .truck_load import Truck_Load
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


hardcoded_catalog = Catalog()
hardcoded_catalog.add_product(Product("Nail", 2))
hardcoded_catalog.add_product(Product("Wooden Plank", 9))
hardcoded_catalog.add_product(Product("Screwdriver", 4))
hardcoded_catalog.add_product(Product("White Paint", 3))
hardcoded_catalog.add_product(Product("Black Paint", 2))
hardcoded_catalog.add_product(Product("Paper Sheet", 7))
hardcoded_catalog.add_product(Product("Fish Hooks", 5))
hardcoded_catalog.add_product(Product("Ducktape", 6))
hardcoded_catalog.add_product(Product("Rope", 7))
hardcoded_catalog.add_product(Product("Pocket Knife", 8))

class Warehouse:
    def __init__(self, ally_number:int, ally_size:int, num_products:int, num_robots:Robot) -> None:
        self.height = ally_size * 2 + 4
        self.length = ally_number * 6 + 1  # Add 1 to the length to account for the extra column
        self.grid = np.empty((self.height, self.length), dtype=object)  # Initialize an empty grid of objects
        self.num_robots = num_robots
        self.robots = []
        self.max_product_types = (ally_size * 2 + (ally_number - 1) * 2 * ally_size) * 4
        if num_products > self.max_product_types:
            raise ValueError("There cannot be more different products than available shelves")
        #self.catalog = Catalog()
        self.catalog = hardcoded_catalog
        #self.catalog.generate_random_catalog(num_products)
        self.generate_warehouse()
        self.orders = []
        self.remaining_orders = []
        self.canceled_orders = []
        self.completed_orders = {}
        self.order_weight = 0
        self.count_orders_for_truckload = 0
        self.truck_loads = []

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

    # def print_warehouse_layout(self):
    #     print("Warehouse layout:")
    #     for row in self.grid:
    #         for cell in row:
    #             print(cell or "empty", end=" ")  # Print the cell or empty space if cell is None
    #         print()  # Move to the next row
    #     print()

    def print_warehouse_layout(self):
        # Define a dictionary to map cell types to numbers
        cell_type_to_num = {Empty_Cell: 0, Loading_Cell: 1, Unloading_Cell: 2, Storage_Cell: 3, Route_Cell: 4}

        # Convert the grid to a numerical grid
        numerical_grid = [[cell_type_to_num[type(cell)] for cell in row] for row in self.grid]

        # Display the grid as an image
        plt.imshow(numerical_grid, cmap='tab10')
        plt.xticks(range(self.length), range(self.length))
        plt.yticks(range(self.height), range(self.height))
        plt.grid(True)
        plt.colorbar(ticks=range(5), label='Cell types')
        plt.show()
    
    def animate_warehouse(self):
        fig, ax = plt.subplots()
        cell_type_to_color = {Empty_Cell: 'white', Loading_Cell: 'blue', Unloading_Cell: 'green', Storage_Cell: 'gray', Route_Cell: 'black'}
        def update(frame):
            ax.clear()
            for i in range(self.height):
                for j in range(self.length):
                    cell = self.grid[i][j]
                    color = cell_type_to_color[type(cell)]
                    ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color, edgecolor='black'))
            for robot in self.robots:
                ax.add_patch(plt.Circle((robot.current_pos.position[1] + 0.5, robot.current_pos.position[0] + 0.5), 0.4, color='red'))
            plt.xlim(0, self.length)
            plt.ylim(0, self.height)
            plt.gca().set_aspect('equal', adjustable='box')
        ani = FuncAnimation(fig, update, frames=range(10), repeat=True)
        plt.show()
    
    
    def populate_shelves(self):
        for i in range(self.height):
            for j in range(self.length):
                cell = self.grid[i][j]
                if isinstance(cell, Storage_Cell):
                    cell.populate_shelves(self.catalog)
    
    def find_storage_cell(self, product: Product) -> Storage_Cell:
        for i in range(self.height):
            for j in range(self.length):
                cell = self.grid[i][j]
                if isinstance(cell, Storage_Cell):
                    for shelf in cell.shelves:
                        if shelf.get_product().get_code() == product.get_code():
                            return cell
        raise ValueError("No storage cell contains this product")
    
    def add_order_to_warehouse(self, name:str):
        new_order = Order(name, self.catalog)  # Assuming you have 'name' and 'catalog' defined somewhere
        new_order.generate_random_order()
        #we have not checked if the product is in
        if self.order_weight>=(400-new_order.get_weight()):
            truck_load = Truck_Load(400)
            truck_order_list = self.orders[-(self.count_orders_for_truckload):] 
            truck_load.generate_truck_load(truck_order_list)
            self.order_weight = 0
            self.count_orders_for_truckload = 0
        self.orders.append(new_order)
        self.order_weight += new_order.get_weight()
        self.count_orders_for_truckload +=1 
        
    def add_truck_load_to_warehouse(self):
        new_truck_load = Truck_Load()
        new_truck_load.generate_random_truck_load(self.catalog)
        self.truck_loads.append(new_truck_load)
                    
    def generate_robots(self):
        for i in range(self.num_robots):
            self.robots.append(Robot())
        for robot in self.robots:
            robot.current_pos = self.grid[self.height // 2 - 1][0]
            self.grid[self.height // 2 - 1][0].add_robot(robot)

    def generate_warehouse(self):
        self.generate_warehouse_layout()
        self.populate_shelves()
        self.generate_robots()
            
    def get_order_weight(self):
        return self.order_weight
    
    def get_count_orders_for_truckload(self) -> int:
        return self.count_orders_for_truckload

    def get_catalog_products(self) -> list[Product]:
        return self.catalog.get_products()
    
    def get_catalog(self) -> Catalog:
        return self.catalog

    def get_product_by_code(self, code: str) -> Product:
        return self.catalog.get_product_by_code(code)

    def get_warehouse_height(self):
        return self.height
    
    def get_warehouse_length(self):
        return self.length - 1

    def get_number_of_shelves(self):
        return self.max_product_types

    def get_robots(self):
        return self.robots
    
    def get_cell(self, position: tuple) -> Cell:
        return self.grid[position]
    
    def get_loading_cell(self) -> Loading_Cell:
        return self.grid[self.height // 2 - 1][0]
    
    def get_unloading_cell(self) -> Unloading_Cell:
        return self.grid[self.height // 2][0]
    
    def get_order_list(self) -> list[Order]:
        return self.orders
    
    def get_completed_order_list(self) -> list[Order]:
        return self.completed_orders

    def get_remaining_orders(self) -> list[Order]:
        return self.remaining_orders

    def get_truck_loads(self) -> list[Truck_Load]:
        return self.truck_loads

    def calculate_route_to_storage_cell(self, cell: Cell) -> list[Cell]:
        """
        Calculate the shortest route from the loading cell to the given cell using grid logic.
        Args:
            cell (Cell): The destination cell.
        Returns:
            list[Cell]: The shortest route from the loading cell to the given cell.
        """
        # Get the position of the loading cell
        loading_cell = self.get_loading_cell().get_position()

        # Get the position of the destination cell
        destination = cell.get_position()

        # Initialize the route list to store the cells along the route
        route = []

        # Calculate the direction to move along the height axis (up or down)
        height_direction = "up" if destination[0] < loading_cell[0] else "down"

        # Calculate the direction to move along the length axis (left or right)
        length_direction = "left" if destination[1] < loading_cell[1] else "right"

        # Check if the destination cell is on the right side of a storage cell pair
        if destination[1] % 2 != 0:
            # Adjust horizontal distance to skip the adjacent storage cell on the left
            horizontal_distance = destination[1] + 2
        else:
            # Calculate the horizontal distance to the destination cell 
            if destination[1] - 2 < 0:
                horizontal_distance = destination[1] + 1
            else:
                horizontal_distance = destination[1] - 3

        # Calculate the vertical distance to the destination cell
        if destination[0] > loading_cell[0]:
            vertical_distance = destination[0] + 1
        else:
            vertical_distance = destination[0] - 1

        # Move horizontally until reaching the destination cell
        while loading_cell[1] != horizontal_distance:
            route.append(self.grid[loading_cell[0]][loading_cell[1]])  # Append the current cell to the route
            if length_direction == "left":
                loading_cell = (loading_cell[0], loading_cell[1] - 1)
            else:
                loading_cell = (loading_cell[0], loading_cell[1] + 1)

        # Move vertically until reaching the same height as the destination cell
        while loading_cell[0] != vertical_distance:
            route.append(self.grid[loading_cell[0]][loading_cell[1]])  # Append the current cell to the route
            if height_direction == "up":
                loading_cell = (loading_cell[0] - 1, loading_cell[1])
            else:
                loading_cell = (loading_cell[0] + 1, loading_cell[1])

        route.pop(0)  # Remove the first cell (loading cell) from the route

        # Append the last cell before the destination cell to the route
        if destination[1] % 2 == 0:
            # If the destination column index is even, add one step horizontally first
            route.append(self.grid[route[-1].get_position()[0]][route[-1].get_position()[1] + 1])
        # Add the next step horizontally
        if destination[1] > route[-1].get_position()[1]:
            route.append(self.grid[route[-1].get_position()[0]][route[-1].get_position()[1] + 1])
        elif destination[1] < route[-1].get_position()[1]:
            route.append(self.grid[route[-1].get_position()[0]][route[-1].get_position()[1] - 1])

        return route

    def calculate_route_back_to_loading_cell(self, cell: Cell) -> list[Cell]:
        """
        Calculate the shortest route from the given cell back to the loading cell using grid logic.
        Args:
            cell (Cell): The current cell.
        Returns:
            list[Cell]: The shortest route from the given cell back to the loading cell.
        """
        # Get the position of the unloading cell
        unloading_cell_position = self.get_unloading_cell().get_position()

        # Get the position of the current cell
        current_position = cell.get_position()

        # Initialize the route list to store the cells along the route
        route_back = []

        # Calculate the direction to move along the height axis (up or down)
        height_direction = "up" if unloading_cell_position[0] < current_position[0] else "down"

        # Calculate the direction to move along the length axis (left or right)
        length_direction = "left" if unloading_cell_position[1] < current_position[1] else "right"

        # Determine whether to move forward or backward for two steps
        if current_position[1] % 2 == 0:  # If the destination column index is even
            # Move two steps backward horizontally
            for _ in range(2):
                current_position = (current_position[0], current_position[1] - 1)
                route_back.append(self.grid[current_position[0]][current_position[1]])  # Append the current cell to the route
        else:
            # Move two steps forward horizontally
            for _ in range(3):
                current_position = (current_position[0], current_position[1] + 1)
                route_back.append(self.grid[current_position[0]][current_position[1]])  # Append the current cell to the route

        # Move vertically until reaching the same height as the unloading cell
        while current_position[0] != unloading_cell_position[0]:
            if height_direction == "up":
                current_position = (current_position[0] - 1, current_position[1])
            else:
                current_position = (current_position[0] + 1, current_position[1])
            route_back.append(self.grid[current_position[0]][current_position[1]])  # Append the current cell to the route

        route_back.pop(-1)  # Remove the last cell (unloading cell) from the route
        route_back.pop(0)  # Remove the first cell (current cell) from the route

        # Move horizontally until reaching column 0
        for _ in range(current_position[1], -1, -1):
            route_back.append(self.grid[current_position[0]][_])  # Append the current cell to the route

        return route_back

    def generate_objective(self, robot:Robot, cell:Cell):
        route_to_cell = self.calculate_route_to_storage_cell(cell)
        route_back = self.calculate_route_back_to_loading_cell(cell)
        robot.set_route(route_to_cell)
        robot.set_route_back(route_back)
        robot.set_target_cell(cell)
        return route_to_cell, route_back

    def get_available_robot(self) -> Robot:
        available_robots = self.get_loading_cell().get_available_robots()
        if len(available_robots) > 0:
            return available_robots[0]
        else:
            ValueError("No available robots in the loading cell")

    def move_robot(self, robot: Robot, route: list[Cell]):
        fig, ax = plt.subplots()
        numerical_grid = self.convert_grid_to_numerical()  # Convert the grid to numerical format
        ax.imshow(numerical_grid, cmap='tab10')
        ax.set_xticks(range(self.length))
        ax.set_yticks(range(self.height))
        ax.grid(True)
        ax.colorbar(ticks=range(5), label='Cell types')
        plt.draw()
        plt.pause(0.1)  # Add a small pause to visualize the initial state

        for cell in route:
            robot.move(cell)
            ax.imshow(numerical_grid, cmap='tab10')
            plt.draw()
            plt.pause(0.1)  # Add a small pause to visualize each step of the movement

            # You can add additional visualization updates here if needed

        # Add a final pause to keep the animation visible after completion
        plt.pause(2)

    def convert_grid_to_numerical(self):
        # Define a dictionary to map cell types to numbers
        cell_type_to_num = {
            Empty_Cell: 0,
            Loading_Cell: 1,
            Unloading_Cell: 2,
            Storage_Cell: 3,
            Route_Cell: 4
        }

        # Convert the grid to a numerical grid
        numerical_grid = [[cell_type_to_num[type(cell)] for cell in row] for row in self.grid]

        return numerical_grid

    def fetch_product(self, robot:Robot, cell:Cell, quantity:int):
        route_to_cell, route_back = self.generate_objective(robot, cell)
        #print(f"Route to cell: {route_to_cell}\n")
        self.move_robot(robot, route_to_cell)
        robot.load_product(quantity)
        self.move_robot(robot, route_back)
        robot.unload_product()
        completed_time = robot.get_objective_time()
        print(f"Robot number {robot.get_robot_id()} used {robot.get_objective_time()} seconds to complete the task\n")
        robot.reset_objective_time()
        return completed_time

    def handle_truck_load(self, truck_load: Truck_Load):
        completed_time = 0
        products = truck_load.get_products().copy()  # Create a copy of the dictionary
        for product, quantity in products.items():
            while quantity > 0:
                print(f"Product: {product.get_code()}, Quantity: {quantity}\n")
                storage_cell = self.find_storage_cell(product)
                robot = self.get_available_robot()
                while robot is None:
                    robot = self.get_available_robot()
                route_to_cell, route_back = self.generate_objective(robot, storage_cell)
                quantity_able_to_carry = min(quantity, robot.get_available_capacity() // product.get_weight())
                robot.set_on_hand(product, quantity_able_to_carry)
                truck_load.decrease_quantity(product, quantity_able_to_carry)
                quantity -= quantity_able_to_carry
                self.move_robot(robot, route_to_cell)
                robot.restock_product()
                self.move_robot(robot, route_back)
        completed_time = robot.get_objective_time()
        print(f"Robot number {robot.get_robot_id()} used {robot.get_objective_time()} seconds to complete the task\n")
        robot.reset_objective_time()
        return completed_time

    def handle_order(self, order:Order) -> None:
        product = order.get_product()
        quantity = order.get_quantity()
        storage_cell = self.find_storage_cell(product)
        robot = self.get_available_robot()
        while self.get_available_robot() == None:
            robot = self.get_available_robot()
        completed_time = self.fetch_product(robot, storage_cell, quantity)
        self.completed_orders[order] = completed_time
        self.remaining_orders.remove(order)

    # def handle_truck_load(self, truck_loads: list):
    #     for truck_load in truck_loads:
    #         products = truck_load.get_products()
    #         for product, quantity in products:
    #             storage_cell = self.find_storage_cell(product)
    #             robot = self.get_available_robot()
    #             while self.get_available_robot() == None:
    #                 robot = self.get_available_robot()
    #             completed_time = self.restock_product(robot, storage_cell, quantity)
    #             truck_load[product] -= quantity
    #             if truck_load[product] == 0:
    #                 del truck_load[product]
    #         truck_loads.remove(truck_load)