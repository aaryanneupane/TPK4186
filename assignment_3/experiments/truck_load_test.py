from modules.warehouse import Warehouse


new_warehouse = Warehouse(1, 3, 10, 1)

new_warehouse.add_order_to_warehouse("Anne")
new_warehouse.add_order_to_warehouse("Benny")
new_warehouse.add_order_to_warehouse("Anne")
new_warehouse.add_order_to_warehouse("Benny")
new_warehouse.add_order_to_warehouse("Anne")
new_warehouse.add_order_to_warehouse("Benny")
new_warehouse.add_order_to_warehouse("Anne")
new_warehouse.add_order_to_warehouse("Benny")
new_warehouse.add_order_to_warehouse("Anne")
new_warehouse.add_order_to_warehouse("Benny")
new_warehouse.add_order_to_warehouse("Anne")
new_warehouse.add_order_to_warehouse("Benny")
new_warehouse.add_order_to_warehouse("Anne")
new_warehouse.add_order_to_warehouse("Benny")
new_warehouse.add_order_to_warehouse("Anne")
new_warehouse.add_order_to_warehouse("Benny")
new_warehouse.add_order_to_warehouse("Benny")
new_warehouse.add_order_to_warehouse("Anne")
new_warehouse.add_order_to_warehouse("Benny")
new_warehouse.add_order_to_warehouse("Anne")
new_warehouse.add_order_to_warehouse("Benny")
new_warehouse.add_order_to_warehouse("Anne")
new_warehouse.add_order_to_warehouse("Benny")
new_warehouse.add_order_to_warehouse("Anne")
new_warehouse.add_order_to_warehouse("Benny")
new_warehouse.add_order_to_warehouse("Anne")
new_warehouse.add_order_to_warehouse("Benny")
new_warehouse.add_order_to_warehouse("Anne")
new_warehouse.add_order_to_warehouse("Benny")


order_list = new_warehouse.get_order_list()   #Have made a string method in order, but not sure how to print this

for order in order_list:
    print(order)
   
print(new_warehouse.get_order_weight())

print(new_warehouse.get_order_list())

print(new_warehouse.get_count_orders_for_truckload())
