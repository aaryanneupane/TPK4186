from modules.warehouse import Warehouse
from modules.robot import Robot
from modules.cell import *
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors



class Simulator:
    client_list = [
        "Anne",
        "John",
        "Kari",
        "Lise",
        "Tora",
        "Lars",
        "Antoine",
        "Bjørn",
        "Helene",
        "Julie",
        "Johanne",
        "Erik",
    ]

    def __init__(self, end_time: int, ally_size:int, storage_size:int, product_size:int, robot_size:int) -> None:
        self.time = end_time
        self.current_time = 0
        self.ally_size = ally_size
        self.storage_size = storage_size
        self.product_size = product_size
        self.robot_size = robot_size
        self.robot_markers = {}
        self.colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)  # Dictionary of available colors

    def plot_warehouse(self, warehouse:Warehouse):
        # Define a dictionary to map cell types to numbers
        cell_type_to_num = {Empty_Cell: 0, Loading_Cell: 1, Unloading_Cell: 2, Storage_Cell: 3, Route_Cell: 4}

        # Convert the grid to a numerical grid
        numerical_grid = [[cell_type_to_num[type(cell)] for cell in row] for row in warehouse.grid]

        # Initialize a plot of the warehouse grid
        self.fig, self.ax = plt.subplots()
        self.grid = numerical_grid
        self.im = self.ax.imshow(self.grid, cmap='gray', interpolation='none')

        # Display the grid as an image
        self.ax.set_xticks(range(warehouse.length))
        self.ax.set_yticks(range(warehouse.height))
        self.ax.set_xticklabels(range(warehouse.length))
        self.ax.set_yticklabels(range(warehouse.height))
        self.ax.tick_params(axis='both', which='both', length=0)  # Hide ticks

        # Create gridlines at each cell boundary
        self.ax.set_xticks([x - 0.5 for x in range(1, warehouse.length)], minor=True)
        self.ax.set_yticks([y - 0.5 for y in range(1, warehouse.height)], minor=True)
        self.ax.grid(which='minor', color='k', linewidth=2)

        #plt.show()

    def update_warehouse(self, frame, warehouse:Warehouse):

        if self.current_time >= self.time:
            print(f"------------------------------------------------------------------------------------------------")
            print("\nSimulation has ended\n")
            print(f"------------------------------------------------------------------------------------------------\n")
            total_time = 0
            number_of_completed_orders = len(warehouse.completed_orders)
            number_of_cancelled_orders = len(warehouse.canceled_orders)
            remaining_orders = len(warehouse.remaining_orders)
            for order, time in warehouse.completed_orders.items():
                total_time += time

            average_pick_up_time = total_time / number_of_completed_orders

            print(f"At the end of the simulation of {self.time} seconds, with {len(warehouse.get_robots())} robots, in a {warehouse.get_warehouse_height()} X {warehouse.get_warehouse_length()} Warehouse, these are our results:\n")
            print(f"The total amount of orders delivered were: {number_of_completed_orders}\n")
            print(f"The total amount of cancelled orders were: {number_of_cancelled_orders}\n")
            print(f"The amount of remaining orders we could not deliver: {remaining_orders}\n")
            print(f"The average amount of time it took to pick up the order was {average_pick_up_time}\n")
            print(f"The amount of truck loads that were handled are: {len(warehouse.completed_truck_loads.keys())}\n")
            if sum(warehouse.completed_truck_loads.values()):
                print(f"The average amount of time it took to handle a truck load was: {sum(warehouse.completed_truck_loads.values()) / len(warehouse.completed_truck_loads)}\n")
            return
        
        warehouse.handle_next_time_step()
        if self.current_time % 140 == 0:
                order_name = random.choice(Simulator.client_list)
                warehouse.add_order_to_warehouse(order_name)
        self.current_time += 10
        
        # Update the plot based on the current state of the warehouse
        for robot in warehouse.get_robots():
            pos = robot.get_current_pos().get_position()
            color = self.get_robot_color(robot.get_robot_id())
            if robot.get_robot_id() not in self.robot_markers:
                self.robot_markers[robot.get_robot_id()] = self.ax.plot(pos[1], pos[0], 'o', markersize=8, color=color)[0]  # Add marker for new robot
            else:
                self.robot_markers[robot.get_robot_id()].set_data(pos[1], pos[0])  # Update marker position for existing robot
            print(f"Robot {robot.get_robot_id()} is at position {pos}")
        self.im.set_array(self.grid)
        return self.im,

    def get_robot_color(self, robot_id):
        # Return a color for a given robot ID
        color_index = robot_id % len(self.colors)
        return list(self.colors.values())[color_index]

    def animate_warehouse(self, warehouse):
        # Animate the warehouse plot
        ani = animation.FuncAnimation(self.fig, self.update_warehouse, frames=range(self.time), fargs=(warehouse,), interval=200)
        plt.show()

    def execute_simulation_loop(self):
        warehouse = Warehouse(self.ally_size, self.storage_size, self.product_size, self.robot_size)
        self.plot_warehouse(warehouse)
        self.animate_warehouse(warehouse)
        plt.pause(0.1)  # Add a pause to display each frame
        #print(f"The remaining order are {warehouse.get_remaining_orders()}")
        total_time = 0
        number_of_completed_orders = len(warehouse.completed_orders)
        number_of_cancelled_orders = len(warehouse.canceled_orders)
        remaining_orders = len(warehouse.remaining_orders)
        for order, time in warehouse.completed_orders.items():
            total_time += time

        average_pick_up_time = total_time / number_of_completed_orders

        print(f"At the end of the simulation of {self.time} seconds, with {len(warehouse.get_robots())} robots, these are our results:\n")
        print(f"The total amount of orders delivered were: {number_of_completed_orders}\n")
        print(f"The total amount of cancelled orders were: {number_of_cancelled_orders}\n")
        print(f"The amount of remaining orders we could not deliver: {remaining_orders}\n")
        print(f"The average amount of time it took to pick up the order was {average_pick_up_time}")
