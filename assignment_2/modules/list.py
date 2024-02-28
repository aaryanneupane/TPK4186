
class List:
    def __init__(self, list_type, items = []):
        self.list_type = list_type
        self.items = items

    def get_list_type(self):
        if self.list_type == "uo":
            return "unordered"
        return "ordered"

    def get_items(self) -> list:
        return self.items
    
    def get_item(self, index: int) -> str:
        return self.items[index]
    
    def delete_item(self, index: int) -> None:
        self.items.pop(index)

    def add_item(self, item) -> None:
        self.items.append(item)
