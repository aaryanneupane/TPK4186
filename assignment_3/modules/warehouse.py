
class Warehouse:
    def __init__(self, height, length) -> None:
        self.height = height
        self.length = length
        self.route_cells = []
        for i in range(height):
            for j in range(length):
                self.storage_cells.append(Storage_Cell())
        