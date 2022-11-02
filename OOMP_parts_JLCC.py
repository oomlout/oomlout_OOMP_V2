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
            hexID = getHexID(oompID)
            part["hexID"] = hexID
            print(oompID + " " + hexID)    
            part["datasheet"] = part["Datasheet"]
            d = {"type" : part["oompType"], "size" : part["oompSize"], "color" : part["oompColor"], "desc" : part["oompDesc"], "index" : part["oompIndex"], "hexID" : part["hexID"], "datasheet" : part["datasheet"], "extraTags" : part["extraTags"]}
            OOMP_parts_BASE.makePart(dict = d)
            count = count + 1
        else:
            print(oompID + " "  + part["Description"])  
            pass
    print("Parts Matched: " + str(count))

def matchPart(part):
    part["oompType"] = "UNMATCHED"
    part["oompSize"] = "UNMATCHED"
    part["oompColor"] = "UNMATCHED"
    part["oompDesc"] = "UNMATCHED"
    part["oompIndex"] = "UNMATCHED"
    part["hexID"] = "XXX"

    
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
    



    for test in tests:
        if test[0] == lcscPart:
            for tag in test[1]:
                part[tag] = test[1][tag]
            pass





    return part

def extraTags(part):
    part["extraTags"] = []

    part["extraTags"].append(["oplPartNumber",{"code" : "C-JLCC", "name" : "JLC Parts Library", "partID" : part["LCSC Part"], "partName" : part["Description"]}])
    part["extraTags"].append(["distributorPartNumber",{ "code" : "C-LCSC", "name" : "LCSC" , "partID" : part["LCSC Part"]}])
    part["extraTags"].append(["manufacturerPartNumber",{ "code" : "C-XXXX", "name" : part["Manufacturer"], "partID" : part["MFR.Part"], "partName" : part["MFR.Part"] }])


    return part

def getHexID(oompID):
    
    list = []
    list.append(["CAPC-","C"])
    list.append(["LEDS-","L"])
    list.append(["RESE-","R"])
    ######size
    list.append(["0201-","2"])
    list.append(["0402-","4"])
    list.append(["0603-","6"])
    list.append(["0805-","8"])
    list.append(["1206-","12"])
    list.append(["03-","3"])
    list.append(["05-","5"])

    
    ######desc
        ###### CAPC
    list.append(["PF","P"])
    list.append(["NF","N"])
    list.append(["UF","U"])

    list.append(["STAN",""])


    ######index          
    if "CAPC" in oompID:  
        list.append(["-V50",""])  
        list.append(["-V25",""])  
    list.append(["-V",""])
    list.append(["-D",""])
    list.append(["-01",""])
        
     ######color
    list.append(["X-",""])
    list.append(["R-","R"])
    list.append(["O-","O"])
    list.append(["Y-","Y"])
    list.append(["G-","G"])
    list.append(["L-","L"])
    list.append(["V-","V"])
    list.append(["B-","B"])
    list.append(["P-","P"])   
    list.append(["W-","W"])   

    for l in list:
        oompID = oompID.replace(l[0],l[1])
    return oompID

