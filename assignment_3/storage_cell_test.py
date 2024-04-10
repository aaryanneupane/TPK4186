from modules.warehouse import Warehouse
from modules.printer import Printer

new_warehouse = Warehouse(1, 3, 2, 1)

new_printer = Printer(new_warehouse)

new_printer.print_catalog()

anne = new_warehouse.get_catalog().get_product_by_code("Anne")
print(new_warehouse.find_storage_cell(anne))