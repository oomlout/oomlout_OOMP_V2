import OOMP
import OOMP_projects_BASE

def createProjects():
    projects = []
    
    count = 1
    base = {}
    base["oompSize"] = "OOML"
    base["format"] = "kicad"
    base["github"] = "https://github.com/oomlout/"
    base["oompIndex"] = "01"    ###### default to rev 01

    #############################################################
    #############################################################    

    projectStrings = []
    projectStrings.append("DLSB-DRIVERBOARD-V1")
    
    #############################################################
    for item in projectStrings:
        if isinstance(item, list):
            repo = item[0]
            file = item[1]
            if len(item) > 2:
                name = item[2]
            else:
                name = item[1]
        else:
            repo = item
            file = item
            name = item
        if repo != "":
            d = base.copy()    
            d["repo"] = repo
            d["file"] = file.replace("_hw","")    
            d["name"] = name.replace("_hw","").replace("_"," ").replace("-"," ").capitalize()
            d["count"] = count; count = count + 1
            projects.append(d)

    for d in projects:
        OOMP_projects_BASE.makeProjectNew(d)

