import collections
import os
from pyclbr import readmodule_ex
import random
import shutil
import time
from wsgiref.handlers import BaseCGIHandler
import json
from oomBase import *

import importlib

baseDir = ""

def getPythonLine(part="newPart",tagName="",tagValue=""):  
    if isinstance(tagValue,dict) or isinstance(tagValue,list) :
        rv = part + "['" + tagName + "'].append(" + str(tagValue).replace("\\","") + ")\n" 
    else:     
        rv =  part + "['" + tagName + "'].append('" + str(tagValue) + "')\n"     
    return rv
    
def preloadItem(newPart):
    for tag in tagNames:
        newPart[tagNames[tag]["code"]] = []

######  FILENAME AND DIRECTORY ROUTINES

###### file filters
defaultFilter = ["details.py","details2.py","details3.py"]
projectsFilter = ["details.py","details2.py","details3.py","detailsPartsOomp.py","detailsPartsRaw.py"]
partsFilter = ["details.py","details2.py","detailsInstancesOomp.py","detailsFootprintsOomp.py"]

rs = ["parts","eda","kicad","modules","collections","projects"]
repos = {}
type = "collections"
for type in rs:
    repos[type] = {}
    repos[type]["code"] = type    
    repos[type]["fileFilter"] = defaultFilter
    if type == "parts":
        repos[type]["fileFilter"] = partsFilter
    if type == "projects":
        repos[type]["fileFilter"] = projectsFilter
    repos[type]["directory"] = "oomlout_OOMP_" + type + "_V2"


def getDir(type, base=False):
    global baseDir
    rv = ""
    if base:
        rv = baseDir
    for t in repos:    
        if type.lower() == t:
            rv = rv + "oomlout_OOMP_" + t + "_V2/"
    return rv

###### Loading and pickle
def loadPickle():
    global items
    print("Loading Pickle")
    start = time.process_time()
    load()
    picklePartsFile = "sourceFiles/picklePartsOOMP.json"
    items = json.loads(oomReadFileToString(picklePartsFile))
    loadItemTypes()
    print(getReport(startTime=start))
    pass

import time

def makePickle():
    print("Making Pickle:")
    start = time.process_time()
    load()
    copyAllFiles()
    importAllFiles()
    loadItemTypes()        
    exportPickle()
    print(getReport(startTime=start))
    
def exportPickle(picklePartsFile="sourceFiles/picklePartsOOMP.json"): 
    if picklePartsFile == "":
        picklePartsFile= "sourceFiles/picklePartsOOMP.json"
    oomWriteToFile(picklePartsFile,json.dumps(items))

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
            importlib.reload(mod)
    

def makePythonSafe(string):
    rv = string
    rv = rv.replace("-","_").replace(".","_")
    return rv




def loadDirectory(directory,fileFilter=["details.py"],filename="sourceFiles/oompLoad.py",type=""):    
    directory = "sourceFiles/" + type + "/" 
    oomMakeDir(directory)    
    skip = "Pololu_Breakout-16_15.2x20.3mm"
    for filter in fileFilter:
        files = glob.glob(directory + "**/" + filter,recursive=True)
        for file in files:
            if skip not in file:
                inFile = file
                outfile = directory + file.split("\\")[len(file.split("\\"))-1]
                string = oomReadFileToString(file)
                f.write(string + "\n")
            else:
                pass


def makeSingleFile():
    f = open(filename, "a+")
    f.write("""
import OOMP 

defTn = OOMP.tagNames

    
def preloadItem(newPart,tn=defTn):
    for tag in tn:
        newPart[tn[tag]["code"]] = []
""")
    f.close()

def loadDirectoryOld(directory,fileFilter=["details.py"],   filename="sourceFiles/oompLoad.py"):    
    
    oomMakeDir("sourceFiles/")
    f = open(filename, "a+")
    f.write("""
import OOMP 

defTn = OOMP.tagNames

    
def preloadItem(newPart,tn=defTn):
    for tag in tn:
        newPart[tn[tag]["code"]] = []
""")
    testing = 1000000000000000000
    skip = "Pololu_Breakout-16_15.2x20.3mm"
    for filter in fileFilter:
        files = glob.glob(directory + "**/" + filter,recursive=True)
        for file in files:
            if skip not in file:
                string = oomReadFileToString(file)
                f.write(string + "\n")
            else:
                pass
    f.close()


def getReport(startTime=""):
    rv = ""   
    rv = rv + "Number of Items: "+ str(len(items)) + "\n"
    for r in repos:
        rv = rv + "Number of " + r + ": "+ str(len(itemsTypes[r])) + "\n"
    if startTime != "":
        rv = rv + "Time to execute: " + str(round(time.process_time()-startTime)) + " sec"
    return rv

######### OLD


#def oompAddDetail(category,code,name,sort="",extra1="",extra2=""):
#    details.append(oompDetail(category,code,name,sort,extra1="",#extra2=""))

def getDetailFromCode(category,code):
    """
    for x in details:
        if x.category == category:
            if x.code == code:
                return x
    return oompDetail("","","","")
    """
    try:
        rv = details[category + "-" + code]
    except KeyError:
        rv = oompDetail("","","","")
    return rv

def getDetailsCategory(category=""):
    rv = []
    for detail in details:
        if category in detail.category:
            rv.append(detail)
    return rv

def getParts():
    return parts

def getItems(type="",cache=False):
    global parts, partsFootprints, partsParts, partsNoFootprints, partsProjects, partsTemplates, partsSymbols
    if type == "load":
        getItems("footprints",cache=False)
        getItems("symbols",cache=False)
        getItems("parts",cache=False)
        getItems("modules",cache=False)
        getItems("collectionss",cache=False)
        getItems("nofootprints",cache=False)
        getItems("projects",cache=False)
        getItems("templates",cache=False)        
    if not cache:
        rv = parts
        if type.upper() == "FOOTPRINTS":
            rv = []
            for part in parts:
                t = part.getTag("oompType")
                if t.value == "FOOTPRINT":
                    rv.append(part)
            partsFootprints = rv
        if type.upper() == "MODULES":
            rv = []
            for part in parts:
                t = part.getTag("oompType")
                if t.value == "BLOCK" or t.value == "MODULE" :
                    rv.append(part)
            partsSymbols = rv
        if type.upper() == "COLLECTIONS":
            rv = []
            for part in parts:
                t = part.getTag("oompType")
                if t.value == "COLLECTION":
                    rv.append(part)
            partsSymbols = rv
        if type.upper() == "SYMBOLS":
            rv = []
            for part in parts:
                t = part.getTag("oompType")
                if t.value == "SYMBOL":
                    rv.append(part)
            partsSymbols = rv
        if type.upper() == "PARTS":
            rv = []
            for part in parts:
                t = part.getTag("oompType")
                if t.value == "TEMPLATE" or t.value == "FOOTPRINT" or t.value == "SYMBOL" or t.value == "PROJ"   or t.value == "BLOCK"   or t.value == "MODULE"     or t.value == "COLLECTION"  :
                    c = "SKIP"
                else:
                    rv.append(part)
            partsParts = rv
        if type.upper() == "NOFOOTPRINTS":
            rv = []
            for part in parts:
                t = part.getTag("oompType")
                if not t.value == "FOOTPRINT" and not t.value == "TEMPLATE":
                    rv.append(part)
                else:
                    c = "SKIP"
            partsNoFootprints = rv        
        if type.upper() == "PROJECTS":
            rv = []
            for part in parts:
                t = part.getTag("oompType")

                if t.value == "PROJ":
                    rv.append(part)
            partsProjects = rv
        if type.upper() == "TEMPLATES":
            rv = []
            for part in parts:
                t = part.getTag("oompType")
                if t == "TEMPLATE":
                    rv.append(part)                
            partsTemplates = rv
    else:
        rv = parts
        if type.upper() == "FOOTPRINTS":
            rv = partsFootprints
        if type.upper() == "SYMBOLS":
            rv = partsSymbols
        if type.upper() == "PARTS":
            rv = partsParts
        if type.upper() == "NOFOOTPRINTS":
            rv = partsNoFootprints
        if type.upper() == "PROJECTS":
            rv = partsProjects
        if type.upper() == "TEMPLATES":
            rv = partsTemplates
    return rv

#def getPartByID(part):
##    print("     Get Part By ID: " + part)
#    try:
#        rv = parts[part]
#    except KeyError:
#        rv = oompItem()
#    return rv

#def getPartByHex(hexid):
##    print("     Get Part By ID: " + part)
#    for x in parts:
#        valueTest = x.getTag("hexID").value
#        if valueTest == hexid:
#            return x     
#    return oompItem("")

# def getPartByName(name):
# ##    print("     Get Part By ID: " + part)
#     for x in parts:
#         if x.getTag("name").value == name:
#             return x     
#     return oompItem("")    


# def getDetailByCode(category, code):    
# ##    print("     Get Part By ID: " + code)
#     for x in details:
#         #print("    Matching: " + x.code + " with -- " + code)
#         if x.code == code:
#             return x     
#     return oompDetail("","","","")


def printParts():
    print("OOMP Parts")
    for x in parts:
        b = 0
        #print("    Part: " + str(x.fullString()))
        oompID = x.getTag("oompID").value
        print("Loading: ", oompID)

def getNextIndex():
    return len(parts) + 1
        

def getAddTagLine(tagName,value,quotes="single"):
    if quotes == "single":
        return 'newPart.addTag("' + tagName + '", "' + value + '")\n'
    elif quotes == "triple":
        return 'newPart.addTag("' + tagName + '", """' + value + '""")\n'


def getReportOld():
    rv = ""   
    rv = rv + "Number of Items: "+ str(len(getItems("all"))) + "\n"
    rv = rv + "Number of Footprints: "+ str(len(getItems("footprints"))) + "\n"
    rv = rv + "Number of Parts: "+ str(len(getItems("parts"))) + "\n"
    rv = rv + "Number of Projects: "+ str(len(getItems("projects"))) + "\n"
    rv = rv + "Number of Modules: "+ str(len(getItems("modules"))) + "\n"
    return rv

######  Directory routines

def setBaseDir(base):
    global baseDir
    baseDir = base 
    baseDir = "C:/GH/oomlout_OOMP_V2/"



def getFileOpening(hexID="",type="",size="",color="",desc="",index=None,name=None):
    if index == None:
        index = getNextIndex()
    rv = ""

    rv = rv + "###### OOMP FILE  ######\n"
    rv = rv + "\n"
    rv = rv + "import OOMP\n"
    rv = rv + "import OOMPtags\n"    
    rv = rv + "\n"
    rv = rv + "newPart = OOMP.oompItem()\n"
    rv = rv + "\n"
    rv = rv + getAddTagLine("hexID",hexID)
    rv = rv + getAddTagLine("oompType",type)
    rv = rv + getAddTagLine("oompSize",size)
    rv = rv + getAddTagLine("oompColor",color)
    rv = rv + getAddTagLine("oompDesc",desc)
    rv = rv + getAddTagLine("oompIndex",index)

    if name != None:
        rv = rv + getAddTagLine("oompName",name)

    rv = rv + "\n"

    return rv

def getFileEnding():
    return 'OOMP.parts.append(newPart)' 


instanceCount = 0

def getInstanceCount(calc=False):
    global instanceCount
    if instanceCount == 0 or calc:
        instanceCount = 0
        for part in getItems("PARTS"):
            instanceCount = instanceCount + len(part.getTags("oompInstances"))
    return instanceCount


class oompDict(dict):
    def __init__(self,index=None):
        self.__dict__ = {}     

    def append(self,newPart):
        oompID = newPart.getTag("oompID").value
        if oompID == "----":
            oompID = newPart.getTag("taxaID").value
        self.__dict__[oompID] = newPart

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __iter__(self):
        return iter(self.values())

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()        
     

class oompDetailDict(dict):
    def __init__(self,index=None):
        self.__dict__ = {}

    def append(self,newDetail):
        detailID = newDetail.category + "-" + newDetail.code
        self.__dict__[detailID] = newDetail


    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __iter__(self):
        return iter(self.values())

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

class oompItemDict(dict):
    def __init__(self,index=None):
        self.__dict__ = {}

    def append(self,item):
        detailID = item.name
        self.__dict__[detailID] = newDetail


    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __iter__(self):
        return iter(self.values())

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()


class oompItem:

    def __init__(self,index=None):
        if index == None:
            index = getNextIndex()
        self.tags=list()
        if index == 0:
            index = len(parts) + 1
        #self.index=index
        self.addTag("index", index)

    def __str__(self):
        rv = ""
        rv = rv + self.getName()
        #for x in self.tags:
        #    rv = rv + "    " + str(x)
        return rv

    def getID(self):
        return self.getTag("oompID").value
    def getName(self):
        return self.getTag("name").value
    def getType(self):
        return self.getTag("oompType").value
    def getHex(self):
        return self.getTag("hexID").value

    def fullString(self):
        rv = ""
        rv = rv + self.getName() + "\n"
        for x in self.tags:
            rv = rv + "" + str(x)
##            if not isinstance(x.value, list):
##                rv = rv + "    " + str(x)
##            else: #tag has a list
##                rv = rv + "    " + str(x) + "\n"
##                for y in x.value:
##                    if isinstance(y, list):
##                        rv = rv + "    " + str(y) + "\n"
##                        for c in y:
##                            rv = rv + "            " + str(c) + "\n"
##                    else:
##                        rv = rv + "        " + str(y) + "\n"
        return rv
    
    def getDir(self):  
        return self.getFolder()

    def getFolder(self,style=""):        
        rv = ""
        oompType = self.getTag("oompType").value.replace(":","-")
        oompSize = self.getTag("oompSize").value.replace(":","-")
        oompColor = self.getTag("oompColor").value.replace(":","-")
        oompDesc = self.getTag("oompDesc").value.replace(":","-")
        oompIndex = self.getTag("oompIndex").value.replace(":","-")
        oompID = self.getTag("oompID").value.replace(":","-")
        if style == "":
            if oompType == 'FOOTPRINT':
                rv = "oomlout_OOMP_eda/" + oompType + "/" + oompSize + "/" + oompColor + "/" + oompDesc + "/" + oompIndex.replace(":","-").replace("\\","-").replace("/","-") + "/"
            elif oompType == "SYMBOL":
                rv = "oomlout_OOMP_eda/" + oompType + "/" + oompSize + "/" + oompColor + "/" + oompDesc + "/" + oompIndex.replace(":","-").replace("\\","-").replace("/","-") + "/"
            elif oompType == "MODULE" or oompType == "BLOCK" :
                rv = "oomlout_OOMP_modules/" + oompID + "/"
            elif oompType == "COLLECTION":
                rv = "oomlout_OOMP_collections/" + oompID + "/"
            elif oompType == "PROJ":
                rv = "oomlout_OOMP_projects/"  + oompID + "/" 
            else:
                rv = "oomlout_OOMP_parts_V2/"  + oompID + "/" 
        elif style == "github":
            if oompType == "FOOTPRINT":
                rv = "https://github.com/oomlout/oomlout_OOMP_eda/tree/main/" + oompType + "/" + oompSize + "/" + oompColor + "/" + oompDesc + "/" + oompIndex.replace(":","-").replace("\\","-").replace("/","-") + "/"
            elif oompType == "SYMBOL":
                rv = "https://github.com/oomlout/oomlout_OOMP_eda/tree/main/" + oompType + "/" + oompSize + "/" + oompColor + "/" + oompDesc + "/" + oompIndex.replace(":","-").replace("\\","-").replace("/","-") + "/"
            elif oompType == "PROJ":
                rv = "https://github.com/oomlout/oomlout_OOMP_projects/tree/main/"  + oompID + "/" 
            else:
                rv = "https://github.com/oomlout/oomlout_OOMP_parts_V2/tree/main/"  + oompID + "/" 

        return rv


    def ifFileExists(self,filename,relative="",resolution="",extension=""):
        file= self.getFilename(filename,relative=relative,resolution=resolution,extension=extension)
        rv = os.path.isfile(file)
        return rv

    def getFilename(self,filename,relative="",resolution="",extension=""):
        oompType = self.getTag("oompType").value

        allNames = []
        allImagesNames = []

        ################################# Resolution String
        resolutionString = ""
        if resolution != "":
            resolutionString = "_" + str(resolution)

        ################################# Define Base

        base = ""
        if relative == "": ## relative to oomlout_OOMP
            base = self.getFolder()
        elif relative.lower() == "flat": ## relative to directory
            base = ""
        elif relative.lower() == "full": ## relative to c
            base = baseDir + self.getFolder()
        elif relative.lower() == "github": ## relative to c
            oompID = self.getTag("oompID").value
            if "FOOTPRINT" in oompID or "SYMBOL" in oompID:
                oompID = self.getTag("oompIDslashes").value
                base = "https://github.com/oomlout/oomlout_OOMP_eda/tree/main/" + oompID + "/"
            elif "PROJ" in oompID:
                base = "https://github.com/oomlout/oomlout_OOMP_projects/tree/main/" + oompID + "/"
            elif "MODULE" in oompID or  "BLOCK" in oompID:
                base = "https://github.com/oomlout/oomlout_OOMP_modules/tree/main/" + oompID + "/"
            elif "MODULE" in oompID or  "COLLECTION" in oompID:
                base = "https://github.com/oomlout/oomlout_OOMP_collections/tree/main/" + oompID + "/"
            else:    
                base = "https://github.com/oomlout/oomlout_OOMP_parts_V2/tree/main/" + oompID + "/"
        elif relative.lower() == "githubweb": ## relative to c
            oompID = self.getTag("oompID").value
            if "FOOTPRINT" in oompID  or "SYMBOL" in oompID:
                oompID = self.getTag("oompIDslashes").value
                base = "https://htmlpreview.github.io/?https://github.com/oomlout/oomlout_OOMP_eda/blob/main/" + oompID + "/"
            elif "MODULE" in oompID or  "BLOCK" in oompID:
                base = "https://htmlpreview.github.io/?https://github.com/oomlout/oomlout_OOMP_modules/blob/main/" + oompID + "/"
            elif "COLLECTION" in oompID:
                base = "https://htmlpreview.github.io/?https://github.com/oomlout/oomlout_OOMP_collections/blob/main/" + oompID + "/"
            elif "PROJ" in oompID:
                base = "https://htmlpreview.github.io/?https://github.com/oomlout/oomlout_OOMP_projects/blob/main/" + oompID + "/"
            elif "COLLECTION" in oompID:
                base = "https://htmlpreview.github.io/?https://github.com/oomlout/oomlout_OOMP_collections/blob/main/" + oompID + "/"
            else:    
                base = "https://htmlpreview.github.io/?https://github.com/oomlout/oomlout_OOMP_parts_V2/blob/main/" + oompID + "/"
        elif relative.lower() == "githubraw": ## relative to c
            oompID = self.getTag("oompID").value
            if "FOOTPRINT" in oompID or "SYMBOL" in oompID:
                oompID = self.getTag("oompIDslashes").value
                base = "https://raw.githubusercontent.com/oomlout/oomlout_OOMP_eda/main/" + oompID + "/"
            elif "MODULE" in oompID or  "BLOCK" in oompID:
                base = "https://raw.githubusercontent.com/oomlout/oomlout_OOMP_modules/main/" + oompID + "/"        
            elif "PROJ" in oompID:
                base = "https://raw.githubusercontent.com/oomlout/oomlout_OOMP_projects/main/" + oompID + "/"
            elif "COLLECTION" in oompID:
                base = "https://raw.githubusercontent.com/oomlout/oomlout_OOMP_collections/main/" + oompID + "/"
            elif "COLLECTION" in oompID:
                base = "https://raw.githubusercontent.com/oomlout/oomlout_OOMP_collections/main/" + oompID + "/"
            else:    
                base = "https://raw.githubusercontent.com/oomlout/oomlout_OOMP_parts_V2/main/" + oompID + "/"
        else:
            base = baseDir + self.getFolder()
        fileExtra = filename
        

        ###########################  Define File


        ######  Basic
        name =   "readme"
        allNames.append(name)
        if filename.lower() == name:            
            fileExtra = "README.md"
        name =   "collection"
        allNames.append(name)
        if filename.lower() == name:            
            fileExtra = "COLLECTION.md"
        
        ######  Bom Files      
        name =   "bominteractive"
        allNames.append(name)
        if filename.lower() == name:            
            fileExtra = "kicad/bom/ibom.html"
        name =   "bominteractivefront"
        allNames.append(name)        
        allImagesNames.append(name)
        if filename.lower() == name:            
            fileExtra = "bomFront"  + resolutionString + ".png"
        name =   "bominteractiveback"
        allNames.append(name)
        allImagesNames.append(name)
        if filename.lower() == name:            
            fileExtra = "bomBack"  + resolutionString + ".png"
        name =   "bominteractivecsv"
        allNames.append(name)
        if filename.lower() == name:            
            fileExtra = "kicad/bom/parts.csv"
        
        
        
        ######  Datasheet
        name = "datasheet"
        allNames.append(name)
        if filename.lower() == name:
            fileExtra = "datasheet.pdf"
        ######  Image files
        name = "image"
        allNames.append(name)
        allImagesNames.append(name)
        if filename.lower() == name:
            type = self.getTag("oompType")
            if type.value.upper() == "FOOTPRINT" or type.value.upper() == "SYMBOL":
                if extension != "":
                    fileExtra = "image" + resolutionString + "." + extension 
                else:    
                    fileExtra = "image" + resolutionString + "." + "png"  
            else :
                if extension != "":
                    fileExtra = "image" + resolutionString + "." + extension 
                else:
                    fileExtra = "image" + resolutionString + ".jpg"  
            
        
        imageTypePng = ["kicadPcb3d","kicadPcb3dFront","kicadPcb3dBack","kicadSchem", "eagleImage","eagleSchemImage"]        

        for imageType in imageTypePng:            
            name = imageType
            allNames.append(name)
            allImagesNames.append(name)
            if filename.lower() == imageType.lower():
                fileExtra = imageType + resolutionString + ".png"  

        imageTypeJpg = ["image_RE","image_TOP","image_BOTTOM"]        
        for imageType in imageTypeJpg: 
            name = imageType
            allNames.append(name)
            allImagesNames.append(name)
            if filename.lower() == imageType.lower():
                fileExtra = imageType + resolutionString + ".jpg"  

        ###### Diagram files
        diagTypes = ['diagBBLS','diagDIAG','diagIDEN','diagSCHEM','diagSIMP'] 
        for type in diagTypes:
            allNames.append(type)
            allImagesNames.append(type)
            if filename.lower() == type.lower():
                if extension == "":
                    extension = "png"
                fileExtra = type + resolutionString + "." + extension
           



        ######  Eagle Files         
        name = "boardeagle"
        allNames.append(name)
        if filename.lower() == name:
            fileExtra = "boardEagle.brd"
        name = "schemeagle"
        allNames.append(name)
        if filename.lower() == name:
            
            if extension == "":
                fileExtra = "schematicEagle.sch"
            elif extension == "png":
                fileExtra = "eagleSchemImage" + resolutionString + "." + extension
            
        name = "eagleparts"
        allNames.append(name)
        if filename.lower() == name:        
            fileExtra = "eagleparts.txt"
        name = "eaglebom"
        allNames.append(name)
        if filename.lower() == name:        
            fileExtra = "eagleBOM.csv"

        ######  Kicad files
        name = "kicadFootprint"
        allNames.append(name)
        if filename.lower() == name.lower():        
            fileExtra = "footprint.kicad_mod"

        ###### module stuff



        ###### collection stuff
        name = "readme"
        allNames.append(name)
        if filename.lower() == name.lower():        
            fileExtra = "README.md"

        


        name = "boardkicad"
        allNames.append(name)                
        if filename.lower() == name:        
            if oompType == "MODULE" or  oompType == "BLOCK": 
                fileExtra = self.getID() + ".kicad_pcb"
            else:
                fileExtra = "kicad/boardKicad.kicad_pcb"
        name = "kicadbom"
        allNames.append(name)
        if filename.lower() == name:        
            fileExtra = "kicad/boardKicadBom.csv"
        name = "schemkicad"
        allNames.append(name)
        if filename.lower() == name:        
            if oompType == "MODULE" or  oompType == "BLOCK": 
                fileExtra = self.getID() + ".kicad_sch"    
            else:
                fileExtra = "kicad/schematicKicad.kicad_sch"
                

        if filename.lower() == "dirkicad":
            fileExtra = "kicad/"


        
        name = "symbolkicad"
        allNames.append(name)
        if filename.lower() == name:        
            fileExtra = "symbol.kicad_sym"

        ###### pcb draw files
        name = "pcbdraw"
        allNames.append(name)
        allImagesNames.append(name)
        if filename.lower() == name:
            if extension == "":        
                fileExtra = "pcbdraw.svg"
            else:
                fileExtra = "pcbdraw"  + resolutionString + "." + extension

        name = "pcbdrawback"
        allNames.append(name)
        allImagesNames.append(name)
        if filename.lower() == name:
            if extension == "":        
                fileExtra = "pcbdrawBack.svg"
            else:
                fileExtra = "pcbdrawBack"  + resolutionString + "." + extension


        ######  Label Files
        labels = ["label-front","label-inventory","label-spec"]
        for label in labels:
                
            name = label
            allNames.append(name)
            allImagesNames.append(name)
            if filename.lower() == name:        
                if extension == "png" or resolution != "":
                    fileExtra = label + resolutionString + ".png"  
                elif extension == "svg":
                    fileExtra = label + ".svg"    
                else:
                    fileExtra = label + ".pdf"    

        ######  Python Files
        name = "details"
        allNames.append(name)
        if filename.lower() == name:        
            fileExtra = "details.py"                
        name = "detailspartsraw"
        allNames.append(name)
        if filename.lower() == name:        
            fileExtra = "detailsPartsRaw.py"
        name = "detailspartsoomp"
        allNames.append(name)
        if filename.lower() == name:        
            fileExtra = "detailsPartsOomp.py"   
        name = "detailsinstancesoomp"
        allNames.append(name)
        if filename.lower() == name:        
            fileExtra = "detailsInstancesOomp.py"  
        name = "detailsfootprintsoomp"
        allNames.append(name)
        if filename.lower() == name:        
            fileExtra = "detailsFootprintsOomp.py"   
             

        ######  Redirect
        name = "redirect"
        allNames.append(name)
        if filename.lower() == name:        
            base = base.replace(self.getFolder(),"")            
            fileExtra = "sourceFiles/redirects/" + self.getTag("oompID").value.replace("/","-").replace(":","-") + "/index.html"
        name = "redirecthex"
        allNames.append(name)
        if filename.lower() == name:        
            base = base.replace(self.getFolder(),"")            
            fileExtra = "sourceFiles/redirects/" + self.getTag("hexID").value + "/index.html"

        if filename.lower() == "all":
            all = []
            for item in allNames:
                all.append(self.getFilename(item,relative=relative,resolution=resolution,extension=extension))
            return all
        if filename.lower() == "allimages":
            all = []
            for item in allImagesNames:
                if item == "image":
                    all.append(self.getFilename(item,relative=relative,resolution=resolution,extension=""))
                else:                    
                    all.append(self.getFilename(item,relative=relative,resolution=resolution,extension="png"))
            return all
        if filename.lower() == "allimagesnames":
            all = []
            for item in allImagesNames:
                all.append(item)
            return all




        return base + fileExtra


    def exportTags(self,filetype,tags):
        
        filename = self.getFilename(filetype)
        oompID = self.getTag("oompID").value

        

        contents = "import OOMP" + "\n"
        contents = contents + 'newPart = OOMP.getPartByID("' + oompID + '")' + "\n"
        contents = contents  + '' + '\n'
        contents2 = ""
        for tag in tags:
            values = self.getTags(tag)
            for value in values:
                contents2 = contents2 + value.getPythonLine() + '\n'
        if contents2 != "":
            print("    Exporting tags to: " + filename)
            oomWriteToFile(filename,contents+contents2,utf2=True)


    ##No longer used    
    def indexMd(self):
        oompID = self.getTag("oompID").value
        name = self.getTag("name").value
        hexID = self.getTag("hexID").value
        rv = ""
        image = ""
        filename = getDir("parts") + oompID +  "/image_140.jpg"
        if os.path.isfile(filename):
            image = "![" + name + "](" + oompID +  "/image_140.jpg)"
        text = "[" + oompID + " <br> " + name + "](" + oompID + "/)"
        hex = ""
        if hexID != "":
            hex = "[" + hexID + "](" + oompID + "/)"
        rv = rv + image + "<br>" + text + "<br>" + hex
        return rv

    def mdLine(self, value):
        values = value.split(",")
        identifier = values[1]
        gitLink = self.getFilename("",resolution="140",relative="github")
        gitImage = self.getFilename("image",resolution="140",relative="githubRaw")
        oompID = self.getTag("oompID").value
        hexID = self.getTag("hexID").value
        name = self.getTag("name").value
        rv = "<table><tr>"

        rv = rv + "<td>![" + oompID + "](" + gitImage + ")</td>"
        rv = rv + "<td>" + identifier + "</td>"
        rv = rv + "<td>[" + oompID + "<br>" + name + "](" + gitLink + ")</td>"
        rv = rv + "<td>[" + hexID + "](" + gitLink + ")</td>"
        

        rv = rv + "</tr></table>"
        return rv




    ##No longer used
    def mdPage(self,file):
        oompID = item.getTag("oompID").value
        name = item.getTag("name").value
        with MarkdownGenerator(
            # By setting enable_write as False, content of the file is written
            # into buffer at first, instead of writing directly into the file
            # This enables for example the generation of table of contents
            filename=filename, enable_write=False
        ) as doc:
            header = oompID + ">" + name
            doc.addHeader(1, header)

            doc.writeTextLine(f'{doc.addBoldedText("This is just a test.")}')
            doc.addHeader(2, "Second level header.")
            table = [
                {"Column1": "col1row1 data", "Column2": "col2row1 data"},
                {"Column1": "col1row2 data", "Column2": "col2row2 data"},
            ]

            doc.addTable(dictionary_list=table)
            doc.writeTextLine("Ending the document....")

    def mdPageOld(self):        
        oompID = self.getTag("oompID").value
        name = self.getTag("name").value
        rv = ""
        rv = rv + "# " + oompID + " > " + name + "  \n"
        rv = rv + "![" + name + "](image_600.jpg)  \n"
        for x in self.tags:
            rv = rv + "" + x.getMD() + ""
        return rv
    
    def addTag(self,name,value,singleValue=False,noDuplicate=False):
        skip = False
        if noDuplicate:
            tests = self.getTags(name)
            for test in tests:
                if value == test.value:
                    skip = True
        if not skip:        
            singleValueTags = ["hexID"]
            for singleValueTag in singleValueTags:
                if name == singleValueTag:
                    singleValue = True
            if singleValue:
                workingTag = self.getTag(name)
                if workingTag.name == name:
                    workingTag.value = value
                else:  ## if not already there add a new one
                    self.tags.append(oompTag(name,value))
            else:
                self.tags.append(oompTag(name,value))

    def addTagSupplied(self,name,value,tag):
        tag.append(oompTag(name,value))
        return tag


    def removeTag(self,name):
        for x in self.tags:
            if x.name == name:
                self.tags.remove(x)
        pass
    

    def getTag(self,name):
        if name.lower() == "oompid":
            id = ""
            for x in self.tags:
                if x.name.lower() == "oompid":
                    id = x
                if id != "":
                    return id
            else:
                id = self.getTag("oompType").value + "-" +  self.getTag("oompSize").value + "-" +  self.getTag("oompColor").value + "-" +  self.getTag("oompDesc").value + "-" +  self.getTag("oompIndex").value
                self.addTag("oompID",id)
                return(oompTag("oompID", id))
        ###### Footprint Help
        if name.lower() == "oompfootprinttype":
            return self.getTag("oompSize")
        if name.lower() == "oompowner":
            return self.getTag("oompColor")
        if name.lower() == "oomplibrary":
            return self.getTag("oompDesc")            
        if name.lower() == "oompfootprintname":
            return self.getTag("oompIndex")
        if name.lower() == "oompidslashes":
            id = ""
            for x in self.tags:
                if x.name.lower() == "oompidslashes":
                    id = x
                if id != "":
                    return id
            else:
                id = self.getTag("oompType").value + "/" +  self.getTag("oompSize").value + "/" +  self.getTag("oompColor").value + "/" +  self.getTag("oompDesc").value + "/" +  self.getTag("oompIndex").value                
                return(oompTag("oompIDslashes", id))
        elif name == "taxaID":
            id = self.getTag("taxaDomain").value.upper() + "-" + self.getTag("taxaKingdom").value.upper() + "-" + self.getTag("taxaDivision").value.upper() + "-" + self.getTag("taxaClass").value.upper() + "-" + self.getTag("taxaOrder").value.upper() + "-" + self.getTag("taxaFamily").value.upper() + "-" + self.getTag("taxaGenus").value.upper() + "-" + self.getTag("taxaSpecies").value.upper()
            return(oompTag("oompID", id))
        #elif name == "hexID":
        #    hexValue = hex(self.getTag("index").value).replace("0x","").upper()
        #    return(oompTag("hexID",hexValue))
        elif name == "name":
            id = self.getTag("namename").value
            if id == "" or id == "XXXXX":
                name = ""
                #size
                value = getDetailFromCode("size",self.getTag("oompSize").value).name
                if value != "":
                    name = name + value + " "

                #desc
                value = getDetailFromCode("desc",self.getTag("oompDesc").value).name
                if value != "":
                    name = name + value + " "
                    
                #color
                value = getDetailFromCode("color",self.getTag("oompColor").value).name
                if value != "":
                    name = name + value + " "
                    
                #type
                value = getDetailFromCode("type",self.getTag("oompType").value).name
                if value != "":
                    name = name + value + " "
                    
                #index
                value = getDetailFromCode("index",self.getTag("oompIndex").value).name
                if value != "":
                    name = name + value + " "                      

                name = name.strip()
                return(oompTag("name", name))
            else:
                return self.getTag("namename")
        elif name == "footprintFolder":
            folder = getDir("eda") + self.getTag("oompSize").value + "/" + self.getTag("oompSize").value + "/" +  self.getTag("oompColor").value + "/" + self.getTag("oompDesc").value +"/" + self.getTag("oompIndex").value + "/"
            return(oompTag("footprintFolder",folder))
            


        else:
            if name == "namename":
                name = "name"
            for x in self.tags:
                if x.name.lower() == name.lower():
                    return x
            return oompTag("","")

    def getTags(self,tagName):
        rv = []
        if tagName == "allParts":
            oompParts = self.getTags("oompParts")
            rawParts = self.getTags("rawParts")
            for part in oompParts:
                id = part.value.split(",")[0]
                for rpart in rawParts:
                    testid = rpart.value.split(",")[0]
                    if testid == id:
                        rv.append(oompTag("allParts",part.value + "," + rpart.value))
        else:
            for tag in self.tags:
                if tag.name == tagName:
                    rv.append(tag)
        return rv

    def getName(self,br=" "):
        name = self.getTag("oompName").value
        if name == "":
            name = self.getTag("name").value
        return self.getTag("oompID").value + br + name

    
class oompTag:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        if isinstance(self.value, list):
            rv = "oompTagCC " + self.name + "\n"
            for x in self.value:
                rv = rv + "    " + str(x) 
            return rv
        elif isinstance(self.value, oompTag):
            return "     " + self.name + "    \n" + str(self.value) + "\n"
        else:
            return "     " + str(self.name) + " : " + str(self.value)+ "\n"

    def getMD(self):
        if isinstance(self.value, list):
            rv = "oompTagCC " + self.name + "\n"
            for x in self.value:
                rv = rv + "" + str(x) 
            return rv
        elif isinstance(self.value, oompTag):
            return "" + self.name + "  \n" + str(self.value) + "  \n"
        else:
            return "" + str(self.name) + " : " + str(self.value)+ "  \n"

    

    def getPythonLineOld(self):
        v = self.value
        if "QH" in str(v):
            pass
        if isinstance(v,dict) or isinstance(v,list) :
            rv = "newPart.addTag('" + self.name + "'," + str(self.value).replace("\\","") + ")" 
            return rv
        else:
            rv = "newPart.addTag('" + self.name + "','" + str(self.value).replace("'","").replace('"','').replace("\\","") + "')" 
            return rv

    def getValue(self):
        return self.value

class oompDetail:

    def __init__(self, category, code, name, sort="", extra1="", extra2=""):
        self.category = category
        self.code = code
        self.name = name
        self.sort = sort
        self.extra1 = extra1
        self.extra2 = extra2

    def __str__(self):
        return self.category + "   " + self.code  + "   " + self.name  + "   " + self.sort
    
#### import detail lists


    

def loadDirectoryOld02(directory,fileFilter=["details.py"]):
    testing = 1000000000000000000
    for filter in fileFilter:
        files = glob.glob(directory + "**/" + filter,recursive=True)
        for file in files:
            moduleName = file.replace(".py","").replace("\\",".")
            #moduleName = subdir.replace("\\",".") + "." + moduleName
            try:
                __import__(moduleName)    
            except:
                ###### For dealing with folders with a full stop
                sourceFile =  file
                destFile = "sourceFiles/temp/" + str(random.randint(0,999999999)) + ".py"
                moduleName = destFile.replace("\\",".").replace("/",".").replace(".py","")
                shutil.copyfile(sourceFile,destFile)
                time.sleep(0.01)
                __import__(moduleName)   
                os.remove(destFile) 


def loadDirectoryOld(directory,fileFilter="details.py"):
    testing = 1000000000000000000
    #testing = 10000
    #testing = 7000
    #testing = 5000
    #testing = 1000
    skip = ["Pololu_Breakout-16_15.2x20.3mm"]
    count = 0
    for subdir, dirs, files in os.walk(directory):
            if count > testing:
                print("Breaking " + str(count) + " " + str(testing))
                break
            for file in files:
                count = count + 1
                if count > testing:
                    print("Breaking " + str(count) + " " + str(testing))
                    break
                if(fileFilter in file):
                    if skip not in file:
                        moduleName = file.replace(".py","")
                        moduleName = subdir.replace("\\",".") + "." + moduleName
                        ##print("    moduleName: " + moduleName)
                        #print(".",end="")
                        try:
                            __import__(moduleName)    
                        except:
                            ###### For dealing with folders with a full stop
                            sourceFile = subdir + "/" + file
                            destFile = "sourceFiles/temp/" + str(random.randint(0,999999999)) + ".py"
                            moduleName = destFile.replace("\\",".").replace("/",".").replace(".py","")
                            shutil.copyfile(sourceFile,destFile)
                            time.sleep(0.01)
                            __import__(moduleName)   
                            os.remove(destFile) 


#### import parts

def reset():
    global partsFootprints,partsSymbols,partsParts,partsNoFootprints,partsProjects,partsTemplates,details,parts
    
    partsFootprints = oompDict()
    partsSymbols = oompDict()
    partsParts = oompDict()
    partsNoFootprints = oompDict()
    partsProjects = oompDict()
    partsTemplates = oompDict()

    details = oompDetailDict()

    parts = oompDict()

partsFootprints = oompDict()
partsSymbols = oompDict()
partsParts = oompDict()
partsNoFootprints = oompDict()
partsProjects = oompDict()
partsTemplates = oompDict()

details = oompDetailDict()

parts = oompDict()



def load():
    tagNames = {}
    tagDetails = []
    items = {}    
    itemsTypes = {}
    itemsHex = {}

def loadItemTypes():
    global itemsTypes
    tests = {}
    tests["collections"] = ["COLLECTION"]
    tests["eda"] = ["FOOTPRINT","SYMBOL"]
    tests["modules"] = ["BLOCK","MODULE"]
    tests["projects"] = ["PROJECT"]
    tests["parts"]=[]
    for t in tagDetails:
        if t["category"] == "type":
            tests["parts"].append(t["code"])
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


tagNames = {}
tagDetails = []
items = {}
itemsHex = {}
itemsTypes = {}
import OOMP_tag



pass