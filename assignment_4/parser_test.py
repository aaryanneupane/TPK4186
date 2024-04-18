from modules.projectParser import ProjectParser
import xml.etree.ElementTree as ET

new_parser = ProjectParser()

xml_file = '''
<project name="ControlSystem">
<gate name="begin"/>
<lane name="MethodologyGroup">
<task name="SpecifySystem" minimum-duration="6.0" maximum-duration="10.0"/>
<task name="DeploySystem" minimum-duration="4.0" maximum-duration="8.0"/>
</lane>
<lane name="HardwareGroup">
<task name="DesignHardware" minimum-duration="8.0" maximum-duration="12.0"/>
<task name="PrototypeHardware" minimum-duration="4.0" maximum-duration="8.0"/>
<task name="TestHardware" minimum-duration="1.0" maximum-duration="3.0"/>
<task name="ManufactureHardware" minimum-duration="8.0" maximum-duration="12.0"/>
<precedence-constraint source="DesignHardware" target="PrototypeHardware"/>
<precedence-constraint source="PrototypeHardware" target="TestHardware"/>
<precedence-constraint source="TestHardware" target="ManufactureHardware"/>
</lane>
<lane name="SoftwareGroup">
<task name="DesignSoftware" minimum-duration="12.0" maximum-duration="20.0"/>
<task name="ImproveSoftware" minimum-duration="8.0" maximum-duration="10.0"/>
<task name="ReleaseSoftware" minimum-duration="8.0" maximum-duration="10.0"/>
<precedence-constraint source="ImproveSoftware" target="ReleaseSoftware"/>
</lane>
<lane name="CertificationGroup">
<task name="DesignDocumentation" minimum-duration="4.0" maximum-duration="8.0"/>
<task name="DesignTraining" minimum-duration="4.0" maximum-duration="6.0"/>
<task name="PrepareCertification" minimum-duration="6.0" maximum-duration="12.0"/>
<task name="TrainOperators" minimum-duration="6.0" maximum-duration="8.0"/>
<task name="FinalizeCertification" minimum-duration="10.0" maximum-duration="20.0"/>
<precedence-constraint source="DesignDocumentation" target="DesignTraining"/>
<precedence-constraint source="DesignDocumentation" target="PrepareCertification"/>
</lane>
<precedence-constraint source="begin" target="SpecifySystem"/>
<precedence-constraint source="SpecifySystem" target="DesignHardware"/>
<precedence-constraint source="SpecifySystem" target="DesignSoftware"/>
<precedence-constraint source="SpecifySystem" target="DesignDocumentation"/>
<gate name="MidProject"/>
<precedence-constraint source="TestHardware" target="MidProject"/>
<precedence-constraint source="DesignSoftware" target="MidProject"/>
<precedence-constraint source="DesignTraining" target="MidProject"/>
<precedence-constraint source="PrepareCertification" target="MidProject"/>
<precedence-constraint source="MidProject" target="ManufactureHardware"/>
<precedence-constraint source="MidProject" target="ImproveSoftware"/>
<precedence-constraint source="MidProject" target="TrainOperators"/>
<precedence-constraint source="MidProject" target="FinalizeCertification"/>
<precedence-constraint source="ManufactureHardware" target="DeploySystem"/>
<precedence-constraint source="ReleaseSoftware" target="DeploySystem"/>
<precedence-constraint source="TrainOperators" target="DeploySystem"/>
<gate name="end"/>
<precedence-constraint source="DeploySystem" target="end"/>
<precedence-constraint source="FinalizeCertification" target="end"/>
</project>
'''
file = "controlSystemProject.xml"

root = ET.fromstring(xml_file)

for child in root:
    print(child.tag, child.attrib)
    
print(new_parser.parse_xml('controlSystemProject.xml'))