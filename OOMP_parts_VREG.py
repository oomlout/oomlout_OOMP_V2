import OOMP

import OOMP_parts_BASE

def addParts():
    ##############################
    ######  VREG
    
    ###### KAP2112K 
    type = "VREG";size = "";color = "X";desc = "KAP2112K";index = "01";hexID = ""
    datasheet = "sourceDatasheets/VREG-SO235-X-KAP2112K-V33D.pdf"
    extraTags = []
    list = ["SO235","SO8",]
    list2 = ["V12D","V18D","V25D","V26D","V33D"]        
    for l in list:
        size = l
        for ll in list2:
            index = ll
            hexID = "VR2112" + l.replace("SO","").replace("T","").replace("T","").replace("DPAK","D") + ll.replace("D","").replace("V","")
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d) 

    ######  KLD1117
    type = "VREG";size = "";color = "X";desc = "KLD1117";index = "01";hexID = ""
    datasheet = "sourceDatasheets/VREG-SO223-X-KLD1117-01.pdf"
    extraTags = []
    list = ["SO223","SO8","DPAK","T220"]
    list2 = ["V12D","V18D","V25D","V33D","V5"]
    for l in list:
        size = l
        for ll in list2:
            index = ll
            hexID = "VR1117" + l.replace("SO","").replace("T","").replace("T","").replace("DPAK","D") + ll.replace("D","").replace("V","")
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d) 

    ###### KMIC5225
    type = "VREG";size = "";color = "X";desc = "KMIC5205";index = "01";hexID = ""
    datasheet = "sourceDatasheets/VREG-SO235-X-KMIC5205-V5.pdf"
    extraTags = []
    list = ["SO235"]
    list2 = ["V25D","V27D","V25D","V3","V33D","V5","VADJ"]        
    for l in list:
        size = l
        for ll in list2:
            index = ll
            hexID = "VR5225" + l.replace("SO","").replace("T","").replace("T","").replace("DPAK","D") + ll.replace("D","").replace("V","")
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d) 

    ###### KMIC5205
    type = "VREG";size = "";color = "X";desc = "KMIC5225";index = "01";hexID = ""
    datasheet = "sourceDatasheets/VREG-SO235-X-KMIC5225-V33D.pdf"
    extraTags = []
    list = ["SO235"]
    list2 = ["V15D","V18D","V25D","V27D","V3","V33D","V5","VADJ"]        
    for l in list:
        size = l
        for ll in list2:
            index = ll
            hexID = "VR5225" + l.replace("SO","").replace("T","").replace("T","").replace("DPAK","D") + ll.replace("D","").replace("V","")
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)                 


    