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

        
   
    def addClassifications(self, gate : Gate):
         
        with open(self.filename, newline = '') as csvfile, \
            open("classified_" + self.filename, 'w', newline='') as classified_file:
            reader = csv.reader(csvfile)
            writer = csv.writer(classified_file)


            header = next(reader)
            writer.writerow(header)
            header.append('Status')    
            for row in reader:
                print(row)
                minimumTotalDuration = 0
                maximumTotalDuration = 0
                #totalDuration = float(row[1])
                if gate.getName() == "MidProject":
                    totalDuration = float(row[2])
                if gate.getName() == "end":
                    totalDuration = float(row[1])
                tasks_checked = []
                for task in self.project.getTasks():
                    if task.getEndDate() <= gate.getStartDate() and task not in tasks_checked:   
                            minimumTotalDuration += task.getMinimumDuration()
                            maximumTotalDuration += task.getMaximumDuration()
                            tasks_checked.append(task)           
                            #denne burde også kanskje lese fra fil? vi kunne lagt til kolonner i fila: max/min tid ved middle gate og samme for end gate
                            #også heller fått tallene derfra
                                           
                                    
                print('For rad:')
                print(row)
                print('og gaten er:')
                print(gate.getName())
                print('så er actual total duration på gaten:')
                print(totalDuration)
                print('minimum total duration på gaten:')
                print(minimumTotalDuration)
                print('maximum total duration på gaten:')
                print(maximumTotalDuration)

                if (totalDuration < (1.3 * minimumTotalDuration)):
                    label = "on-time"
                elif (totalDuration > 1.3 * minimumTotalDuration) and (totalDuration < maximumTotalDuration):
                    label = "delayed"
                else: label = "failure"
                print(label)
                row.append(label)
                writer.writerow(row)
                                

                        
    
    def classify(self):
        
        sim = MonteCarloSimulation(self.project, 10)
        sim.execute_simulation(self.filename)

        self.addClassifications(self.gate)