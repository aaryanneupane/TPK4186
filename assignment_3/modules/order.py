from .catalog import catalog
import random

class Order:
    def __init__(self, name:str, catalog:catalog) -> None:
        self.customer = name
        self.catalog = catalog
        self.items = {}
    
    def get_customer(self) -> str:
        return self.customer

    def get_catalog(self) -> list:
        return self.catalog
    
    def set_name(self, new_name:str) -> None:
        self.code = new_name



    def generate_random_order(self, num_products: int) -> None:
        for i in range(num_products):
            item = random.choice(self.get_catalog.products)
            num_item = random.randint(1, 100)
            self.items[item] = num_item