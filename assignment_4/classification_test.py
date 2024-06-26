from modules.project import Project
from modules.mc_simulation import MonteCarloSimulation
from modules.projectParser import ProjectParser
from modules.classification import Classification

parser = ProjectParser()
project = parser.parse_xml("controlSystemProject.xml")
end_gate = None
mid_gate = None
for gate in project.getGates():
    if gate.getName() == "end":
        end_gate = gate
    if gate.getName() == "MidProject":
        mid_gate = gate

classification = Classification(project, end_gate, 200, "results.csv")

classification.classify()

classification.training_and_testing()

classification.predict_classification()

classification.evaluate_models_classifier()

classification.predict_regression()

classification.evaluate_models_regression()
