import OOMP
import OOMP_projects_BASE

def createProjects():
    projects = []
    
    count = 1
    base = {}
    base["oompSize"] = "PDP7"
    base["format"] = "kicad"
    base["github"] = "https://github.com/pdp7/"
    base["oompIndex"] = "01"    ###### default to rev 01

    #############################################################
    #############################################################    

    projectStrings = []
    projectStrings.append("kicad-teensy-epaper")
    projectStrings.append(["teensy-touch","hardware/teensy-touch"])
    projectStrings.append(["TeensyEpaperShield","hardware/EpaperTeensyBoard"])
    projectStrings.append("rotary-encoder-breakout")
    projectStrings.append("gtb")
    projectStrings.append(["teensy-wifi-weather-logger","hardware/teensyi2c"])
    projectStrings.append(["art","art","Art 01"])
    projectStrings.append(["art","art2","Art 02"])
    projectStrings.append(["art","art3","Art 03"])
    projectStrings.append(["art","flower-v3","Flower v3"])
    projectStrings.append(["art","leaf","Leaf"])
    projectStrings.append(["art","sixlayer"])
    projectStrings.append(["teensy-weather-badge","hardware/teensyi2c"])

    



    #############################################################
    for item in projectStrings:
        if isinstance(item, list):
            repo = item[0]
            file = item[1]
            if len(item) > 2:
                name = item[2]
            else:
                name = item[1]
        else:
            repo = item
            file = item
            name = item
        if repo != "":
            d = base.copy()    
            d["repo"] = repo
            d["file"] = file.replace("_hw","")    
            d["name"] = name.replace("_hw","").replace("_"," ").capitalize()
            d["count"] = count; count = count + 1
            projects.append(d)

    for d in projects:
        OOMP_projects_BASE.makeProjectNew(d)

