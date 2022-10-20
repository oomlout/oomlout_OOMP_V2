import OOMP
import OOMP_projects_BASE

def createProjects():
    d = {}
    d["oompType"] = "PROJ"
    d["oompSize"] = "SEED"
    d["oompColor"] = "20054"
    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01"
    
    d["hexID"] = "PRS20054"

    d["name"] = "Grove - ADXL345 - 3-Axis Digital Accelerometer(+/-16g)"
    #d["gitRepo"] = ""
    #d["gitName"] = ""
    #d["eagleBoard"] = ""
    #d["eagleSchem"] = d["eagleBoard"].replace(".brd",".sch")
    d["extraTags"] = []
    d["extraTags"].append(["linkBuyPage","https://www.seeedstudio.com/Grove-3-Axis-Digital-Accelerometer-16g.html"])

    
    OOMP_projects_BASE.makeProject(d)
