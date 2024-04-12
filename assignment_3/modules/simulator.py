from modules.warehouse import Warehouse

class simulator:
    def __init__(self, warehouse:Warehouse, end_time:int) -> None:
        self.warehouse = warehouse
        self.time = end_time
        self.current_time = 0
        
    def execute_simulation_loop(self):
        for time in range(0, self.time):
            self.warehouse.handle_order()
        
    
        

    def add_orders_with_frequency(self, end_time:int):
        for frequency in end_time(0, 5001, 500):
            self.warehouse.add_order_to_warehouse()

    