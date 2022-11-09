import OOMP

import math
from mdutils.mdutils import MdUtils
from oomBase import *

import OOMP_summaries_PAGES
import OOMP_summaries_INDEXES

def createSummary(item,overwrite=False):
    #print("    Making Summary")
    generateReadme(item,overwrite)

def generateReadme(item,overwrite=False):  
    oompID = item["oompID"][0]
    ping(1000)
    filename = OOMP.getFileItem(item,"readme")
    if not os.path.isfile(filename) or overwrite:       
        rFile = newReadme(filename)
        ## Add main image
        addMainImage(item,rFile)
        ###### Summary        
        addSummary(item,rFile)
        
        ######  Specific items
        type = OOMP.getType(item)
        if type== "eda":
            OOMP_summaries_PAGES.generateReadmeFootprint(item, rFile)
        elif type== "collections":
            OOMP_summaries_PAGES.generateReadmeCollection(item, rFile)
        elif type== "projects" or  type== "modules"  :
            OOMP_summaries_PAGES.generateReadmeProject(item, rFile)
        else:
            OOMP_summaries_PAGES.generateReadmePart(item, rFile)                
        
        ###### Images  
        addImages(item,rFile)             
        ###### Tags
        addTags(item,rFile)
        addToc(rFile)
        #print("Writing Readme: " + oompID)
        saveReadme(rFile)

#########################################################################
######  Collections

def generateCollectionsIndex(): 
    OOMP_summaries_INDEXES.generateCollectionsIndex()
    


###### oomp md helpers
def addMainImage(item,mdFile):
    ######  Image work  
        mainImageTree=["image","kicadPcb3dFront","kicadPcb3dBack","kicadPcb3d"]
        imageList = []
        mainImage = ""
        ###### see which images exist
        for image in mainImageTree:
            imageFile = OOMP.getFileItem(item,image,resolution="450", relative="")
            if(os.path.exists(imageFile)):
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
            if len(item[tagName]) > 1:
                tag = str(item[tagName]).replace("[","").replace("]","").replace("'","").replace('"',"")
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

def addToc(mdFile):
   mdFile.new_table_of_contents(table_title='Contents', depth=2) 

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
    if link != "":
        if text != None:
            return "[" + text + "](" + link + ")"
        
        else:
            return text
    else:
        return text

def getImageItem(item,image,resolution="140",link=True):
    lin = OOMP.getFileItem(item,image,relative="github")
    imageOut = getImage(OOMP.getFileItem(item,image,resolution=resolution,relative="githubRaw"))
    if ".svg" in imageOut:        
        imageOut = getImage(OOMP.getFileItem(item,image,resolution=resolution,relative="githubRaw",extension="png"))
    if link:
        return getLink(imageOut,lin)
    else:        
        return imageOut

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