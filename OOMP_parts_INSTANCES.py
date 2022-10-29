import OOMP



def loadAllInstances():
    for partID in OOMP.itemsTypes["parts"]["items"]: ###### reset oomp instances
        OOMP.items[partID]["oompInstances"] = []
    for project in OOMP.itemsTypes["projects"]["items"]:
        loadInstances(OOMP.items[project])
    for partID in OOMP.itemsTypes["parts"]["items"]: ###### reset oomp instances
        OOMP.exportTagsItem(OOMP.items[partID],"detailsInstancesOomp",["oompInstances"])

def loadInstances(project):
    oompID = project["oompID"][0]
    parts = project["oompParts"][0]
    if len(parts) > 0:
        for part in parts:
            p = {}
            p["PROJECT"] = project["oompID"][0]
            p["ID"] = part
            try:
                oompPart = OOMP.items[parts[part]]
                OOMP.items[parts[part]]["oompInstances"].append(p)
                pass
            except:
                print("        loadInstances: part not in OOMP, " + parts[part])
