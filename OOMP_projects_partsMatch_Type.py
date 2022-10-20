import OOMP
import OOMP_projects_partsMatch

def matchType(project,part,oompType="",oompSize="",oompColor="",oompDesc="",oompIndex=""):
    partDict = OOMP_projects_partsMatch.loadPartDict(part,project)    
    rv= "UNMATCHED"

    ###### Getting useful items
    partLetter = OOMP_projects_partsMatch.getUseful(part,"partLetter")
    #partNumber = re.sub(r'\d+', '', part[PART])


    ###### BUTTONS
    tests = ["KMR2","EVQ-Q2"]
    for test in tests:
        if test in partDict["PACKAGE"].upper():
            rv = "BUTA"


    ###### Capacitor
    if partDict["PARTLETTER"] == "C" or "UF" in partDict["VALUE"].upper() :
        rv = "CAPX"
        ###### CAPC test
        tests = ["0805","0603","0402","1206"]
        for test in tests:
            if test in partDict["PACKAGE"]:
                rv = "CAPC"
        tests = ["EIA3216"]
        for test in tests:
            if test in partDict["PACKAGE"]:
                rv = "CAPT"
        tests = ["PANASONIC_B","PANASONIC_C","PANASONIC_D","PANASONIC_D8","PANASONIC_E","PANASONIC_F","PANASONIC_G"]                
        for test in tests:
            if test in partDict["PACKAGE"]:
                rv = "CAPE"
    ###### DCJACK
    tests = ["POWER_JACK"]
    for test in tests:
        if test in partDict["VALUE"].upper():
            rv = "DCJP"

    ###### DIODE
    if partDict["PARTLETTER"] == "D":
        if "APA102" in partDict["VALUE"] or "LED" in partDict["PACKAGE"]:
            return "LEDS"
        rv = "DIOD"

    ###### FERITE BEAD
    if partDict["PARTLETTER"] == "FB":
        rv = "FERB"

    ###### HEADER
    if "HEADER" in partDict["DEVICE"].upper():
        rv = "HEAD"
    if "HEADER" in partDict["DESC"].upper():
        rv = "HEAD"
    if partDict["PARTLETTER"].upper() == "JP":
        if "1X" in partDict["PACKAGE"].upper():
            rv = "HEAD"
    if "STEMMA_I2C" in partDict["VALUE"].upper():
        rv = "HEAD"
    if "QWIIC_CONNECTOR" in partDict["VALUE"].upper() or "QWIIC RIGHT" in partDict["VALUE"].upper():
        rv = "HEAD"        

    ###### LED
    if partDict["DEVICE"].startswith("LED") or partDict["PART"].startswith("LED"):
        rv = "LEDS"


    ###### MOSFETS
    if "N-CHANNEL MOSFET" in partDict["DESC"].upper():
        rv = "MOSN"
    if "P-CHANNEL MOSFET" in partDict["DESC"].upper():
        rv = "MOSP"

    ###### PTC
    if "PTCSMD" in partDict["DEVICE"]:
        return "REFU"

    ###### Terminal Strip
    list = []
    list.append(["SCREWTERMINAL","TERS"])
    list.append(["-3.5MM","TERS"])
    for l in list:
        if l[0] in partDict["PACKAGE"].upper():
            return l[1]

    ######Resistor
    if partDict["PARTLETTER"] == "R" or partDict["PART"] == "R-PROG2":
        if "RESPACK_4X0603" in partDict["PACKAGE"]:
            return "RESA"
        else:
            return "RESE"



    ######  Voltage Regulators
    options = []
    options.append("MIC5225")
    options.append("MIC5205")
    options.append("LP298XS")
    options.append("AP2112K")
    for option in options:
        if option in partDict["VALUE"] or option in partDict["DEVICE"]:
            return "VREG"


    ###### SKIP
    ###### BOM
    list = []
    list.append("EXCLUDE")
    for l in list:
        if l in partDict["BOM"]:
            rv = "SKIP"

    ###### VALUE
    list = []
    list.append("ALLIGATOR")
    list.append("CREATIVE")
    list.append("ELAST")
    list.append("FIDUCIAL")
    list.append("FRAME")
    list.append("GATOR")
    list.append("JUMPER-SMT")
    list.append("LOGO")
    list.append("M01SNAP") 
    list.append("MOUSE-BITE")  
    list.append("MOUNTINGHOLE")    
    list.append("PERFHOLE")
    list.append("PAD")
    list.append("REVISION")
    list.append("SINGLE_PAD")
    list.append("STAND-OFF")
    list.append("STANDOFF")
    list.append("SOLDERJUMPER")
    list.append("SOLDER_PAD")
    list.append("DNP")
    list.append("SEWTAP")
    list.append("TAB_GATOR")
    list.append("TESTPOINT")
    list.append("TEST-POINT")
    list.append("TPTP20R")
    list.append("TP_")
    for l in list:
        if l in partDict["VALUE"]:
            rv = "SKIP"
    ###### DEVICE
    list = []
    list.append("JUMPER-PAD")
    list.append("SOLDERJUMPER")
    list.append("TESTPOINT")
    for l in list:
        if l in partDict["DEVICE"]:
            rv = "SKIP"            
        

    

    return rv