from oomBase import *
import OOMP


def harvestAllParts(overwrite=False):
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        harvestParts(OOMP.items[itemID],overwrite)
    for itemID in OOMP.itemsTypes["modules"]["items"]:
        harvestParts(OOMP.items[itemID],overwrite)    


def harvestParts(item,overwrite=False):
    ###### Try eagle File
    bomFile = OOMP.getFileItem(item,"eagleBOM")

    if os.path.exists(bomFile):
        parts = oomReadFileToString(bomFile,encoding="utf-8")
        parts = parts.split("\n")
        item["rawParts"] = [{}]
        item["rawParts"][0]["kicadBom"] = []
        item["rawParts"][0]["eagleBom"] = []
        ###### remove tags before starting
        for part in parts:
            if '"Part";"Value"' in part or part == '':
                pass #skip title line
            else:
                part = part.replace('"','').replace("'","")
                values = part.split(";")
                line = {}
                line["Part"] = values[0].replace("�","u")
                line["Value"] = values[1].replace("�","u")
                line["Device"] = values[2].replace("�","u")
                line["Package"] = values[3].replace("�","u")
                line["Description"] = values[4].replace("�","u")
                line["BOM"] = values[5]
                item["rawParts"][0]["eagleBom"].append(line)
    bomFile = OOMP.getFileItem(item,"kicadBOM")
    if os.path.exists(bomFile):
        parts = oomReadFileToString(bomFile)
        parts = parts.split("\n")

        for part in parts:
            if '"Id";"Designator"' in part or part == '':
                pass #skip title line
            else:
                value = part
                values = value.split(";")
                identifiers = values[1].replace('"',"").split(",")
                for identifier in identifiers:                    
                    part = part.replace('"','').replace("'","")
                    values = part.split(";")
                    line = {}
                    line["Part"] = identifier
                    line["Value"] = values[4]
                    line["Device"] = values[2] + " " + values[4]
                    line["Package"] = values[2]
                    line["Description"] = values[5]
                    line["BOM"] = ""
                    if len(item["rawParts"]) == 0:
                        item["rawParts"].append({"kicadBom" : [], "eagleBom" : []})
                    item["rawParts"][0]["kicadBom"].append(line)
    OOMP.exportTagsItem(item,"detailspartsRaw",["rawParts"])

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
