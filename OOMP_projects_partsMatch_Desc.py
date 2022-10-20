import OOMP
import OOMP_projects_partsMatch

def matchDesc(project,part,oompType="",oompSize="",oompColor="",oompDesc="",oompIndex=""):
    global PART, VALUE, DEVICE, PACAKGE, DESC, BOM    
    partDict = OOMP_projects_partsMatch.loadPartDict(part,project)   
    rv= "UNMATCHED"


    ######  BUTTONS
    if oompType == "BUTA":
        rv = "STAN"

    if oompType.startswith("CAP"):
        ######  Capacitors
        #if "UF" in partDict["VALUE"].upper() or partDict["VALUE"].upper().endswith("U"):
        if "U" in partDict["VALUE"].upper() or partDict["VALUE"].upper().endswith("U"):
            ###### full uf
            for x in range(11,99):
                test = str(x/10)
                if test == partDict["VALUENUMBER"]:
                    return "UF" + str(x) + "D"            
            for x in range(1,999):
                test = str(x)
                if test == partDict["VALUENUMBER"]:
                    return "UF" + str(x)
        #if "PF" in partDict["VALUE"].upper():
        if "P" in partDict["VALUE"].upper():
            ###### full PF
            for x in range(11,99):
                test = str(x/10)
                if test == partDict["VALUENUMBER"]:
                    return "PF" + str(x) + "D"
            for x in range(1,999):
                test = str(x)
                if test == partDict["VALUENUMBER"]:
                    return "PF" + str(x)
        #if "NF" in partDict["VALUE"].upper():
        if "N" in partDict["VALUE"].upper():
            for x in range(11,99):
                test = str(x/10)
                if test == partDict["VALUENUMBER"]:
                    return "PF" + str(x) + "D"        
            ###### full NF
            for x in range(1,999):
                test = str(x)
                if test == partDict["VALUENUMBER"]:
                    return "NF" + str(x)
        list = []
        list.append([".1UF","NF100"])
        list.append([".1U","NF100"])
        list.append(["0.1UF","NF100"])
        list.append([".22UF","NF220"])
        list.append(["0.22UF","NF220"])
        list.append(["47UF","UF47"])
        list.append(["2U2","UF22D"])



        for l in list:
            if l[0] in partDict["VALUE"].upper():    
                return l[1]
        
        ###### 0. uf
        for x in range(100,999):
            test = "0." + str(x)
            if test.startswith(partDict["VALUENUMBER"]):
                return "NF" + str(x)

    ################### DEBUG
    if partDict["PART"] == "PC1":
        pass    

    ######  DC JACKS
    if oompType == "DCJP":
        rv = "STAN"


    ######  Headers
    if oompType == "HEAD":
        exclusions = ["ZZZZZZZ"]
        for exclusion in exclusions:
            if exclusion in partDict["PACKAGE"]:
                return "UNMATCHED"
        for x in range(1,40):
            if "1X" + str(x).zfill(2) in partDict["PACKAGE"].upper():
                return "PI" + str(x).zfill(2)
            if "2X" + str(x).zfill(2) in partDict["PACKAGE"].upper():    
                return "PI2X" + str(x).zfill(2)
        if partDict["PART"]== "ICSP":                
            pass

        list = []
        list.append(["STEMMA_I2C","PI04"])
        list.append(["QWIIC_CONNECTOR","PI04"])
        list.append(["3X2","PI2X03"])
        for l in list:
            if partDict["VALUE"].upper() == l[0]:
                return l[1] + extra

    ######  Headers
    if oompType == "LEDS":
        rv = "STAN"

    ######  Resistors
    if oompType == "RESE" or oompType == "RESA":
        extra = ""
        if oompType == "RESA":
            if "4X" in partDict["PACKAGE"]:
                extra = "X4"
        for x in range(1,999):
            if partDict["VALUE"] == str(x):
                if x < 100:
                    twoDig = int(x)
                    return "O" + str(twoDig) + "0" + extra
                else:
                    twoDig = int(x/10)
                    return "O" + str(twoDig) + "1"  + extra
            if partDict["VALUE"].upper() == str(x) + "K":
                if x < 10:
                    twoDig = int(x*10)
                    return "O" + str(twoDig) + "2"  + extra
                elif x < 1000: 
                    twoDig = int(x)
                    return "O" + str(twoDig) + "3" + extra
                else:
                    twoDig = int(x/10)
                    return "O" + str(twoDig) + "4"     + extra
            if partDict["VALUE"].upper() == str(x) + "M":
                if x < 10:
                    twoDig = int(x*10)
                    return "O" + str(twoDig) + "5"     + extra
                else:
                    twoDig = int(x)
                    return "O" + str(twoDig) + "6"    + extra
        list = []
        list.append(["1.0K","O102"])
        list.append(["2.2K","O222"])
        list.append(["3.9K","O392"])
        list.append(["4.7K","O472"])
        list.append(["5.1K","O472"])
        for l in list:
            if partDict["VALUE"].upper() == l[0]:
                return l[1] + extra


    ######Pairs   
    # ####### VALUE     
    pairs = []
    pairs.append(["1N4148","K4148"])
    pairs.append(["2811","K2811"])
    pairs.append(["2812","K2812"])
    pairs.append(["MBR120","KMBR120"])
    pairs.append(["BSS138","KBSS138"])
    pairs.append(["IRLML6401","K6401"])
    pairs.append(["MIC5225","KMIC5225"])
    pairs.append(["MIC5205","KMIC5205"])
    pairs.append(["LP298XS","KLP298XS"])
    pairs.append(["AP2112K","KAP2112K"])
    pairs.append(["MMZ1608B121C","O121"])
    
    for pair in pairs:
        if pair[0].upper() in partDict["VALUE"].upper():        
            return pair[1]
        if oompType == "VREG":
            if pair[0].upper() in partDict["DEVICE"].upper():        
                return pair[1]
    # ####### PACKAGE     
    pairs = []
    pairs.append(["1X2-3.5MM","PI02"])
    pairs.append(["1X3-3.5MM","PI03"])
    pairs.append(["1X4-3.5MM","PI04"])
    pairs.append(["1X5-3.5MM","PI05"])
    pairs.append(["1X6-3.5MM","PI06"])
    pairs.append(["1X7-3.5MM","PI07"])
    pairs.append(["1X8-3.5MM","PI08"])
    pairs.append(["SCREWTERMINAL-3.5MM-2","PI02"])
    pairs.append(["SCREWTERMINAL-3.5MM-3","PI03"])
    pairs.append(["SCREWTERMINAL-3.5MM-4","PI04"])
    pairs.append(["SCREWTERMINAL-3.5MM-8","PI08"])
    pairs.append(["APA102","K102"])
    for pair in pairs:
        if pair[0].upper() in partDict["PACKAGE"].upper():        
            return pair[1]

                
    return rv