from modules.warehouse import Warehouse

new_warehouse = Warehouse(1, 3, 10, 2)


order = new_warehouse.add_order_to_warehouse("Anne")

print(new_warehouse.get_remaining_orders())

print(new_warehouse.get_robots())

for _ in range(100):
    new_warehouse.handle_next_time_step()
    if _ == 13:
        new_warehouse.add_order_to_warehouse("Tora")
        print(new_warehouse.get_remaining_orders())

    if _ == 50:
        new_warehouse.add_order_to_warehouse("Anne")
        print(new_warehouse.get_remaining_orders())

print(new_warehouse.get_completed_order_list())
print(new_warehouse.get_remaining_orders())
