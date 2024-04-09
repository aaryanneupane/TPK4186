from .product import Product

import random

class catalog:
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        self.products.remove(product)

    def get_product_by_code(self, code: str) -> Product:
        for product in self.products:
            if product.get_code() == code:
                return product
        return None

    def generate_random_catalog(self, num_products: int) -> None:
        for _ in range(num_products):
            code = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=6))
            weight = random.randint(2, 40)
            product = Product(code, weight)
            self.add_product(product)