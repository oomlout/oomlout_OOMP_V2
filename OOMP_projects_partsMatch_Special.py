import OOMP
import OOMP_projects_partsMatch

def matchSpecial(project,part,oompType="",oompSize="",oompColor="",oompDesc="",oompID=""):  
    partDict = OOMP_projects_partsMatch.loadPartDict(part,project)   

    ######  Full text test
    list = []
    ###### BUTA
    list.append([["MOMENTARY-SWITCH-SPST-LED-PTH-12MM"],"BUTA-12-X-LEDS-01"])
    ###### HEAD
        ###### QWIIC Connector
    list.append([["JST_SH_SM04B-SRSS-TB_1x04-1MP_P1.00mm_Horizontal"],"HEAD-JSTSH-X-PI04-RS"])
    list.append([["STEMMA_I2C"],"HEAD-JSTSH-X-PI04-RS"])
    list.append([["QWIIC"],"HEAD-JSTSH-X-PI04-RS"])    
    ###### MCUU
        ###### ATTINY
    list.append([["ATTINY84","SO14"],"HEAD-JSTSH-X-PI04-RS"])        
    ###### SENS
        ###### ADXL345
    list.append([["ADXL345"],"SENS-LG14-X-K345-01"])
    list.append([["ADXL343"],"SENS-LG14-X-K345-01"])


    for l in list:
        #if l[0].upper() in partDict["FULL"].upper():
        include = False
        if all(x in partDict["FULL"] for x in l[0]):
            oompID = l[1]


    return oompID