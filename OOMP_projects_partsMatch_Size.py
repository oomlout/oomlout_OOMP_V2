import OOMP
import OOMP_projects_partsMatch

def matchSize(project,part,oompType="",oompSize="",oompColor="",oompDesc="",oompIndex=""):
    partDict = OOMP_projects_partsMatch.loadPartDict(part,project)    
    rv= "UNMATCHED"

    ######direct replacments
    tests = ["0805","0603","0402","1206"]
    for test in tests:
        if partDict["PACKAGENUMBER"] == test:
        #if test in partDict["PACKAGE"]:
            rv = test



    ###### CAPACITORS
    if oompType == "CAPE":
        list = []
        list.append(["PANASONIC_B","PANB"])
        list.append(["PANASONIC_C","PANC"])
        list.append(["PANASONIC_D","PAND"])
        list.append(["PANASONIC_D8","PAD8G"])
        list.append(["PANASONIC_E","PANE"])
        list.append(["PANASONIC_F","PANF"])
        list.append(["PANASONIC_G","PANG"])
        for l in list:
            if l[0] in partDict["PACKAGE"]:
                return l[1]

    ######  DC JACK
    if oompType == "DCJP":
        rv = "21D"
        if "JACKSMD" in partDict["DEVICE"]:
            return "S21D"


    ######headers
    if oompType == "HEAD":
        ###### not 0.1"
        exclusions = ["MM"]
        for exclusion in exclusions:
            if exclusion in partDict["PACKAGE"]:
                return "UNMATCHED"
        if "STEMMA_I2C" in partDict["VALUE"].upper():
            rv = "01"
        if "QWIIC_CONNECTOR" in partDict["VALUE"].upper() or "QWIIC RIGHT" in partDict["VALUE"].upper():
            rv = "01"                
        return "I01"



    ###### Screw Terminals
    if oompType == "TERS":
        if "3.5MM" in partDict["PACKAGE"]:
            return "35D"

    ######Pairs        
    ######  PACKAGE
    pairs = []
    ###### Kicad surface mounts
    pairs.append(["0603_1608Metric","0603"])
    pairs.append(["0805_2012Metric","0805"])
    pairs.append(["DO214","D214"])
    pairs.append(["EIA3216","3216"])
    pairs.append(["EIA3528","3528"])
    pairs.append(["EIA6032","6032"])
    pairs.append(["EIA7343","7343"])
    pairs.append(["SOD-123","S123"])
    pairs.append(["SOD-323","S323"])
    pairs.append(["SOT-23-5","SO235"])
    pairs.append(["SOT23-5","SO235"])
    pairs.append(["SOT23","SO23"])
    pairs.append(["SOT363","SO363"])
    pairs.append(["SOT23-5L","SO235"])
    pairs.append(["2121","2121"])
    pairs.append(["2020","2020"])
    pairs.append(["3535","3535"])
    pairs.append(["4.6X2.8","4628"])
    pairs.append(["5050","5050"])
    pairs.append(["EVQ-Q2","6060"])
    pairs.append(["RESPACK_4X0603","06038"])
    for pair in pairs:
        if pair[0] in partDict["PACKAGE"]:
            return pair[1]
    ######  DEVICE
    pairs = []
    pairs.append(["5050","5050"])
    for pair in pairs:
        if pair[0] in partDict["DEVICE"]:
            return pair[1]
    

    return rv