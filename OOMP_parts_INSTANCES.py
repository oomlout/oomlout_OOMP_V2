import OOMP



def loadAllInstances():
    for partID in OOMP.itemsTypes["parts"]["items"]: ###### reset oomp instances
        OOMP.items[partID]["oompInstances"] = []
    for project in OOMP.itemsTypes["projects"]["items"]:
        loadInstances(OOMP.items[project])
    for partID in OOMP.itemsTypes["parts"]["items"]: ###### reset oomp instances
        OOMP.exportTagsItem(OOMP.parts[partID],"detailsoompInstances",["oompInstances"])

def loadInstances(project):
    oompID = project["oompID"][0]
    parts = project["oompParts"][0]
    if len(parts) > 0:
        for part in parts:
            p = {}
            p["PROJECT"] = project["oompID"][0]
            p["ID"] = part
            try:
                oompPart = OOMP.parts[parts[part]]
                OOMP.parts[parts[part]].append(p)
            except:
                print("        loadInstances: part not in OOMP " + parts[part])
