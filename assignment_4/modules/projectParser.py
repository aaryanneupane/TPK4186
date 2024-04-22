# Project Parser
# --------------

# Table of Contents
# -----------------
# 1. Imported modules
# 2. Parser
# 3. Test


# 1. Imported modules
# -------------------

import xml.dom.minidom

# 2. Parser
# --------- 

import xml.etree.ElementTree as ET
from modules.task import Task
from modules.lane import Lane
from modules.gate import Gate
from modules.constraint import Constraint
from modules.project import Project

class ProjectParser:

    def __init__(self):
        pass

    def parse_xml(self, xml_file):
        with open(xml_file, 'r') as file:
            text = file.read()
        id = 0
        root = ET.fromstring(text)
        if root.tag == "project":
            id +=1;
            project = Project(id, root.attrib['name'])
        for child in root:
            id +=1
            if child.tag == 'gate':
                gate_name = child.attrib['name']
                project.newGate(id, gate_name)
            if child.tag == 'lane':
                lane_name = child.attrib['name']
                lane = project.newLane(id, lane_name)
                for grandchild in child:
                    id +=1
                    if  grandchild.tag == 'task':
                        task_name = grandchild.attrib['name']
                        #print(task_name)
                        min_duration = float(grandchild.attrib['minimum-duration'])
                        max_duration = float(grandchild.attrib['maximum-duration'])

                        task_exists = False
                        for task in project.getTasks():
                            if task_name == task.getName():
                                task_exists = True
                                break
                
                        if not task_exists:
                            task = project.newTask(id, task_name)
                            lane.appendTasks(task)
                            task.setMinimumDuration(min_duration)
                            task.setMaximumDuration(max_duration)

        
                           
                        
                        

                    if grandchild.tag == 'precedence-constraint':
                        source_name = grandchild.attrib['source']
                        target_name = grandchild.attrib['target']
                        source_node = None
                        target_node = None
                        for task in project.getTasks():
                            if task.getName() == source_name:
                                source_node = task
                            if task.getName() == target_name:
                                task.getId()
                                target_node = task
                        for gate in project.getGates():
                            if gate.getName() == source_name:
                                gate.getId()
                                source_node = gate
                            if gate.getName() == target_name:
                                gate.getId()
                                target_node = gate
                        
                        
                        project.newConstraint(source_node, target_node)
                
                        
                        
                 
            if child.tag == 'precedence-constraint':
                source_name = grandchild.attrib['source']
                target_name = grandchild.attrib['target']
                source_node = None
                target_node = None
                for task in project.getTasks():
                    if task.getName() == source_name:
                        source_node = task
                    if task.getName() == target_name:
                        task.getId()
                        target_node = task
                for gate in project.getGates():
                    if gate.getName() == source_name:
                        gate.getId()
                        source_node = gate
                    if gate.getName() == target_name:
                        gate.getId()
                        target_node = gate

                project.newConstraint(source_node, target_node)
    



                        
        return project