import OOMP
import re

from oomBase import *

import OOMP_projects_partsMatch_Type
import OOMP_projects_partsMatch_Size
import OOMP_projects_partsMatch_Color
import OOMP_projects_partsMatch_Desc
import OOMP_projects_partsMatch_Index
import OOMP_projects_partsMatch_Special


def partReport():
    print("    Generating OOMP Part report")
    filenameM = "csv/oompReportMatched.csv"
    filenameU = "csv/oompReportUnMatched.csv"
    fM = open(filenameM,"w+")
    fU = open(filenameU,"w+")
    first = True
    for partID in OOMP.itemsTypes["projects"]["items"]:
        ping()
        part = OOMP.items[partID]
        oompParts = part["oompParts"][0]
        if len(part["rawParts"]) > 0:
            rParts = part["rawParts"][0]
            rawParts = rParts["kicadBom"]
            if len(rawParts) == 0:
                rawParts = rParts["eagleBom"]
            if len(rawParts) > 0:
                for oompPart in oompParts:
                    line = ""
                    if first:
                        line = line + "Project;"
                        line = line + "OOMP ID;"
                        for entry in rawParts[0]: 
                            line = line + entry+";"
                        
                        line = line + "\n"
                        first = False
                    else:
                        line = partID + ";"
                        line = line + oompParts[oompPart]+";"
                        line = line + oompPart+";"
                        for part in rawParts: 
                                if part["Part"] == oompPart:
                                    for entry in part:
                                        line = line + part[entry]+";"
                    line = line + "\n"
                    line = line.replace('\u03a9',"Ohm")
                    line = line.replace('\u03bc',"u")
                    line = line.replace('\u2126',"Ohm")
                    if "UNMATCHED" in line or "Project;" in line:
                        fU.write(line)                 
                    else:    
                        fM.write(line)          
                        
    fM.close()
    fU.close()
                



def matchParts(project):
    print("    Matching Parts")
    ###### remove tags before starting
    project["oompParts"] = [{}]
    try:
        parts = project["rawParts"][0]["eagleBom"]
    except:
        try:
            parts = project["rawParts"][0]["kicadBom"]
        except:
            parts = []
    for part in parts:
        oompPart = matchPart(project,part)
        if not "SKIP-" in oompPart:
            project["oompParts"][0][part["Part"]] = oompPart

    
    OOMP.exportTagsItem(project,"detailsPartsOomp",["oompParts"])    

def matchPart(project,part):
    oompType = OOMP_projects_partsMatch_Type.matchType(project,part)
    oompSize = OOMP_projects_partsMatch_Size.matchSize(project,part,oompType=oompType)
    oompColor = OOMP_projects_partsMatch_Color.matchColor(project,part,oompType=oompType,oompSize=oompSize)
    oompDesc = OOMP_projects_partsMatch_Desc.matchDesc(project,part,oompType=oompType,oompSize=oompSize,oompColor=oompColor)
    oompIndex = OOMP_projects_partsMatch_Index.matchIndex(project,part,oompType=oompType,oompSize=oompSize,oompColor=oompColor,oompDesc=oompDesc)  


    rv = oompType + "-" + oompSize + "-" + oompColor + "-" + oompDesc + "-" + oompIndex
    if "UNMATCHED" in rv:
        rv = OOMP_projects_partsMatch_Special.matchSpecial(project,part,oompType=oompType,oompSize=oompSize,oompColor=oompColor,oompDesc=oompDesc,oompID=rv)  
    return rv




def getUseful(part,name):
    global PART, VALUE, DEVICE, PACAKAGE, DESC, BOM
    rv = ""
    if name == "partLetter":
        rv = re.sub(r'\d+', '', part["Part"])
    if name == "packageNumber":
        rv = re.sub(r'\D+', '', part["Package"])
    if name == "valueNumber":
        rv = re.sub(r'[a-zA-Z]+', '', part["Value"])    ######  Maintains full stop for decimal

    return rv

def loadPartDict(part,project):
    global PART, VALUE, DEVICE, PACAKAGE, DESC, BOM
    rv = {}
    ######unicode testing
    for x in part["Value"]:
        if ord(x) > 127:
            pass
    part["Value"] = part["Value"].replace("Ã\x82Âµ","U").replace("µ","U") ###### unicode micro fix
    rv["PART"] = part["Part"]
    rv["PARTLETTER"] = getUseful(part,"partLetter")
    rv["VALUE"] = part["Value"]
    rv["VALUENUMBER"] = getUseful(part,"valueNumber")
    rv["DEVICE"] = part["Device"]
    rv["PACKAGE"] = part["Package"]    
    rv["PACKAGENUMBER"] = getUseful(part,"packageNumber")
    rv["DESC"] = part["Description"]
    rv["BOM"] = part["BOM"]
    rv["OWNER"] = project["oompSize"][0]

    full = ""
    for c in part:
        full = full + part[c] + ","
    rv["FULL"] = full

    if rv["PART"] == "C13":
        pass

    return rv

def loadProjectDict(project):
    rv = {}
    rv["OWNER"] = project["oompSize"][0]
    rv["INDEX"] = project["oompColor"][0]
    

    return rv

