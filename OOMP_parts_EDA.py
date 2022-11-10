
import OOMP
from oomBase import *
import os

def matchFootprintsSymbols():
    for partID in OOMP.itemsTypes["parts"]["items"]:
        matchFootprint(OOMP.items[partID])
        OOMP.exportTagsItem(OOMP.items[partID],"detailsFootprintsOomp",["footprintEagle","footprintKicad","symbolKicad"]) 
    

def matchFootprint(part):
    #part["footprintEagle"] = []
    #part["footprintKicad"] = []
    #part["symbolEagle"] = []
    #part["symbolKicad"] = []
    dict = {}
    #projectID = project.getID()
    oompID = part["oompID"][0]
    oompType = part["oompType"][0]
    oompSize = part["oompSize"][0]
    oompColor = part["oompColor"][0]
    oompDesc = part["oompDesc"][0]
    oompIndex = part["oompIndex"][0]
    #print("Matching Footprint for: " + "  " + oompID)
    ping()
    if oompID != "----":        
        if oompType == "BUTA":
            addBUTASymbols(part,dict)      
        if oompType == "CAPC":
            addCAPCSymbols(part,dict)        
        if oompType == "HEAD":
            addHEADSymbols(part,dict)    
        if oompType == "LEDS":
            addLEDSSymbols(part,dict)        
        if oompType == "RESE":
            addRESESymbols(part,dict)        
        if oompType == "XTAL":
            addXTALSymbols(part,dict)        
        if "HEAD-I01" in oompID and oompIndex == "01":
            addHEAD01(part,dict)
        if "HEAD-I01" in oompID and oompIndex =="SHRO":
            addHEAD01SHRO(part,dict)
        if "HEAD-I01" in oompID and oompIndex =="SM":
            addHEAD01SM(part,dict)
        if "HEAD-JSTXH" in oompID and oompIndex == "01":
            addHEADJSTXH(part,dict)
        if "HEAD-JSTSH" in oompID and oompIndex == "SM":
            addHEADJSTSH(part,dict)
        if "HEAD-JSTSHR" in oompID and oompIndex == "RS":
            addHEADJSTSH(part,dict)
        if "LEDS-03" in oompID:
            addLEDS03(part,dict)
        if "LEDS-05" in oompID:
            addLEDS05(part,dict)
        if "LEDS-0201" in oompID:
            addLEDS0201(part,dict)
        if "LEDS-0402" in oompID:
            addLEDS0402(part,dict)
        if "LEDS-0603" in oompID:
            addLEDS0603(part,dict)
        if "LEDS-0805" in oompID:
            addLEDS0805(part,dict)
        if "LEDS-1206" in oompID:
            addLEDS1206(part,dict)
        if "XTAL" in oompID:
            addXTAL(part,dict)

        if oompSize == "0402":
            add0402(part,dict)
        if oompSize == "0603":
            add0603(part,dict)
        if oompSize == "0805":
            add0805(part,dict)
        if oompSize == "1206":
            add1206(part,dict)
        if oompSize == "SO8":
            addSO8(part,dict)
        if oompSize == "SO223":
            addSO223(part,dict)
        if oompSize == "SO235":
            addSO235(part,dict)
        if oompSize == "T220":
            addT220(part,dict)
        
        
        
        if oompType == "TERS":
            addTERSSymbols(part,dict)
        if "TERS-35D-" in oompID:
            addTERS35D(part,dict)

    else:
        "    SKIPPING"

#part["footprintEagle", "")
#part["footprintKicad", "")
def add(part,dict):
    oompType = part["oompType"][0]
    tags = []
    tags.append(["footprintEagle", ""])
    for tag in tags:
        part[tag[0]].append(tag[1])
    tags = []
    tags.append(["footprintKicad", ""])
    for tag in tags:
        part[tag[0]].append(tag[1])

def addEdaTags(part,tags):   
    

    #addEdaTags(part=newPart,tags=symbols,type="symbolKicad") 
    for i in tags:        
        type = i[0]
        f = i[1]
        try:
            oompID = OOMP.items[f]
            partID = part["oompID"][0]
            if partID == "LEDS-0603-R-STAN-01":
                pass
            if f not in part[type]:
                part[type].append(f)
            else:
                pass
        except:
            print("footprint not found) " + f )
            #raise Exception("EDA Item not found: " + type + " - " + oompID)        

def add0201(part,dict):
    oompType = part["oompType"][0]
    """
    tags = []
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1W"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1R"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1AW"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1AR"])
    if "RES" in oompType:
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805"])
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805-ARV"])
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805"])
    if "CAP" in oompType:
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Capacitors-0805"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-rc-0805_SENSE"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-rc-0805"])
    for tag in tags:
        part[tag[0]].append(tag[1])
    """
    tags = []
    if "CAP" in oompType:
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0201_0603Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0201_0603Metric_Pad0.64x0.40mm_HandSolder"])
    if "RESE" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0201_0603Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0201_0603Metric_Pad0.64x0.40mm_HandSolder"])   
    addEdaTags(part=part,tags=tags)

def add0402(part,dict):
    oompType = part["oompType"][0]
    """
    tags = []
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1W"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1R"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1AW"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1AR"])
    if "RES" in oompType:
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805"])
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805-ARV"])
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805"])
    if "CAP" in oompType:
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Capacitors-0805"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-rc-0805_SENSE"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-rc-0805"])
    for tag in tags:
        part[tag[0]].append(tag[1])
    """
    tags = []
    if "CAP" in oompType:
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0402_1005Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0402_1005Metric_Pad0.74x0.62mm_HandSolder"])
    if "RESE" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0402_1005Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0402_1005Metric_Pad0.72x0.64mm_HandSolder"])   
    addEdaTags(part=part,tags=tags)

def add0603(part,dict):
    oompType = part["oompType"][0]
    """
    tags = []
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1W"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1R"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1AW"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1AR"])
    if "RES" in oompType:
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805"])
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805-ARV"])
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805"])
    if "CAP" in oompType:
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Capacitors-0805"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-rc-0805_SENSE"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-rc-0805"])
    for tag in tags:
        part[tag[0]].append(tag[1])
    """
    tags = []
    if "CAP" in oompType:
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0603_1608Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0603_1608Metric_Pad1.08x0.95mm_HandSolder"])    
    if "RESE" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0603_1608Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0603_1608Metric_Pad0.98x0.95mm_HandSolder"])   
    addEdaTags(part=part,tags=tags)

def add0805(part,dict):
    oompType = part["oompType"][0]
    tags = []
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1W"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1R"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1AW"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1AR"])
    if "RES" in oompType:
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805"])
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805-ARV"])
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805"])        
    if "CAP" in oompType:
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Capacitors-0805"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-rc-0805_SENSE"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-rc-0805"])
    addEdaTags(part=part,tags=tags)
    tags = []
    if "CAP" in oompType:
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0805_2012Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0805_2012Metric_Pad1.18x1.45mm_HandSolder"])
    if "RESE" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0805_2012Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0805_2012Metric_Pad1.18x1.45mm_HandSolder"])   
    addEdaTags(part=part,tags=tags)

def add1206(part,dict):
    oompType = part["oompType"][0]
    """
    tags = []
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1W"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1R"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1AW"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1AR"])
    if "RES" in oompType:
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805"])
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805-ARV"])
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805"])
    if "CAP" in oompType:
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Capacitors-0805"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-rc-0805_SENSE"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-rc-0805"])
    for tag in tags:
        part[tag[0]].append(tag[1])
    """
    tags = []
    if "CAP" in oompType:
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_1206_3216Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_1206_3216Metric_Pad1.33x1.80mm_HandSolder"])           
    if "RESE" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_1206_3216Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_1206_3216Metric_Pad1.30x1.75mm_HandSolder"])   
    addEdaTags(part=part,tags=tags)

def addSO8(part,dict):
    tags = []
    tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Package_SO-SO-8_3.9x4.9mm_P1.27mm"])
    addEdaTags(part=part,tags=tags)

def addSO223(part,dict):
    tags = []
    tags.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-SOT-223-3_TabPin2"])
    addEdaTags(part=part,tags=tags)

def addSO235(part,dict):
    tags = []
    tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-SOT-23-5"])
    tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-SOT-23-5_HandSoldering"])
    addEdaTags(part=part,tags=tags)

def addT220(part,dict):
    tags = []
    tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_THT-TO-220-3_Vertical"])
    addEdaTags(part=part,tags=tags)


def addBUTASymbols(part,dict):
    tags = []
    tags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Switch-SW_Push"])
    

    addEdaTags(part=part,tags=tags)


def addCAPCSymbols(part,dict):
    tags = []
    tags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Device-C"])
    

    addEdaTags(part=part,tags=tags)



def addHEADSymbols(part,dict):
    newPart = part
    oompDesc = part["oompDesc"][0]
    pinss = oompDesc.replace("PI2X","")
    pinss = pinss.replace("PI","")
    if pinss.isnumeric():
        if "PI2X" in oompDesc:
                ###### FOOTPRINTS
                symbols = []
                
                #symbols.append("SYMBOL-kicad-kicad-symbols-Connector_Generic-DIN41612_02x" + pinss + "_AB")
                base = "SYMBOL-kicad-kicad-symbols-Connector_Generic-Conn_02x" + pinss
                symbols.append(["symbolKicad",base  + "_Odd_Even"])
                symbols.append(["symbolKicad",base  + "_Row_Letter_First"])
                symbols.append(["symbolKicad",base  + "_Row_Letter_Last"])
                symbols.append(["symbolKicad",base  + "_Counter_Clockwise"])
                symbols.append(["symbolKicad",base  + "_Top_Bottom"])
                symbols.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Connector-Conn_01x" + str(int(pinss)*2).zfill(2) + "_Male"])
                addEdaTags(part=newPart,tags=symbols)
                    
        else:
            symbols = []
            symbols.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Connector-Conn_01x" + pinss + "_Male"])
            symbols.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Connector_Generic-Conn_01x" + pinss + ""])
            addEdaTags(part=newPart,tags=symbols)


def addLEDSSymbols(part,dict):

    tags = []
    tags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Device-LED"])
    addEdaTags(part=part,tags=tags)


def addRESESymbols(part,dict):
    
    tags = []
    tags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Device-R"])
    addEdaTags(part=part,tags=tags)


def addXTALSymbols(part,dict):
    tags = []
    tags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Device-Crystal"])
    addEdaTags(part=part,tags=tags)



def addHEAD01(part,dict):
    oompID = part["oompID"][0]
    oompDesc = part["oompDesc"][0]
    if "PI2X" not in oompID:
        pinss = oompDesc.replace("PI","")
        newPart = part
        if pinss.isnumeric():
            ###### FOOTPRINTS
            ##newPart["kicadFootprint","Connector_PinHeader_2.54mm/PinHeader_1x" + pinss + "_P2.54mm_Vertical")
            ######  Sparkfun footprints
            sparkfunStyles = ["", "_BIG", "_LOCK", "_LOCK_LONGPADS", "_NO_SILK", "_PP_HOLES_ONLY"]
            for style in sparkfunStyles: 
                imageFile = "oomlout_OOMP_eda/FOOTPRINT/eagle/SparkFun-Eagle-Libraries/Sparkfun-Connectors/1X" + pinss + style + "/image.png"
                #print("Image File: " + imageFile)
                if os.path.isfile(imageFile):
                    addEdaTags(newPart,["footprintEagle","FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-1X" + pinss + style])
            
            
            adafruitStyles = ["", "-CLEANBIG", "-BIGLOCK", "-CLEAN", "-LOCK", "-CB"]
            for style in adafruitStyles: 
                imageFile = "oomlout_OOMP_eda/FOOTPRINT/eagle/Adafruit-Eagle-Library/adafruit/1X" + pinss + style + "/image.png"
                #print("Image File: " + imageFile)
                if os.path.isfile(imageFile):
                    addEdaTags(newPart,["footprintEagle","FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-1X" + pinss + style])
            
            
            pimoroniStyles = ["","-0.1&quot;-CASTELLATED-BCREAM", "-0.1&quot;-CASTELLATED-BIGGER-ROUNDED", "-0.1&quot;-CASTELLATED-BIGGER", "-0.1&quot;-CASTELLATED", "-LOCK-MALE", "-CB","_LONGPADS"]
            for style in pimoroniStyles: 
                imageFile = "oomlout_OOMP_eda/FOOTPRINT/eagle/Pimoroni-Eagle-Library/pimoroni-headers/1X" + pinss.replace("0","") + style + "/image.png"
                #print("Image File: " + imageFile)
                if os.path.isfile(imageFile):
                    addEdaTags(newPart["footprintEagle","FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-headers-1" + pinss + style])
            
            addEdaTags(newPart,["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Connector_PinHeader_2.54mm-PinHeader_1x" + pinss + "_P2.54mm_Vertical"])
    else:
        pinss = oompDesc.replace("PI2X","")
        newPart = part
        if pinss.isnumeric():
            footprints = []
            base = "FOOTPRINT-kicad-kicad-footprints-Connector_PinHeader_2.54mm-PinHeader_2x" + pinss
            footprints.append(["footprintKicad", base + "_P2.54mm_Vertical"])

            addEdaTags(part=newPart,tags=footprints)
            

def addHEAD01SHRO(part,dict):
    oompDesc = part["oompDesc"][0]
    pinss = oompDesc.replace("PI2X","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_IDC-IDC-Header_2x" + pinss
        #footprints.append(base + "_P2.54mm_Horizontal")
        footprints.append(["footprintKicad",base + "_P2.54mm_Vertical"])
        addEdaTags(part=newPart,tags=footprints)

def addHEAD01SM(part,dict):
    oompDesc = part["oompDesc"][0]
    pinss = oompDesc.replace("PI2X","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_PinHeader_2.54mm-PinHeader_2x" + pinss
        footprints.append(["footprintKicad",base + "_P2.54mm_Vertical_SMD"])
        addEdaTags(part=newPart,tags=footprints)

def addHEADJSTSH(part,dict):
    oompDesc = part["oompDesc"][0]
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        #FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_SH_BM04B-SRSS-TB_1x04-1MP_P1.00mm_Vertical
        #JST_SH_BM04B-SRSS-TB_1x04-1MP_P1.00mm_Vertical
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_SH_BM" + pinss + "B-SRSS-TB_1x" + pinss + "-1MP_P1.00mm_Vertical"
        footprints.append(["footprintKicad",base])
        addEdaTags(part,footprints)



def addHEADJSTSHR(part,dict):
    oompDesc = part["oompDesc"][0]
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        #FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_SH_SM04B-SRSS-TB_1x04-1MP_P1.00mm_Horizontal
        
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_SH_SM" + pinss + "B-SRSS-TB_1x" + pinss + "-1MP_P1.00mm_Horizontal"
        footprints.append(["footprintKicad",base])
        addEdaTags(part,footprints)



def addLEDS03(part,dict):
    oompDesc = part["oompDesc"][0]
    newPart = part
    footprints = []
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D3.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D3.0mm_Horizontal_O1.27mm_Z6.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D3.0mm_Horizontal_O1.27mm_Z10.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D3.0mm_Horizontal_O3.81mm_Z2.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D3.0mm_Horizontal_O3.81mm_Z6.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D3.0mm_Horizontal_O3.81mm_Z10.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D3.0mm_Horizontal_O6.35mm_Z2.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D3.0mm_Horizontal_O6.35mm_Z6.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D3.0mm_Horizontal_O6.35mm_Z10.0mm"])
    addEdaTags(part,footprints)

def addLEDS05(part,dict):
    oompDesc = part["oompDesc"][0]
    footprints = []
    newPart = part
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D5.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D5.0mm_Horizontal_O1.27mm_Z3.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D5.0mm_Horizontal_O1.27mm_Z9.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D5.0mm_Horizontal_O1.27mm_Z15.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D5.0mm_Horizontal_O3.81mm_Z3.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D5.0mm_Horizontal_O3.81mm_Z9.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D5.0mm_Horizontal_O3.81mm_Z15.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D5.0mm_Horizontal_O6.35mm_Z3.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D5.0mm_Horizontal_O6.35mm_Z9.0mm"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D5.0mm_Horizontal_O6.35mm_Z15.0mm"])
    addEdaTags(part,footprints)

def addLEDS0201(part,dict):
    oompDesc = part["oompDesc"][0]
    footprints = []
    newPart = part
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0201_0603Metric"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0201_0603Metric_Pad0.64x0.40mm_HandSolder"])
    addEdaTags(part,footprints)

def addLEDS0402(part,dict):
    oompDesc = part["oompDesc"][0]
    footprints = []
    newPart = part  
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0402_1005Metric"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0402_1005Metric_Pad0.77x0.64mm_HandSolder"])
    addEdaTags(part,footprints)

def addLEDS0603(part,dict):
    oompDesc = part["oompDesc"][0]
    footprints = []
    newPart = part
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0603_1608Metric"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0603_1608Metric_Pad1.05x0.95mm_HandSolder"])
    addEdaTags(part,footprints)

def addLEDS0805(part,dict):
    oompDesc = part["oompDesc"][0]
    footprints = []
    newPart = part
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0805_2012Metric"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0805_2012Metric_Pad1.15x1.40mm_HandSolder"])
    addEdaTags(part,footprints)

def addLEDS1206(part,dict):
    oompDesc = part["oompDesc"][0]
    footprints = []
    newPart = part
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_1206_3216Metric"])
    footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder"])
    addEdaTags(part,footprints)

def addXTAL(part,dict):
    oompSize = part["oompSize"][0]
    footprints = []
    if oompSize == "HC49":
        footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Crystal-Crystal_HC49-4H_Vertical"])
    elif oompSize == "HC49S":
        footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Crystal-Crystal_SMD_HC49-SD"])
        footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Crystal-Crystal_SMD_HC49-SD_HandSoldering"])
    elif oompSize == "5032":
        footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Crystal-Crystal_SMD_5032-2Pin_5.0x3.2mm"])
        footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Crystal-Crystal_SMD_5032-2Pin_5.0x3.2mm_HandSoldering"])
    elif oompSize == "3225P4":
        footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Crystal-Crystal_SMD_3225-4Pin_3.2x2.5mm"])
        footprints.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Crystal-Crystal_SMD_3225-4Pin_3.2x2.5mm_HandSoldering"])    
    addEdaTags(part,footprints)


def addHEADJSTXH(part,dict):
    oompDesc = part["oompDesc"][0]
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        #FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_XH_B10B-XH-AM_1x10_P2.50mm_Vertical
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_XH_B" + str(int(pinss)) + "B-XH-AM_1x" + pinss
        footprints.append(["footprintKicad",base + "_P2.50mm_Vertical"])
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_XH_B" + str(int(pinss)) + "B-XH-A_1x" + pinss
        footprints.append(["footprintKicad",base + "_P2.50mm_Vertical"])
        addEdaTags(part,footprints)


def addTERSSymbols(part,dict):
    oompDesc = part["oompDesc"][0]
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        ###### FOOTPRINTS
        symbols = []
        base = "SYMBOL-kicad-kicad-symbols-Connector-Screw_Terminal_01x" + pinss
        symbols.append(["symbolKicad",base])
        addEdaTags(part,symbols)
        

def addTERS35D(part,dict):
    oompDesc = part["oompDesc"][0]
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        base = "FOOTPRINT-kicad-kicad-footprints-TerminalBlock_4Ucon-TerminalBlock_4Ucon_1x" + pinss
        footprints.append(["footprintKicad",base + "_P3.50mm_Vertical"])
        addEdaTags(part,footprints)
        
