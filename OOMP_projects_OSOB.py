import OOMP
import OOMP_projects_BASE

def createProjects():
    projects = []
    
    count = 1
    base = {}
    base["oompSize"] = "OSOB"
    base["format"] = "eagle"
    base["github"] = "https://github.com/joeycastillo/"
    base["oompIndex"] = "01"    ###### default to rev 01

    #############################################################
    #############################################################    

    projectStrings = []
    projectStrings.append(["Sensor-Watch","PCB/ Main Boards/OSO-SWAT-A1-05","Sensor Watch"])
    projectStrings.append(["LCD-FeatherWing","OSO-WILD-A3/OSO-WILD-A3","LCD FeatherWing"])
    

    #############################################################
    for item in projectStrings:
        if isinstance(item, list):
            repo = item[0]
            file = item[1]
            if len(item) > 2:
                name = item[2]
            else:
                name = item[1]
            if len(item) > 3:
                index = item[3]
            else:
                index = "01"            
        else:
            repo = item
            file = item
            name = item
            index = "01"
        if repo != "":
            d = base.copy()    
            d["repo"] = repo
            d["file"] = file.replace("_hw","")    
            d["name"] = name.replace("_hw","").replace("_"," ").capitalize
            d["count"] = count ; count = count + 1 
            if index != "01":
                d["oompIndex"] = index
            ###### company specific checks
            #############
            projects.append(d)

    for d in projects:
        OOMP_projects_BASE.makeProjectNew(d)

