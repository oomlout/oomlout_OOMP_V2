import OOMP

import OOMP_parts_BASE

def addParts():
##############################
    ######  DIOD
    type = "DIOD";size = "S323";color = "X";desc = "K4148";index = "01";hexID = "D34148"    
    datasheet = "sourceDatasheets/DIOD-S323-X-K4184-01.pdf"
    extraTags = []

    d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
    OOMP_parts_BASE.makePart(dict = d)


    type = "DIOD";size = "S123";color = "X";desc = "KMBR120";index = "01";hexID = "D34148"    
    datasheet = "sourceDatasheets/DIOD-S123-X-KMBR120-01.pdf"
    extraTags = []

    d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
    OOMP_parts_BASE.makePart(dict = d)


    
    ######  PROJ_ELLA
    type = "DIOD";size = "S523";color = "X";desc = "KRB520S30T";index = "01";hexID = "D34148"    
    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index 
    datasheet = "sourceDatasheets/" + oompID + ".pdf"
    extraTags = []
    extraTags.append(["matchSpecial",[["RB520S30T1G"],oompID]])     
    extraTags.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Diode_SMD-D_SOD-523"])     
    extraTags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Device-D"])            
    
    d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
    OOMP_parts_BASE.makePart(dict = d)

    type = "DIOD";size = "SO236";color = "X";desc = "KSRV05X4";index = "01";hexID = "D34148"    
    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index 
    datasheet = "sourceDatasheets/" + oompID + ".pdf"
    extraTags = []
    extraTags.append(["matchSpecial",[["SRV05-4"],oompID]])     
    extraTags.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-SOT-23-6"])     
    extraTags.append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-SOT-23-6_Handsoldering"])     
    extraTags.append(["symbolKicad","SYMBOL-kicad-kicad-symbols-Device-D"])            
    
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