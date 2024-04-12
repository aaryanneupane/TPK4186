from modules.warehouse import Warehouse

new_warehouse = Warehouse(1, 3, 10, 1)


new_order = new_warehouse.add_order_to_warehouse("Anne")

print(new_warehouse.get_remaining_orders())

new_warehouse.handle_order(new_order)
new_warehouse.animate_warehouse()

print(new_warehouse.get_completed_order_list())
print(new_warehouse.get_remaining_orders())
