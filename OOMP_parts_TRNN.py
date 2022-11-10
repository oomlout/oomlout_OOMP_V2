import OOMP

import OOMP_parts_BASE

def addParts():

    values = ["K2N3904","KC1815","KBC337","K2N2222"]
    ##############################
    ######### TRNN
    #####################################################################
    type = "TRNN";size = "";color = "X";desc = "";index = "01";hexID = ""
    sizes = ["T92"]
    for size in sizes:

        for desc in values: 
            datasheet = "sourceDatasheets/" + type + "-" + size + "-X-" + desc + "-01.pdf"           
            oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
            hexID = OOMP_parts_BASE.getHexID(oompID)
            extraTags = []
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)
    
    values = ["KA1015","KS8550","K2N3906","K2N2907","KBC327"]
    ##############################
    ######### TRNP
    #####################################################################
    type = "TRNP";size = "";color = "X";desc = "";index = "01";hexID = ""
    sizes = ["T92"]
    for size in sizes:
        for desc in values:                        
            datasheet = "sourceDatasheets/" + type + "-" + size + "-X-" + desc + "-01.pdf"           
            oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
            hexID = OOMP_parts_BASE.getHexID(oompID)
            extraTags = []
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)

