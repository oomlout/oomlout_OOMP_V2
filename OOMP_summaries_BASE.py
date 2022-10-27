import OOMP

import math
from mdutils.mdutils import MdUtils
from oomBase import *

def createSummary(item,overwrite=False):
    #print("    Making Summary")
    generateReadme(item,overwrite)

def generateReadme(item,overwrite=False):  
    oompID = item["oompID"][0]
    ping()
    filename = OOMP.getFileItem(item,"readme")
    if not os.path.isfile(filename) or overwrite:       
        rFile = newReadme(filename)
        ## Add main image
        addMainImage(item,rFile)
        ###### Summary        
        addSummary(item,rFile)
        """
        ######  Specific items
        type = item.getType()
        if type== "FOOTPRINT":
            generateReadmeFootprint(item, mdFile)
        elif type== "PROJ" or  type== "MODULE" or  type== "BLOCK"  :
            generateReadmeProject(item, mdFile)
        elif type== "SYMBOL":
            generateReadmeProject(item, mdFile)
        else:
            generateReadmePart(item, mdFile)                
        """
        ###### Images  
        addImages(item,rFile)             
        ###### Tags
        addTags(item,rFile)
        
        #print("Writing Readme: " + oompID)
        saveReadme(rFile)

#########################################################################
######  Collections

def generateCollectionsIndex(): 
    print("Generating Collection Index")  
    filename = OOMP.getDir("collections") + "/COLLECTION.md"
    
    rFile = newReadme(filename)
    addHeader(rFile, title="Collections", level=1)
    
    parts = ["Collections"]
    for collectionID in OOMP.itemsTypes["collections"]["items"]:
        collection = OOMP.items[collectionID]
        name = collection["name"][0]
        description = collection["description"][0]    
        entry = ""
        entry = entry + getLink(text = name,link = OOMP.getFileItem(collection,"collection",relative="flat")) + "  <br>"
        entry = entry + description + ""
        
        parts.append(entry)
    addDisplayTable(rFile,parts,1,align="left")   
    
    saveReadme(rFile)

def generateCollectionPage(collection):    
    oompID = collection["oompID"][0]  
    
    filename = OOMP.getFileItem(collection,"collection")
    name = collection["name"][0]
    description = collection["description"][0]
    rFile = newReadme(filename)
    
    print("    Generating collection page for: " + oompID) 

    addHeader(rFile,title="Collection: " + name,level=1)
    addLine(rFile,description)
    
    items = []
    for itemID in collection["collection"][0]["items"]:
        item = OOMP.items[itemID]
        string = getPictureLink(item,resolution="140",link="")
        items.append(string)
    addDisplayTable(rFile,items,4)
    
    saveReadme(rFile)


###### oomp md helpers
def addMainImage(item,mdFile):
    ######  Image work  
        mainImageTree=["image","kicadPcb3dFront","kicadPcb3dBack","kicadPcb3d"]
        imageList = []
        mainImage = ""
        ###### see which images exist
        for image in mainImageTree:
            if(os.path.exists(OOMP.getFileItem(item,image,resolution="450", relative=""))):
                mainImage = OOMP.getFileItem(item,image,resolution="450", relative="flat")
                imageList.append(image)
        if mainImage != "":        
            mdFile.new_line(mdFile.new_reference_image(text='', path=mainImage, reference_tag='im'))
        else:
            mdFile.new_line("NO IMAGE  ")
            pass
 
def addSummary(item,mdFile):
    type = item["oompType"][0]
    oompID = item["oompID"][0]
    hexID = item["hexID"][0]
    try:
        name = item["name"][0]
    except:
        name = ""
    
    title = hexID + " > " + name
    mdFile.new_header(level=1, title=title)
    summary = []
    summary.append("ID: " + oompID)
    summary.append("Hex ID: " + hexID)
    summary.append("Name: " + name) 
    summary.append("Description: " + name) 
    summary.append("Long Link: " + getLink("http://oom.lt/" + oompID, "http://oom.lt/" + oompID))
    summary.append("Short Link: " + getLink("http://oom.lt/" + hexID, "http://oom.lt/" + hexID))
    mdFile.new_list(summary)

def addImages(item, mdFile):
    imageNames = OOMP.getImagesItem(item)
    images = []
    for image in imageNames:
        images.append(image + "<br>" + getImageItem(item,image,resolution=140))
    title='Images'
    if len(images) > 0:
        addDisplayTable(mdFile,images,4)
    else:
        mdFile.new_line("NO IMAGES  ")

def addTags(item,mdFile):
    mdFile.new_header(level=2, title='Tags')
    tags = []
    tags.append("Tag Name")    
    tags.append("Tag Code")
    tags.append("Tag Value")
    #print(item.fullString())
    for tagName in OOMP.tagNames:
        try:
            tag = item[tagName][0]
        except:
            tag = ""
        if tag != "":
            tagNameString = OOMP.tagNames[tagName]["name"] 
            tagCodeString = OOMP.tagNames[tagName]["code"]            
            tagValueString = str(tag)
            if "{" in tagValueString:
                tagValueString = tagValueString.replace("{","<table><tr><td>")
                tagValueString = tagValueString.replace("}","</td></tr></table>")
                tagValueString = tagValueString.replace(":","</td></tr><tr><td>")
                tagValueString = tagValueString.replace(",","</td><td>")
            tags.append(tagNameString)
            tags.append(tagCodeString)
            tags.append(tagValueString)
    #mdFile.new_list(tags)        
    addDisplayTable(mdFile,tags,3,align="left")


###### md helpers
def newReadme(filename):
    return MdUtils(file_name=filename,title='')      

def saveReadme(mdFile):
    try:
        mdFile.create_md_file()
    except:
        print("Error with writing readme (largely for that one with a pi in the name (" + mdFile.file_name + ")")
###### ADDS

def addHeader(mdFile,title,level):
    mdFile.new_header(level=level,title=title)    

def addLine(mdFile,line):
    mdFile.new_line(line)    

###### GET 

def getLink(text,link):
    return "[" + text + "](" + link + ")"

def getImageItem(item,image,resolution="140"):
    link = OOMP.getFileItem(item,image,relative="github")
    imageOut = getImage(OOMP.getFileItem(item,image,resolution=resolution,relative="githubRaw"))
    if ".svg" in imageOut:
        imageOut = getImage(OOMP.getFileItem(item,image,resolution=resolution,relative="githubRaw",extension="png"))
    return getLink(imageOut,link)

def getImage(image,alt=""):
    return "![" + alt + "](" + image + ")"

def getPictureLink(item,resolution="",link="type"):        
    oompID = item["oompID"][0]
    hexID = item["hexID"][0]
    try:
        name = item["name"][0]
    except:
        name = ""

    rv = ""
    type = ""
    if os.path.exists(OOMP.getFileItem(item,"kicadPcb3d")):
        type = "kicadPcb3d"
    elif os.path.exists(OOMP.getFileItem(item,"image")):
        type = "image"

    if type != "":
        string = getImage(OOMP.getFileItem(item,type,relative="githubRaw",resolution=resolution)) + "<br>" + OOMP.getDisplayName(item,br="<br>")
    else:
        string = OOMP.getDisplayName(item,br="<br>")
    if link == "type":
        link = type
    string = getLink(string,OOMP.getFileItem(item,link,relative="github"))
    return string

def addDisplayTable(mdFile,cells,width=4,align="center"):
    mdFile.new_line()

    numCells = len(cells)
    rows = math.floor(numCells / width) + 1
    difference = rows * width - len(cells)

    for r in range(0,difference):
        cells.append("")

    #print("Table Test: " + str(len(cells)) + "    rows: " + str(rows)  + "    Cols: " + str(width))
    mdFile.new_table(columns=width, rows=rows, text=cells, text_align=align)                           