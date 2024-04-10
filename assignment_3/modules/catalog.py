from .product import Product

import random
class Catalog:
    def __init__(self) -> None:
        self.products: list[Product] = []
    
    def __str__(self) -> str:
        product_codes = [product.get_code() for product in self.products]
        return f"Catalog with products:\n{product_codes}"

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        self.products.remove(product)

    def get_product_by_code(self, code: str) -> Product:
        for product in self.products:
            if product.get_code() == code:
                return product
        return None

    def generate_random_catalog(self, num_products:int) -> None:
        for _ in range(num_products):
            code = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=6))
            
            weight = self.random_weight()
            product = Product(code, weight)
            self.add_product(product)

    def random_weight(self) -> int:
        if random.random() < 0.8:
            return random.randint(2, 9)
        else:
            return random.randint(10, 40)

    def get_products(self) -> list:
        return self.products

    def get_random_product(self) -> Product:
        return random.choice(self.products) if self.products else None
    
    def get_product_by_code(self, code:str) -> Product:
        for product in self.products:
            if product.get_code() == code:
                return product
        return None