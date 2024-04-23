import numpy as np
import matplotlib.pyplot as plt
import random
from modules.project import Project
from modules.task import Task
from modules.gate import Gate



class MonteCarloSimulation:
    def  __init__(self, project: Project, samples: int):
        self.project = project
        self.samples = samples
    

    
    def setDurations(self):
        for task in self.project.getTasks():
            min = task.getMinimumDuration()
            max = task.getMaximumDuration()
            task.setExpectedDuration(random.randint(min, max))

        
    
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
                            node.setEndDate(node.getStartDate() + node.getExpectedDuration())
                        if isinstance(node, Gate):
                            node.setStartDate(start_time)
                            node.setEndDate(start_time)
                        remaining_tasks_and_gates.remove(node)
    
    
    def execute_simulation(self):
        project_durations = []
        for _ in range (self.samples):
            self.setDurations()
            self.calculateStartAndEndTimes()
            for gate in self.project.getGates():
                if gate.getName() == "end":
                    project_duration = gate.getEndDate()
                    project_durations.append(project_duration)
        durations_array = np.array(project_durations)
        mean = np.mean(durations_array)
        standard_deviation = np.std(durations_array)     
        min_value = np.min(durations_array)
        max_value = np.max(durations_array)
        median = np.percentile(durations_array, 50)
        quantile_90 = np.percentile(durations_array, 90)
        print("Mean:" + str(mean))
        print("Standard_deviation:" + str(standard_deviation))
        print("Minimum value:" + str(min_value))
        print("Maximum value:" + str(max_value))
        print("Median:" + str(median))
        print("Quantile 90:" + str(quantile_90))

        
        
        plt.hist(durations_array, bins=30, edgecolor='black')
        plt.title('Histogram of Project Durations')
        plt.xlabel('Duration')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
                            

        
