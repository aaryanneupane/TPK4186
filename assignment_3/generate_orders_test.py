from modules.warehouse import Warehouse


new_warehouse = Warehouse(1, 3, 10, 1)

new_warehouse.add_order_to_warehouse("Anne")

order_list = new_warehouse.get_order_list()   #Have made a string method in order, but not sure how to print this