import OOMP

import OOMP_parts_BASE

def addParts():
##############################
    ######  HEAD
    #########
    ######### I01
    #####################################################################

        ######### PI1X
        #####################################################################

        type = "HEAD";size = "I01";color = "X";desc = "";index = "01";hexID = ""
        datasheet = "sourceDatasheets/HEAD-I01-X-PI03-01.pdf"
        
        for x in range(1,20+1):
            desc = "PI" + str(x).zfill(2)
            hexID = "H" + str(x) + ""
            extraTags = []
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)

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

    #########
    #########
        type = "HEAD";size = "I01";color = "X";desc = "";index = "RS";hexID = ""
        datasheet = "sourceDatasheets/HEAD-I01-X-PI03-RS.pdf"

        for x in range(2,20+1):
            extraTags = []
            desc = "PI" + str(x).zfill(2)
            hexID = "H" + str(x) + "RS"
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)

        ######### PI2X
        #####################################################################

        type = "HEAD";size = "I01";color = "X";desc = "PI2X10";index = "SHRO";hexID = "H2X10SH"
        datasheet="sourceDatasheets/HEAD-I01-X-PI2X03-01.pdf"

        for x in range(1,10+1):
            desc = "PI2X" + str(x).zfill(2)
            hexID = "H2X" + str(x) + "SH"
            extraTags = []
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)
    ##########
    ##########
        type = "HEAD";size = "I01";color = "X";desc = "";index = "01";hexID = ""
        datasheet = "sourceDatasheets/HEAD-I01-X-PI2X03-01.pdf"
        
        for x in range(1,10+1):
            desc = "PI2X" + str(x).zfill(2)
            hexID = "H2X" + str(x) + ""
            extraTags = []
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)

    ##########
    ##########
        type = "HEAD";size = "I01";color = "X";desc = "";index = "SM";hexID = ""
        datasheet = "sourceDatasheets/HEAD-I01-X-PI2X03-SM.pdf"
        
        for x in range(1,10+1):
            desc = "PI2X" + str(x).zfill(2)
            hexID = "H2X" + str(x) + "SM"
            extraTags = []
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)

    #########
    #########
        type = "HEAD";size = "I01";color = "X";desc = "";index = "RS";hexID = ""
        datasheet = "sourceDatasheets/HEAD-I01-X-PI2X03-RS.pdf"

        for x in range(2,10+1):
            extraTags = []
            desc = "PI2X" + str(x).zfill(2)
            hexID = "H2X" + str(x) + "RS"
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)

    #########
    #########        
    ######### JST
    #####################################################################
        type = "HEAD";size = "JSTXH";color = "X";desc = "";index = "01";hexID = ""
        datasheet = "sourceDatasheets/HEAD-JSTXH-X-PI03-01.pdf"

        for x in range(1,20+1):
            desc = "PI" + str(x).zfill(2)
            hexID = "HXH" + str(x)
            extraTags = []
            extraTags.append(["manufacturerPartNumber",{"partLink" : "https://www.jst.co.uk/productSeries.php?pid=136"}])
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)

    #########
    #########   
        
        type = "HEAD";size = "JSTSH";color = "X";desc = "";index = "SM";hexID = ""
        datasheet = "sourceDatasheets/HEAD-JSTSH-X-PI03-01.pdf"

        for x in range(1,20+1):
            desc = "PI" + str(x).zfill(2)
            hexID = "HSH" + str(x)
            extraTags = []
            extraTags.append(["manufacturerPartNumber",{"partLink" : "https://www.jst.co.uk/productSeries.php?pid=93"}])
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)

        #type = "HEAD";size = "JSTSH";color = "X";desc = "";index = "SM";hexID = ""
        index = "RS"
        datasheet = "sourceDatasheets/HEAD-JSTSH-X-PI03-01.pdf"
        for x in range(1,20+1):
            desc = "PI" + str(x).zfill(2)
            hexID = "HSH" + str(x)
            extraTags = []
            extraTags.append(["manufacturerPartNumber",{"partLink" : "https://www.jst.co.uk/productSeries.php?pid=93"}])
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)
