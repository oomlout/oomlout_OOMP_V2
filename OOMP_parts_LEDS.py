import OOMP
import os

import OOMP_parts_BASE

def addParts():
##############################
    ######  HEAD
    #########
    ######### 
    #####################################################################

    ######### STANDARD LEDs
    #####################################################################

    type = "LEDS";size = "";color = "X";desc = "STAN";index = "01";hexID = ""
    datasheet = ""
    
    list = sizes = ["03","05","10","0402","0603","0805","1206"]
    list2 = colours = ["R","G","L","Y","W","O"]
    for l in list:
        size = l
        for ll in list2:
            color = ll
            testDatasheet = "sourceDatasheets/LEDS-" + l + "-" + ll + "-STAN-01.pdf"
            datasheet = ""
            if os.path.exists(testDatasheet):
                datasheet = testDatasheet
            extraTags = []
            oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
            hexID = OOMP_parts_BASE.getHexID(oompID)
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)

    ######### CREE XHP70
    #####################################################################
    type = "LEDS";size = "XHP70";color = "W";desc = "CREE";index = "01";hexID = "LXHP70"    
    datasheet = "sourceDatasheets/LEDS-XHP70-W-CREE-01.pdf"
    extraTags = []

    d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
    OOMP_parts_BASE.makePart(dict = d)
        