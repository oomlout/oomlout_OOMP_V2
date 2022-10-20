
import OOMP

import os

def matchFootprintsSymbols():
    for part in OOMP.getItems("parts"):
        matchFootprint(part)
        part.exportTags("detailsFootprintsOomp",["footprintEagle","footprintKicad","symbolKicad"]) 
    

def matchFootprint(part):
    for c in range(0,100):
        part.removeTag("footprintEagle")
        part.removeTag("footprintKicad")        
        part.removeTag("symbolKicad")        
        part.removeTag("symbolEagle")
    dict = {}
    #projectID = project.getID()
    oompID = part.getID()
    oompType = part.getTag("oompType").value
    oompSize = part.getTag("oompSize").value
    oompColor = part.getTag("oompColor").value
    oompDesc = part.getTag("oompDesc").value
    oompIndex = part.getTag("oompIndex").value
    print("Matching Footprint for: " + "  " + oompID)
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
        if oompSize == "0402":
            add0402(part,dict)
        if oompSize == "0603":
            add0603(part,dict)
        if oompSize == "0805":
            add0805(part,dict)
        if oompSize == "1206":
            add1206(part,dict)
        if oompType == "TERS":
            addTERSSymbols(part,dict)
        if "TERS-35D-" in oompID:
            addTERS35D(part,dict)

    else:
        "    SKIPPING"

#part.addTag("footprintEagle", "")
#part.addTag("footprintKicad", "")
def add(part,dict):
    oompType = part.getTag("oompType").value
    tags = []
    tags.append(["footprintEagle", ""])
    for tag in tags:
        part.addTag(tag[0],tag[1],noDuplicate=True)
    tags = []
    tags.append(["footprintKicad", ""])
    for tag in tags:
        part.addTag(tag[0],tag[1],noDuplicate=True)

def addEdaTags(part,type,tags):
    
    
    for f in tags:
        s = OOMP.getPartByID(f)
        oompID = s.getID()
        if oompID != "----":            
            part.addTag(type,f)
        else:
            pass
        #raise Exception("EDA Item not found: " + type + " - " + symbol)        

def add0201(part,dict):
    oompType = part.getTag("oompType").value
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
        part.addTag(tag[0],tag[1],noDuplicate=True)
    """
    tags = []
    if "CAP" in oompType:
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0201_0603Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0201_0603Metric_Pad0.64x0.40mm_HandSolder"])
    if "LEDS" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0201_0603Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0201_0603Metric_Pad0.64x0.40mm_HandSolder"])
    if "RESE" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0201_0603Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0201_0603Metric_Pad0.64x0.40mm_HandSolder"])   
    for tag in tags:
        part.addTag(tag[0],tag[1],noDuplicate=True)

def add0402(part,dict):
    oompType = part.getTag("oompType").value
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
        part.addTag(tag[0],tag[1],noDuplicate=True)
    """
    tags = []
    if "CAP" in oompType:
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0402_1005Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0402_1005Metric_Pad0.74x0.62mm_HandSolder"])
    if "LEDS" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0402_1005Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0402_1005Metric_Pad0.77x0.64mm_HandSolder"])
    if "RESE" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0402_1005Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0402_1005Metric_Pad0.72x0.64mm_HandSolder"])   
    for tag in tags:
        part.addTag(tag[0],tag[1],noDuplicate=True)

def add0603(part,dict):
    oompType = part.getTag("oompType").value
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
        part.addTag(tag[0],tag[1],noDuplicate=True)
    """
    tags = []
    if "CAP" in oompType:
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0603_1608Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0603_1608Metric_Pad1.08x0.95mm_HandSolder"])
    if "LEDS" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0603_1608Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0603_1608Metric_Pad1.05x0.95mm_HandSolder"])
    if "RESE" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0603_1608Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0603_1608Metric_Pad0.98x0.95mm_HandSolder"])   
    for tag in tags:
        part.addTag(tag[0],tag[1],noDuplicate=True)

def add0805(part,dict):
    oompType = part.getTag("oompType").value
    tags = []
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1W"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1R"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1AW"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1AR"])
    if "RES" in oompType:
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805"])
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805-ARV"])
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805"])        
    if "LEDS" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0805_2012Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-LED_SMD-LED_0805_2012Metric_Pad1.15x1.40mm_HandSolder"])
    if "CAP" in oompType:
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Capacitors-0805"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-rc-0805_SENSE"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-rc-0805"])
    for tag in tags:
        part.addTag(tag[0],tag[1],noDuplicate=True)
    tags = []
    if "CAP" in oompType:
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0805_2012Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0805_2012Metric_Pad1.18x1.45mm_HandSolder"])
    if "RESE" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0805_2012Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_0805_2012Metric_Pad1.18x1.45mm_HandSolder"])   
    for tag in tags:
        part.addTag(tag[0],tag[1],noDuplicate=True)

def add1206(part,dict):
    oompType = part.getTag("oompType").value
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
        part.addTag(tag[0],tag[1],noDuplicate=True)
    """
    tags = []
    if "CAP" in oompType:
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_1206_3216Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_1206_3216Metric_Pad1.33x1.80mm_HandSolder"])       
    if "LEDS" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-LED_1206_3216Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder"])
    if "RESE" in oompType:         
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_1206_3216Metric"])
        tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Resistor_SMD-R_1206_3216Metric_Pad1.30x1.75mm_HandSolder"])   
    for tag in tags:
        part.addTag(tag[0],tag[1],noDuplicate=True)


def addBUTASymbols(part,dict):
    part.addTag("symbolKicad","SYMBOL-kicad-kicad-symbols-Switch-SW_Push")

def addCAPCSymbols(part,dict):
    part.addTag("symbolKicad","SYMBOL-kicad-kicad-symbols-Device-C")



def addHEADSymbols(part,dict):
    newPart = part
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI2X","")
    pinss = pinss.replace("PI","")
    if pinss.isnumeric():
        if "PI2X" in oompDesc:
                ###### FOOTPRINTS
                symbols = []
                
                #symbols.append("SYMBOL-kicad-kicad-symbols-Connector_Generic-DIN41612_02x" + pinss + "_AB")
                base = "SYMBOL-kicad-kicad-symbols-Connector_Generic-Conn_02x" + pinss
                symbols.append(base  + "_Odd_Even")
                symbols.append(base  + "_Row_Letter_First")
                symbols.append(base  + "_Row_Letter_Last")
                symbols.append(base  + "_Counter_Clockwise")
                symbols.append(base  + "_Top_Bottom")
                symbols.append("SYMBOL-kicad-kicad-symbols-Connector-Conn_01x" + str(int(pinss)*2).zfill(2) + "_Male")
                for symbol in symbols:
                    ###### TODO add a check for existance
                    addEdaTags(part=newPart,tags=symbols,type="symbolKicad")
                    
        else:
            newPart.addTag("symbolKicad","SYMBOL-kicad-kicad-symbols-Connector-Conn_01x" + pinss + "_Male")
            newPart.addTag("symbolKicad","SYMBOL-kicad-kicad-symbols-Connector_Generic-Conn_01x" + pinss + "")


def addLEDSSymbols(part,dict):
    part.addTag("symbolKicad","SYMBOL-kicad-kicad-symbols-Device-LED")

def addRESESymbols(part,dict):
    part.addTag("symbolKicad","SYMBOL-kicad-kicad-symbols-Device-R")


def addHEAD01(part,dict):
    oompID = part.getID()
    oompDesc = part.getTag("oompDesc").value
    if "PI2X" not in oompID:
        pinss = oompDesc.replace("PI","")
        newPart = part
        if pinss.isnumeric():
            ###### FOOTPRINTS
            ##newPart.addTag("kicadFootprint","Connector_PinHeader_2.54mm/PinHeader_1x" + pinss + "_P2.54mm_Vertical")
            ######  Sparkfun footprints
            sparkfunStyles = ["", "_BIG", "_LOCK", "_LOCK_LONGPADS", "_NO_SILK", "_PP_HOLES_ONLY"]
            for style in sparkfunStyles: 
                imageFile = "oomlout_OOMP_eda/FOOTPRINT/eagle/SparkFun-Eagle-Libraries/Sparkfun-Connectors/1X" + pinss + style + "/image.png"
                #print("Image File: " + imageFile)
                if os.path.isfile(imageFile):
                    newPart.addTag("footprintEagle","FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-1X" + pinss + style)
            
            
            adafruitStyles = ["", "-CLEANBIG", "-BIGLOCK", "-CLEAN", "-LOCK", "-CB"]
            for style in adafruitStyles: 
                imageFile = "oomlout_OOMP_eda/FOOTPRINT/eagle/Adafruit-Eagle-Library/adafruit/1X" + pinss + style + "/image.png"
                #print("Image File: " + imageFile)
                if os.path.isfile(imageFile):
                    newPart.addTag("footprintEagle","FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-1X" + pinss + style)
            
            
            pimoroniStyles = ["","-0.1&quot;-CASTELLATED-BCREAM", "-0.1&quot;-CASTELLATED-BIGGER-ROUNDED", "-0.1&quot;-CASTELLATED-BIGGER", "-0.1&quot;-CASTELLATED", "-LOCK-MALE", "-CB","_LONGPADS"]
            for style in pimoroniStyles: 
                imageFile = "oomlout_OOMP_eda/FOOTPRINT/eagle/Pimoroni-Eagle-Library/pimoroni-headers/1X" + pinss.replace("0","") + style + "/image.png"
                #print("Image File: " + imageFile)
                if os.path.isfile(imageFile):
                    newPart.addTag("footprintEagle","FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-headers-1" + pinss + style)
            
            newPart.addTag("footprintKicad","FOOTPRINT-kicad-kicad-footprints-Connector_PinHeader_2.54mm-PinHeader_1x" + pinss + "_P2.54mm_Vertical")
    else:
        pinss = oompDesc.replace("PI2X","")
        newPart = part
        if pinss.isnumeric():
            footprints = []
            base = "FOOTPRINT-kicad-kicad-footprints-Connector_PinHeader_2.54mm-PinHeader_2x" + pinss
            footprints.append(base + "_P2.54mm_Vertical")

            addEdaTags(part=newPart,tags=footprints,type="footprintKicad")
            

def addHEAD01SHRO(part,dict):
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI2X","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_IDC-IDC-Header_2x" + pinss
        #footprints.append(base + "_P2.54mm_Horizontal")
        footprints.append(base + "_P2.54mm_Vertical")


        for footprint in footprints:
            newPart.addTag("footprintKicad",footprint)

def addHEAD01SM(part,dict):
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI2X","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_PinHeader_2.54mm-PinHeader_2x" + pinss
        footprints.append(base + "_P2.54mm_Vertical_SMD")


        for footprint in footprints:
            newPart.addTag("footprintKicad",footprint)

def addHEADJSTSH(part,dict):
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        #FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_SH_BM04B-SRSS-TB_1x04-1MP_P1.00mm_Vertical
        #JST_SH_BM04B-SRSS-TB_1x04-1MP_P1.00mm_Vertical
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_SH_BM" + pinss + "B-SRSS-TB_1x" + pinss + "-1MP_P1.00mm_Vertical"
        footprints.append(base)


        for footprint in footprints:
            newPart.addTag("footprintKicad",footprint)

def addHEADJSTSHR(part,dict):
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        #FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_SH_SM04B-SRSS-TB_1x04-1MP_P1.00mm_Horizontal
        
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_SH_SM" + pinss + "B-SRSS-TB_1x" + pinss + "-1MP_P1.00mm_Horizontal"
        footprints.append(base)


        for footprint in footprints:
            newPart.addTag("footprintKicad",footprint)

def addHEADJSTXH(part,dict):
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        #FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_XH_B10B-XH-AM_1x10_P2.50mm_Vertical
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_XH_B" + str(int(pinss)) + "B-XH-AM_1x" + pinss
        footprints.append(base + "_P2.50mm_Vertical")
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_XH_B" + str(int(pinss)) + "B-XH-A_1x" + pinss
        footprints.append(base + "_P2.50mm_Vertical")


        for footprint in footprints:
            newPart.addTag("footprintKicad",footprint)


def addTERSSymbols(part,dict):
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        ###### FOOTPRINTS
        symbols = []
        base = "SYMBOL-kicad-kicad-symbols-Connector-Screw_Terminal_01x" + pinss
        symbols.append(base)
        for symbol in symbols:
            ###### TODO add a check for existance
            newPart.addTag("symbolKicad",symbol)

def addTERS35D(part,dict):
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        base = "FOOTPRINT-kicad-kicad-footprints-TerminalBlock_4Ucon-TerminalBlock_4Ucon_1x" + pinss
        footprints.append(base + "_P3.50mm_Vertical")
    
        for footprint in footprints:
            newPart.addTag("footprintKicad",footprint)  

