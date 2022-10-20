import OOMP
import os
from oomBase import *

def addTags(newPart,filter,pins=0,pitch=0,hexID=None,oompType=None,oompSize=None,oompColor=None,oompDesc=None,oompIndex=None):
    if(filter == ""):
        x=0
    if oompType == "FOOTPRINT":
        footprintHex = getFootprintHex(filter)    
        newPart.addTag("hexID",footprintHex)  
    elif("RESE-0603" in filter):
        pass
        #newPart.addTag("footprintEagle","Adafruit-Eagle-Library/adafruit/R0603")  
        #newPart.addTag("footprintKicad","kicad-footprints/Resistor_SMD/R_0603_1608Metric_Pad0.98x0.95mm_HandSolder")  
        #newPart.addTag("footprintKicad","kicad-footprints/Resistor_SMD/R_0603_1608Metric")  
    elif(filter == "HEAD-I01-X-X-X"):
        pinss = "{:02d}".format(pins)
        newPart.addTag("oompType", "HEAD")
        newPart.addTag("oompSize", "I01")
        newPart.addTag("oompColor", "X")
        newPart.addTag("oompDesc", "PI" + pinss)
        newPart.addTag("oompIndex", "01")

        newPart.addTag("hexID","H" + pinss)
        newPart.addTag("oompSort","")

        newPart.addTag("oompClass","Through Hole")
        newPart.addTag("oompClassCode","THTH")
        newPart.addTag("ooPitch","2.54")
        newPart.addTag("ooPinHeight","11.60")
        newPart.addTag("ooPinWidth","0.64")
        newPart.addTag("ooPinOffset","1.53")
        newPart.addTag("oompBbls","variable;pins;" + str(pins) )
        newPart.addTag("oompBbls","template;XXXX-I01-X-XX-01-bbls")
        newPart.addTag("oompDiag","variable;pins;" + str(pins) )
        newPart.addTag("oompDiag","template;HEAD-I01-X-XX-01-diag")
        newPart.addTag("oompIden","variable;pins;" + str(pins) )
        newPart.addTag("oompIden","template;XXXX-I01-X-XX-01-iden")
        newPart.addTag("oompSchem","variable;pins;" + str(pins) )
        if pins % 2 == 1:
            newPart.addTag("oompSchem","template;XXXX-XX-X-XX-01-PINS-ODD-schem")
        else:
            newPart.addTag("oompSchem","template;XXXX-XX-X-XX-01-PINS-EVEN-schem")
        newPart.addTag("oompSimp","variable;pins;" + str(pins) )
        newPart.addTag("oompSimp","template;XXXX-I01-X-XX-01-simp")
        newPart.addTag("ooNumPins",str(pins))
        #newPart.addTag("ooFootprint","OOMP-HEAD-I01-X-PI" + pinss + "-01")

        newPart.addTag("ooDesignator","J1")
        newPart.addTag("schematicSymbol","HEAD-XX-X-PI" + pinss + "-XX")
        #newPart.addTag("pcbFootprint","HEAD-I01-X-PI" + pinss + "-01")
        """
        ###### FOOTPRINTS
        newPart.addTag("kicadSymbol","Connector/Conn_01x" + pinss + "_Male")
        ##newPart.addTag("kicadFootprint","Connector_PinHeader_2.54mm/PinHeader_1x" + pinss + "_P2.54mm_Vertical")
        ######  Sparkfun footprints
        sparkfunStyles = ["", "_BIG", "_LOCK", "_LOCK_LONGPADS", "_NO_SILK", "_PP_HOLES_ONLY"]
        for style in sparkfunStyles: 
            imageFile = "oomlout_OOMP_eda/footprints/eagle/SparkFun-Eagle-Libraries/Sparkfun-Connectors/1X" + pinss + style + "/image.png"
            #print("Image File: " + imageFile)
            if os.path.isfile(imageFile):
                newPart.addTag("footprintEagle","SparkFun-Eagle-Libraries/Sparkfun-Connectors/1X" + pinss + style)
        
        newPart.addTag("footprintKicad","kicad-footprints/Connector_PinHeader_2.54mm/PinHeader_1x" + pinss + "_P2.54mm_Vertical")
        """
    return newPart



def genReport(filename,tags,multi=False,filter="all"):
    outputString = ""
    items = OOMP.getItems(filter)
    count = 0
    numDots = int(len(items)/500)
    for c in range(numDots):
        print(">",end="")
    print()    
    

    if not multi:
        for item in items:
            string = ""
            string = string + item.getTag("oompID").value + "\t"
            for tag in tags:
                string = string + item.getTag(tag).value + "\t"
            string = string + "\n"    
            count = count + 1
            if count % 500 == 0:
                print(".",end="")
            outputString = outputString + string + ""
    else:
        for item in items:
            string = ""
            oompID = item.getTag("oompID").value
            
            tag = tags[0]
            partTags = item.getTags(tag)
            for partTag in partTags:
                string = string + oompID + "\t" + partTag.value + "\n"
                count = count + 1
            if count % 500 == 0:
                print(".",end="")
            outputString = outputString + string + ""


    oomWriteToFile(filename,outputString,utf=False)

def getSymbolHex(filter):
    return getFootprintHex(filter)

def getFootprintHex(filter):
    filter = filter.upper()
    replaceList = []
    replaceList.append(["FOOTPRINT-","FZ"])
    replaceList.append(["SYMBOL-","SZ"])
    ### adafruit ones
    ######  Library
    replaceList.append(["",""])
    replaceList.append(["eagle-Adafruit-Eagle-Library-adafruit-".upper(),"A"])
    ######  additions
    replaceList.append(["",""])
    replaceList.append(["-0.7MM","07"])
    replaceList.append(["-0.5MM","05"])
    replaceList.append(["-3.5MM","35"])
    replaceList.append(["ADAFRUIT","ADA"])
    replaceList.append(["ARDUINO","ARD"])
    replaceList.append(["-BIG","B"])
    replaceList.append(["CLUEFRUIT","BF"])
    replaceList.append(["-BIGPOGO","BP"])
    replaceList.append(["-CLEANBIG","CB"])
    replaceList.append(["-CLEAN","C"])
    replaceList.append(["-CB","CB"])
    replaceList.append(["_DIM","D"])
    replaceList.append(["-DIM","D"])
    replaceList.append(["EDGELAUNCH","EL"])
    replaceList.append(["FEATHERWING","FW"])
    
    replaceList.append(["INLINE","I"])
    replaceList.append(["JACK","J"])
    replaceList.append(["EAGLEBONE","EB"])
    replaceList.append(["MINI_MELF","MM"])
    replaceList.append(["MOLEX","MX"])
    
    replaceList.append(["NARROW","N"])
    replaceList.append(["NOIOREF","NI"])
    replaceList.append(["-NOTEXT","NT"])
    replaceList.append(["-NODIM","ND"])
    replaceList.append(["-NOHOLE","NH"])
    replaceList.append(["-OSHWLOGO","OL"])
    replaceList.append(["-PANASONIC","P"])
    replaceList.append(["PUSHBUTTON","PB"])
    
    replaceList.append(["PWRONLY",""])
    replaceList.append(["PTH","P"])
    
    replaceList.append(["REVERSE","R"])
    replaceList.append(["-ROUND","R"])    
    replaceList.append(["SEGMENT","S"])
    replaceList.append(["-SIDE","SD"])
    replaceList.append(["SKINNYPADS","SP"])
    replaceList.append(["SMA","S"])
    replaceList.append(["SMD","SM"])
    replaceList.append(["SKINNIER","SK"])
    replaceList.append(["-SMALLS","S"])
    replaceList.append(["-SMT","S"])
    replaceList.append(["_SMT","S"])
    
    replaceList.append(["THM","T"])
    replaceList.append(["-LOCK","L"])
    
    replaceList.append(["WHEEL","W"])
    
    ### Dangerous Prototypes ones
    ######  Library
    replaceList.append(["",""])
    replaceList.append(["DangerousPrototypes-Eagle-Library-dp_devices.v6-".upper(),"DP"])
   ### eagle ones    
    replaceList.append(["",""])
    replaceList.append(["eagle-eagle-default-".upper(),"E"])


   ### kicad ones    
    replaceList.append(["",""])
    replaceList.append(["kicad-kicad-footprints".upper(),"K"])
    replaceList.append(["kicad-kicad-symbols".upper(),"K"])
    ######  Kicad libraries
    replaceList.append(["Varistor".upper(),"V"])
    replaceList.append(["Audio_Module".upper(),"A"])
    replaceList.append(["Battery".upper(),"BAT"])
    replaceList.append(["Button_Switch_Keyboard".upper(),"B"])
    replaceList.append(["Button_Switch_SMD".upper(),"B"])
    replaceList.append(["Button_Switch_THT".upper(),"B"])
    replaceList.append(["Buzzer_Beeper".upper(),"BZ"])
    replaceList.append(["Calibration_Scale".upper(),"CS"])
    replaceList.append(["Capacitor_SMD".upper(),"C"])
    replaceList.append(["Capacitor_Tantalum_SMD".upper(),"C"])
    replaceList.append(["Capacitor_THT".upper(),"C"])
    replaceList.append(["Connector".upper(),"CN"])
    replaceList.append(["Connector_AMASS".upper(),"CN"])
    replaceList.append(["Connector_Amphenol".upper(),"CN"])
    replaceList.append(["Connector_Audio".upper(),"CNA"])
    replaceList.append(["Connector_BarrelJack".upper(),"CNBJ"])
    replaceList.append(["Connector_Card".upper(),"CN"])
    replaceList.append(["Connector_Coaxial".upper(),"CN"])
    replaceList.append(["Connector_DIN".upper(),"CDIN"])
    replaceList.append(["Connector_Dsub".upper(),"CDSUB"])
    replaceList.append(["Connector_FFC-FPC".upper(),"CFPC"])
    replaceList.append(["Connector_Harting".upper(),"CN"])
    replaceList.append(["Connector_Harwin".upper(),"CN"])
    replaceList.append(["Connector_HDMI".upper(),"CHDMI"])
    replaceList.append(["Connector_Hirose".upper(),"C"])
    replaceList.append(["Connector_IDC".upper(),"CIDC"])
    replaceList.append(["Connector_JAE".upper(),"C"])
    replaceList.append(["Connector_JST".upper(),"CJST"])
    replaceList.append(["Connector_Molex".upper(),"CMOL"])
    replaceList.append(["Connector_PCBEdge".upper(),"CN"])
    replaceList.append(["Connector_Phoenix_GMSTB".upper(),"CN"])
    replaceList.append(["Connector_Phoenix_MC".upper(),"CNPH"])
    replaceList.append(["Connector_Phoenix_MC_HighVoltage".upper(),"CNPH"])
    replaceList.append(["Connector_Phoenix_MSTB".upper(),"CNPH"])
    replaceList.append(["Connector_Pin".upper(),"CNP"])
    replaceList.append(["Connector_PinHeader_1.00mm".upper(),"CNP"])
    replaceList.append(["Connector_PinHeader_1.27mm".upper(),"CNP"])
    replaceList.append(["Connector_PinHeader_2.00mm".upper(),"CNP"])
    replaceList.append(["Connector_PinHeader_2.54mm".upper(),"CNP"])
    replaceList.append(["Connector_PinSocket_1.00mm".upper(),"CNS"])
    replaceList.append(["Connector_PinSocket_1.27mm".upper(),"CNS"])
    replaceList.append(["Connector_PinSocket_2.00mm".upper(),"CNS"])
    replaceList.append(["Connector_PinSocket_2.54mm".upper(),"CNS"])
    replaceList.append(["Connector_RJ".upper(),"CNRJ"])
    replaceList.append(["Connector_Samtec".upper(),"CN"])
    replaceList.append(["Connector_Samtec_HLE_SMD".upper(),"CN"])
    replaceList.append(["Connector_Samtec_HLE_THT".upper(),"CN"])
    replaceList.append(["Connector_SATA_SAS".upper(),"CN"])
    replaceList.append(["Connector_Stocko".upper(),"CN"])
    replaceList.append(["Connector_TE-Connectivity".upper(),"CNTE"])
    replaceList.append(["Connector_USB".upper(),"CN"])
    replaceList.append(["Connector_Wago".upper(),"CNWA"])
    replaceList.append(["Connector_Wire".upper(),"CNWI"])
    replaceList.append(["Connector_Wuerth".upper(),"CN"])
    replaceList.append(["Converter_ACDC".upper(),"CON"])
    replaceList.append(["Converter_DCDC".upper(),"CON"])
    replaceList.append(["Crystal".upper(),"X"])
    replaceList.append(["Diode_SMD".upper(),"D"])
    replaceList.append(["Diode_THT".upper(),"D"])
    replaceList.append(["Display".upper(),"DI"])
    replaceList.append(["Display_7Segment".upper(),"DI"])
    replaceList.append(["Ferrite_THT".upper(),"F"])
    replaceList.append(["Fiducial".upper(),"FID"])
    replaceList.append(["Filter".upper(),"FIL"])
    replaceList.append(["Fuse".upper(),"FU"])
    replaceList.append(["Heatsink".upper(),"H"])
    replaceList.append(["Inductor_SMD".upper(),"IN"])
    replaceList.append(["Inductor_THT".upper(),"IN"])
    replaceList.append(["Jumper".upper(),"J"])
    replaceList.append(["LED_SMD".upper(),"L"])
    replaceList.append(["LED_THT".upper(),"L"])
    replaceList.append(["Module".upper(),"MO"])
    replaceList.append(["Mounting_Wuerth".upper(),"MON"])
    replaceList.append(["MountingEquipment".upper(),"MON"])
    replaceList.append(["MountingHole".upper(),"HOL"])
    replaceList.append(["NetTie".upper(),"NT"])
    replaceList.append(["Obsolete".upper(),"OB"])
    replaceList.append(["OptoDevice".upper(),"OP"])
    replaceList.append(["Oscillator".upper(),"OCS"])
    replaceList.append(["Package_BGA".upper(),"BGA"])
    replaceList.append(["Package_CSP".upper(),"CSP"])
    replaceList.append(["Package_DFN_QFN".upper(),"DFN"])
    replaceList.append(["Package_DIP".upper(),"DIP"])
    replaceList.append(["Package_DirectFET".upper(),"DFET"])
    replaceList.append(["Package_LCC".upper(),"LCC"])
    replaceList.append(["Package_LGA".upper(),"LGA"])
    replaceList.append(["Package_QFP".upper(),"QFP"])
    replaceList.append(["Package_SIP".upper(),"SIP"])
    replaceList.append(["Package_SO".upper(),"SO"])
    replaceList.append(["Package_SO_J-Lead".upper(),"SO"])
    replaceList.append(["Package_SON".upper(),"SON"])
    replaceList.append(["Package_TO_SOT_SMD".upper(),"SOT"])
    replaceList.append(["Package_TO_SOT_THT".upper(),"SOT"])
    replaceList.append(["Potentiometer_SMD".upper(),"P"])
    replaceList.append(["Potentiometer_THT".upper(),"P"])
    replaceList.append(["Relay_SMD".upper(),"REL"])
    replaceList.append(["Relay_THT".upper(),"REL"])
    replaceList.append(["Resistor_SMD".upper(),"R"])
    replaceList.append(["Resistor_THT".upper(),"R"])
    replaceList.append(["RF".upper(),"RF"])
    replaceList.append(["RF_Antenna".upper(),"RF"])
    replaceList.append(["RF_Converter".upper(),"RF"])
    replaceList.append(["RF_GPS".upper(),"GPS"])
    replaceList.append(["RF_GSM".upper(),"GSM"])
    replaceList.append(["RF_Mini-Circuits".upper(),"RF"])
    replaceList.append(["RF_Module".upper(),"RF"])
    replaceList.append(["RF_Shielding".upper(),"RFS"])
    replaceList.append(["RF_WiFi".upper(),"RF"])
    replaceList.append(["Rotary_Encoder".upper(),"RE"])
    replaceList.append(["Sensor".upper(),"SEN"])
    replaceList.append(["Sensor_Audio".upper(),"SA"])
    replaceList.append(["Sensor_Current".upper(),"SCU"])
    replaceList.append(["Sensor_Distance".upper(),"SDI"])
    replaceList.append(["Sensor_Humidity".upper(),"SHU"])
    replaceList.append(["Sensor_Motion".upper(),"SMO"])
    replaceList.append(["Sensor_Pressure".upper(),"SPR"])
    replaceList.append(["Sensor_Voltage".upper(),"SV"])
    replaceList.append(["Socket".upper(),"SO"])
    replaceList.append(["Symbol".upper(),"SY"])
    replaceList.append(["TerminalBlock".upper(),"TB"])
    replaceList.append(["TerminalBlock_4Ucon".upper(),"TB4U"])
    replaceList.append(["TerminalBlock_Altech".upper(),"TBAL"])
    replaceList.append(["TerminalBlock_Dinkle".upper(),"TBDN"])
    replaceList.append(["TerminalBlock_MetzConnect".upper(),"TBME"])
    replaceList.append(["TerminalBlock_Philmore".upper(),"TBPM"])
    replaceList.append(["TerminalBlock_Phoenix".upper(),"TBPH"])
    replaceList.append(["TerminalBlock_RND".upper(),"TBRN"])
    replaceList.append(["TerminalBlock_TE-Connectivity".upper(),"TBTE"])
    replaceList.append(["TerminalBlock_WAGO".upper(),"TBWA"])
    replaceList.append(["TerminalBlock_Wuerth".upper(),"TBWU"])
    replaceList.append(["TestPoint".upper(),"TP"])
    replaceList.append(["Transformer_SMD".upper(),"TR"])
    replaceList.append(["Transformer_THT".upper(),"TR"])
    replaceList.append(["Transistor_Power_Module".upper(),"Q"])
    replaceList.append(["Valve".upper(),"VA"])

    
    ### pimoroni ones    
    replaceList.append(["",""])
    replaceList.append(["eagle-Pimoroni-Eagle-Library".upper(),"P"])

    ##libraries
    replaceList.append(["",""])
    replaceList.append(["-gee_s".upper(),"G"])
    replaceList.append(["-pimoroni".upper(),""])
    replaceList.append(["-pimoroni-boards".upper(),"B"])
    replaceList.append(["-pimoroni-connectors".upper(),"C"])
    replaceList.append(["-pimoroni-flotilla".upper(),"FL"])
    replaceList.append(["-pimoroni-fpc".upper(),"F"])
    replaceList.append(["-pimoroni-headers".upper(),"H"])
    replaceList.append(["-pimoroni-holes".upper(),"HO"])
    replaceList.append(["-pimoroni-ics".upper(),"I"])
    replaceList.append(["-pimoroni-mechanical".upper(),"M"])
    replaceList.append(["-pimoroni-misc".upper(),"MI"])
    replaceList.append(["-pimoroni-optoelectronics".upper(),"O"])
    replaceList.append(["-pimoroni-passives".upper(),"P"])
    replaceList.append(["-pimoroni-rc".upper(),"RC"])


    ### sparkfun ones
    replaceList.append(["eagle-SparkFun-Eagle-Libraries-".upper(),"S"])
    replaceList.append(["LilyPad-Wearables-".upper(),"LW"])
    replaceList.append(["SparkFun-Aesthetics-".upper(),"A"])
    replaceList.append(["SparkFun-Batteries-".upper(),"B"])
    replaceList.append(["SparkFun-Boards-".upper(),"BO"])
    replaceList.append(["SparkFun-Buzzard-".upper(),"BU"])
    replaceList.append(["SparkFun-Capacitors-".upper(),"C"])
    replaceList.append(["SparkFun-Clocks-".upper(),"CL"])
    replaceList.append(["SparkFun-Coils-".upper(),"CO"])
    replaceList.append(["Sparkfun-Connectors-".upper(),"CN"])
    replaceList.append(["SparkFun-DiscreteSemi-".upper(),"DS"])
    replaceList.append(["SparkFun-Displays-".upper(),"D"])
    replaceList.append(["SparkFun-Electromechanical-".upper(),"E"])
    replaceList.append(["SparkFun-Fuses-".upper(),"F"])
    replaceList.append(["SparkFun-GPS-".upper(),"G"])
    replaceList.append(["SparkFun-Hardware-".upper(),"H"])
    replaceList.append(["SparkFun-IC-Amplifiers-".upper(),"IA"])
    replaceList.append(["SparkFun-IC-Comms-".upper(),"IC"])
    replaceList.append(["SparkFun-IC-Conversion-".upper(),"IV"])
    replaceList.append(["SparkFun-IC-Logic-".upper(),"IL"])
    replaceList.append(["SparkFun-IC-Memory-".upper(),"IM"])
    replaceList.append(["SparkFun-IC-Microcontroller-".upper(),"IU"])
    replaceList.append(["SparkFun-IC-Power-".upper(),"IP"])
    replaceList.append(["SparkFun-IC-Special-Function-".upper(),"IS"])
    replaceList.append(["SparkFun-Jumpers-".upper(),"J"])
    replaceList.append(["SparkFun-LED-".upper(),"L"])
    replaceList.append(["SparkFun-MicroMod-".upper(),"M"])
    replaceList.append(["SparkFun-PowerSymbols-".upper(),"P"])
    replaceList.append(["SparkFun-Resistors-".upper(),"R"])
    replaceList.append(["SparkFun-Retired-".upper(),"RT"])
    replaceList.append(["SparkFun-RF-".upper(),"RF"])
    replaceList.append(["SparkFun-Sensors-".upper(),"S"])
    replaceList.append(["SparkFun-Switches-".upper(),"W"])
    replaceList.append(["User-Submitted-".upper(),"U"])

    ###### sparkfun resistors
    replaceList.append(["",""])
    replaceList.append(["_MURATA","M"])
    
    replaceList.append(["_NO0-CREAM","NC"])
    replaceList.append(["_NO_CREAM","NC"])
    replaceList.append(["-TIGHT","T"])
    replaceList.append(["_RA","RA"])
    replaceList.append(["-KIT","K"])
    replaceList.append(["_KIT","K"])
    replaceList.append(["LONGPADS","L"])
    replaceList.append(["LOCK","L"])
    replaceList.append(["STRAIGHT","S"])
    replaceList.append(["HOLES","H"])
    
    
    
    
    replaceList.append(["AXIAL-","A"])
    
    replaceList.append(["RESONATOR","R"])
    
    replaceList.append(["TRIMPOT-SMD","TS"])

    replaceList.append(["FLAME","F"])
    replaceList.append(["-SHROUDEDS","SH"])
    replaceList.append(["-SHROUDED","SH"])
    replaceList.append(["-QWIIC","Q"])
    

    ### common ones
    replaceList.append(["",""])
    replaceList.append(["0204","24"])
    replaceList.append(["0207","27"])
    replaceList.append(["0204","24"])
    replaceList.append(["0402","42"])
    replaceList.append(["0603","63"])
    ###### Last ditch
    #####Sizes
    replaceList.append(["LARGE","L"])
    replaceList.append(["SMALL","S"])
    
    replaceList.append(["",""])
    replaceList.append(["BATTCON","BC"])
    replaceList.append(["BUTTON","B"])
    replaceList.append(["COPPER","C"])
    replaceList.append(["FIDUCIAL","F"])
    replaceList.append(["LED","L"])
    replaceList.append(["LOGO","L"])
    replaceList.append(["MICRO","M"])
    replaceList.append(["NAME","N"])
    replaceList.append(["POGOPIN","PP"])
    
    replaceList.append(["RADIAL","R"])    
    replaceList.append(["SHIELD","SH"])    
    replaceList.append(["TRANSFORMER","TR"])
    
    replaceList.append(["RECTANGULAR","R"])
    replaceList.append(["MM",""])

    replaceList.append(["SOP","S"])

    replaceList.append(["MIL","M"])
    replaceList.append(["USB","U"])    
    replaceList.append(["MINI","M"])

    replaceList.append(["/",""])
    replaceList.append(["-",""])
    replaceList.append(["_",""])
    replaceList.append(["0",""])
    replaceList.append([":",""])
    replaceList.append([".",""])
    replaceList.append([",",""])
    ###### MM
    for x in range(9):
        xs = str(x)
        replaceList.append(["-0" + xs + "MM",xs])
        replaceList.append(["-0" + xs + "mm",xs])
        replaceList.append(["-" + xs + "MM",xs])
        replaceList.append(["-" + xs + "mm",xs])
        replaceList.append([xs + "MM",xs])
        replaceList.append([xs + "MM",xs])



    for replace in replaceList:
        filter = filter.replace(replace[0],replace[1])
    return filter