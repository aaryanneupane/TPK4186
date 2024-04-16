import matplotlib.pyplot as plt
import matplotlib.animation as animation
from modules.warehouse import Warehouse
from modules.cell import Route_Cell

class Warehouse_Animator:
    def __init__(self, warehouse):
        self.warehouse = warehouse
        self.fig, self.ax = plt.subplots()
        self.ax.set_title("Warehouse Simulation")
        self.img = None

    def update(self, frame):
        # Clear the previous frame
        self.ax.clear()

        # Plot the warehouse grid
        for i in range(self.warehouse.get_warehouse_height()):
            for j in range(self.warehouse.get_warehouse_length()):
                cell = self.warehouse.get_cell((i, j))
                color = 'white' if isinstance(cell, Route_Cell) else 'gray'
                self.ax.add_patch(plt.Rectangle((j, -i), 1, 1, color=color))

        # Plot robots
        for robot in self.warehouse.get_robots():
            pos = robot.get_current_pos().get_position()
            self.ax.add_patch(plt.Rectangle((pos[1], -pos[0]), 1, 1, color='blue'))

        # Set axis limits
        self.ax.set_xlim(0, self.warehouse.get_warehouse_length())
        self.ax.set_ylim(-self.warehouse.get_warehouse_height(), 0)

    def animate(self):
        anim = animation.FuncAnimation(self.fig, self.update, frames=100, interval=500)
        plt.show()

# Usage:
warehouse = Warehouse(4, 6, 10, 4)
visualization = Warehouse_Animator(warehouse)
visualization.animate()
