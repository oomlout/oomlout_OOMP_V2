from oomBase import *
import OOMP




def replaceOddChars(line):
    rv = line
    rv = rv.replace("µ","u")
    rv = rv.replace("±","+/-")
    rv = rv.replace("Ω","ohm")
    rv = rv.replace("Ω","ohm") ##ohm
    rv = rv.replace(";",",")
    rv = rv.replace("'","")
    return rv

def harvestParts(item,overwrite=False):
    ###### Try eagle File
    oompFile = "eagleBOM"

    if item.ifFileExists(oompFile):
        parts = oomReadFileToString(item.getFilename(oompFile))
        parts = parts.split("\n")

        ###### remove tags before starting
        for c in range(0,10):
            item.removeTag("rawParts")

        for part in parts:
            if '"Part";"Value"' in part or part == '':
                pass #skip title line
            else:
                value = part
                item.addTag("rawParts",value.replace("'","").replace(";",",").replace('"','')) ##switch from semi colons to commas and remove apostrophes
    else:
        oompFile = "kicadBOM"
        test = item.getTag("oompSize").value
        if test == "SOPA":
            pass
        if item.ifFileExists(oompFile):
            parts = oomReadFileToString(item.getFilename(oompFile))
            parts = parts.split("\n")

            ###### remove tags before starting
            for c in range(0,10):
                item.removeTag("rawParts")

            for part in parts:
                if '"Id";"Designator"' in part or part == '':
                    pass #skip title line
                else:
                    value = part
                    values = value.split(";")
                    identifiers = values[1].replace('"',"").split(",")
                    for identifier in identifiers:
                        partString = identifier + "," +  values[4].replace('"',"") +  "," +  values[2].replace('"',"") + "," + values[2].replace('"',"") + ",,,,"
                        item.addTag("rawParts",partString) ##switch from semi colons to commas and remove apostrophes
    item.exportTags("detailspartsRaw",["rawParts"])




def makePartsFile(item,oompParts,rawParts):
    partsFile = item.getFilename("pythonParts")
    projectID = item.getTag("oompID").value
    contents = ""

    contents = contents + "import OOMP" + "\n"
    contents = contents + 'newPart = OOMP.getPartByID("' + projectID + '")\n'
    
    contents = contents + "" + "\n"

    for part in oompParts:
        partString = str(part).replace("[","",).replace("]","",).replace("'","",)

        contents = contents + 'newPart.addTag("oompPart","' +partString + '")' + "\n"

    for part in rawParts:
        partString = str(part).replace("[","",).replace("]","",).replace("'","",)

        contents = contents + 'newPart.addTag("rawPart","' + partString + '")' + "\n"


    oomWriteToFile(partsFile,contents,utf=False)


def loadInstances(project):
    oompID = project.getID()
    parts = project.getTags("oompParts")
    if len(parts) > 0:
        for part in parts:
            deets = part.value.split(",")
            p = {}
            p["PROJECT"] = oompID
            p["ID"] = deets[0]
            oompPart = OOMP.getPartByID(deets[1])
            partID = oompPart.getID()
            if partID != "----":
                oompPart.addTag("oompInstances",p)
            else:
                if not "UNMATCHED" in deets[1] :
                    print("SKIPPING: " + deets[1])


def matchFootprintsR(project,overwrite=False):
    global PART, VALUE, DEVICE, PACAKGE, DESC, BOM
    ###### remove tags before starting
    for c in range(0,100):
        project.removeTag("footprintEagle")
        project.removeTag("footprintKicad")        
        project.removeTag("symbolKicad")        
        project.removeTag("symbolEagle")
    parts = project.getTags("allParts")
    for part in parts:
        p = part.value.split(",")
        dict = {
            "IDENTIFIER" : p[0],
            "OOMPID" : p[1],
            "VALUE" : p[3],
            "DESC" : p[4],
            "PACKAGE" : p[5],
            "INFO" : p[6],
            "OWNER" : project.getTag("oompSize").value
        }        
        oompPart = OOMP.getPartByID(dict["OOMPID"])
        #matchFootprint(project,oompPart,dict)

###### depricated
