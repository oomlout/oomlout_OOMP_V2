import OOMP

import OOMP_parts_BASE

def addParts():

    reseValues = ["O000","O100","O101","O102","O103","O104","O105","O106","O10X","O112","O113","O114","O121","O123","O124","O133","O134","O150","O151","O153","O154","O164","O181","O183","O184","O200","O201","O202","O203","O204","O205","O220","O221","O222","O223","O224","O225","O22X","O241","O243","O244","O270","O271","O273","O274","O301","O302","O303","O304","O305","O330","O331","O332","O333","O334","O361","O363","O364","O391","O393","O394","O402","O4022","O431","O432","O433","O434","O470","O471","O473","O474","O47X","O4992","O499D","O502","O505","O510","O511","O512","O513","O514","O515","O560","O561","O563","O564","O602","O621","O622","O623","O680","O681","O683","O684","O702","O705","O750","O751","O752","O753","O754","O802","O820","O821","O822","O823","O902","O912","O913","O993"]
##############################
    ######  RESE
    #########
    ######### I01
    #####################################################################

    ######### I01 PI1X
    #####################################################################
    type = "RESE";size = "";color = "X";desc = "";index = "01";hexID = ""
    sizes = ["0402","0603","0805","1206","W04"]
    for size in sizes:
        datasheet = "sourceDatasheets/RESE-" + size + "-X-O103-01.pdf"
        for desc in reseValues:            
            oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
            hexID = OOMP_parts_BASE.getHexID(oompID)
            extraTags = []
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)

