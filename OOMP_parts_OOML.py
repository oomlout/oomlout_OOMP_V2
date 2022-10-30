import OOMP

import OOMP_parts_BASE

import OOMP_parts_DIOD
import OOMP_parts_HEAD
import OOMP_parts_LEDS
import OOMP_parts_MCUU
import OOMP_parts_VREG
import OOMP_parts_MOSN


def createParts():    
    ##############################
    ######  BUTA
    if True:
        type = "BUTA";size = "12";color = "X";desc = "LEDS";index = "01";hexID = "B12L"
        datasheet = "sourceDatasheets/BUTA-12-X-LEDS-01.pdf"
        extraTags = []
        extraTags.append(["footprintEagle","FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Switches-TACTILE_SWITCH_LED_PTH_12MM"])            
    
    ##############################
    ######  DIOD
    if True:
        OOMP_parts_DIOD.addParts() 

    ##############################
    ######  HEAD
    if True:
        OOMP_parts_HEAD.addParts() 
    
    ##############################
    ######  LEDS
    if True:
        OOMP_parts_LEDS.addParts() 

    ##############################
    ######  MCUU
    if True:
        OOMP_parts_MCUU.addParts()

    ##############################
    ######  MOSN
    if True:
        OOMP_parts_MOSN.addParts()


    
    ##############################
    ######  REFU
    if True:
        parts=[]
        type = "REFU";size = "1812";color = "X";desc = "";index = "";hexID = ""
        parts.append(["A35D","V6"])
        parts.append(["A3","V6"])
        parts.append(["A26D","V8"])
        parts.append(["A2","V8"])
        parts.append(["A16D","V8"])
        parts.append(["A11D","V8"])
        parts.append(["A15D","V6"])
        parts.append(["A35D","V6"])
        parts.append(["A075D","V132D"])
        parts.append(["A5D","V15"])
        parts.append(["A2D","V30"])
        parts.append(["A1D","V60"])
        datasheet = ""
        for part in parts:
            desc = part[0]
            index = part[1]
            hexID = "RF18" + desc.replace("A","")
            extraTags = []
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)


    ##############################
    ######  RESA
    
    if True:
        type = "RESA";size = "";color = "X";desc = "";index = "01";hexID = ""
        resistorSmall = ["O102","O103","O220","O222","O472"]
        resaPackages = ["06038","12068"]
        datasheet = "sourceDatasheets/" + "RESA-X-X-X-X.pdf"
        for size in resaPackages:
            for desc in resistorSmall:
                hexID = "RA" + size.replace("06038","6").replace("12068","12") + desc.replace("O","")
                desc = desc + "X4"            
            extraTags = []
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)
    ##############################
    ######  SENS
    if True:
    ######
    ###### ADXL345
        type = "SENS";size = "LG14";color = "X";desc = "K345";index = "01";hexID = "SEN345"        
        oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index 
        datasheet = "sourceDatasheets/" + oompID + ".pdf"
        extraTags = []
        extraTags.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_LGA-LGA-14_3x5mm_P0.8mm_LayoutBorder1x6y"])     
        extraTags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Sensor_Motion-ADXL343"])            
        d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
        OOMP_parts_BASE.makePart(dict = d) 
    ##############################
    ######  TERS
    if True:
        type = "TERS";size = "35D";color = "L";desc = "";index = "01";hexID = ""
        datasheet = "sourceDatasheets/TERS-35D-L-PI03-01.pdf"
        for x in range(1,15+1):
            desc = "PI" + str(x).zfill(2)
            hexID = "T35L" + str(x)
            extraTags = []
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)
    ##############################
    ######  TRNN
    if True:
        type = "TRNN";size = "SO23";color = "X";desc = "KS8050";index = "01";hexID = "TNS248050"
        oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index 
        datasheet = "sourceDatasheets/" + oompID + ".pdf"
        extraTags = []
        extraTags.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-SOT-23"])
        extraTags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Device-Q_NPN_BEC"])            
        d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
        OOMP_parts_BASE.makePart(dict = d) 


    ##############################
    ######  USB
    if True:
        ######  C31
        type = "USBS";size = "TC";color = "X";desc = "K31";index = "01";hexID = "USCK31"
        datasheet = "sourceDatasheets/USBS-TC-X-K31-01.pdf"
        extraTags = []
        data = {"name" : "LCSC", "code" : "C-LCSC", "partID" : "C165948", "partName" : "C165948", "partLink" : ""}
        extraTags.append(["distributorPartNumber",data])
        data = {"name" : "Korean Hroparts Elec", "code" : "C-KHRO", "partID" : "TYPE-C-31-M-12", "partName" : "", "partLink" : ""}
        extraTags.append(["manufacturerPartNumber",data])         
        d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
        OOMP_parts_BASE.makePart(dict = d) 
    ##############################
    ######  VREG
    ######  LD1117
    if True:
        OOMP_parts_VREG.addParts() 
        