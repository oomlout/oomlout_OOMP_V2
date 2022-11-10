import OOMP
import OOMP_projects_BASE

def createProjects():
    projects = []
    
    count = 1
    base = {}
    base["oompSize"] = "HYDR"
    base["format"] = "eagle"
    base["github"] = "https://github.com/hydrabus/"
    base["oompIndex"] = "01"    ###### default to rev 01

    #############################################################
    #############################################################    

    projectStrings = []
    projectStrings.append(["hydrabus","hardware/HydraBus_1_0_Rev1_1","HydraBus 1.0 R1.1","R11"])
    projectStrings.append(["hydrabus","hardware/HydraBus_1_0_Rev1_2","HydraBus 1.0 R1.2","R12"])
    projectStrings.append(["hydrabus","hardware/HydraBus_1_0_Rev1_2plus","HydraBus 1.0 R1.2+","R12P"])
    projectStrings.append(["hydrabus","hardware/HydraBus_1_0_Rev1_3","HydraBus 1.0 R1.3","R13"])
    projectStrings.append(["hydrabus","hardware/HydraBus","HydraBus 1.0 R1.4","R14"])


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
            d["name"] = name.replace("_hw","").replace("_"," ").capitalize()
            d["count"] = count ####; count = count + 1 (multiple versions so same count)
            if index != "01":
                d["oompIndex"] = index
            ###### company specific checks
            if index == "R14":
                d["format"] = "kicad"
            #############
            projects.append(d)

    for d in projects:
        OOMP_projects_BASE.makeProjectNew(d)

