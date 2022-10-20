import OOMP
import re


import OOMP_projects_partsMatch_Type
import OOMP_projects_partsMatch_Size
import OOMP_projects_partsMatch_Color
import OOMP_projects_partsMatch_Desc
import OOMP_projects_partsMatch_Index
import OOMP_projects_partsMatch_Special


def matchParts(project):
    global PART, VALUE, DEVICE, PACAKGE, DESC, BOM
    print("    Matching Parts")
    ###### remove tags before starting
    for c in range(0,100):
        project.removeTag("oompParts")
    parts = project.getTags("rawParts")
    for part in parts:
        part = part.value.split(",")
        oompPart = matchPart(project,part)
        if not "SKIP-" in oompPart:
            project.addTag("oompParts", part[PART] + "," + oompPart)


    project.exportTags("detailsPartsOomp",["oompParts"])    

def matchPart(project,part):
    for x in range(0,len(part)):
        part[x] = part[x].replace('"','')


    oompType = OOMP_projects_partsMatch_Type.matchType(project,part)
    oompSize = OOMP_projects_partsMatch_Size.matchSize(project,part,oompType=oompType)
    oompColor = OOMP_projects_partsMatch_Color.matchColor(project,part,oompType=oompType,oompSize=oompSize)
    oompDesc = OOMP_projects_partsMatch_Desc.matchDesc(project,part,oompType=oompType,oompSize=oompSize,oompColor=oompColor)
    oompIndex = OOMP_projects_partsMatch_Index.matchIndex(project,part,oompType=oompType,oompSize=oompSize,oompColor=oompColor,oompDesc=oompDesc)  


    rv = oompType + "-" + oompSize + "-" + oompColor + "-" + oompDesc + "-" + oompIndex
    if "UNMATCHED" in rv:
        rv = OOMP_projects_partsMatch_Special.matchSpecial(project,part,oompType=oompType,oompSize=oompSize,oompColor=oompColor,oompDesc=oompDesc,oompID=rv)  
    return rv

PART = 0
VALUE = 1
DEVICE = 2
PACKAGE = 3
DESC = 4
BOM = 5



def getUseful(part,name):
    global PART, VALUE, DEVICE, PACAKAGE, DESC, BOM
    rv = ""
    if name == "partLetter":
        rv = re.sub(r'\d+', '', part[PART])
    if name == "packageNumber":
        rv = re.sub(r'\D+', '', part[PACKAGE])
    if name == "valueNumber":
        rv = re.sub(r'[a-zA-Z]+', '', part[VALUE])    ######  Maintains full stop for decimal

    return rv

def loadPartDict(part,project):
    global PART, VALUE, DEVICE, PACAKAGE, DESC, BOM
    rv = {}
    part[VALUE] = part[VALUE].replace("Ã\x82Âµ","U") ###### unicode micro fix
    rv["PART"] = part[PART]
    rv["PARTLETTER"] = getUseful(part,"partLetter")
    rv["VALUE"] = part[VALUE]
    rv["VALUENUMBER"] = getUseful(part,"valueNumber")
    rv["DEVICE"] = part[DEVICE]
    rv["PACKAGE"] = part[PACKAGE]    
    rv["PACKAGENUMBER"] = getUseful(part,"packageNumber")
    rv["DESC"] = part[DESC]
    rv["BOM"] = part[BOM]
    rv["OWNER"] = project.getTag("oompSize").value

    full = ""
    for c in part:
        full = full + c + ","
    rv["FULL"] = full

    if rv["PART"] == "C13":
        pass

    return rv

def loadProjectDict(project):
    rv = {}
    rv["OWNER"] = project.getTag("oompSize").value
    rv["INDEX"] = project.getTag("oompColor").value
    

    return rv

