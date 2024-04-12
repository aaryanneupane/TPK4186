from .product import Product

class Shelf:
    def __init__(self) -> None:
        self.product = []
    
    def __str__(self) -> str:
        # shelf_str = "Shelf with products:\n" # To check every item
        # for item in self.shelf:
        #     shelf_str += str(item) + "\n"
        # return shelf_str
        return f"Shelf with {len(self.product)} products with code {self.product[0].get_code()} and weight {self.product[0].get_weight()}"

    def add_product(self, product:Product) -> None:
        total_weight = 0
        for item in self.product:
            total_weight += item.get_weight()
        if total_weight + product.get_weight() > 1000000:
            raise ValueError("Shelf is full")
        self.product.append(product)
    
    def remove_product(self, product: Product) -> None:
        self.product.remove(product)
    
    def remaining_capacity(self) -> int:
        total_weight = 0
        for item in self.product:
            total_weight += item.get_weight()
        return 100 - total_weight
    
    def get_product(self) -> Product:
        if len(self.product) == 0:
            return None
        return self.product[0]
    
