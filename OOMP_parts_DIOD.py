import OOMP

import OOMP_parts_BASE

def addParts():
##############################
    ######  DIOD
    type = "DIOD";size = "S323";color = "X";desc = "K4184";index = "01";hexID = "D34148"    
    datasheet = "sourceDatasheets/DIOD-S323-X-K4184-01.pdf"
    extraTags = []

    d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
    OOMP_parts_BASE.makePart(dict = d)
    
    type = "DIOD";size = "S123";color = "X";desc = "KMBR120";index = "01";hexID = "D34148"    
    datasheet = "sourceDatasheets/DIOD-S123-X-KMBR120-01.pdf"
    extraTags = []

    d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
    OOMP_parts_BASE.makePart(dict = d)

    """
    ##########
    ##########
        type = "HEAD";size = "I01";color = "X";desc = "";index = "SM";hexID = ""
        #datasheet = "sourceDatasheets/HEAD-I01-X-PI03-SM.pdf"
        datasheet = ""
        
        for x in range(1,20+1):
            desc = "PI2X" + str(x).zfill(2)
            hexID = "H2X" + str(x) + "SM"
            extraTags = []
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)
    """