from .product import Product

class Truck_Delivery:
    def __init__(self, delivery_num:str,  max_cap:int = 20 * 1000):
        self.delivery_num = delivery_num
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