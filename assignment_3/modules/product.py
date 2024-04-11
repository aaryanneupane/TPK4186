class Product:
    def __init__(self, code:str, weight:int) -> None:
        self.code = code
        if weight < 2 or weight > 40:
            raise ValueError("Weight must be between 2 and 40")
        self.weight = weight
    
    def __str__(self) -> str:
        return f"product name {self.code} with weight {self.weight}"

    def get_code(self) -> str:
        return self.code

    def get_weight(self) -> int:
        return self.weight
    
    def set_code(self, new_code:str) -> None:
        self.code = new_code
    
    def set_weight(self, new_weight:int) -> None:    
        if new_weight < 2 or new_weight > 40:
            raise ValueError("Weight must be between 2 and 40")
        self.weight = new_weight