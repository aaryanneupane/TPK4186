from modules.project import Project
from modules.gate import Gate
from modules.mc_simulation import MonteCarloSimulation
import csv
import numpy
import sys
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


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


    
    def training_and_testing(self):
        data = pd.read_csv("classified_results.csv")

        # Shuffle the rows to ensure randomness
        data = data.sample(frac=1, random_state=42).reset_index(drop=True)

        # Determine the index for splitting (80% for training, 20% for testing)
        split_index = int(0.8 * len(data))

        # Split the DataFrame into training and test sets
        training_set = data.iloc[:split_index]
        test_set = data.iloc[split_index:]

        # Save the training and test sets to separate CSV files
        training_set.to_csv("training_set.csv", index=False)
        test_set.to_csv("test_set.csv", index=False)




    def predict_classification(self):

        # Read the CSV files into pandas DataFrames
        training_df = pd.read_csv("training_set.csv")
        test_df = pd.read_csv("test_set.csv")

        # Extract features and labels for training set
        trainingInstances = training_df.iloc[:, 2:-1].values
        trainingLabels = training_df.iloc[:, -1].values

        # Extract features and labels for test set
        testInstances = test_df.iloc[:, 2:-1].values
        testLabels = test_df.iloc[:, -1].values

        # Train the Decision Tree Classifier
        model = DecisionTreeClassifier()
        model.fit(trainingInstances, trainingLabels)

        # Predict labels for test instances
        predictedLabels = model.predict(testInstances)

        
       
       # Calculate accuracy

        accuracy = accuracy_score(testLabels, predictedLabels)

        # Calculate precision
        precision = precision_score(testLabels, predictedLabels, average='weighted')

        # Calculate recall
        recall = recall_score(testLabels, predictedLabels, average='weighted')

        # Calculate F1 score
        f1 = f1_score(testLabels, predictedLabels, average='weighted')

        print("Accuracy:", accuracy)
        print("Precision:", precision)
        print("Recall:", recall)
        print("F1 Score:", f1)