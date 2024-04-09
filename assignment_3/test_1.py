from modules.warehouse import Warehouse
from modules.printer import Printer

new_warehouse = Warehouse(1, 3, 10, 1)

new_printer = Printer(new_warehouse)

new_printer.print_warehouse()
new_printer.print_catalog()
new_printer.print_cell((1, 1))
# print(new_warehouse.get_cell((4, 0)).get_available_robots())

for route in new_warehouse.calculate_route(new_warehouse.get_cell((9, 6))):
    print(route)
