from modules.project import Project
from modules.gate import Gate
from modules.mc_simulation import MonteCarloSimulation
import csv


class Classification:


    
    def __init__(self, project: Project, gate: Gate, maximumDuration : int, filename: str):
        self.project = project
        self.gate = gate
        self.maximumDuration = maximumDuration
        self.filename = filename
        self.gate = gate
    
    def read_total_durations(self):
        total_durations = []

        with open(self.filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            
            for row in reader:
                total_duration = float(row[1])  # Assuming the second element is the total duration
                total_durations.append(total_duration)
                
        return total_durations
    
    
    def decideClassification(self):
        minimumTotalDuration = 0
        maximumTotalDuration = 0
        totalDuration = 0
        gate = self.gate
        for task in self.project.getTasks():
            if task.getEndDate() <= gate.getStartDate():
                print(task.getActualDuration())
                
                minimumTotalDuration += task.getMinimumDuration()
                maximumTotalDuration += task.getMaximumDuration()

                totalDuration += task.getActualDuration()
        print(totalDuration)
        print(minimumTotalDuration)      
        if totalDuration < (1.3 * minimumTotalDuration):
            label = "on-time"
        if totalDuration > ((1.3 * minimumTotalDuration) and (totalDuration < maximumTotalDuration)):
            label = "delayed"
        else: label = "failure"
        
        return label
        

                        
    
    def classify(self):
        
        sim = MonteCarloSimulation(self.project, 50)
        sim.execute_simulation(self.filename)

        for sample in sim:
            status = self.decideClassification()
        
        total_durations = self.read_total_durations()
        
        with open(self.filename, 'r') as csvfile, \
            open("classified_" + self.filename, 'w', newline='') as classified_file:
            reader = csv.reader(csvfile)
            writer = csv.writer(classified_file)

        # Read the header and write it to the new file with an additional 'Status' column
            header = next(reader)
            writer.writerow(header + ['Status'])

        # Iterate through each row (sample) in the existing file
            for row, duration in zip(reader, total_durations):
                # Determine the status based on the duration
                status = self.decideClassification()
                # Write the row along with the status to the new file
                writer.writerow(row + [status])
            
            