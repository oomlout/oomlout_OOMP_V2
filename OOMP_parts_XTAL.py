import OOMP

import OOMP_parts_BASE

def addParts():

    values = ["MZ8","MZ16","MZ12","MZ25"]
##############################
    ######  RESE
    #########
    ######### I01
    #####################################################################

    ######### I01 PI1X
    #####################################################################
    type = "XTAL";size = "";color = "X";desc = "";index = "01";hexID = ""
    sizes = ["5032","3225P4","HC49","HC49S"]
    for size in sizes:
        datasheet = "sourceDatasheets/" + type + "-" + size + "-X-" + values[0] + "-01.pdf"
        for desc in values:            
            oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
            hexID = OOMP_parts_BASE.getHexID(oompID)
            extraTags = []
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)

