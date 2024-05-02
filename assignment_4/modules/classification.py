from modules.project import Project
from modules.gate import Gate
from modules.mc_simulation import MonteCarloSimulation
import csv
import numpy
import sys
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.svm import SVC, SVR
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error
from sklearn.neural_network import MLPClassifier


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
                print(row)
                minimumTotalDuration = 0
                maximumTotalDuration = 0
                totalDuration = round(float(row[1]),2)
               # tasks_checked = []
                for task in self.project.getTasks():  
                    minimumTotalDuration += task.getMinimumDuration()
                    maximumTotalDuration += task.getMaximumDuration()
                
                                    
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
                    label = 1
                elif (totalDuration > 1.3 * minimumTotalDuration) and (totalDuration < maximumTotalDuration):
                    label = 0
                else: label = 0
                print(label)
                row.append(label)
                writer.writerow(row)
                                

                        
    
    def classify(self):
        
        sim = MonteCarloSimulation(self.project, 10000)
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

        # Calculate precision
        precision = precision_score(self.y_test, predictedLabels, average='weighted')

        # Calculate recall
        recall = recall_score(self.y_test, predictedLabels, average='weighted')

        # Calculate F1 score
        f1 = f1_score(self.y_test, predictedLabels, average='weighted')
        return accuracy, precision, recall, f1


    def logistical_regression(self):
        # Train the Decision Tree Classifier
        model = LogisticRegression(max_iter=1000)
        model.fit(self.X_train, self.y_train)
        
        # Predict labels for test instances
        predictedLabels = model.predict(self.X_test)

        # Evaluation
        accuracy = accuracy_score(self.y_test, predictedLabels)

        # Calculate precision
        precision = precision_score(self.y_test, predictedLabels, average='weighted')

        # Calculate recall
        recall = recall_score(self.y_test, predictedLabels, average='weighted')

        # Calculate F1 score
        f1 = f1_score(self.y_test, predictedLabels, average='weighted')
        return accuracy, precision, recall, f1

    def svm(self):
        # Train the Decision Tree Classifier
        model = SVC()
        model.fit(self.X_train, self.y_train)
        
        # Predict labels for test instances
        predictedLabels = model.predict(self.X_test)

        # Evaluation
        accuracy = accuracy_score(self.y_test, predictedLabels)

        # Calculate precision
        precision = precision_score(self.y_test, predictedLabels, average='weighted')

        # Calculate recall
        recall = recall_score(self.y_test, predictedLabels, average='weighted')

        # Calculate F1 score
        f1 = f1_score(self.y_test, predictedLabels, average='weighted')

        # print(f"\n---------------------EVALUATION-----------------------------\n")

        # print("Accuracy:", accuracy)
        # print("Precision:", precision)
        # print("Recall:", recall)
        # print("F1 Score:", f1)
        return accuracy, precision, recall, f1


    def evaluate_models(self):
        models = [
        ("Logistic Classification", self.logistical_regression),
        ("Decision Tree", self.decision_tree),
        ("Support Vector Machine", self.svm)]

        print("\n---------------------EVALUATION-----------------------------\n")

        for model_name, model_func in models:
            accuracy, precision, recall, f1 = model_func()
            print(f"{model_name}:")
            print(f"Accuracy: {accuracy:.2f}")
            print(f"Precision: {precision:.2f}")
            print(f"Recall: {recall:.2f}")
            print(f"F1 Score: {f1:.2f}\n")


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
        #print(f"MSE: {accuracy}")
        return accuracy
    
    def lr(self):
        # Train the Decision Tree Classifier
        model = LinearRegression()
        model.fit(self.X_train_r, self.y_train_r)
        
        # Predict labels for test instances
        predictedLabels = model.predict(self.X_test_r)

        # Evaluation
        accuracy = mean_squared_error(self.y_test_r, predictedLabels)
        #print(f"MSE: {accuracy}")
        return accuracy
    
    def NN(self):
        # Train the Decision Tree Classifier
        model = MLPClassifier()
        model.fit(self.X_train_r, self.y_train_r)
        
        # Predict labels for test instances
        predictedLabels = model.predict(self.X_test_r)

        # Evaluation
        accuracy = mean_squared_error(self.y_test_r, predictedLabels)
        #print(f"MSE: {accuracy}")
        return accuracy
    
    def evaluate_models_regression(self):
        models = [
        ("Logistic Regression", self.lr),
        ("Neural Network", self.NN),
        ("Support Vector Machine Regression", self.svr)]

        print("\n---------------------EVALUATION-----------------------------\n")

        for model_name, model_func in models:
            accuracy = model_func()
            print(f"{model_name}:")
            print(f"MSE: {accuracy:.2f}")