import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Grid size
grid_size = 10

# Number of robots
num_robots = 3

# Initialize positions of robots
robot_positions = np.random.randint(0, grid_size, size=(num_robots, 2))

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)

# Plot the initial positions of robots
robots, = ax.plot([], [], 'bo', ms=10)

def init():
    robots.set_data([], [])
    return robots,

def update(frame):
    # Move robots randomly
    for i in range(num_robots):
        move_x = np.random.randint(-1, 2)
        move_y = np.random.randint(-1, 2)
        
        # Update robot position
        robot_positions[i][0] = (robot_positions[i][0] + move_x) % grid_size
        robot_positions[i][1] = (robot_positions[i][1] + move_y) % grid_size

    # Update the positions of robots
    robots.set_data(robot_positions[:, 0], robot_positions[:, 1])
    return robots,

# Create animation
ani = FuncAnimation(fig, update, frames=range(50), init_func=init, blit=True, interval=200)

plt.show()
