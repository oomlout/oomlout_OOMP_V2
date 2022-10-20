from OOMPsummaries import *

from mdutils.mdutils import MdUtils

import OOMP_summaries_BASE as base

def generateCollections():
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
    d["collection"] = []
    proj = OOMP.getItems("projects")
    for project in proj:
        parts = project.getTags("oompParts")
        skip = False
        for part in parts:
            if "HEAD-JSTSH-X-PI04-RS" in part.value and not skip:
                d["collection"].append(project.getID())
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
    d["collection"] = []
    ps = OOMP.getItems("parts")
    for p in ps:
        opl = p.getTags("oplPartNumber")
        for o in opl:
            if o.value["code"] == "C-JLCC":
                d["collection"].append(p.getID())
                skip = True                
    collections.append(d.copy())

    for p in collections:
        makeCollection(p)
    

def generatCollectionsPages():
    generateCollectionsIndex()
    for collection in OOMP.getItems("collections"):
        generateCollectionPage(collection)    

def generateCollectionsIndex():  
    print("Generating Collection Index")  
    filename = "oomlout_OOMP_collections/COLLECTION.md"
    
    mdFile = MdUtils(file_name=filename,title="")
    mdFile.new_line(getNavigation())
    mdFile.new_header(level=1,title="Collections")    
    parts = []
    collections = OOMP.getItems("collections")
    for collection in collections:      
        parts.append(mdGetLink(collection.getTag("name").value,collection.getFilename("collection",relative="github")))
    base.addDisplayTable(mdFile,parts,4)   
    #mdFile.new_table_of_contents(table_title='Contents', depth=2)
    mdFile.create_md_file()     
    


def generateCollectionPage(collection):       
    print("    Generating collection page for: " + collection.getTag("code").value) 
    filename = collection.getFilename("collection")
    
    mdFile = MdUtils(file_name=filename,title="")
    mdFile.new_header(level=1,title="Collection: " + collection.getTag("name").value)
    mdFile.new_line(collection.getTag("description").value + "  \n")
    
    items = []
    for itemID in collection.getTag("collection").value:
        item = OOMP.getPartByID(itemID)
        string = base.getPictureLink(item)
        items.append(string)
    base.addDisplayTable(mdFile,items,4)
    
    mdFile.create_md_file()     

def makeCollection(d):
    type = d["oompType"]
    size = d["oompSize"]
    color = d["oompColor"]
    desc = d["oompDesc"]
    index = d["oompIndex"]

    hexID = d["hexID"]

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index

    inputFile = "templates/collectionsTemplate.py"
    outputDir = "C:/GH/oomlout_OOMP/oomlout_OOMP_collections/" + oompID + "/"
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
    extraTags.append(OOMP.oompTag("name",d["name"]))
    extraTags.append(OOMP.oompTag("description",d["description"]))
    extraTags.append(OOMP.oompTag("code",d["code"]))
    extraTags.append(OOMP.oompTag("collection",d["collection"]))
    for tag in extraTags:
        tagString = tagString + tag.getPythonLine() + "\n"

    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)

