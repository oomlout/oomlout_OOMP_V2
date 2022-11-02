from this import d
import OOMP
import OOMP_hex_FOOTPRINTS
import OOMP_footprints_BASE
from oomBase import *

import glob
import os

from kiutils.footprint import Footprint

def createFootprints():
    print("Creating Eagle Footprints")
    #owners = ["digikey-kicad-library"]
    for git in OOMP_footprints_BASE.footprintGits:
        if OOMP_footprints_BASE.footprintGits[git]["type"] == "eagle":
            owner = OOMP_footprints_BASE.footprintGits[git]["code"]
            print("    Creating for: " + owner)
            print("        Getting Names")
            footprints = getEagleFootprintNames(owner)        
            print("        Making Footprints")
            for footprint in footprints: 
                d = {}
                d["oompType"] =  "FOOTPRINT"
                d["oompSize"] =  "eagle"
                d["oompColor"] =  owner
                d["oompDesc"] =  footprint[0]
                d["oompIndex"] =  footprint[1]
                d["name"] =  footprint[1]
                d["FOOTPRINT"] = footprint
                oompID = d["oompType"] + "-" + d["oompSize"] + "-" + d["oompColor"] + "-" + d["oompDesc"] + "-" + d["oompIndex"]
                d["hexID"] = OOMP_hex_FOOTPRINTS.getFootprintHex(oompID)
                #loadFootprintDict(d)            
                ###### Make required folders
                if True:
                    directory = OOMP.getDir("eda") + "FOOTPRINT/eagle/" +owner
                    oomMakeDir(directory)
                    directory = OOMP.getDir("eda") + "FOOTPRINT/eagle/" + owner + "/" + footprint[0]
                    oomMakeDir(directory)
                ###### Copy source footprint to OOMP directory
                OOMP_footprints_BASE.makeFootprint(d)
        

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
    originalDict["hexID"] = OOMP_hex_FOOTPRINTS.getFootprintHex(oompID)

    ####### fix typo in digikey 603 footprint
    if originalDict["oompIndex"] == "603" and "digikey" in oompID.lower():
        originalDict["oompIndex"] = "0603"
    if originalDict["oompIndex"] == "402" and "digikey" in oompID.lower():
        originalDict["oompIndex"] = "0402"
    if originalDict["oompIndex"] == "805" and "digikey" in oompID.lower():
        originalDict["oompIndex"] = "0805"


    return originalDict

def getEagleFootprintNames(owner):
    footprints = []
    directory = "sourceFiles/git/eagleFootprints/" + owner
    files = glob.glob(directory + "**\\*.lbr",recursive=True)
    for file in files:        
        f = open(file, encoding='utf-8',mode="r")
        fileContents = f.read()
        lines = fileContents.splitlines()
        for line in lines:
            if "<package name=" in line:
                footprint = stringBetween(line,'<package name="','"').replace('"',"").replace("/","_")
                fileToken = os.path.basename(file).replace(".lbr","")
                footprints.append([fileToken,footprint])
    return footprints

def getKicadFootprintNames(owner):
    directory = "sourceFiles/git/kicadFootprints/" + owner + "/"    
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
                        footprints.append([subdir.replace(".pretty","").replace("sourceFiles/git/kicadFootprints/" +owner + "/",""),foot])
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

