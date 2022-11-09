import OOMP
import os

import OOMP_parts_BASE

def addParts():
##############################
    ######  HEAD
    #########
    ######### 
    #####################################################################

    ######### K4184
    #####################################################################
    type = "MOSN";size = "T252";color = "X";desc = "K4184";index = "01";hexID = "MN2524184A"
    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index 
    datasheet = "sourceDatasheets/" + oompID + ".pdf"
    extraTags = []
    extraTags.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-TO-252-3_TabPin2"])     
    extraTags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Device-Q_NMOS_GDS"])            
    d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
    OOMP_parts_BASE.makePart(dict = d) 

    ######### K30N06L
    #####################################################################
    type = "MOSN";size = "T252";color = "X";desc = "K30N06L";index = "01";hexID = "MN30N06D"
    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index 
    datasheet = "sourceDatasheets/" + oompID + ".pdf"
    extraTags = []
    extraTags.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-TO-252-2"])     
    extraTags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Device-Q_NMOS_GDS"])            
    d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
    OOMP_parts_BASE.makePart(dict = d) 

    type = "MOSN";size = "T220";color = "X";desc = "K30N06L";index = "01";hexID = "MN30N06D"
    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index 
    datasheet = "sourceDatasheets/" + oompID + ".pdf"
    extraTags = []
    extraTags.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_THT-TO-220-3_Vertical"])     
    extraTags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Device-Q_NMOS_GDS"])            
    d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
    OOMP_parts_BASE.makePart(dict = d) 


    ######### IRLB8721
    #####################################################################
    type = "MOSN";size = "T220";color = "X";desc = "K30N06L";index = "01";hexID = "MN8721"
    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index 
    datasheet = "sourceDatasheets/" + oompID + ".pdf"
    extraTags = []
    extraTags.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_THT-TO-220-3_Vertical"])    
    extraTags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Device-Q_NMOS_GDS"])            
    d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
    OOMP_parts_BASE.makePart(dict = d) 



        