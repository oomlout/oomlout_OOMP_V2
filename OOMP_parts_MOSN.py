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


        