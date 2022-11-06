import OOMP

from oomBase import *


def loadAllInstances():
    for partID in OOMP.itemsTypes["parts"]["items"]: ###### reset oomp instances
        OOMP.items[partID]["oompInstances"] = []
    for project in OOMP.itemsTypes["projects"]["items"]:
        loadInstances(OOMP.items[project])
    for partID in OOMP.itemsTypes["parts"]["items"]: ###### reset oomp instances
        OOMP.exportTagsItem(OOMP.items[partID],"detailsInstancesOomp",["oompInstances"])

partInstances = {}

def loadInstances():
    global partInstances
    partInstances = {}
    for projectID in OOMP.itemsTypes["projects"]["items"]:
        project = OOMP.items[projectID]
        oompID = project["oompID"][0]
        parts = project["oompParts"][0]
        if len(parts) > 0:
            for part in parts:
                ping()
                p = {}
                p["PROJECT"] = project["oompID"][0]
                p["ID"] = part
                try:
                    oompPart = OOMP.items[parts[part]["OOMPID"]]
                
                    tItem = parts[part]["OOMPID"]
                    #print(tItem)
                    try: 
                        x = len(partInstances[tItem])
                    except KeyError:
                        partInstances[tItem] = []
                    partInstances[tItem].append(p)
                    #OOMP.items[tItem]["oompInstances"].append(p)
                    pass
                except KeyError:
                    
                    pass
    pass
                    #print("        loadInstances: part not in OOMP, " + parts[part]["OOMPID"])
