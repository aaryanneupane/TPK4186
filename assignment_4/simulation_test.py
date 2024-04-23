from modules.project import Project
from modules.mc_simulation import MonteCarloSimulation
from modules.projectParser import ProjectParser


parser = ProjectParser()
project = parser.parse_xml("controlSystemProject.xml")
sim = MonteCarloSimulation(project, 50)

sim.setDurations()
sim.calculateStartAndEndTimes()

for task in project.getTasks():
            print(task.getName())
            print(task.getEndDate())

for gate in project.getGates():
    print(gate.getName())
    print(gate.getEndDate())
    
sim.execute_simulation()


