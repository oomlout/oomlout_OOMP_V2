import OOMP_summaries_BASE
import OOMP

from mdutils.mdutils import MdUtils

import OOMP_summaries_BASE as base

from oomBase import *

def makeAllCollections():
    collections = []
   
    base = {}
   
    ###### QWIIC
    d= base.copy()
    d["oompType"] = "COLLECTION"
    d["oompSize"] = "CONN"
    d["oompColor"] = "QWIIC"
    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01"
    
    d["hexID"] = "COLQWIIC"
    d["code"] = "qwiic"
    d["name"] = "QWIIC Breakouts"
    d["description"] = "A collection of all OOMP projects that have a qwiic connector"
    d["collection"] = {}
    d["collection"]["items"] = []
    for projectID in OOMP.itemsTypes["projects"]["items"]:
        project = OOMP.items[projectID]
        parts = project["oompParts"][0]
        if len(parts) > 0:
            skip = False
            for part in parts:
                if "HEAD-JSTSH-X-PI04-RS" in parts[part] and not skip:
                    d["collection"]["items"].append(projectID)
                    skip = True                
    collections.append(d.copy())
    ###### JLC Parts Library
    d= base.copy()
    d["oompType"] = "COLLECTION"
    d["oompSize"] = "PARTL"
    d["oompColor"] = "JLCC"
    d["oompDesc"] = "BASIC"
    d["oompIndex"] = "01"
    
    d["hexID"] = "COLJLCB"
    d["code"] = "jlcb"
    d["name"] = "JLC Parts Library"
    d["description"] = "A collection of all OOMP parts with JLC parts library details"
    d["collection"] = {}
    d["collection"]["items"] = []
    for partID in OOMP.itemsTypes["parts"]["items"]:
        part = OOMP.items[partID]
        opl = part["oplPartNumber"]
        if len(opl) > 0:
            for o in opl:
                if o["code"] == "C-JLCC":
                    d["collection"]["items"].append(partID)
                    skip = True                
    collections.append(d.copy())

    for p in collections:
        makeCollection(p)
    

def createAllCollections():
    OOMP_summaries_BASE.generateCollectionsIndex()
    print("Generating collection pages")
    for collectionID in OOMP.itemsTypes["collections"]["items"]:
        collection = OOMP.items[collectionID]
        OOMP_summaries_BASE.generateCollectionPage(collection)    


def makeCollection(d):
    type = d["oompType"]
    size = d["oompSize"]
    color = d["oompColor"]
    desc = d["oompDesc"]
    index = d["oompIndex"]
    
    try:
        name = d["name"]
    except:
        pass

    hexID = d["hexID"]

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
    oompSlashes = oompID.replace("-","/")

    inputFile = "templates/partsTemplate.py"
    outputDir = OOMP.baseDir + OOMP.getDir("collections") + oompSlashes + "/"
    oomMakeDir(outputDir)
    oomMakeDir(outputDir + "src/")
    outputFile = outputDir + "details.py"

    print("Making: " + outputFile)

    contents = oomReadFileToString(inputFile)
    contents = contents.replace("TYPEZZ",type)
    contents = contents.replace("SIZEZZ",size)
    contents = contents.replace("COLORZZ",color)
    contents = contents.replace("DESCZZ",desc)
    contents = contents.replace("INDEXZZ",index)
    contents = contents.replace("HEXZZ",hexID)


    extraTags = []
    tagString = ""
    extraTags.append(["name",d["name"]])
    extraTags.append(["description",d["description"]])
    extraTags.append(["code",d["code"]])
    extraTags.append(["collection",d["collection"]])


    tagString = ""
    for tag in extraTags:
        tagString = tagString + OOMP.getPythonLine(tagName=tag[0],tagValue=tag[1]) + "\n"

    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)


