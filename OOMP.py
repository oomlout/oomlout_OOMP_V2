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

def getNameDisplay(item,br="\n"):
    return getDisplayName(item,br=br)

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
        rv = rv + item["oompType"][0] + "/" +  item["oompSize"][0] + "/" + item["oompColor"][0] + "/" +  item["oompDesc"][0] + "/" +  item["oompIndex"][0] + "/"
        rv = rv + extraBack
    


    return extraFront + rv

def getFileItem(item,file,resolution="",extension="",relative=""):
    if item != "":
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
        if file == "image":
            typ = getType(item)                
            if typ == "eda":
                rv = rv.replace(".jpg",".png")

        rv = getDirItem(item,relative) + rv
        return rv
    else:
        return ""

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
    if item != "":
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
    else:
        return ""

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

def makePickle(exclusions=True):
    print("Making Pickle:")
    start = time.time()
    reload()
    copyAllFiles(exclusions=exclusions)
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

def copyAllFiles(exclusions = True):
    exclusionList = getExclusionList()
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
                include = True
                if exclusions:
                    for exclusion in exclusionList:
                        if exclusion in file:
                            include = False
                            break
                if include:
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

def getExclusionList():
    rv = []
    rv.append("digikey-footprints\\")
    rv.append("kicad-symbols\\")
    rv.append("kicad-footprints\\Audio_Module")
    rv.append("kicad-footprints\\Audio_Module")
    rv.append("kicad-footprints\\Batteryrv.append")
    rv.append("kicad-footprints\\Button_Switch_Keyboard")
    #rv.append("kicad-footprints\\Button_Switch_SMD")
    #rv.append("kicad-footprints\\Button_Switch_THT")
    rv.append("kicad-footprints\\Buzzer_Beeper")
    rv.append("kicad-footprints\\Calibration_Scale")
    #rv.append("kicad-footprints\\Capacitor_SMD")
    #rv.append("kicad-footprints\\Capacitor_THT")
    #rv.append("kicad-footprints\\Capacitor_Tantalum_SMD")
    #rv.append("kicad-footprints\\Connector")
    rv.append("kicad-footprints\\Connector_AMASS")
    rv.append("kicad-footprints\\Connector_Amphenol/Amphenol_M8S-03PMMR-SF8001")
    #rv.append("kicad-footprints\\Connector_Audio")
    #rv.append("kicad-footprints\\Connector_BarrelJack")
    rv.append("kicad-footprints\\Connector_Card")
    rv.append("kicad-footprints\\Connector_Coaxial")
    rv.append("kicad-footprints\\Connector_DIN")
    rv.append("kicad-footprints\\Connector_Dsub")
    rv.append("kicad-footprints\\Connector_FFC-FPC")
    rv.append("kicad-footprints\\Connector_HDMI")
    rv.append("kicad-footprints\\Connector_Harting")
    rv.append("kicad-footprints\\Connector_Harwin")
    rv.append("kicad-footprints\\Connector_Hirose")
    #rv.append("kicad-footprints\\Connector_IDC")
    rv.append("kicad-footprints\\Connector_JAE")
    #rv.append("kicad-footprints\\Connector_JST")
    #rv.append("kicad-footprints\\Connector_Molex")
    rv.append("kicad-footprints\\Connector_PCBEdge")
    rv.append("kicad-footprints\\Connector_Phoenix_GMSTB")
    rv.append("kicad-footprints\\Connector_Phoenix_MC")
    rv.append("kicad-footprints\\Connector_Phoenix_MC_HighVoltage")
    rv.append("kicad-footprints\\Connector_Phoenix_MSTB")
    #rv.append("kicad-footprints\\Connector_Pin")
    rv.append("kicad-footprints\\Connector_PinHeader_1.00mm")
    rv.append("kicad-footprints\\Connector_PinHeader_1.27mm")
    rv.append("kicad-footprints\\Connector_PinHeader_2.00mm")
    #rv.append("kicad-footprints\\Connector_PinHeader_2.54mm")
    rv.append("kicad-footprints\\Connector_PinSocket_1.00mm")
    rv.append("kicad-footprints\\Connector_PinSocket_1.27mm")
    rv.append("kicad-footprints\\Connector_PinSocket_2.00mm")
    #rv.append("kicad-footprints\\Connector_PinSocket_2.54mm")
    rv.append("kicad-footprints\\Connector_RJ")
    rv.append("kicad-footprints\\Connector_SATA_SAS")
    rv.append("kicad-footprints\\Connector_Samtec")
    rv.append("kicad-footprints\\Connector_Samtec_HLE_SMD")
    rv.append("kicad-footprints\\Connector_Samtec_HLE_THT")
    rv.append("kicad-footprints\\Connector_Stocko")
    rv.append("kicad-footprints\\Connector_TE-Connectivity")
    #rv.append("kicad-footprints\\Connector_USB")
    rv.append("kicad-footprints\\Connector_Wago")
    rv.append("kicad-footprints\\Connector_Wire")
    rv.append("kicad-footprints\\Connector_Wuerth")
    rv.append("kicad-footprints\\Converter_ACDC")
    rv.append("kicad-footprints\\Converter_DCDC")
    #rv.append("kicad-footprints\\Crystal")
    #rv.append("kicad-footprints\\Diode_SMD")
    #rv.append("kicad-footprints\\Diode_THT")
    rv.append("kicad-footprints\\Display")
    rv.append("kicad-footprints\\Display_7Segment")
    rv.append("kicad-footprints\\Ferrite_THT/LairdTech_28C0236-0JW-10")
    rv.append("kicad-footprints\\Fiducial")
    rv.append("kicad-footprints\\Filter")
    rv.append("kicad-footprints\\Fuse")
    rv.append("kicad-footprints\\Heatsink")
    rv.append("kicad-footprints\\Inductor_SMD")
    rv.append("kicad-footprints\\Inductor_THT")
    rv.append("kicad-footprints\\Jumper")
    #rv.append("kicad-footprints\\LED_SMD")
    #rv.append("kicad-footprints\\LED_THT")
    rv.append("kicad-footprints\\Module")
    rv.append("kicad-footprints\\Motors/Vybronics_VZ30C1T8219732L")
    rv.append("kicad-footprints\\MountingEquipment/DINRailAdapter_3xM3_PhoenixContact_1201578")
    rv.append("kicad-footprints\\MountingHole")
    rv.append("kicad-footprints\\Mounting_Wuerth")
    rv.append("kicad-footprints\\NetTie")
    #rv.append("kicad-footprints\\OptoDevice")
    rv.append("kicad-footprints\\Oscillator")
    rv.append("kicad-footprints\\Package_BGA")
    rv.append("kicad-footprints\\Package_CSP")
    #rv.append("kicad-footprints\\Package_DFN_QFN")
    #rv.append("kicad-footprints\\Package_DIP")
    #rv.append("kicad-footprints\\Package_DirectFET")
    rv.append("kicad-footprints\\Package_LCC")
    #rv.append("kicad-footprints\\Package_LGA")
    rv.append("kicad-footprints\\Package_QFP")
    #rv.append("kicad-footprints\\Package_SIP")
    #rv.append("kicad-footprints\\Package_SO")
    #rv.append("kicad-footprints\\Package_SON")
    #rv.append("kicad-footprints\\Package_SO_J-Lead/TSOC-6_3.76x3.94mm_P1.27mm")
    #rv.append("kicad-footprints\\Package_TO_SOT_SMD")
    #rv.append("kicad-footprints\\Package_TO_SOT_THT")
    #rv.append("kicad-footprints\\Potentiometer_SMD")
    #rv.append("kicad-footprints\\Potentiometer_THT")
    rv.append("kicad-footprints\\RF")
    rv.append("kicad-footprints\\RF_Antenna")
    rv.append("kicad-footprints\\RF_Converter")
    rv.append("kicad-footprints\\RF_GPS")
    rv.append("kicad-footprints\\RF_GSM")
    rv.append("kicad-footprints\\RF_Mini-Circuits")
    rv.append("kicad-footprints\\RF_Module")
    rv.append("kicad-footprints\\RF_Shielding")
    rv.append("kicad-footprints\\RF_WiFi/USR-C322")
    rv.append("kicad-footprints\\Relay_SMD")
    rv.append("kicad-footprints\\Relay_THT")
    #rv.append("kicad-footprints\\Resistor_SMD")
    #rv.append("kicad-footprints\\Resistor_THT")
    rv.append("kicad-footprints\\Rotary_Encoder")
    #rv.append("kicad-footprints\\Sensor")
    rv.append("kicad-footprints\\Sensor_Audio")
    rv.append("kicad-footprints\\Sensor_Current")
    rv.append("kicad-footprints\\Sensor_Distance/ST_VL53L1x")
    #rv.append("kicad-footprints\\Sensor_Humidity")
    #rv.append("kicad-footprints\\Sensor_Motion")
    #rv.append("kicad-footprints\\Sensor_Pressure")
    rv.append("kicad-footprints\\Sensor_Voltage/LEM_LV25-P")
    rv.append("kicad-footprints\\Socket")
    rv.append("kicad-footprints\\Symbol")
    rv.append("kicad-footprints\\TerminalBlock")
    #rv.append("kicad-footprints\\TerminalBlock_4Ucon")
    rv.append("kicad-footprints\\TerminalBlock_Altech")
    rv.append("kicad-footprints\\TerminalBlock_Dinkle")
    rv.append("kicad-footprints\\TerminalBlock_MetzConnect")
    rv.append("kicad-footprints\\TerminalBlock_Philmore")
    #rv.append("kicad-footprints\\TerminalBlock_Phoenix")
    rv.append("kicad-footprints\\TerminalBlock_RND")
    rv.append("kicad-footprints\\TerminalBlock_TE-Connectivity")
    rv.append("kicad-footprints\\TerminalBlock_WAGO")
    rv.append("kicad-footprints\\TerminalBlock_Wuerth")
    rv.append("kicad-footprints\\TestPoint")
    rv.append("kicad-footprints\\Transformer_SMD")
    rv.append("kicad-footprints\\Transformer_THT")
    rv.append("kicad-footprints\\Transistor_Power_Module")
    rv.append("kicad-footprints\\Valve")
    rv.append("kicad-footprints\\Varistor")

    rv = [""]

    return rv