from modules.warehouse import Warehouse
from modules.printer import Printer

new_warehouse = Warehouse(1, 3, 10, 1)

new_printer = Printer(new_warehouse)

wanted_product = new_warehouse.get_product_by_code("Pocket Knife")

product_stored_at = new_warehouse.find_storage_cell(wanted_product)

print()
print(f"Wanted {wanted_product} and it is stored at {product_stored_at}\n")

available_robot = new_warehouse.get_available_robot()

new_warehouse.fetch_product(available_robot, product_stored_at, quantity=4)

new_warehouse.animate_warehouse()