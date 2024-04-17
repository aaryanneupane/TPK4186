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
        id = 0
        root = ET.fromstring(xml_file)
        if root.tag == "project":
            print(root.tag)
            print(root.attrib['name'])
            id +=1;
            project = Project(id, root.attrib['name'])
        for child in root:
            id +=1
            if child.tag == 'gate':
                gate_name = child.attrib['name']
                gate = Gate(id, gate_name)
            if child.tag == 'lane':
                lane_name = child.attrib['name']
                lane = Lane(id, lane_name)
            if child.tag == 'precendence-contstraint':
                source = child.attrib['source']
                target = child.attrib['target']
                source_node = project.lookForNode(source)
                target_node = project.lookForNode(target)
                constraint = Constraint(id, source_node, target_node)
                project.constraints.append(constraint)
            if  child.tag == 'task':
                task_name = child.attrib['name']
                min_duration = float(child.attrib['minimum-duration'])
                max_duration = float(child.attrib['maximum-duration'])
                task = Task(id, task_name)
                task.setMinimumDuration(min_duration)
                task.setMaximumDuration(max_duration)
                lane.tasks.append(task)
                        
        return project