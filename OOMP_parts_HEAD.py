import OOMP

import OOMP_parts_BASE

def addParts():
##############################
    ######  HEAD
    #########
    ######### I01
    #####################################################################

    ######### I01 PI1X
    #####################################################################
    type = "HEAD";size = "I01";color = "X";desc = "";index = "";hexID = ""
    indexes = ["01","SM","RS"]
    for index in indexes:
        datasheet = "sourceDatasheets/HEAD-I01-X-PI03-" + index + ".pdf"
        for x in range(1,20+1):
            desc = "PI" + str(x).zfill(2)
            oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
            hexID = OOMP_parts_BASE.getHexID(oompID)
            extraTags = []
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)



    ######### I01 PI2X
    #####################################################################
    type = "HEAD";size = "I01";color = "X";desc = "";index = "SM";hexID = ""
    indexes = ["01","SM","RS","SHRO","SHRR"]
    #datasheet = "sourceDatasheets/HEAD-I01-X-PI03-SM.pdf"
    datasheet = ""

    for index in indexes:
        datasheet = "sourceDatasheets/HEAD-I01-X-PI2X03-" + index + ".pdf"
        for x in range(2,20+1):
            desc = "PI2X" + str(x).zfill(2)
            oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
            hexID = OOMP_parts_BASE.getHexID(oompID)
            extraTags = []
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)


    
    #########
    #########        
    ######### JST
    #####################################################################
        #########
        #########   JSTXH
        type = "HEAD";size = "JSTXH";color = "X";desc = "";index = "01";hexID = ""
        datasheet = "sourceDatasheets/HEAD-JSTXH-X-PI03-01.pdf"

        for x in range(1,20+1):
            desc = "PI" + str(x).zfill(2)
            oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
            hexID = OOMP_parts_BASE.getHexID(oompID)
            extraTags = []
            extraTags.append(["manufacturerPartNumber",{"partLink" : "https://www.jst.co.uk/productSeries.php?pid=136"}])
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)

        #########
        #########   JSTPH
        type = "HEAD";size = "JSTPH";color = "X";desc = "";index = "";hexID = ""
        datasheet = "sourceDatasheets/HEAD-JSTPH-X-PI03-01.pdf"
        indexes = ["RA","01","SM"]
        for index in indexes:
            for x in range(1,20+1):
                desc = "PI" + str(x).zfill(2)
                oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
                hexID = OOMP_parts_BASE.getHexID(oompID)
                extraTags = []
                extraTags.append(["manufacturerPartNumber",{"partLink" : "https://www.jst.co.uk/productSeries.php?pid=6626"}])
                d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
                OOMP_parts_BASE.makePart(dict = d)


        #########
        #########   JSTSH
        type = "HEAD";size = "JSTSH";color = "X";desc = "";index = "SM";hexID = ""
        datasheet = "sourceDatasheets/HEAD-JSTSH-X-PI03-01.pdf"
        indexes = ["RA","RS"]
        for index in indexes:
            for x in range(1,20+1):
                desc = "PI" + str(x).zfill(2)
                oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
                hexID = OOMP_parts_BASE.getHexID(oompID)
                extraTags = []
                extraTags.append(["manufacturerPartNumber",{"partLink" : "https://www.jst.co.uk/productSeries.php?pid=93"}])
                d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
                OOMP_parts_BASE.makePart(dict = d)

