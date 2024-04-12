from modules.warehouse import Warehouse
from modules.robot import Robot
import random

class Simulator:
    client_list = ["Anne", "John", "Kari", "Lise", "Tora", "Lars", "Antoine", "Bjørn", "Helene", "Julie", "Johanne", "Erik"]

    def __init__(self, end_time:int) -> None:
        self.time = end_time
        self.current_time = 0
       
        
    def execute_simulation_loop(self):
        warehouse = Warehouse(1,3,10,2)
        for _ in range(1, self.time, 10):
            warehouse.handle_next_time_step()
            if (self.current_time%100==0):
                order_name = random.choice(Simulator.client_list)
                warehouse.add_order_to_warehouse(order_name)
            self.current_time+=10
            print(warehouse.get_remaining_orders())
        total_time = 0
        number_of_completed_orders = len(warehouse.completed_orders)
        for order,time in warehouse.completed_orders.items():
            total_time+= time

        average_pick_up_time = total_time/number_of_completed_orders
        print(f"At the end of the simulation of {self.time} seconds, these are our results:" + "\n")
        print(f"The total amount of orders delivered were: {number_of_completed_orders}\n")
        print(f"The average amount of time it took to pick up the order was {average_pick_up_time} seconds\n")