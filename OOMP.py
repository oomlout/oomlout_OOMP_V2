import os
import time
import json
from oomBase import *

import importlib

baseDir = "C:/GH/oomlout_OOMP_V2/"

def getPythonLine(part="newPart",tagName="",tagValue="",indent="    "):  
    if isinstance(tagValue,dict) or isinstance(tagValue,list) :
        rv = indent + part + "['" + tagName + "'].append(" + str(tagValue).replace("\\","") + ")" 
    else:     
        rv = indent + part + "['" + tagName + "'].append('" + str(tagValue) + "')"     
    return rv

def getPythonLineItems(part="it",partID="",tagName="",tagValue="",indent="    "):  
    rv = indent + part + "['"+ partID + "']['" + tagName + "'] = " + str(items[partID][tagName]).replace("\\","")
    return rv


def preloadItem(newPart):
    for tag in tagNames:
        newPart[tagNames[tag]["code"]] = []
    return newPart

def getDisplayName(item,br="\n"):
    try:
        name = item["name"][0]
    except:
        name = ""
    return item["oompID"][0] + br + name

def getDir(type, base=False):
    global baseDir
    rv = ""
    if base:
        rv = baseDir
    for t in repos:    
        if type.lower() == t:
            rv = rv + "oomlout_OOMP_" + t + "_V2/"
    return rv

def getDirItem(item,relative):
    extraFront = ""
    extraBack = ""
    
    if relative.lower() == "github":
        extraFront = "https://github.com/oomlout/"
        extraBack = "tree/main/"
    if relative.lower() == "githubraw":
        extraFront = "https://raw.githubusercontent.com/oomlout/"
        extraBack = "main/"
    rv = ""
    if relative != "flat":
        rv = getDir(getType(item))
    rv = rv + extraBack
    rv = rv + item["oompType"][0] + "/" +  item["oompSize"][0] + "/" + item["oompColor"][0] + "/" +  item["oompDesc"][0] + "/" +  item["oompIndex"][0] + "/"


    return extraFront + rv

def getFileItem(item,file,resolution="",extension="",relative=""):
    resolution = str(resolution)
    rv = filenames[file]["filename"]
    if "&&res&&" in rv:
        if resolution != "":
            rv = rv.replace("&&res&&","_" + resolution)
        else:
            rv = rv.replace("&&res&&","")
    if "&&ext&&" in rv:
        if extension != "":
            rv = rv.replace("&&ext&&",extension)
        else:
            rv = rv.replace("&&ext&&",filenames[file]["defaultExtension"])
    rv = getDirItem(item,relative) + rv
    return rv

def getImagesItem(item,resolution=""):
    images = []
    for image in filenames["IMAGE"]:
        testFile = getFileItem(item,image,resolution)
        if os.path.exists(testFile):
            images.append(image)
    return images

def getName(item): 
    order = ["Size", "Desc","Color","Type","Index"]
    name = ""
    for part in order:
        oompPart = item["oomp" + part][0]
        try:
            extra = tagDetails[part.lower()][oompPart]["name"]
        except:
            extra = ""
        if extra != "":
            name = name + extra + " "
    name = name.strip()
    return name

def getType(item):
    tests = {}
    tests["collections"] = ["COLLECTION"]
    tests["eda"] = ["FOOTPRINT","SYMBOL"]
    tests["modules"] = ["BLOCK","MODULE"]
    tests["projects"] = ["PROJ"]
    rv = "parts"
    oompType = item["oompType"][0]
    for t in tests:
        if oompType in tests[t]:
            rv = t
    return rv

def setBaseDir(base):
    global baseDir
    baseDir = base 
    baseDir = "C:/GH/oomlout_OOMP_V2/"

    return baseDir


##############################################################################
##############################################################################
##############################################################################
######  LOADING ROUTINES

###### file filters
defaultFilter = ["details.py","details2.py","details3.py"]
projectsFilter = ["details.py","details2.py","details3.py","detailsPartsOomp.py","detailsPartsRaw.py"]
partsFilter = ["details.py","details2.py","detailsInstancesOomp.py","detailsFootprintsOomp.py"]
rs = ["parts","eda","kicad","modules","collections","projects"]
typesNames = rs
repos = {}
type = "collections"
for type in rs:
    repos[type] = {}
    repos[type]["code"] = type    
    repos[type]["fileFilter"] = defaultFilter
    if type == "parts":
        repos[type]["fileFilter"] = partsFilter
    if type == "projects" or  type == "modules":
        repos[type]["fileFilter"] = projectsFilter
    repos[type]["directory"] = "oomlout_OOMP_" + type + "_V2"


###### Loading and pickle
def loadPickle():
    global items
    print("Loading Pickle")
    start = time.time()
    reload()
    picklePartsFile = "sourceFiles/picklePartsOOMP.json"
    items = json.loads(oomReadFileToString(picklePartsFile))
    loadItemTypes()    
    print(getReport(startTime=start))
    pass

import time

def makePickle():
    print("Making Pickle:")
    start = time.time()
    reload()
    copyAllFiles()
    importAllFiles()
    loadNames()
    exportPickle()
    loadItemTypes()            
    print(getReport(startTime=start))
    
def exportPickle(picklePartsFile="sourceFiles/picklePartsOOMP.json"): 
    if picklePartsFile == "":
        picklePartsFile= "sourceFiles/picklePartsOOMP.json"
    oomWriteToFile(picklePartsFile,json.dumps(items))

import keyboard

def copyAllFiles():
    oomMakeDir("sourceFiles\\load\\")
    for l in repos:
        copyDir = "sourceFiles\\load\\" + l + "\\"
        oomMakeDir(copyDir)
        print("    Copying:    " + repos[l]["code"])
        directory = "oomlout_OOMP_" + repos[l]["code"] + "_V2\\"
        for filter in repos[l]["fileFilter"]:
            files = glob.glob(directory + "**\\" + filter,recursive=True)
            outFiles = glob.glob(copyDir + "**\\*",recursive=True)
            for file in files:

                inFile = file
                oompID = inFile.replace(directory,"").replace(filter,"").replace("\\","")
                outFile = copyDir + makePythonSafe(oompID + filter.replace(".py","")) + ".py"
                
                if not outFile in outFiles:
                    oomCopyFile(inFile,outFile)
                    ping()
                else:
                    inSize = os.path.getsize(inFile)
                    outSize = os.path.getsize(outFile)
                    if inSize != outSize:
                        oomCopyFile(inFile,outFile)
                        ping()

def importAllFiles():
    print("    Importing Files")
    copyDir = "sourceFiles\\load\\"  # + l + "\\"
    files = glob.glob(copyDir + "**\\*",recursive=False)
    for file in files:
        if ".py" in file:
            name = file.replace("\\",".").replace(".py","")
            mod = importlib.import_module(name)
            newPart = {}
            newPart = preloadItem(newPart)
            newPart = mod.load(newPart,items)
            if newPart != None:
                items[newPart["oompID"][0]] = newPart
                itemsHex[newPart["hexID"][0]] = newPart
            #importlib.reload(mod)

def makePythonSafe(string):
    rv = string
    rv = rv.replace("-","_").replace(".","_")
    return rv


def getReport(startTime="",indent = "    "):
    rv = ""   
    rv = rv + indent + "Number of Items: "+ str(len(items)) + "\n"
    for r in repos:
        rv = rv + indent + "Number of " + r + ": "+ str(len(itemsTypes[r]["items"])) + "\n"
    if startTime != "":
        rv = rv + indent + "Time to execute: " + str(round(time.time()-startTime)) + " sec"
    return rv


def reload():
    global items, itemsTypes
    items = {}    
    itemsTypes = {}

def load():
    global tagNames,tagDetails,items,itemsTypes,itemsHex,filenames
    tagNames = {}
    tagDetails = {}
    items = {}    
    itemsTypes = {}
    itemsHex = {}
    filenames = {}

def loadItemTypes():
    global itemsTypes
    tests = {}
    tests["collections"] = ["COLLECTION"]
    tests["eda"] = ["FOOTPRINT","SYMBOL"]
    tests["modules"] = ["BLOCK","MODULE"]
    tests["projects"] = ["PROJ"]
    tests["parts"]=[]
    for t in tagDetails["type"]:
        tests["parts"].append(tagDetails["type"][t]["code"])
    itemsTypes = {}
    for r in repos:
        itemsTypes[r] = {}
        itemsTypes[r]["items"] = []
    for t in tests:
        itemsTypes[t]["type"] = t
        
        for item in items:
            if items[item]["oompType"][0] in tests[t]:
                itemsTypes[t]["items"].append(item)
    pass

def loadNames():
    print("Loading Names")
    for id in items:
        if len(items[id]["name"]) == 0:
            items[id]["name"].append(getName(items[id]))
            pass



def exportTagsItem(item,filetype,tags):
        filename = getFileItem(item,filetype)
        oompID = item["oompID"][0]       

        contents = "def load(newPart,it):" + "\n"
        contents2 = ""
        for tag in tags:
            contents2 = contents2 + getPythonLineItems(part="it",partID=oompID,tagName=tag) + '\n'
        if contents2 != "":
            print("    Exporting tags to: " + filename)
            oomWriteToFile(filename,contents+contents2)

















tagNames = {}
tagDetails = {}
items = {}
itemsHex = {}
itemsTypes = {}
filenames = {}

import OOMP_tag
