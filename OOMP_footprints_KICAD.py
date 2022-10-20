from this import d
import OOMP
import OOMPtags #### hex for footprint
import OOMP_footprints_BASE
from oomBase import *

import glob
import os

from kiutils.footprint import Footprint

###### kicad mousepoints
X = 0
Y = 0
kicadActive =[515,14]
kicadFootprintFilter =[145,114]
kicadFootprintFirstResult = [145,185]
kicadFootprintMiddle = [945,545] 
kicadFootprintMiddlePlus = [950,550] 
kicadFootprintTopLeft = [365,86] 
kicadSymbolMiddle = [1105,555] 
kicadSymbolMiddlePlus = [1110,560] 

kicadFile = [80,35]
kicad3dView = [145,35]


kicadLibraryTop = [210,115]


def createFootprints():
    print("Creating Kicad Footprints")
    #owners = ["digikey-kicad-library"]
    for git in OOMP_footprints_BASE.footprintGits:
        
        owner = OOMP_footprints_BASE.footprintGits[git]["code"]
        print("    Creating for: " + owner)
        print("        Getting Names")
        footprints = getKicadFootprintNames(owner)        
        print("        Making Footprints")
        for footprint in footprints: 
            d = {}
            d["oompType"] =  "FOOTPRINT"
            d["oompSize"] =  "kicad"
            d["oompColor"] =  owner
            d["oompDesc"] =  footprint[0]
            d["FOOTPRINT"] = footprint[1]
            loadFootprintDict(d)            
            directory = OOMP.getDir("eda") + "FOOTPRINT/kicad/" +owner
            oomMakeDir(directory)
            directory = OOMP.getDir("eda") + "FOOTPRINT/kicad/" + owner + "/" + footprint[0]
            oomMakeDir(directory)
            sourceFootprint = "sourceFiles/git/kicadStuff/" + owner + "/" + footprint[0] + ".pretty/" + d["oompIndex"] +".kicad_mod"
            destDir = OOMP.getDir("eda") + "FOOTPRINT/kicad/" + owner + "/" + footprint[0] + "/" +  d["oompIndex"] + "/"
            oomMakeDir(destDir)
            destFile = destDir + "footprint.kicad_mod"
            oomCopyFile(sourceFootprint,destFile)
            makeFootprint(d)
    

def makeFootprint(d):
    type = d["oompType"]
    size = d["oompSize"]
    color = d["oompColor"]
    desc = d["oompDesc"]   
    index = d["oompIndex"]

    hexID = d["hexID"]

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index

    #print("    Making Footprint")
    ping()

    oompSlashes = type + "/" + size + "/" + color + "/" + desc + "/" + index + "/"

    inputFile = "templates/projectsTemplate.py"
    outputDir = OOMP.getDir("eda") + oompSlashes
    outputFile = outputDir + "details.py"

    #print("Making: " + outputFile)

    contents = oomReadFileToString(inputFile)
    contents = contents.replace("TYPEZZ",type)
    contents = contents.replace("SIZEZZ",size)
    contents = contents.replace("COLORZZ",color)
    contents = contents.replace("DESCZZ",desc)
    contents = contents.replace("INDEXZZ",index)
    contents = contents.replace("HEXZZ",hexID)

    repoName = ""

    skipTags = ["oompType","oompSize","oompColor","oompDesc","oompIndex","FOOTPRINT","hexID"]

    extraTags = []
    for tag in d:
        if tag not in skipTags:
            extraTags.append([tag,d[tag]])        
    tagString = ""
    for tag in extraTags:
        tagString = tagString + OOMP.getPythonLine(tagName=tag[0],tagValue=tag[1]) + "\n"

    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)
    pass

def loadFootprintDict(originalDict):
    
    footprint = originalDict["FOOTPRINT"]
    d = {}
    d["name"] = str(footprint.libraryLink).replace("'","")
    try:
        d["description"] = footprint.description.replace("'","")
    except:
        pass
    d["tags"] = footprint.tags



    attributes = footprint.attributes
    d["attribute" + "Type"] = attributes.type
    
    for model in footprint.models:
        d["threeDModel"] = model.path

    try:
        d["pins"] = {}
        for pad in footprint.pads:
            d["pins"]["type"] = pad.type
            d["pins"]["shape"] = pad.shape
            d["pins"]["position"] = "'"+pad.position+"'"
            d["pins"]["size"] = "'"+pad.size+"'"
    except:
        pass
        #print("        Unable to capture pads")
    

    originalDict["footprintKicadDetails"] = d
    
    originalDict["oompIndex"] = d["name"]

    
    oompID = originalDict["oompType"] + "-" + originalDict["oompSize"] + "-" + originalDict["oompColor"] + "-" + originalDict["oompDesc"] + "-" + originalDict["oompIndex"]
    originalDict["hexID"] = OOMPtags.getFootprintHex(oompID)

    ####### fix typo in digikey 603 footprint
    if originalDict["oompIndex"] == "603" and "digikey" in oompID.lower():
        originalDict["oompIndex"] = "0603"
    if originalDict["oompIndex"] == "402" and "digikey" in oompID.lower():
        originalDict["oompIndex"] = "0402"
    if originalDict["oompIndex"] == "805" and "digikey" in oompID.lower():
        originalDict["oompIndex"] = "0805"


    return originalDict

def getKicadFootprintNames(owner):
    directory = "sourceFiles/git/kicadStuff/" + owner + "/"    
    footprints = []
    count = 0
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if not "/src" in subdir: ###### skip source folder
                filename = subdir + "/" + file
                if("kicad_mod" in file and "Obsolete" not in filename):                                
                    #print("Working on File: "  + filename)
                    ping()
                    try:
                        foot = Footprint().from_file(filename)
                        footprints.append([subdir.replace(".pretty","").replace("sourceFiles/git/kicadStuff/" +owner + "/",""),foot])
                    except:
                        print("    ERROR Unable to parse file into kiutils")
                        
                    count = count + 1
                    if count > 1:
                        pass
                        #break  ## For only one file
        if count > 1:
            pass
            #break  ## For only one file
    return footprints    



def harvestFootprints(overwrite=False,copySourceFiles=False,harvestFootprintImages=False):        
    for footprint in OOMP.getItems("footprints"):
        type =  footprint.getTag("oompFootprintType").value
        if type.lower() == "kicad":
            harvestFootprint(footprint,all=True,copySourceFiles=copySourceFiles,harvestFootprintImages=harvestFootprintImages,overwrite=overwrite)

def harvestFootprint(footprint,all=False,copySourceFiles=False,harvestFootprintImages=False,overwrite=False):
    print("Working on: " + footprint.getID())
    if all or copysourceFiles:
        pass
        #copySourceFile(footprint,overwrite)
    if all or harvestFootprintImages:
        harvestKicadFootprint(footprint)


def copySourceFile(footprint,overwrite=False):    
    type =  footprint.getTag("oompFootprintType").value
    destFile = footprint.getFilename("kicadFootprint")
    print("    Copying Footprint Source File")
    if not os.path.exists(destFile) or overwrite:        
        owner = footprint.getTag("oompOwner").value
        library = footprint.getTag("oompLibrary").value
        name = footprint.getTag("oompFootprintName").value
        sourceFile = "sourceFiles/git/" + owner + "/" + library + ".pretty/" + name + ".kicad_mod"

        if os.path.isfile(destFile):
            print("        Deleting: " + destFile)
            os.remove(destFile)
        
        shutil.copyfile(sourceFile, destFile)
    print("       SKIPPING")

def harvestKicadFootprint(footprint,overwrite=False):
    print("    Harvesting files")

    oompID = footprint.getID()
    oompFileName = footprint.getFilename("image",relative="full")
    oompFileName3D = footprint.getFilename("kicadPcb3d",relative="full")
    oompFileName3Dfront = footprint.getFilename("kicadPcb3dFront",relative="full")
    oompFileName3Dback = footprint.getFilename("kicadPcb3dBack",relative="full")
    footprintFilename = footprint.getFilename("kicadFootprint",relative="full")

    #if overwrite or not os.path.isfile(oompFileName) :
    if overwrite or not os.path.isfile(oompFileName3D) :
        shortDelay = 1
        longDelay = 3
        footprintName = footprint.getTag("oompLibrary").value
        footprintDir = footprint.getTag("oompFootprintName").value
        print("Capturing :" + str(footprint))
        oomMouseClick(pos=kicadActive)
        oomDelay(shortDelay)
        ##apply filter
        oomMouseClick(pos=kicadFootprintFilter)
        oomDelay(shortDelay)
        oomSendCtrl("a")
        oomDelay(shortDelay)
        oomSend(footprintName + " " + footprintDir)
        oomDelay(longDelay)
        oomMouseDoubleClick(pos=kicadFootprintFirstResult)
        oomDelay(longDelay)
        #### Discard Changes
        oomSendRight()
        oomDelay(shortDelay)
        oomSendEnter()
        oomDelay(longDelay)
        #### Export PNG
        file = oompFileName.replace("/","\\")
        if not os.path.exists(file):
            oomSendAltKey("f",2)
            oomSend("e",1)
            oomSend("p",2)
            oomSend(file,3)
            oomSendEnter(delay=1)
            oomSend("y",2)
        #### Export Footprint
        file = footprintFilename.replace("/","\\")
        if not os.path.exists(file):        
            oomSendAltKey("f",2)
            oomSend("e",1)
            oomSend("f",2)
            oomSend(file,3)
            oomSendEnter(delay=1)
            oomSend("y",2)
            oomSendEnter(delay=1)
        #### 3d 
        oomMouseClick(pos=[153,36],delay=1)
        oomSendDown(times=2,delay=1)
        oomSendEnter(delay=5)
        oomSendWindowsKey("up")
        ##### raytracing
        if "_BALL" not in oompID.upper() and "_FLG" not in oompID.upper():
            oomSendAltKey("p",1)
            oomSendEnter(2)
            oomDelay(10)
        #### front
        oomSendAltKey("f",2)
        oomSendEnter(delay=1)
        oomSend(oompFileName3Dfront.replace("/","\\"),3)
        oomSendEnter(delay=1)
        oomSend("y",2)
        oomSend("r",2)       
        #### back
        oomMouseClick(pos=[595,60],delay=5)
        oomDelay(10)
        oomSendAltKey("f",2)
        oomSendEnter(delay=1)
        oomSend(oompFileName3Dback.replace("/","\\"),3)
        oomSendEnter(delay=1)
        oomSend("y",2)        
        oomSend("r",2)       
        #### ortho
        #oomMouseClick(pos=[595,60],delay=5)  
        # Needs hotkey setting rotate x clockwise to a, z counter clockwise to d 
        oomSend("aaaa",2)
        # for b in range(0,4):
        #     oomSendAltKey("v",delay=0.5)
        #     oomSendDown(4,delay=1)  
        #     oomSendEnter(delay=1)   
        oomSend("dd",2)
        oomDelay(10)
        # for b in range(0,2):
        #     oomSendAltKey("v",delay=0.5)
        #     oomSendDown(9,delay=1)  
        #     oomSendEnter(delay=1)      
        oomSendAltKey("f",2)
        oomSendEnter(delay=1)
        oomSend(oompFileName3D.replace("/","\\"),3)
        oomSendEnter(delay=1)
        oomSend("y",2)
        ##### close
        oomSendAltKey("f",delay=1)
        oomSendUp(delay=1)
        oomSendEnter(delay=3)







        oomDelay(longDelay)    

        oomDelay(5)
