from modules.project import Project
from modules.gate import Gate
from modules.mc_simulation import MonteCarloSimulation
import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.svm import SVC, SVR
from sklearn.metrics import accuracy_score, mean_squared_error, confusion_matrix, mean_absolute_error
from sklearn.neighbors import KNeighborsRegressor


class Classification:

    def __init__(self, project: Project, gate: Gate, maximumDuration : int, filename: str):
        self.project = project
        self.gate = gate
        self.maximumDuration = maximumDuration
        self.filename = filename
        self.gate = gate

        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

        self.X_train_r = None
        self.y_train_r = None
        self.X_test_r = None
        self.y_test_r = None
        


   
    def addClassifications(self, gate : Gate):
         
        with open(self.filename, newline = '') as csvfile, \
            open("classified_" + self.filename, 'w', newline='') as classified_file:
            reader = csv.reader(csvfile)
            writer = csv.writer(classified_file)


            header = next(reader)
            header.append('Status')    
            writer.writerow(header)
            for row in reader:
                #print(row)
                minimumTotalDuration = 0
                maximumTotalDuration = 0
                totalDuration = round(float(row[1]),2)
               # tasks_checked = []
                for task in self.project.getTasks():  
                    minimumTotalDuration += task.getMinimumDuration()
                    maximumTotalDuration += task.getMaximumDuration()
                
                                    
                # print('For rad:')
                # print(row)
                # print('og gaten er:')
                # print(gate.getName())
                # print('så er actual total duration på gaten:')
                # print(totalDuration)
                # print('minimum total duration på gaten:')
                # print(minimumTotalDuration)
                # print('maximum total duration på gaten:')
                # print(maximumTotalDuration)

                if (totalDuration < (1.3 * minimumTotalDuration)):
                    label = 1
                elif (totalDuration > 1.3 * minimumTotalDuration) and (totalDuration < maximumTotalDuration):
                    label = 0
                else: label = 0
                #print(label)
                row.append(label)
                writer.writerow(row)
                                

                        
    
    def classify(self):
        
        sim = MonteCarloSimulation(self.project, 1000)
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

       
        features = ["SpecifySystem", "DesignHardware", "PrototypeHardware", "TestHardware", 
        "DesignSoftware", "DesignDocumentation", "DesignTraining", "PrepareCertification", "Total_duration_at_mid_gate", "Status"]

        training_df = training_df[features]
        test_df = test_df[features]

        # Extract features and labels for training set
        trainingInstances = training_df.iloc[:, :-1]
        trainingLabels = training_df.iloc[:, -1]

        # Extract features and labels for test set
        testInstances = test_df.iloc[:, :-1]
        testLabels = test_df.iloc[:, -1]

        self.X_train = trainingInstances
        self.y_train = trainingLabels
        self.X_test = testInstances
        self.y_test = testLabels

    def decision_tree(self):
        # Train the Decision Tree Classifier
        model = DecisionTreeClassifier()
        model.fit(self.X_train, self.y_train)
        
        # Predict labels for test instances
        predictedLabels = model.predict(self.X_test)

        # Evaluation
        accuracy = accuracy_score(self.y_test, predictedLabels)

        return accuracy, predictedLabels


    def logistical_classifier(self):
        # Train the Decision Tree Classifier
        model = LogisticRegression(max_iter=1000)
        model.fit(self.X_train, self.y_train)
        
        # Predict labels for test instances
        predictedLabels = model.predict(self.X_test)

        # Evaluation
        accuracy = accuracy_score(self.y_test, predictedLabels)

        return accuracy, predictedLabels

    def svm(self):
        # Train the Decision Tree Classifier
        model = SVC()
        model.fit(self.X_train, self.y_train)
        
        # Predict labels for test instances
        predictedLabels = model.predict(self.X_test)

        # Evaluation
        accuracy = accuracy_score(self.y_test, predictedLabels)
        return accuracy, predictedLabels




    def predict_regression(self):
        # Read the CSV files into pandas DataFrames
        training_df = pd.read_csv("training_set.csv")
        test_df = pd.read_csv("test_set.csv")

       
        features = ["SpecifySystem", "DesignHardware", "PrototypeHardware", "TestHardware",
        "DesignSoftware", "DesignDocumentation", "DesignTraining", "PrepareCertification", "Total_duration_at_mid_gate", "Total_Duration"]

        training_df = training_df[features]
        test_df = test_df[features]

        # Extract features and labels for training set
        trainingInstances = training_df.iloc[:, :-1]
        trainingLabels = training_df.iloc[:, -1]

        # Extract features and labels for test set
        testInstances = test_df.iloc[:, :-1]
        testLabels = test_df.iloc[:, -1]

        self.X_train_r = trainingInstances
        self.y_train_r = trainingLabels
        self.X_test_r= testInstances
        self.y_test_r= testLabels

    def svr(self):
        # Train the Decision Tree Classifier
        model = SVR()
        model.fit(self.X_train_r, self.y_train_r)
        # Predict labels for test instances
        predictedLabels = model.predict(self.X_test_r)
        # Evaluation
        accuracy = mean_squared_error(self.y_test_r, predictedLabels)
        return accuracy, predictedLabels
    
    def lr(self):
        # Train the Decision Tree Classifier
        model = LinearRegression()
        model.fit(self.X_train_r, self.y_train_r)
        
        # Predict labels for test instances
        predictedLabels = model.predict(self.X_test_r)

        # Evaluation
        accuracy = mean_squared_error(self.y_test_r, predictedLabels)
        return accuracy, predictedLabels
    
    def KN(self):
        # Train the Decision Tree Classifier
        model = KNeighborsRegressor()
        model.fit(self.X_train_r, self.y_train_r)
        
        # Predict labels for test instances
        predictedLabels = model.predict(self.X_test_r)

        # Evaluation
        accuracy = mean_squared_error(self.y_test_r, predictedLabels)
        return accuracy, predictedLabels
    
    def evaluate_models_classifier(self):
        models = [
        ("Logistical Regression Classifier", self.logistical_classifier),
        ("Decision Tree Classifier", self.decision_tree),
        ("Support Vector Classifier", self.svm)]

        print("\n---------------------EVALUATION-----------------------------\n")

        for model_name, model_func in models:
            accuracy, preds = model_func()
            confusion = confusion_matrix(self.y_test, preds)
            tn, fp, fn, tp = confusion.ravel()
            print(f"{model_name}:\n")
            print(f"Accuracy: {accuracy:.2f}")
            print("\t\t   Predicted")
            print("\t\tOn-Time\tDelayed")
            print(f"Actual On-Time:\t{tp}\t{fn}")
            print(f"Actual Delayed:\t{fp}\t{tn}\n")
            print(f"------------------------------------------------------------")
            
    def evaluate_models_regression(self):
        models = [
        ("Logistical Regression", self.lr),
        ("KNeighbors Regressor", self.KN),
        ("Support Vector Regression", self.svr)]

        print("\n---------------------EVALUATION-----------------------------\n")

        for model_name, model_func in models:
            mse, preds = model_func()
            print(f"{model_name}:\n")
            print(f"MSE: {mse:.2f}\n")
            print(f"MAE: {mean_absolute_error(self.y_test_r, preds):.2f}\n")
            print(f"------------------------------------------------------------")


            # Plotting prediction difference
            plt.figure()
            plt.title(f"{model_name} - Prediction Difference")
            plt.scatter(np.arange(len(self.y_test_r)), self.y_test_r - preds, label="Difference")
            plt.axhline(y=0, color='r', linestyle='-', label="Zero Difference")
            plt.xlabel("Data Point")
            plt.ylabel("Difference")
            plt.legend()
            plt.show()