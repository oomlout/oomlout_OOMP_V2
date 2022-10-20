import OOMP
import OOMP_projects_partsMatch

def matchColor(project,part,oompType="",oompSize="",oompColor="",oompDesc="",oompIndex=""):
    global PART, VALUE, DEVICE, PACAKGE, DESC, BOM    
    partDict = OOMP_projects_partsMatch.loadPartDict(part,project)   
    projectDict = OOMP_projects_partsMatch.loadProjectDict(project)

    rv= "X"

    if oompType == "LEDS":
        rv = "G"
        if "RGB" in partDict["VALUE"] or "2812" in partDict["VALUE"] or "2811" in partDict["VALUE"]:
            return "RGB"
        if "APA102" in partDict["PACKAGE"]:
            return "RGB"
        if projectDict["OWNER"] == "ADAF":
            if projectDict["INDEX"] == "3467":
                return "L"
            if projectDict["INDEX"] == "3134":
                return "R"
            if projectDict["INDEX"] == "2946":
                return "W"
        list = []
        list.append(["RED","R"])
        list.append(["ORANGE","O"])
        list.append(["YELLOW","Y"])
        list.append(["GREEN","G"])
        list.append(["BLUE","L"])
        list.append(["PINK","P"])

        for l in list:
            if l[0] in partDict["VALUE"].upper():
                return l[1]

    ######  SCREW TERMINAL
    if oompType == "TERS":        
        list = []
        list.append(["SCREWTERMINAL-3.5MM-","L"])
        list.append(["3.5MM","L"])

        for l in list:
            if l[0] in partDict["PACKAGE"].upper():
                return l[1]


    return rv

