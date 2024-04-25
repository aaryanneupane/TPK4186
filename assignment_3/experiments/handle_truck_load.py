from modules.warehouse import Warehouse
from modules.truck_load import Truck_Load


new_warehouse = Warehouse(4, 6, 10, 3)

new_warehouse.add_truck_load_to_warehouse()

print(new_warehouse.truck_loads)

available_robot = new_warehouse.get_available_robot()

new_warehouse.handle_truck_load(new_warehouse.truck_loads[0], available_robot)
