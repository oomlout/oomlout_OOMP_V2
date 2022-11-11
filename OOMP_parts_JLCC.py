from multiprocessing.dummy import active_children
import OOMP

import OOMP_parts_BASE

from oomBase import *

def createParts():
    print("    Generating JLCC Parts")
    pass
    partsFile = "csv/C-JLCC-basicPartList.csv"

    contents = oomReadFileToString(partsFile)

    parts = []
    cellNames = []

    lines = contents.split("\n")
    for line in lines:
        
        cells = line.split("\t")
        if "LCSC Part" in cells[0]:
            for cell in cells:
                cellNames.append(cell)
        else:
            part = {}
            for x in range(0,len(cells)-1):
                part[cellNames[x]] = cells[x]
            if len(part) > 2:
                parts.append(part)

    for part in parts:
            part = matchPart(part)
            
    count = 0
    for part in parts:
        oompID = part["oompType"] + "-" + part["oompSize"] + "-" + part["oompColor"]  + "-" + part["oompDesc"]  + "-" + part["oompIndex"]
        if "UNMATCHED" not in oompID:
            hexID = OOMP_parts_BASE.getHexID(oompID)
            part["hexID"] = hexID
            #print(oompID + " " + hexID)    
            ping()
            part["datasheet"] = part["Datasheet"]
            d = {"type" : part["oompType"], "size" : part["oompSize"], "color" : part["oompColor"], "desc" : part["oompDesc"], "index" : part["oompIndex"], "hexID" : part["hexID"], "datasheet" : part["datasheet"], "extraTags" : part["extraTags"]}
            OOMP_parts_BASE.makePart(dict = d)
            count = count + 1
        else:
            #print(oompID + " "  + part["Description"])  
            pass
    print("Parts Matched: " + str(count))

def matchPart(part):
    part["oompType"] = "UNMATCHED"
    part["oompSize"] = "UNMATCHED"
    part["oompColor"] = "UNMATCHED"
    part["oompDesc"] = "UNMATCHED"
    part["oompIndex"] = "UNMATCHED"
    part["hexID"] = "XXX"
    part["extraTags"] = []

    
    part = matchType(part)
    part = matchSize(part)
    part = matchColor(part)
    part = matchDesc(part)
    part = matchIndex(part)
    part = matchSpecial(part)


    part = extraTags(part)

    return part


def matchType(part):
    sc = part["Second Category"] 
    list = []
    list.append(["Ferrite Beads","FERB"])
    list.append(["Multilayer Ceramic Capacitors MLCC - SMD/SMT","CAPC"])
    list.append(["Chip Resistor - Surface Mount","RESE"])

    for l in list:
        if sc == l[0]:
            part["oompType"] = l[1]

    return part


def matchSize(part):
    size = part["Package"]

    list = []
    list.append(["201","0201"])    
    list.append(["402","0402"])
    list.append(["603","0603"])
    list.append(["805","0805"])
    list.append(["1206","1206"])
    list.append(["0201","0201"])    
    list.append(["0402","0402"])
    list.append(["0603","0603"])
    list.append(["0805","0805"])
    list.append(["1206","1206"])

    for l in list:
        if size in l[0]:
            part["oompSize"] = l[1]

    return part


def matchColor(part):

    part["oompColor"] = "X"

    return part

def matchDesc(part):
    description = part["Description"]
    ###### capacitor    
    if part["oompType"] == "CAPC":
        match = False
        for test in OOMP.tagDetails["desc"]:
            name = OOMP.tagDetails["desc"][test]["name"]
            code = OOMP.tagDetails["desc"][test]["code"]
            if name.replace(" ","") in description and name != "" and name != "SMD" and not match:
                part["oompDesc"] = code
                match = True
    ###### Resistor    
    if part["oompType"] == "RESE":
        match = False
        for test in OOMP.tagDetails["desc"]:            
            name = OOMP.tagDetails["desc"][test]["name"]
            code = OOMP.tagDetails["desc"][test]["code"]
            if "Ohm" in name:
                testString = name.replace(" Ohm","?? ") + part["oompSize"]
                if testString in description:
                    part["oompDesc"] = code
                    match = True 
                testString = name.replace(" Ohm","¦¸ ") + part["oompSize"]
                if testString in description:
                    part["oompDesc"] = code
                    match = True 
                testString = name.replace(" Ohm","Ω ") + part["oompSize"]
                if testString in description:
                    part["oompDesc"] = code
                    match = True 
                    #'200mA 1 450mΩ 600Ω@100MHz ±25% 0603  Ferrite Beads ROHS'
    return part


def matchIndex(part):
    description = part["Description"]
    if part["oompType"] == "CAPC":
        list = []
        list.append(["50V","V50"])    
        list.append(["16V","V16"])
        list.append(["25V","V25"])
        list.append(["10V","V10"])
        list.append(["100V","V100"])
        list.append(["500V","V500"])
        list.append(["2kV","V2000"])
        list.append(["6.3V","V63D"])

        for l in list:
            if description.startswith(l[0]):
                part["oompIndex"] = l[1]
    
    if part["oompType"] == "RESE":
        part["oompIndex"] = "01"

    return part

def matchSpecial(part):
    pass
    lcscPart = part["LCSC Part"]
    newDict  = {"oompType" : "","oompSize" : "","oompColor" : "","oompDesc" : "","oompIndex" : ""}
    tests = []

    ###### ICIC   
    newDict = {"oompType" : "ICIC","oompSize" : "","oompColor" : "X","oompDesc" : "","oompIndex" : "01"}

    newDict["oompSize"] = "SC16"
    dic = newDict.copy(); dic["oompDesc"] = "K2003";tests.append(["C7512", dic])
    newDict["oompSize"] = "SC18W"
    dic = newDict.copy(); dic["oompDesc"] = "K2803";tests.append(["C9683", dic])
    
    ###### LEDS
        ######  0603
    newDict = {"oompType" : "LEDS","oompSize" : "0603","oompColor" : "","oompDesc" : "STAN","oompIndex" : "01"}
    dic = newDict.copy(); dic["oompColor"] = "W";tests.append(["C2290", dic])
    dic = newDict.copy(); dic["oompColor"] = "G";tests.append(["C72043", dic])
    dic = newDict.copy(); dic["oompColor"] = "R";tests.append(["C2286", dic])
    dic = newDict.copy(); dic["oompColor"] = "Y";tests.append(["C72038", dic])
    dic = newDict.copy(); dic["oompColor"] = "L";tests.append(["C72038", dic])
        ######  0805
    newDict = {"oompType" : "LEDS","oompSize" : "0805","oompColor" : "","oompDesc" : "STAN","oompIndex" : "01"}
    dic = newDict.copy(); dic["oompColor"] = "W";tests.append(["C34499", dic])
    dic = newDict.copy(); dic["oompColor"] = "R";tests.append(["C84256", dic])
    dic = newDict.copy(); dic["oompColor"] = "Y";tests.append(["C2296", dic])

    ###### MOSN
    newDict = {"oompType" : "MOSN","oompSize" : "","oompColor" : "X","oompDesc" : "","oompIndex" : "01"}
    newDict["oompSize"] = "SO23"
    dic = newDict.copy(); dic["oompDesc"] = "K2N7002";tests.append(["C8545", dic])
    dic = newDict.copy(); dic["oompDesc"] = "KAO3400A";tests.append(["C20917", dic])

    ###### MOSP
    newDict = {"oompType" : "MOSP","oompSize" : "","oompColor" : "X","oompDesc" : "","oompIndex" : "01"}
    newDict["oompSize"] = "SO23"
    dic = newDict.copy(); dic["oompDesc"] = "KLBSS84LT1G";tests.append(["C8492", dic])
    dic = newDict.copy(); dic["oompDesc"] = "KSI2301CDS";tests.append(["C8492", dic])
    dic = newDict.copy(); dic["oompDesc"] = "KAO3401A";tests.append(["C15127", dic])


    ###### TRNN
    newDict = {"oompType" : "TRNN","oompSize" : "","oompColor" : "X","oompDesc" : "","oompIndex" : "01"}
    newDict["oompSize"] = "SO23"
    dic = newDict.copy(); dic["oompDesc"] = "K5551";tests.append(["C2145", dic])
    dic = newDict.copy(); dic["oompDesc"] = "KS8050";tests.append(["C2146", dic])
    dic = newDict.copy(); dic["oompDesc"] = "KSS8050";tests.append(["C2150", dic])
    dic = newDict.copy(); dic["oompDesc"] = "KS9013";tests.append(["C6749", dic])
    dic = newDict.copy(); dic["oompDesc"] = "KMMBT2222A";tests.append(["C8512", dic])
    dic = newDict.copy(); dic["oompDesc"] = "KD882";tests.append(["C9634", dic])
    dic = newDict.copy(); dic["oompDesc"] = "KMMBT3904";tests.append(["C20526", dic])

    
    
    
    
    ###### TRNP
    newDict = {"oompType" : "TRNP","oompSize" : "","oompColor" : "X","oompDesc" : "","oompIndex" : "01"}    
    newDict["oompSize"] = "SO23"
    dic = newDict.copy(); dic["oompDesc"] = "KS9015";tests.append(["C2149", dic])
    dic = newDict.copy(); dic["oompDesc"] = "KMMBT5401";tests.append(["C8326", dic])
    dic = newDict.copy(); dic["oompDesc"] = "KSS8550";tests.append(["C8542", dic])
    dic = newDict.copy(); dic["oompDesc"] = "KS8550";tests.append(["C105432", dic])
    dic = newDict.copy(); dic["oompDesc"] = "KS9012";tests.append(["C8543", dic])
    dic = newDict.copy(); dic["oompDesc"] = "KB772";tests.append(["C24278", dic])
    
    ###### VREG
    newDict = {"oompType" : "VREG","oompSize" : "SO223","oompColor" : "X","oompDesc" : "KLD1117","oompIndex" : "V33D"}
    newDict["hexID"] = "VR11172233"
    baseSymbol = ["symbolKicad","SYMBOL-kicad-kicad-symbols-Regulator_Linear-AP1117-15"]
    symbol = ["symbolKicad","SYMBOL-kicad-kicad-symbols-Regulator_Linear-LD1117S" + "33" + "TR_SOT223"]
    newDict["extraTags"] = [baseSymbol,symbol]
    dic = newDict.copy()
    tests.append(["C6186", dic])
    
    newDict["oompIndex"] = "V5"
    newDict["hexID"] = "VR11172235"
    symbol = ["symbolKicad","SYMBOL-kicad-kicad-symbols-Regulator_Linear-LD1117S" + "50" + "TR_SOT223"]
    newDict["extraTags"] = [baseSymbol,symbol]
    dic = newDict.copy()
    tests.append(["C6187", dic])


    ###### XTAL    
    newDict = {"oompType" : "XTAL","oompSize" : "","oompColor" : "X","oompDesc" : "","oompIndex" : "01"}
    newDict["oompSize"] = "3225P4"
    dic = newDict.copy(); dic["oompDesc"] = "MZ12";tests.append(["C9002", dic])
    dic = newDict.copy(); dic["oompDesc"] = "MZ25";tests.append(["C9006", dic])
    dic = newDict.copy(); dic["oompDesc"] = "MZ16";tests.append(["C13738", dic])
    newDict["oompSize"] = "3215"
    dic = newDict.copy(); dic["oompDesc"] = "KZ327D";tests.append(["C32346", dic])
    newDict["oompSize"] = "5032"
    dic = newDict.copy(); dic["oompDesc"] = "MZ11";tests.append(["C112574", dic])
    dic = newDict.copy(); dic["oompDesc"] = "MZ8";tests.append(["C115962", dic])
    newDict["oompSize"] = "HC49S"
    dic = newDict.copy(); dic["oompDesc"] = "MZ8";tests.append(["C12674", dic])
    

    for test in tests:
        if test[0] == lcscPart:
            for tag in test[1]:
                part[tag] = test[1][tag]
            pass





    return part

def extraTags(part):
    part["extraTags"] = part["extraTags"]

    part["extraTags"].append(["oplPartNumber",{"code" : "C-JLCC", "name" : "JLC Parts Library", "partID" : part["LCSC Part"], "partName" : part["Description"]}])
    part["extraTags"].append(["distributorPartNumber",{ "code" : "C-LCSC", "name" : "LCSC" , "partID" : part["LCSC Part"]}])
    part["extraTags"].append(["manufacturerPartNumber",{ "code" : "C-XXXX", "name" : part["Manufacturer"], "partID" : part["MFR.Part"], "partName" : part["MFR.Part"] }])

    

    return part


