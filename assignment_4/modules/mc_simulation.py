import numpy as np
import matplotlib.pyplot as plt
import random
from modules.project import Project
from modules.task import Task
from modules.gate import Gate
import csv


class MonteCarloSimulation:
    def  __init__(self, project: Project, samples: int):
        self.project = project
        self.samples = samples
    

    
    def setDurations(self):
        for lane in self.project.getLanes():
            workload = random.random()
            for task in lane.getTasks():
                duration = task.getMinimumDuration() + (task.getMaximumDuration() - task.getMinimumDuration())*workload
                task.setExpectedDuration(duration)
       
        for task in self.project.getTasks():
            min = task.getMinimumDuration()
            max = task.getMaximumDuration()
            print("dette er min og max")
            print(min)
            print(max)
            rand= random.randint(min, max)
            task.setActualDuration(rand)

        
    
    def calculateStartAndEndTimes(self):
        # Step 1: Initialize start and completion dates of all nodes at -1
        remaining_tasks_and_gates = []
        
        for task in self.project.getTasks():
            task.setStartDate(-1)
            task.setEndDate(-1)
            remaining_tasks_and_gates.append(task)
            
        for gate in self.project.getGates():
            gate.setStartDate(-1)
            gate.setEndDate(-1)
            remaining_tasks_and_gates.append(gate)

        while len(remaining_tasks_and_gates) > 0:
            
        
        
            for node in remaining_tasks_and_gates:
                has_predecessor_in_remaining = False
                for predecessor in node.getPredecessors():
                    if predecessor in remaining_tasks_and_gates:
                        has_predecessor_in_remaining = True
                        break
                
                if has_predecessor_in_remaining:
                    continue

                else:
                    start_time = 0
                    for predecessor in node.getPredecessors():
                        if predecessor.getEndDate() > start_time:
                            start_time = predecessor.getEndDate()
                    if isinstance(node, Task): 
                        node.setStartDate(start_time)
                        node.setEndDate(node.getStartDate() + node.getActualDuration())
                    if isinstance(node, Gate):
                        node.setStartDate(start_time)
                        node.setEndDate(start_time)
                        
                    remaining_tasks_and_gates.remove(node)
    

        
    
    def execute_simulation(self, csv_filename="simulation_results.csv"):
        
         
        with open(csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['Sample', 'Total_Duration'] + [task.getName() for task in self.project.getTasks()]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for sample in range(self.samples):
                self.setDurations()
                self.calculateStartAndEndTimes()
                
                task_durations = {task.getName(): task.getActualDuration() for task in self.project.getTasks()}
                
                total_duration = None
                for gate in self.project.getGates():
                    print(gate.getName())
                    print(gate.getEndDate())
                    if gate.getName() == "end":
                        total_duration = gate.getEndDate()
                        break
            
                
                writer.writerow({
                    'Sample': sample + 1,
                    'Total_Duration': total_duration,
                    **task_durations
                })
        

                
        

        # After saving data to CSV, calculate and display statistics and histogram
        project_durations = list(task_durations.values())
        
        durations_array = np.array(project_durations)
        mean = np.mean(durations_array)
        standard_deviation = np.std(durations_array)
        min_value = np.min(durations_array)
        max_value = np.max(durations_array)
        median = np.percentile(durations_array, 50)
        quantile_90 = np.percentile(durations_array, 90)

        print("Mean:", mean)
        print("Standard_deviation:", standard_deviation)
        print("Minimum value:", min_value)
        print("Maximum value:", max_value)
        print("Median:", median)
        print("Quantile 90:", quantile_90)
        
        '''plt.hist(durations_array, bins=30, edgecolor='black')
        plt.title('Histogram of Project Durations')
        plt.xlabel('Duration')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()''' #This is commented out as the code wont stop running when we have this.

      

                            

        
