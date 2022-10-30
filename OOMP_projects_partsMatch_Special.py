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
    list.append([["JST_SH_SM04B-SRSS-TB_1x04-1MP_P1.00mm_Horizontal","STEMMA_I2C","QWIIC","I2C_STANDARDJS-1MM"],"HEAD-JSTSH-X-PI04-RS"])
        ###### ISP Programmer
    list.append([["AVR_SPI_PRG"],"HEAD-JSTSH-X-PI04-RS"])      
        ###### Raspberry Pi  
    list.append([["RASPBERRYPI_BPLUS_BONNET_THMSMT"],"HEAD-I01-X-PI2X20-01"])      
        
    ###### MCUU
        ###### ATTINY
        ###### TODO ADD SIZE differentiation
    list.append([["ATTINY84"],"MCUU-SC14-84-ATTINY-01"])        
    ###### SENS
        ###### ADXL345
    list.append([["ADXL345"],"SENS-LG14-X-K345-01"])
    list.append([["ADXL343"],"SENS-LG14-X-K345-01"])


    for l in list:
        #if l[0].upper() in partDict["FULL"].upper():
        include = False        
        for x in l[0]:
            if x in partDict["FULL"]:
                oompID = l[1]


    return oompID