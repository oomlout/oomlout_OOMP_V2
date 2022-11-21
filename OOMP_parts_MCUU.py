import OOMP

import OOMP_parts_BASE

def addParts():
##############################
    ######  MCUU
    if True:
        mcuList = []

        ###### WCH
        ###############################
        base = {}
        base["TYPE"] = "MCUU"
        base["SIZE"] = ""
        base["COLOR"] = "X"
        base["DESC"] = ""
        base["INDEX"] = ""
        base["HEXID"] = ""
        

        ss = base.copy()
        #ss["TYPE"] = ""
        ss["SIZE"] = "TS20"
        ss["COLOR"] = "003"
        ss["DESC"] = "KCH32V"
        ss["INDEX"] = "01"
        ss["HEXID"] = "MCK323T20"
        ss["EXTRATAGS"] = []
        #ss["EXTRATAGS"].append(["symbolKicad",""])
        #ss["EXTRATAGS"].append(["symbolKicad",""])        
        ss["EXTRATAGS"].append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_SO-HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm"])
        #ss["EXTRATAGS"].append(["footprintKicad",""])
        ss["DATASHEET"] = "sourceDatasheets/MCUU-TS20-003-KCH32V-01.pdf"
        ####### DPN and MPN enter in oomlout_OOMP_parts_V2/OOMP_parts_DISTRIBUTORNUMBERS.py
        mcuList.append(ss)

        ss= ss.copy()
        ss["SIZE"] = "QFN20"
        ss["EXTRATAGS"] = []
        ss["EXTRATAGS"].append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_DFN_QFN-QFN-20-1EP_3x3mm_P0.4mm_EP1.65x1.65mm"])        
        mcuList.append(ss)
        
        ss= ss.copy()
        ss["SIZE"] = "SP16"
        ss["EXTRATAGS"] = []
        ss["EXTRATAGS"].append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_SO-SOP-16_3.9x9.9mm_P1.27mm"])        
        mcuList.append(ss)
        
        ss= ss.copy()
        ss["SIZE"] = "SP08"
        ss["EXTRATAGS"] = []
        ss["EXTRATAGS"].append(["footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_SO-SOP-8_3.9x4.9mm_P1.27mm"])
        mcuList.append(ss)



        for s in mcuList:
            d = {"type" : s["TYPE"], "size" : s["SIZE"], "color" : s["COLOR"], "desc" : s["DESC"], "index" : s["INDEX"], "hexID" : s["HEXID"], "datasheet" : s["DATASHEET"], "extraTags" : s["EXTRATAGS"]}
            OOMP_parts_BASE.makePart(dict = d)   

        ###### ATTINY
        ###############################

            ####### ATTINY84
        type = "MCUU";size = "";color = "84";desc = "ATTINY";index = "01";hexID = "MCAT84SC14"
        datasheet = "sourceDatasheets/MCUU-SC14-84-ATTINY-01.pdf"
        
        ss = {}
        id = "QFN14"
        ss[id] = {}
        ss[id]["SYMBOL"] = "SYMBOL-kicad-kicad-symbols-MCU_Microchip_ATtiny-ATtiny24V-10M"
        ss[id]["SYMBOL2"] = "SYMBOL-kicad-kicad-symbols-MCU_Microchip_ATtiny-ATtiny84-20M"
        ss[id]["FOOTPRINT"] = "FOOTPRINT-kicad-kicad-footprints-Package_DFN_QFN-QFN-20-1EP_4x4mm_P0.5mm_EP2.6x2.6mm"
        ss[id]["HEXID"] = "MCAT84QF14"
        id = "DI14"
        ss[id] = {}
        ss[id]["SYMBOL"] = "SYMBOL-kicad-kicad-symbols-MCU_Microchip_ATtiny-ATtiny24V-10P"
        ss[id]["SYMBOL2"] = "SYMBOL-kicad-kicad-symbols-MCU_Microchip_ATtiny-ATtiny84-20P"
        ss[id]["FOOTPRINT"] = "FOOTPRINT-kicad-kicad-footprints-Package_DIP-DIP-14_W7.62mm"
        ss[id]["HEXID"] = "MCAT84DI14"
        id = "SC14"
        ss[id] = {}
        ss[id]["SYMBOL"] = "SYMBOL-kicad-kicad-symbols-MCU_Microchip_ATtiny-ATtiny20-SS"
        ss[id]["FOOTPRINT"] = "FOOTPRINT-kicad-kicad-footprints-Package_SO-SOIC-14_3.9x8.7mm_P1.27mm"
        ss[id]["HEXID"] = "MCAT84SC14"
        for s in ss:
            size = s
            extraTags = []
            extraTags.append(["footprintKicad",ss[s]["FOOTPRINT"]])
            extraTags.append(["symbolKicad",ss[s]["SYMBOL"]])
            try:
                extraTags.append(["symbolKicad",ss[s]["SYMBOL2"]])
            except KeyError:
                pass
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : ss[s]["HEXID"], "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)   

    
