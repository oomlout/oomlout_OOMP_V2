import OOMP
import OOMP_projects
import OOMP_projects_BASE
import OOMP_projects_SPAR_generated
from oomBase import *
import json


###### Geto repos
def farmProjects():
    OOMP_projects_BASE.farmProjects(user="sparkfun",code="SPAR")
    OOMP_projects_BASE.farmProjects(user="sparkfunx",code="SPAR")


def makeBaseProjects():
    OOMP_projects_BASE.makeBaseProjects(company="sparkfun",code="SPAR")    
###### make projects from json file of repos


def createProjects():
    OOMP_projects_SPAR_generated.createProjects()
    projects = []

    count = 1
    base = {}
    base["oompType"] = "PROJ"
    base["oompSize"] = "SPAR"
    base["format"] = "eagle"
    
    base["github"] = "https://github.com/sparkfun/"

    projects = []

    d = base.copy()
    d["name"] = "Qwiic EEPROM - 512Kbit"
    d["repo"] = "Qwiic_EEPROM_Breakout"
    d["file"] = "Qwiic AHT20 Breakout"
    d["count"] = 18355    
    projects.append(d.copy())



    ###### SparkFun X Projects
    base["github"] = "https://github.com/sparkfunX/"
    d = base.copy()
    d["name"] = "SparkFun Qwiic Humidity AHT20"
    d["repo"] = "Qwiic_Humidity_AHT20"
    d["file"] = "Hardware/Qwiic EEPROM"
    d["count"] = 16618    
    projects.append(d.copy())

    d = base.copy()
    d["name"] = "Qwiic BMP388 Pressure Sensor"
    d["repo"] = d["name"].replace(" ","_")
    d["file"] = "Hardware/" + d["repo"]
    d["count"] = 17001    
    projects.append(d.copy())


    for d in projects:
        OOMP_projects_BASE.makeProjectNew(d)

    count = count +1


def processDirSparkfun(directory,d):
    hardwareDir = directory + "Hardware/"
    hardwareDir2 = directory + "Hardware/Qwiic Micro/"
    readmeFile = ""
    boardFile = ""
    schematicFile = ""
    licenseFile = ""
    index = 0

    ############ Finding Files
    ###### Test if it has a hardware path
    if os.path.isdir(hardwareDir):
        files = [f for f in os.listdir(directory)]
        #print(files)
        for file in files:
            name = directory.replace("oomlout_OOMP_projects\sourceFiles/sparkfun/","").replace("_"," ").replace("/","").replace("\\","")
            if file.lower() == "license.md":
                print("        Found License")
                licenseFile = directory+file
            if file.lower() == "readme.md":
                print("        Found Readme")
                readme = oomReadFileToString(directory+file)
                readmeFile = directory+file
                index = stringBetween(readme,"https://www.sparkfun.com/products/","\\)")
                if not index.isnumeric():
                    index = stringBetween(readme,'href="https://www.sparkfun.com/products/','">')   
                if not index.isnumeric():
                    index = stringBetween(readme,'href="https://www.sparkfun.com/products/','">')   
                if not index.isnumeric():
                    ###### for debugging skipped repositories
                    c=0    
                d["count"] = index
                print ("            Index: " + str(index))

        ###### Hardware Folder
        files = [f for f in os.listdir(hardwareDir)]   
        for file in files:
            print(file)
            if ".brd" in file.lower():                
                print("        Found Board")
                boardFile = hardwareDir+file
                d["file"] = file
            if ".sch" in file.lower():
                print("        Found Schematic")
                schematicFile = hardwareDir+file
        ###### test for qwiic nested files   
        if index == "20170":
            c=0
        if os.path.isdir(hardwareDir2) and boardFile == "":
            files = [f for f in os.listdir(hardwareDir2)]   
            for file in files:
                print(file)
                if ".brd" in file.lower():                
                    print("        Found Board")
                    d["file"] = file
                    boardFile = hardwareDir2+file
                if ".sch" in file.lower():
                    print("        Found Schematic")
                    schematicFile = hardwareDir2+file                   

        if index != 0 and index != "" and boardFile != "" and schematicFile != "" :
            ############ Making OOMP file
            oompType = "PROJ"
            oompSize = "SPAR"
            oompColor = str(index)
            oompDesc = "STAN"
            oompIndex = "01" 
            hexID = "PRS" + index   
            directory = OOMP.getDir("projects") + oompType + "/"  + oompSize + "/"  + oompColor + "/"  + oompDesc + "/"  + oompIndex + "/"
            oomMakeDir(directory)  

            ############ Moving Files
            if readmeFile != "":
                oomCopyFile(readmeFile, directory + "srcReadme.md")
            if boardFile != "":
                pass
                #oomCopyFile(boardFile, directory + "boardEagle.brd")
            if schematicFile != "":            
                pass
                #oomCopyFile(schematicFile, directory + "schematicEagle.sch")
            if licenseFile != "":    
                oomCopyFile(licenseFile, directory + "srcLicense.md")

            extraTags = []
            extraTags.append(["sources","All source files from https://github.com/sparkfun/" + name.replace(" ","_") + " (source licence details in srcLicense.md)"])
            extraTags.append(["linkBuyPage","https://www.sparkfun.com/products/" + str(index)])

            d["name"] = name
            #d["repo"] = "Qwiic_EEPROM_Breakout"
            #d["file"] = "Qwiic AHT20 Breakout"
            #d["count"] = 18355            

            return d
        return None
    else:
        print("SKIPING")
            #delay(1)
        return None
