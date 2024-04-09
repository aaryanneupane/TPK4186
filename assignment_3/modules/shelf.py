from .product import Product

class Shelf:
    def __init__(self) -> None:
        self.shelf = []
    
    def __str__(self) -> str:
        # shelf_str = "Shelf with products:\n" # To check every item
        # for item in self.shelf:
        #     shelf_str += str(item) + "\n"
        # return shelf_str
        return f"Shelf with {len(self.shelf)} products with code {self.shelf[0].get_code()} and weight {self.shelf[0].get_weight()}"

    def add_product(self, product:Product) -> None:
        total_weight = 0
        for item in self.shelf:
            total_weight += item.get_weight()
        if total_weight + product.get_weight() > 100:
            raise ValueError("Shelf is full")
        self.shelf.append(product)
    
    def remove_product(self, product:Product) -> None:
        self.shelf.remove(product)
    
    def remaining_capacity(self) -> int:
        total_weight = 0
        for item in self.shelf:
            total_weight += item.get_weight()
        return 100 - total_weight