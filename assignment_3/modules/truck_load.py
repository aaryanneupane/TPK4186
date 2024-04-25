from .product import Product
from .catalog import Catalog 


class Truck_Load:
    last_delivery_number = 0
    
    def __init__(self, max_cap:int = 20 * 1000):
        Truck_Load.last_delivery_number += 1
        self.delivery_number = Truck_Load.last_delivery_number
        self.max_cap = max_cap
        self.products = dict()
        self.current_weight = self.calculate_weight()

    def __str__(self) -> str:
        return f"Delivery number: {self.delivery_number}, current weight: {self.current_weight}, max weight: {self.max_cap}"
    
    def __repr__(self) -> str:
        return str(self)
        
    def calculate_weight(self) -> int:
        return sum([Product.get_weight() * quantity for Product, quantity in self.products.items()])
        
    def add_product(self, product:Product, quantity:int) -> bool:
        if self.current_weight + product.get_weight() * quantity > self.max_cap:
            return False
        if product.get_code() in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity
        self.current_weight += product.get_weight() * quantity
        return True
    
    def generate_truck_load(self, truck_order_list: list):
        for order in truck_order_list:
            self.add_product(order.get_product(), order.get_quantity())
        
    def generate_random_truck_load(self,  catalog:Catalog):
        for product in catalog.get_products():
            self.add_product(product, 2) # 2 is a random number, it can be changed to any number

    def get_products(self) -> dict:
        return self.products
    
    def get_first_item(self) -> tuple[Product, int]:
        if len(self.products) == 0:
            return None
        return next(iter(self.products.items()))

    
    def decrease_quantity(self, product:Product, quantity:int) -> None:
        print(self.products)
        self.products[product] -= quantity
        self.current_weight -= product.get_weight() * quantity
        if self.products[product] == 0:
            self.products.pop(product)
    

        