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
        if len(self.product) > 0:
            if product.get_code() == self.product[0].get_code():
                for item in self.product:
                    total_weight += item.get_weight()
                    if total_weight + product.get_weight() > 100:
                        print(total_weight)       #hva skal skje med resten av produktene når det er fullt? Når det kommer en truckload ikke ved initialisering 
                        print("Shelf is full")    #kanskje ha en egen metode for å fylle opp hyllen ved restock
                    else:
                        self.product.append(product)
            else:
                raise ValueError("You can only have one type of product per shelf. Find another shelf.")
        else: 
            if product.get_weight() > 100:
                raise ValueError("Shelf is full")
            self.product.append(product) 
    
 
    
    def remove_product(self, product: Product) -> None:
        self.shelf.remove(product)
    
    def remaining_capacity(self) -> int:
        total_weight = 0
        for item in self.product:
            total_weight += item.get_weight()
        return 100 - total_weight
    
    def get_product(self) -> Product:
        if len(self.product) == 0:
            return None
        return self.product[0]
    
