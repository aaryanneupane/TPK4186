import numpy as np
from .cell import *
from .catalog import Catalog
from .product import Product
from .robot import Robot
from .order import Order
from .truck_load import Truck_Load
from time import sleep

class Warehouse:
    def __init__(
        self, ally_number: int, ally_size: int, num_products: int, num_robots: Robot
    ) -> None:
        self.height = ally_size * 2 + 4
        self.length = (
            ally_number * 6 + 1
        )  # Add 1 to the length to account for the extra column
        self.grid = np.empty(
            (self.height, self.length), dtype=object
        )  # Initialize an empty grid of objects
        self.num_robots = num_robots
        self.robots: list[Robot] = []
        self.max_product_types = (ally_size * 2 + (ally_number - 1) * 2 * ally_size) * 4
        if num_products > self.max_product_types:
            raise ValueError(
                "There cannot be more different products than available shelves"
            )
        self.catalog = Catalog()
        self.catalog.generate_random_catalog(num_products)
        self.generate_warehouse()
        self.orders = []
        self.remaining_orders = []
        self.canceled_orders = []
        self.completed_orders = {}
        self.order_weight = 0
        self.count_orders_for_truckload = 0
        self.truck_loads = []
        self.completed_truck_loads = {}

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
            self.add_cell("storage", (self.height - i - 1, 1))
            self.add_cell("storage", (i, self.length - 1))
            self.add_cell("storage", (self.height - i - 1, self.length - 1))

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
        print("Warehouse layout:")
        for row in self.grid:
            for cell in row:
                print(
                    cell or "empty", end=" "
                )  # Print the cell or empty space if cell is None
            print()  # Move to the next row
        print()

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
                    for shelf in cell.get_shelves():
                        if shelf.get_product() == product:
                            return cell
        return None

    def add_order_to_warehouse(self, name: str):
        new_order = Order(
            name, self.catalog
        )  # Assuming you have 'name' and 'catalog' defined somewhere
        new_order.generate_random_order()
        # we have not checked if the product is in
        if self.order_weight >= (400 - new_order.get_weight()):
            truck_load = Truck_Load(400)
            truck_order_list = self.orders[-(self.count_orders_for_truckload) :]
            truck_load.generate_truck_load(truck_order_list)
            self.truck_loads.append(truck_load)
            print(f"Truck load {truck_load} added to warehouse\n")
            self.order_weight = 0
            self.count_orders_for_truckload = 0
        self.orders.append(new_order)
        self.remaining_orders.append(new_order)
        self.order_weight += new_order.get_weight()
        self.count_orders_for_truckload += 1
        return new_order

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
            route.append(
                self.grid[loading_cell[0]][loading_cell[1]]
            )  # Append the current cell to the route
            if length_direction == "left":
                loading_cell = (loading_cell[0], loading_cell[1] - 1)
            else:
                loading_cell = (loading_cell[0], loading_cell[1] + 1)

        # Move vertically until reaching the same height as the destination cell
        while loading_cell[0] != vertical_distance:
            route.append(
                self.grid[loading_cell[0]][loading_cell[1]]
            )  # Append the current cell to the route
            if height_direction == "up":
                loading_cell = (loading_cell[0] - 1, loading_cell[1])
            else:
                loading_cell = (loading_cell[0] + 1, loading_cell[1])

        route.pop(0)  # Remove the first cell (loading cell) from the route

        # Append the last cell before the destination cell to the route
        if destination[1] % 2 == 0:
            # If the destination column index is even, add one step horizontally first
            route.append(
                self.grid[route[-1].get_position()[0]][route[-1].get_position()[1] + 1]
            )
        # Add the next step horizontally
        if destination[1] > route[-1].get_position()[1]:
            route.append(
                self.grid[route[-1].get_position()[0]][route[-1].get_position()[1] + 1]
            )
        elif destination[1] < route[-1].get_position()[1]:
            route.append(
                self.grid[route[-1].get_position()[0]][route[-1].get_position()[1] - 1]
            )

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
        height_direction = (
            "up" if unloading_cell_position[0] < current_position[0] else "down"
        )

        # Calculate the direction to move along the length axis (left or right)
        length_direction = (
            "left" if unloading_cell_position[1] < current_position[1] else "right"
        )

        # Determine whether to move forward or backward for two steps
        if current_position[1] % 2 == 0:  # If the destination column index is even
            # Move two steps backward horizontally
            for _ in range(2):
                current_position = (current_position[0], current_position[1] - 1)
                route_back.append(
                    self.grid[current_position[0]][current_position[1]]
                )  # Append the current cell to the route
        else:
            # Move two steps forward horizontally
            for _ in range(3):
                current_position = (current_position[0], current_position[1] + 1)
                route_back.append(
                    self.grid[current_position[0]][current_position[1]]
                )  # Append the current cell to the route

        # Move vertically until reaching the same height as the unloading cell
        while current_position[0] != unloading_cell_position[0]:
            if height_direction == "up":
                current_position = (current_position[0] - 1, current_position[1])
            else:
                current_position = (current_position[0] + 1, current_position[1])
            route_back.append(
                self.grid[current_position[0]][current_position[1]]
            )  # Append the current cell to the route

        route_back.pop(-1)  # Remove the last cell (unloading cell) from the route
        route_back.pop(0)  # Remove the first cell (current cell) from the route

        # Move horizontally until reaching column 0
        for _ in range(current_position[1], -1, -1):
            route_back.append(
                self.grid[current_position[0]][_]
            )  # Append the current cell to the route

        return route_back

    def generate_objective(self, robot: Robot, cell: Cell):
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

    def remove_robot_from_loading_cell(self, robot: Robot):
        self.get_loading_cell().remove_robot(robot)

    def add_available_robot(self, robot: Robot):
        self.get_loading_cell().add_robot(robot)

    def handle_truck_load(self, truck_load: Truck_Load, robot: Robot):
        print(f"Robot {robot.get_robot_id()} is handling truck load {truck_load}\n")
        self.remove_robot_from_loading_cell(robot)
        next_product = truck_load.get_first_item()
        # Finish the truck load if there are no more products
        if next_product is None: 
            self.truck_loads.remove(truck_load)
            self.add_available_robot(robot)
            robot.set_order(None)
            robot.set_objective_time(0)
            print(f"Truck load {truck_load} is completed\n")
            return
        truck_load.decrease_quantity(next_product[0], next_product[1])
        print(f"This many products left in truck load: {len(truck_load.get_products().keys())}\n")
        storage_cell = self.find_storage_cell(next_product[0])
        # Handle if the product is not in the warehouse
        if storage_cell is None:
            storage_cell = self.get_first_empty_cell()
            if storage_cell is None:
                raise ValueError("No empty storage cells available")
        robot.set_on_hand(next_product[0], next_product[1])
        route_to_cell, route_back = self.generate_objective(robot, storage_cell)
        print(route_to_cell)
        robot.set_route(route_to_cell)
        robot.set_second_last_cell(route_to_cell[-1])
        robot.set_route_back(route_back)
        robot.set_objective(True)
        robot.set_current_state("Moving")
        robot.set_order(truck_load)

    def get_first_empty_cell(self):
        for i in range(self.height):
            for j in range(self.length):
                cell = self.grid[i][j]
                if isinstance(cell, Storage_Cell):
                    for shelf in cell.get_shelves():
                        if shelf.get_product() is None:
                            return cell
        return None

    def handle_order(self, robot: Robot, order: Order) -> None:
        print(f"Robot {robot.get_robot_id()} is handling order {order.get_order_number()}\n")
        self.remove_robot_from_loading_cell(robot)
        product = order.get_product()
        quantity = order.get_quantity()
        storage_cell = self.find_storage_cell(product)
        if storage_cell is None:
            return None
        route_to_cell, route_back = self.generate_objective(robot, storage_cell)
        robot.set_route(route_to_cell)
        robot.set_second_last_cell(route_to_cell[-1])
        robot.set_route_back(route_back)
        robot.set_fetch_quantity(quantity)
        robot.set_objective(True)
        robot.set_order(order)
        robot.set_current_state("Moving")
        return True

    def handle_next_time_step(self):
        # Handle actions for each robot
        for robot in self.robots:
            time = robot.do_next_action()
            if time:
                # Check if the action completed a truck load
                if isinstance(robot.get_order(), Truck_Load):
                    self.add_available_robot(robot)
                    self.completed_truck_loads[robot.get_order()] = time
                    robot.set_order(None)
                    robot.set_objective_time(0)
                else:
                    # Handle completed order
                    self.add_available_robot(robot)
                    current_order = robot.get_order()
                    self.completed_orders[current_order] = time[0]
                    robot.set_order(None)
                    robot.set_objective_time(0)
                    robot.make_robot_available()

        # If there are remaining orders, prioritize them
        if len(self.remaining_orders) > 0:
            robot = self.get_available_robot()
            if robot is not None:
                no_stock = self.handle_order(robot, self.remaining_orders[0])
                if no_stock is None:
                    self.canceled_orders.append(self.remaining_orders[0])
                    self.add_available_robot(robot)
                    print(f"Order {self.remaining_orders[0].get_order_number()} was canceled\n")
                self.remaining_orders.remove(self.remaining_orders[0])

        # If there are no remaining orders but there are truck loads available, handle them
        elif len(self.truck_loads) > 0:
            robot = self.get_available_robot()
            if robot is not None:
                self.handle_truck_load(self.truck_loads[0], robot)  