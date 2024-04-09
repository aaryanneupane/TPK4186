from .product import Product

class Truck_Load:
    def __init__(self, delivery_number:str,  max_cap:int = 20 * 1000):
        self.delivery_number = delivery_number
        self.max_cap = max_cap
        self.products = dict()
        self.current_weight = self.calculate_weight()
        
    def calculate_weight(self) -> int:
        return sum([Product.get_weight() * quantity for Product, quantity in self.products.items()])
        
    def add_product(self, product:Product, quantity:int) -> bool:
        if self.current_weight + product.get_weight() * quantity > self.max_cap:
            return False
        if product.get_code() in self.products:
            self.products[product.get_code()] += quantity
        else:
            self.products[product.get_code()] = quantity
        self.current_weight += product.get_weight() * quantity
        return True