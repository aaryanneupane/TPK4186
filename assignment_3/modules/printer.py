from .warehouse import Warehouse

class Printer:
    def __init__(self, warehouse:Warehouse) -> None:
        self.warehouse = warehouse
        pass


    def print_catalog(self) -> None:
        print("Catalog:")
        for product in self.warehouse.get_catalog_products():
            print(product)
        print()
    
    def print_warehouse(self) -> None:
        print("Warehouse length:" + str(self.warehouse.get_warehouse_length()) + "\n")
        print("Warehouse height:" + str(self.warehouse.get_warehouse_height()) + "\n")
        print("Number of shelves:" + str(self.warehouse.get_number_of_shelves()) + "\n")
        print("Number of products:" + str(len(self.warehouse.get_catalog_products())) + "\n")
        print("Number of Robots:" + str(len(self.warehouse.get_robots())) + "\n")
        self.warehouse.print_warehouse_layout()   
    
    def print_cell(self, position:tuple) -> None:
        if self.warehouse.is_valid_position(position):
            cell = self.warehouse.get_cell(position)
            if cell.get_type() == "SC":
                for shelf in cell.shelves:
                    print(shelf)
        else:
            print("Invalid position")