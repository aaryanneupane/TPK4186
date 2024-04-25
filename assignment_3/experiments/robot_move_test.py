from modules.warehouse import Warehouse
from modules.printer import Printer

new_warehouse = Warehouse(1, 3, 10, 1)

new_warehouse.print_warehouse_layout()

route_to_cell = new_warehouse.calculate_route_to_storage_cell(
    new_warehouse.get_cell((0, 6))
)
# for route in route_to_cell:
#     print(route)

# print(new_warehouse.get_loading_cell()) # Check if robot is added to loading cell
# print(new_warehouse.get_available_robot())


# Give the first available robot a route to the storage cell
available_robot = new_warehouse.get_available_robot()
storage_cell = new_warehouse.get_cell((0, 6))
new_warehouse.generate_objective(available_robot, storage_cell)

#print(available_robot)

new_warehouse.move_robot(available_robot)

