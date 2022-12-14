import OOMP_modules_BASE

def makeModules():
    
    ############################################################
    #############################################################
    ############  BLOCKS

    ############################################################
    ######  CONN 
    #    
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "CONN"
    d["oompColor"] = "I2C";    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01";    d["hexID"] = "BCI"
    d["name"] = "Connector Block (I2C)"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "CONN"
    d["oompColor"] = "USB";    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01";    d["hexID"] = "BCUSB"
    d["name"] = "Connector Block USB"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "CONN"
    d["oompColor"] = "POWE";    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01";    d["hexID"] = "BCP"
    d["name"] = "Connector Block Power"    
    d["extraTags"] = []
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "CONN"
    d["oompColor"] = "PROG";    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01";    d["hexID"] = "BCPR"
    d["name"] = "Connector Block Programing"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "CONN"
    d["oompColor"] = "I2C";    d["oompDesc"] = "EXTRA"
    d["oompIndex"] = "01";    d["hexID"] = "BCIE"
    d["name"] = "Connector Block (I2C) Plus Extra Pins"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    OOMP_modules_BASE.makeModule(d)
        ######  OOBB
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "CONN"
    d["oompColor"] = "OOBB";    d["oompDesc"] = "BA"
    d["oompIndex"] = "01";    d["hexID"] = "BCOBA"
    d["name"] = "Connector Block OOBB Basic"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    OOMP_modules_BASE.makeModule(d)
        ######  RASP
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "CONN"
    d["oompColor"] = "RASP";    d["oompDesc"] = "PICO"
    d["oompIndex"] = "2040";    d["hexID"] = "BCRP2040"
    d["name"] = "Connector Block Raspberry Pi Pico (2040)"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    OOMP_modules_BASE.makeModule(d)

    ############################################################
    ######  MCUU
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "MCUU"
    d["oompColor"] = "STAN";    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01";    d["hexID"] = "BMS"
    d["name"] = "Microcontroller Block"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    OOMP_modules_BASE.makeModule(d)

    ############################################################
    ######  POWE    
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "POWE"
    d["oompColor"] = "V12R";    d["oompDesc"] = "V33D"
    d["oompIndex"] = "01";    d["hexID"] = "BP123"
    d["name"] = "Power Block About 12 v In, 3.3 v Out"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "POWE"
    d["oompColor"] = "STAN";    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01";    d["hexID"] = "BPS"
    d["name"] = "Power Block"    
    d["extraTags"] = []
    #d["extraTags"].append([])

    ############################################################
    ######  SENS    
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "SENS"
    d["oompColor"] = "ACCEL";    d["oompDesc"] = "I2C"
    d["oompIndex"] = "01";    d["hexID"] = "BSAI"
    d["name"] = "Sensor Block (Accelerometer) I2C"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    OOMP_modules_BASE.makeModule(d)    

    ############################################################
    #############################################################
    ############  MODULES

    ############################################################
    ######  CONN

        ######  BRBO
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "BRBO";    d["oompDesc"] = "IBBC"
    d["oompIndex"] = "SZ01";    d["hexID"] = "MCBI1"
    d["name"] = "Connector Module Breakout Board IBBZ Size 01"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-CONN-I2C-EXTRA-01"])
    oompParts = {}
    oompParts["J1"] = {"OOMPID" : "HEAD-I01-X-PI06-01"}    
    oompParts["J2"] = {"OOMPID" : "HEAD-I01-X-PI06-01"}    
    d["extraTags"].append(["oompParts",oompParts]) 

    d["extraTags"].append(["componentModules","M1,MODULE-CONN-I2C-QWIIC-01"]) 
    d["extraTags"].append(["componentModules","M2,MODULE-CONN-I2C-QWIIC-01"]) 
    OOMP_modules_BASE.makeModule(d)
        ######  DADB
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "DADB";    d["oompDesc"] = ""
    d["oompIndex"] = "01";    d["hexID"] = ""
    d["name"] = ""    
    d["extraTags"] = []
    for x in range(2,21+1):
        dd = d.copy()
        dd["oompDesc"] = "PI" + str(x).zfill(2)
        dd["hexID"] = "MCD" + str(x)
        d["name"] = "Connector Module DADB " + str(x) + " Pins"
        OOMP_modules_BASE.makeModule(dd)

        ######  DCJP
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "DCJP";    d["oompDesc"] = "21D"
    d["oompIndex"] = "01";    d["hexID"] = "MCD2"
    d["name"] = "Connector Module 2.1 mm DC Jack"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-CONN-POWE-STAN-01"])
    oompParts = {}
    oompParts["J1"] = {"OOMPID" : "DCJP-21D-X-STAN-01"}    
    d["extraTags"].append(["oompParts",oompParts]) 
    OOMP_modules_BASE.makeModule(d)
        ######  I2C
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "I2C";    d["oompDesc"] = "QWIIC"
    d["oompIndex"] = "01";    d["hexID"] = "MCQ"
    d["name"] = "Connector Module I2C QWIIC"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-CONN-I2C-STAN-01"])
    oompParts = {}
    oompParts["J1"] = {"OOMPID" : "HEAD-JSTSH-X-PI04-01"}    
    d["extraTags"].append(["oompParts",oompParts]) 
    OOMP_modules_BASE.makeModule(d)
        ######  I2C
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "I2C";    d["oompDesc"] = "QWIIC"
    d["oompIndex"] = "I01";    d["hexID"] = "MCQI01"
    d["name"] = "Connector Module I2C QWIIC"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-CONN-I2C-STAN-01"])
    oompParts = {}
    oompParts["J1"] = {"OOMPID" : "HEAD-I01-X-PI04-RS"}    
    d["extraTags"].append(["oompParts",oompParts]) 
    
    OOMP_modules_BASE.makeModule(d)
        ######  ISP
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "ISP";    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01";    d["hexID"] = "MCISP"
    d["name"] = "Connector Module ISP Programming"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-CONN-PROG-STAN-01"])
    oompParts = {}
    oompParts["J1"] = {"OOMPID" : "HEAD-I01-X-PI2X03-01"}    
    d["extraTags"].append(["oompParts",oompParts]) 
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "ISP";    d["oompDesc"] = "STAN"
    d["oompIndex"] = "SM";    d["hexID"] = "MCISPSM"
    d["name"] = "Connector Module ISP Programming (SMD)"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-CONN-PROG-STAN-01"])
    oompParts = {}
    oompParts["J1"] = {"OOMPID" : "HEAD-I01-X-PI2X03-SM"}    
    d["extraTags"].append(["oompParts",oompParts]) 
    
    OOMP_modules_BASE.makeModule(d)


        ######  OOBB
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "OOBB";    d["oompDesc"] = "BA"
    d["oompIndex"] = "01";    d["hexID"] = "MCOBA"
    d["name"] = "Connector Module OOBB Basic"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-CONN-OOBB-BA-01"])        
    oompParts = {}
    oompParts["J1"] = {"OOMPID" : "HEAD-I01-X-PI03-RA"}    
    d["extraTags"].append(["oompParts",oompParts]) 
    OOMP_modules_BASE.makeModule(d)
        ######  OOML
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "OOML";    d["oompDesc"] = "LED2X3"
    d["oompIndex"] = "01";    d["hexID"] = "MCOL23"
    d["name"] = "Connector Module 2x3 Header for LED Power"    
    d["extraTags"] = []
    #d["extraTags"].append(["matchingBlock","BLOCK-CONN-OOBB-BA-01"])
    
    oompParts = {}
    oompParts["J1"] = {"OOMPID" : "HEAD-I01-X-PI2X03-01"}    
    d["extraTags"].append(["oompParts",oompParts]) 
    
    OOMP_modules_BASE.makeModule(d)
        ######  RASP
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "RASP";    d["oompDesc"] = "PICO"
    d["oompIndex"] = "2040";    d["hexID"] = "MCRP2040"
    d["name"] = "Connector Module Raspberry Pi Pico 2040 01"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-CONN-RASP-PICO-2040"])
    oompParts = {}
    oompParts["J1"] = {"OOMPID" : "HEAD-I01-X-PI20-01"}
    oompParts["J2"] = {"OOMPID" : "HEAD-I01-X-PI20-01"}    
    d["extraTags"].append(["oompParts",oompParts]) 
    OOMP_modules_BASE.makeModule(d)
        ######  USB
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "USB";    d["oompDesc"] = "MICRO"
    d["oompIndex"] = "01";    d["hexID"] = "MCUMC"
    d["name"] = "Connector Module USB Micro"    
    d["extraTags"] = []
    oompParts = {}
    oompParts["J1"] = {"OOMPID" : " USBS-TC-X-K31-01"}
    d["extraTags"].append(["oompParts",oompParts]) 
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "USB";    d["oompDesc"] = "MEGA"
    d["oompIndex"] = "01";    d["hexID"] = "MCUMEGA"
    d["name"] = "Connector Module USB Mega (Universal Micro and C31 Type C)"    
    d["extraTags"] = []
    oompParts = {}
    d["extraTags"].append(["oompParts",oompParts]) 
    
    OOMP_modules_BASE.makeModule(d)

    ############################################################
    ######  MCUU
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "MCUU"
    d["oompColor"] = "ATTINY84";    d["oompDesc"] = "SO14"
    d["oompIndex"] = "01";    d["hexID"] = "MMAT84S"
    d["name"] = "Microcontroller Module ATTiny84 (SOIC 14)"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-MCUU-STAN-STAN-01"])
    oompParts = {}
    oompParts["U1"] = {"OOMPID" : "MCUU-SC14-84-ATTINY-01"}
    oompParts["C2"] = {"OOMPID" : "CAPC-0603-X-NF100-V50"}    
    d["extraTags"].append(["oompParts",oompParts]) 
    
    OOMP_modules_BASE.makeModule(d)
    
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "MCUU"
    d["oompColor"] = "K328";    d["oompDesc"] = "MUR"
    d["oompIndex"] = "01";    d["hexID"] = "MM328M"
    d["name"] = "MCU Module ATMega 328 (MUR)"    
    d["extraTags"] = []
    OOMP_modules_BASE.makeModule(d)

    ############################################################
    ######  MOSN
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "MOSN"
    d["oompColor"] = "K4184";    d["oompDesc"] = "T252"
    d["oompIndex"] = "TL";    d["hexID"] = "MMN4184252TL"
    d["name"] = "N Channel Mosfet Module K4184 (T252) (Transistor Logic Added)"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-MCUU-STAN-STAN-01"])
    oompParts = {}
    oompParts["Q1"] = {"OOMPID" : "MOSN-T252-X-K4184-01"}
    oompParts["Q2"] = {"OOMPID" : "TRNN-SO23-X-KSS8050-01"}    
    d["extraTags"].append(["oompParts",oompParts]) 
    OOMP_modules_BASE.makeModule(d)

    ############################################################
    ######  POWE
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "POWE"
    d["oompColor"] = "KAP2112K";    d["oompDesc"] = "SO235"
    d["oompIndex"] = "V33D";    d["hexID"] = "MP2112"
    d["name"] = "Power Module AP2112K"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-POW-STAN-STAN-01"])
    oompParts = {}
    oompParts["U1"] = {"OOMPID" : "VREG-SO235-X-KAP2112K-V33D"}
    oompParts["C1"] = {"OOMPID" : "CAPC-0603-X-NF100-V50"}
    oompParts["C2"] = {"OOMPID" : "CAPC-0603-X-NF100-V50"}
    d["extraTags"].append(["oompParts",oompParts]) 
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "POWE"
    d["oompColor"] = "KLD1117";    d["oompDesc"] = "SO223"
    d["oompIndex"] = "V33D";    d["hexID"] = "MP1117"
    d["name"] = "Power Module LD1117"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-POW-STAN-STAN-01"])
    oompParts = {
    "U1" : {"OOMPID" : "VREG-SO235-X-KAP2112K-V33D"},
    "C1" : {"OOMPID" : "CAPC-0603-X-NF100-V50"},
    "C2" : {"OOMPID" : "CAPC-0603-X-NF100-V50"}
    }
    d["extraTags"].append(["oompParts",oompParts]) 
    OOMP_modules_BASE.makeModule(d)

    ############################################################
    ######  SENS    
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "SENS"
    d["oompColor"] = "K345";    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01";    d["hexID"] = "MS345"
    d["name"] = "Sensor Module ADXL345"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-SENS-ACCEL-I2C-01"])
    oompParts = {
    "U1" : {"OOMPID" : "SENS-LG14-X-K345-01"}
    }
    d["extraTags"].append(["oompParts",oompParts]) 

    OOMP_modules_BASE.makeModule(d)
    
    
    ############################################################
    ######  XTAL
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "XTAL"
    d["oompColor"] = "5032";    d["oompDesc"] = "MZ16"
    d["oompIndex"] = "01";    d["hexID"] = "MX53M16"
    d["name"] = "Crystal Module 5032 16 MHz"    
    d["extraTags"] = []
    OOMP_modules_BASE.makeModule(d)

    ############################################################
    ######  DADB
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "DADB"
    d["oompColor"] = "MCUU";    d["oompDesc"] = "K328"
    d["oompIndex"] = "01";    d["hexID"] = "MD328M"
    d["name"] = "DADB Module ATMega 328 (MUR)"    
    d["extraTags"] = []
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "DADB"
    d["oompColor"] = "CONN";    d["oompDesc"] = "HEADI01PI15"
    d["oompIndex"] = "01";    d["hexID"] = "MDCI15"
    d["name"] = "DADB Module Connector 2.54mm 15 Pin"    
    d["extraTags"] = []    
    OOMP_modules_BASE.makeModule(d)
