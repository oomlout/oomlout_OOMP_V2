import OOMP
import OOMP_projects_BASE

def createProjects():
    projects = []

    count = 1
    base = {}
    base["oompType"] = "PROJ"
    base["oompSize"] = "DANP"
    base["format"] = "eagle"
    
    base["github"] = "https://github.com/DangerousPrototypes/"

    d = base.copy()
    v = "1A"
    d["name"] = "Bus Pirate Ultra " + v 
    d["repo"] = "BusPirateUltraHardware"
    d["file"] = "BPUv1a/BusPirate-ultra.v1.0a"
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy())
    d = base.copy()
    v = "1B"
    d["name"] = "Bus Pirate Ultra " + v 
    d["repo"] = "BusPirateUltraHardware"
    d["file"] = "BPUv1b/BusPirate-ultra.v1.0b"
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy())
    d = base.copy()
    v = "1C"
    d["name"] = "Bus Pirate Ultra " + v 
    d["repo"] = "BusPirateUltraHardware"
    d["file"] = "BPUv1c/BusPirate-ultra.v1.0c"
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy())
    d = base.copy()
    v = "2A"
    d["format"] = "kicad"
    d["name"] = "Bus Pirate Ultra " + v 
    d["repo"] = "BusPirateUltraHardware"
    d["file"] = "BPUv2a/BPUv2a"
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy())

    ###### Bus Pirate
    count = count+1    
    d = base.copy()
    v = "v0a"
    d["name"] = "Bus Pirate " + v 
    d["repo"] = "Bus_Pirate"
    d["file"] = "hardware/" + v + "/BusPirate-24F" + v
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy()) 
    d = base.copy()
    v = "v1a"
    d["name"] = "Bus Pirate " + v 
    d["repo"] = "Bus_Pirate"
    d["file"] = "hardware/" + v + "/BusPirate-24Fv1a.final"
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy())
    d = base.copy()
    v = "v2a"
    d["name"] = "Bus Pirate " + v 
    d["repo"] = "Bus_Pirate"
    d["file"] = "hardware/" + v + "/BusPirate-" + v
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy()) 
    d = base.copy()
    v = "v25"
    d["name"] = "Bus Pirate " + v 
    d["repo"] = "Bus_Pirate"
    d["file"] = "hardware/v2go/BusPirate-v25"
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy()) 
    d = base.copy()
    v = "v35c"
    d["name"] = "Bus Pirate " + v 
    d["repo"] = "Bus_Pirate"
    d["file"] = "hardware/v3.5/BusPiratev3.5c-SOIC"
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy())
    v = "v36a"
    d["name"] = "Bus Pirate " + v 
    d["repo"] = "Bus_Pirate"
    d["file"] = "hardware/v3.6/BusPirate-v3.6a-SSOP"
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy()) 
    v = "v38a"
    d["name"] = "Bus Pirate " + v 
    d["repo"] = "Bus_Pirate"
    d["file"] = "hardware/v3.8a/BusPirate-v3.8a-SSOP"
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy()) 
    v = "v39"
    d["name"] = "Bus Pirate " + v 
    d["repo"] = "Bus_Pirate"
    d["file"] = "hardware/v3.9/BusPirate-v3.9-SSOP"
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy()) 
    v = "v3"
    d["name"] = "Bus Pirate " + v 
    d["repo"] = "Bus_Pirate"
    d["file"] = "hardware/v3/BusPirate-v3a-final"
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy()) 
    v = "v4e"
    d["name"] = "Bus Pirate " + v 
    d["repo"] = "Bus_Pirate"
    d["file"] = "hardware/v4/BusPirate-v4e"
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy()) 
    v = "v5"
    d["name"] = "Bus Pirate " + v 
    d["repo"] = "Bus_Pirate"
    d["file"] = "hardware/v5.0/tests/v5_with_MOLEX_USB/BusPirate-v5.0-SSOP"
    d["oompIndex"] = v.upper()
    d["count"] = count
    projects.append(d.copy()) 

        
    

    count = count + 1


    for d in projects:
        OOMP_projects_BASE.makeProjectNew(d)

    count = count +1

def breakoutDict(d,bName,count):
    #### Manual
    d["name"] = bName + " Breakout Board (sirboard)"
    d["repo"] = "BreakoutBoards"
    d["file"] = bName + "/" + bName
    #### Auto
    d["count"] = count
    return d

