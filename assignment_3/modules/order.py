import random
from .catalog import Catalog
from .product import Product

class Order:
    last_order_number = 0
    
    
    def __init__(self, name:str, catalog:Catalog) -> None:
        self.customer = name
        Order.last_order_number += 1
        self.order_number = Order.last_order_number
        self.catalog = catalog
        self.product = None
        self.quantity = None
        
    def __str__(self) -> str:
        return f"Order {self.order_number} by {self.customer}: {self.quantity} piece(s) of {self.product}"

    def __repr__(self) -> str:
        return str(self)
    
    def get_customer(self) -> str:
        return self.customer

    def get_catalog(self) -> list:
        return self.catalog
    
    def set_name(self, new_name:str) -> None:
        self.code = new_name

    def get_order_number(self) ->int:
        return self.order_number


    def generate_random_order(self) -> None:
        self.product = random.choice(self.catalog.get_products())
        self.quantity = random.randint(1, 100)

        
