import os
import time
import json
from oomBase import *

import importlib

baseDir = ""

def getPythonLine(part="newPart",tagName="",tagValue="",indent="    "):  
    if isinstance(tagValue,dict) or isinstance(tagValue,list) :
        rv = indent + part + "['" + tagName + "'].append(" + str(tagValue).replace("\\","") + ")" 
    else:     
        rv = indent +  part + "['" + tagName + "'].append('" + str(tagValue) + "')"     
    return rv
    
def preloadItem(newPart):
    for tag in tagNames:
        newPart[tagNames[tag]["code"]] = []
    return newPart

def getDir(type, base=False):
    global baseDir
    rv = ""
    if base:
        rv = baseDir
    for t in repos:    
        if type.lower() == t:
            rv = rv + "oomlout_OOMP_" + t + "_V2/"
    return rv

def setBaseDir(base):
    global baseDir
    baseDir = base 
    baseDir = "C:/GH/oomlout_OOMP_V2/"

def getID(self):
    return self.getTag("oompID").value
def getName(self):
    return self.getTag("name").value
def getType(self):
    return self.getTag("oompType").value
def getHex(self):
    return self.getTag("hexID").value


##############################################################################
##############################################################################
##############################################################################
######  LOADING ROUTINES

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
            newPart = mod.load(newPart)
            items[newPart["oompID"][0]] = newPart
            itemsHex[newPart["hexID"][0]] = newPart
            #importlib.reload(mod)

def makePythonSafe(string):
    rv = string
    rv = rv.replace("-","_").replace(".","_")
    return rv


def getReport(startTime=""):
    rv = ""   
    rv = rv + "Number of Items: "+ str(len(items)) + "\n"
    for r in repos:
        rv = rv + "Number of " + r + ": "+ str(len(itemsTypes[r]["items"])) + "\n"
    if startTime != "":
        rv = rv + "Time to execute: " + str(round(time.process_time()-startTime)) + " sec"
    return rv

######### OLD


#def oompAddDetail(category,code,name,sort="",extra1="",extra2=""):
#    details.append(oompDetail(category,code,name,sort,extra1="",#extra2=""))

def getDetailFromCode(category,code):
    pass

def getDetailsCategory(category=""):
    pass

class oompItem:

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

tagNames = {}
tagDetails = {}
items = {}
itemsHex = {}
itemsTypes = {}

import OOMP_tag
