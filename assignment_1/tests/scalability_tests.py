import timeit as t
import time as t2
from generators.grid_generator import grid_generator
from generators.square_generator import square_generator

"""This is an experiment to check the run times for the different functionalities to check their scalability"""


# Running for the square generator
def measure_square_generator_performance():
    setup_code = "from generators.square_generator import square_generator"
    stmts = [
        "square_generator('Scalibility_1', 100)",
        "square_generator('Scalibility_2', 1000)",
        "square_generator('Scalibility_3', 10000)",
    ]
    execution_times = []
    for stmt in stmts:
        execution_time = t.timeit(stmt=stmt, setup=setup_code, number=1)
        execution_times.append(round(execution_time, 2))
    return execution_times

# Running for the grid generator
def measure_grid_generator_performance():
    setup_code = "from generators.grid_generator import grid_generator"
    stmts = [
        "grid_generator('Scalibility_4', 10, 10)",
        "grid_generator('Scalibility_5', 100, 10)",
        "grid_generator('Scalibility_6', 100, 100)",
    ]
    execution_times = []
    for stmt in stmts:
        execution_time = t.timeit(stmt=stmt, setup=setup_code, number=1)
        execution_times.append(round(execution_time, 2))
    return execution_times

# Running for the fastest route in the given network
def measure_fastest_route_performance(
    network, source_node_code, end_node_code, day, time
):
    start_time = t2.time()
    network.fastest_route(source_node_code, end_node_code, day, time)
    end_time = t2.time()
    execution_time = end_time - start_time
    return round(execution_time, 5)

def main():
    # Calculate the running times for the square and grid generators
    square_generator_times = measure_square_generator_performance()
    grid_generator_times = measure_grid_generator_performance()
    nodes = [100, 1000, 10000]

    for i, n in enumerate(nodes):
        print(f'''\n
              The runtime for generating a square network with {n} nodes was {square_generator_times[i]} seconds.
              The runtime for generating a grid network with {n} nodes was {grid_generator_times[i]} seconds.
              \n''')

    # Create road network instances
    simple_square = square_generator("square_100", 100)
    complex_square = square_generator("square_1000", 1000)
    simple_grid = grid_generator("Grid_100", 10, 10)
    complex_grid = grid_generator("Grid_1000", 100, 10)

    # Measure the performance of finding the fastest route
    fastest_route_simple_square = measure_fastest_route_performance(network=simple_square,source_node_code="47",end_node_code="94",day="Thursday",time=420)
    fastest_route_simple_grid = measure_fastest_route_performance(network=simple_grid,source_node_code="35",end_node_code="77",day="Saturday",time=840,)
    fastest_route_complex_square = measure_fastest_route_performance(network=complex_square,source_node_code="94",end_node_code="864",day="Wednesday",time=1020,)
    fastest_route_complex_grid = measure_fastest_route_performance(network=complex_grid,source_node_code="452",end_node_code="134",day="Saturday",time=1140,)

    # Assuming an edge exists between the chosen nodes
    print(
        f"""\n
           [Square 100 Nodes] The runtime for finding the fastest route between the node 47 and 94 on a Thursday at 7 is {fastest_route_simple_square} seconds.
           [Grid 100 Nodes] The runtime for finding the fastest route between the node 35 and 77 on a Saturday at 14 is {fastest_route_simple_grid} seconds.
           \n
           [Square 1000 Nodes] The runtime for finding the fastest route between the node 94 and 864 on a Wednesday at 17 is {fastest_route_complex_square} seconds.
           [Grid 1000 Nodes] The runtime for finding the fastest route between the node 452 and 134 on a Tuesday at 19 is {fastest_route_complex_grid} seconds.
           \n"""
    )


if __name__ == "__main__":
    main()
