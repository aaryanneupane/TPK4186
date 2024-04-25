from modules.warehouse import Warehouse

new_warehouse = Warehouse(1, 3, 10, 1)

new_warehouse.add_truck_load_to_warehouse()

print(new_warehouse.get_truck_loads())

for truck_load in new_warehouse.get_truck_loads():
    print(truck_load.get_products())

first_load = new_warehouse.get_truck_loads()[0]

new_warehouse.handle_truck_load(first_load)

print(new_warehouse.get_truck_loads())