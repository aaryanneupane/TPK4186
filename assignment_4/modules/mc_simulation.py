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
                task.setExpectedDuration(round(duration,2))
       
        for task in self.project.getTasks():
            min = task.getMinimumDuration()
            max = task.getMaximumDuration()
            actual=np.random.triangular(min, task.getExpectedDuration(), max, size=None)
            task.setActualDuration(round(actual,2))
        
    
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
                        node.setEndDate((start_time + node.getActualDuration()))
                    if isinstance(node, Gate):
                        node.setStartDate(start_time)
                        node.setEndDate(start_time)
                    remaining_tasks_and_gates.remove(node)
       
           
    

        
    
    def execute_simulation(self, csv_filename="simulation_results.csv"):
        
        project_durations = []
        with open(csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['Sample', 'Total_Duration', 'Total_duration_at_mid_gate'] + [task.getName() for task in self.project.getTasks()]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for sample in range(self.samples):
                self.setDurations()
                self.calculateStartAndEndTimes()
                
                task_durations = {task.getName(): task.getActualDuration() for task in self.project.getTasks()}
                total_duration_mid_project = 0
                total_duration = sum(task_durations.values())
                mid_gate = None
                for gate in self.project.getGates():
                    if gate.getName() == "MidProject":
                        mid_gate = gate

                for task in self.project.getTasks():
                    if task.getEndDate()<= mid_gate.getEndDate():
                        total_duration_mid_project+=task.getActualDuration()
                        
                project_durations.append(total_duration)

                writer.writerow({
                    'Sample': sample + 1,
                    'Total_Duration': total_duration,
                    **task_durations,
                    'Total_duration_at_mid_gate': round(total_duration_mid_project,2)
                })

        # After saving data to CSV, calculate and display statistics and histogram
        
        
        durations_array = np.array(project_durations)
        mean = np.mean(durations_array)
        standard_deviation = np.std(durations_array)
        min_value = np.min(durations_array)
        max_value = np.max(durations_array)
        median = np.percentile(durations_array, 50)
        quantile_90 = np.percentile(durations_array, 90)

        print("Mean:", round(mean,2))
        print("Standard_deviation:", round(standard_deviation,2))
        print("Minimum value:", round(min_value,2))
        print("Maximum value:", round(max_value,2))
        print("Median:", round(median,2))
        print("Quantile 90:", round(quantile_90,2))
        
        plt.hist(durations_array, bins=30, edgecolor='black')
        plt.title('Histogram of Project Durations')
        plt.xlabel('Duration')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

      

                            

        
