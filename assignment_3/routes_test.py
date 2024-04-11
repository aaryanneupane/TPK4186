from modules.warehouse import Warehouse
from modules.printer import Printer

new_warehouse = Warehouse(4, 6, 120, 5)

new_printer = Printer(new_warehouse)

new_printer.print_warehouse()
# new_printer.print_catalog()
# new_printer.print_cell((1, 1))
# print(new_warehouse.get_cell((4, 0)).get_available_robots())

to_storage = new_warehouse.calculate_route_to_storage_cell(
    new_warehouse.get_cell((1, 19))
)

for route in to_storage:
    print(route)

back_to_loading = new_warehouse.calculate_route_back_to_loading_cell(
    new_warehouse.get_cell((13, 19))
)
print("Back to loading:\n")
for route in back_to_loading:
    print(route)
