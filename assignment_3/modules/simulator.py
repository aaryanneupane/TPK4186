from modules.warehouse import Warehouse
from modules.robot import Robot
import random

class Simulator:
    client_list = ["Anne", "John", "Kari", "Lise", "Tora", "Lars", "Antoine", "Bjørn", "Helene", "Julie", "Johanne", "Erik"]

    def __init__(self, end_time:int) -> None:
        self.time = end_time
        self.current_time = 0
       
        
    def execute_simulation_loop(self):
        warehouse = Warehouse(1,3,10,1)
        for _ in range(self.time):
            warehouse.handle_next_time_step()
            if (self.current_time%1000==0):
                order_name = random.choice(Simulator.client_list)
                warehouse.add_order_to_warehouse(order_name)
            self.current_time+=1
            #for robot in robots:
                #robot.set_global_state()
                #robot.get_current_pos()
           

   

  
    

    