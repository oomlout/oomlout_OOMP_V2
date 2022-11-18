import OOMP
import os

import OOMP_parts_BASE

def addParts():
##############################
    ######  SENS
    #########
    ######### 
    #####################################################################

    ######### KL3GD20
    #####################################################################
    type = "SENS";size = "LG163030S";color = "X";desc = "KL3GD20";index = "01";hexID = "MN2524184A"
    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index 
    datasheet = "sourceDatasheets/" + oompID + ".pdf"
    extraTags = []
    extraTags.append(["matchSpecial",[["L3GD20H_LGA16L"],"SENS-LG163030S-X-KL3GD20-01"]])     
    #extraTags.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_LGA-LGA-16_4x4mm_P0.65mm_LayoutBorder4x4y"])     
    extraTags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Sensor_Motion-L3GD20"])            
    d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
    OOMP_parts_BASE.makePart(dict = d)

    ######
    ###### ADXL345
    type = "SENS";size = "LG143050";color = "X";desc = "K345";index = "01";hexID = "SEN345"        
    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index 
    datasheet = "sourceDatasheets/" + oompID + ".pdf"
    extraTags = []
    extraTags.append(["matchSpecial",[["ADXL343"],oompID]])     
    extraTags.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_LGA-LGA-14_3x5mm_P0.8mm_LayoutBorder1x6y"])     
    extraTags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Sensor_Motion-ADXL343"])            
    d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
    OOMP_parts_BASE.makePart(dict = d) 
