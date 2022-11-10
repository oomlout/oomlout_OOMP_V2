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
            extraTags = []
            index = ll
            hexID = "VR2112" + l.replace("SO","").replace("T","").replace("T","").replace("T252","25") + ll.replace("D","").replace("V","")

            if "SO235" in size:
                vString = ll.replace("V5","50").replace("V","").replace("D","")
                vString = vString.replace("25","-2.5").replace("12","-1.2").replace("18","-1.8").replace("26","-2.6").replace("3","-3.0").replace("33","-3.3").replace("50","-5.0").replace("ADJ","")
                symbol = "SYMBOL-kicad-kicad-symbols-Regulator_Linear-AP2112K" + vString
                baseSymbol = "SYMBOL-kicad-kicad-symbols-Regulator_Linear-AP2204K-1.5"
                extraTags.append(["symbolKicad",baseSymbol])
                extraTags.append(["symbolKicad",symbol])


            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d) 

    ######  KLD1117
    type = "VREG";size = "";color = "X";desc = "KLD1117";index = "01";hexID = ""
    datasheet = "sourceDatasheets/VREG-SO223-X-KLD1117-01.pdf"
    extraTags = []
    list = ["SO223","SO8","T252","T220"]
    list2 = ["V12D","V18D","V25D","V33D","V5","ADJ"]
    for l in list:
        size = l
        for ll in list2:
            extraTags = []
            extraTags.append(["oompNote","LCSC Part number set in VREG/SO223/X/KLD1117/V5/details2.py"])
            index = ll
            hexID = "VR1117" + l.replace("SO","").replace("T","").replace("T","").replace("T252","25") + ll.replace("D","").replace("V","")            
            
            if "SO8" not in size and "ADJ" not in index:
                vString = ll.replace("V5","50").replace("V","").replace("D","")
                symbol = "SYMBOL-kicad-kicad-symbols-Regulator_Linear-LD1117S" + vString + "TR_SOT223" 
                baseSymbol = "SYMBOL-kicad-kicad-symbols-Regulator_Linear-AP1117-15"
                extraTags.append(["symbolKicad",baseSymbol])
                extraTags.append(["symbolKicad",symbol])

            
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d) 

    ###### KMIC5205
    type = "VREG";size = "";color = "X";desc = "KMIC5205";index = "01";hexID = ""
    datasheet = "sourceDatasheets/VREG-SO235-X-KMIC5205-V5.pdf"
    extraTags = []
    list = ["SO235"]
    list2 = ["V25D","V27D","V3","V33D","V5","VADJ"]        
    for l in list:
        size = l
        for ll in list2:
            extraTags = []
            index = ll
            hexID = "VR5225" + l.replace("SO","").replace("T","").replace("T","").replace("T252","25") + ll.replace("D","").replace("V","")

            vString = ll.replace("V5","50").replace("V","").replace("D","")
            vString = vString.replace("25","-2.5").replace("27","-2.7").replace("3","-3.0").replace("33","-3.3").replace("50","-5.0").replace("ADJ","")
            symbol = "SYMBOL-kicad-kicad-symbols-Regulator_Linear-MIC5205" + vString + "YM5" 
            baseSymbol = "SYMBOL-kicad-kicad-symbols-Regulator_Linear-AP131-15"
            extraTags.append(["symbolKicad",baseSymbol])
            extraTags.append(["symbolKicad",symbol])
            


            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d) 

    ###### KMIC5225
    type = "VREG";size = "";color = "X";desc = "KMIC5225";index = "01";hexID = ""
    datasheet = "sourceDatasheets/VREG-SO235-X-KMIC5225-V33D.pdf"
    
    list = ["SO235"]
    list2 = ["V15D","V18D","V25D","V27D","V3","V33D","V5","VADJ"]        
    for l in list:
        size = l
        for ll in list2:
            extraTags = []
            index = ll
            hexID = "VR5225" + l.replace("SO","").replace("T","").replace("T","").replace("T252","25") + ll.replace("D","").replace("V","")

            vString = ll.replace("V5","50").replace("V","").replace("D","")
            vString = vString.replace("25","-2.5").replace("27","-2.7").replace("3","-3.0").replace("33","-3.3").replace("50","-5.0").replace("ADJ","")
            symbol = "SYMBOL-kicad-kicad-symbols-Regulator_Linear-MIC5205" + vString + "YM5" 
            extraTags.append(["symbolKicad",symbol])
            

            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)                 


    