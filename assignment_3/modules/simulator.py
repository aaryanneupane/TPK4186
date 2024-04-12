from modules.warehouse import Warehouse
from modules.robot import Robot

class simulator:
    def __init__(self, end_time:int) -> None:
        self.time = end_time
        self.current_time = 0
       
        
    def execute_simulation_loop(self):
        warehouse = Warehouse(1,3,10,1)
        robots = warehouse.get_robots()
        for _ in range(self.time):
            if (self.current_time%1000==0):
                warehouse.add_order_to_warehouse("Anne")
            if len(warehouse.get_remaining_orders()) > 0:
                self.warehouse.handle_order()
            for robot in robots:
                robot.set_global_state()
            self.current_time+=1

   

    def add_orders_with_frequency(self, end_time:int):
        for frequency in end_time(0, 5001, 500):
            self.warehouse.add_order_to_warehouse()

    

    