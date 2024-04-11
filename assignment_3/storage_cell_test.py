from modules.warehouse import Warehouse
from modules.printer import Printer

new_warehouse = Warehouse(1, 3, 10, 1)

new_printer = Printer(new_warehouse)

new_printer.print_catalog()

product = new_warehouse.get_catalog().get_product_by_code("Pocket Knife")
new_warehouse.print_warehouse_layout()
print(new_warehouse.find_storage_cell(product))   #This gives "No storage cell contains this product" because all products from the catalog is not necessarily in the warehouse....
