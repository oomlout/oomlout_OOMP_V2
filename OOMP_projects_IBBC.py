import OOMP
import OOMP_projects_BASE

def createProjects():
    projects = []

    count = 1
    base = {}
    base["oompType"] = "PROJ"
    base["oompSize"] = "IBBC"
    base["format"] = "kicad"
    
    base["github"] = "https://github.com/oomlout/"

    base["name"] = "ADXL345 Breakout"
    d = processDict(base.copy(),"IBBC_0001",count,version="V001");projects.append(d.copy());
    d = processDict(base.copy(),"IBBC_0001",count,version="V002");projects.append(d.copy());
    
    for d in projects:
        OOMP_projects_BASE.makeProjectNew(d)
    

def processDict(d,bName,count,version):
    #### Manual
    
    d["name"] = d["name"] + " " + version
    d["repo"] = bName
    d["file"] = bName + "_" + version + "/" + bName
    d["oompIndex"] = version
    #### Auto
    d["count"] = count
    return d


