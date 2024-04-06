import product

class Shelf:
    def __init__(self) -> None:
        self.shelf = []

    def add_product(self, product: product.Product) -> None:
        total_weight = 0
        for item in self.shelf:
            total_weight += item.get_weight()
        if total_weight + product.get_weight() > 100:
            raise ValueError("Shelf is full")
        self.shelf.append(product)