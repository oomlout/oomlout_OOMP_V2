import OOMP
import OOMP_projects_partsMatch

specialMatches  =[]

def loadMatches():
    global specialMatches

    list  =[]
    for partID in OOMP.itemsTypes["parts"]["items"]:
        matchSpecial = OOMP.items[partID]["matchSpecial"]
        if len(matchSpecial) > 0:
            for match in matchSpecial:
                list.append(match)

    ###### legacy 
    ###### BUTA
    list.append([["MOMENTARY-SWITCH-SPST-LED-PTH-12MM"],"BUTA-12-X-LEDS-01"])
        
    ###### MCUU

    specialMatches = list


def matchSpecial(project,part,oompType="",oompSize="",oompColor="",oompDesc="",oompID=""):  
    global specialMatches
    partDict = OOMP_projects_partsMatch.loadPartDict(part,project)   

    ######  Full text test
    oompID = ""
    list = specialMatches
    for l in list:
        #if l[0].upper() in partDict["FULL"].upper():
        include = False        
        for x in l[0]:
            if x in partDict["FULL"]:
                oompID = l[1]

    return oompID