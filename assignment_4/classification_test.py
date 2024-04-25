from modules.project import Project
from modules.mc_simulation import MonteCarloSimulation
from modules.projectParser import ProjectParser
from modules.classification import Classification

parser = ProjectParser()
project = parser.parse_xml("controlSystemProject.xml")
end_gate = None
for gate in project.getGates():
    if gate.getName() == "end":
        end_gate = gate

classification = Classification(project, gate, 200, "results.csv")

classification.classify()

