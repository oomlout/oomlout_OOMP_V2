from oomBase import *
from OOMPeda import *
import OOMP
import OOMPprojectHarvest
import os
import shutil
import subprocess

##################
######  Adafruit Section

def harvestProjectsAdafruit():
    srcDir = "oomlout_OOMP_projects\sourceFiles/adafruit/"
    print("Harvesting Adafruit!")
    directory = srcDir
    for dir in os.listdir(directory):
        if(os.path.isdir(directory)):
            print("    Harvesting: " + srcDir + dir)
            processProjectDirAdafruit(srcDir + dir + "/")
            

def processProjectDirAdafruit(directory):
    hardwareDir = directory 
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
            name = directory.replace("oomlout_OOMP_projects\sourceFiles/sparkfun/","").replace("-"," ").replace("/","").replace("\\","")
            if file.lower() == "license.txt":
                #print("        Found License")
                licenseFile = directory+file
            if file.lower() == "readme.md":
                #print("        Found Readme")
                readme = oomReadFileToString(directory+file)
                readmeFile = directory+file
                index = stringBetween(readme,'href="http://www.adafruit.com/products/','">')
                if not index.isnumeric():                    
                    ###### for debugging skipped repositories
                    c=0    
                
                #print ("            Index: " + str(index))

        ###### Hardware Folder
        files = [f for f in os.listdir(hardwareDir)]   
        for file in files:
            #print(file)
            if ".brd" in file.lower():                
                #print("        Found Board")
                boardFile = hardwareDir+file
            if ".sch" in file.lower():
                #print("        Found Schematic")
                schematicFile = hardwareDir+file

        if index != 0 and index != "" and boardFile != "" and schematicFile != "" :
            ############ Making OOMP file
            oompType = "PROJ"
            oompSize = "ADAF"
            oompColor = str(index)
            oompDesc = "STAN"
            oompIndex = "01" 
            hexID = "PRA" + index   
            directory = "oomlout_OOMP_projects/" + oompType + "-"  + oompSize + "-"  + oompColor + "-"  + oompDesc + "-"  + oompIndex + "/"
            oomMakeDir(directory)  

            fileName = directory + "details.py"
            f = open(fileName,"w")
            name = name
            f.write(OOMP.getFileOpening(hexID,oompType,oompSize,oompColor,oompDesc,oompIndex,name))
            ###### extra details
            f.write(OOMP.getAddTagLine("sources","All source files from https://github.com/adafruit/" + name.replace(" ","-") + " (source licence details in srcLicense.md)"))
            f.write(OOMP.getAddTagLine("linkBuyPage","http://www.adafruit.com/products/" + str(index)))

            f.write("\n")
            f.write(OOMP.getFileEnding())
            f.close()


            ############ Moving Files
            if readmeFile != "":
                oomCopyFile(readmeFile, directory + "srcReadme.md")
            if boardFile != "":
                oomCopyFile(boardFile, directory + "boardEagle.brd")
            if schematicFile != "":            
                oomCopyFile(schematicFile, directory + "schematicEagle.sch")
            if licenseFile != "":    
                oomCopyFile(licenseFile, directory + "srcLicense.md")

    else:
        print("SKIPING")
    #delay(1)
                            
                                
##################
######  Arduino Section
def harvestProjectsArduino():

    arduinoProjects = []

    oompID = ""
    eagleFiles = ""
    drawing = ""
    datasheet =""
    ###uno
    oompID = "PROJ-ARDU-UNO-REV3-01"
    eagleFiles = "https://content.arduino.cc/assets/UNO-TH_Rev3e-reference.zip"
    drawing = "http://arduino.cc/documents/ArduinoUno.dxf"
    datasheet ="https://docs.arduino.cc/resources/datasheets/A000066-datasheet.pdf"
    source = "https://store.arduino.cc/collections/boards/products/arduino-uno-rev3"
    #arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source])
    ###uno smd
    oompID = "PROJ-ARDU-UNO-REV3-SM"
    eagleFiles = "https://content.arduino.cc/assets/UNOSMD_V3.zip"
    drawing = "http://arduino.cc/documents/ArduinoUno.dxf"
    datasheet ="https://docs.arduino.cc/resources/datasheets/A000066-datasheet.pdf"
    source = "https://store.arduino.cc/collections/boards/products/arduino-uno-rev3-smd"
    #arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source])
    ###leo
    oompID = "PROJ-ARDU-LEO-STAN-01"
    eagleFiles = "https://content.arduino.cc/assets/Leonardo-reference.zip"
    drawing = ""
    datasheet =""
    source = "https://store.arduino.cc/collections/boards/products/arduino-leonardo-with-headers"
    #arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source])

    ###due
    oompID = "PROJ-ARDU-DUE-STAN-01"
    eagleFiles = "https://content.arduino.cc/assets/ArduinoDUE_v02g.zip"
    drawing = "https://content.arduino.cc/assets/Arduino_Due_Technical_Drawing.pdf"
    datasheet =""
    source = "https://store.arduino.cc/collections/boards/products/arduino-due"
    fritzing = "https://content.arduino.cc/assets/Arduino%20Due%20%28Rev2b%29.fzpz"
    arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source,fritzing])
    ###mega
    oompID = "PROJ-ARDU-MEGA-2560-01"
    eagleFiles = "https://content.arduino.cc/assets/MEGA2560_Rev3e-reference.zip"
    drawing = "http://arduino.cc/documents/dimensioniMega.dxf"
    datasheet =""
    source = "https://store.arduino.cc/collections/boards/products/arduino-mega-2560-rev3"
    fritzing = ""
    arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source,fritzing])

    ###nano
    oompID = "PROJ-ARDU-NANO-STAN-01"
    eagleFiles = "https://content.arduino.cc/assets/Nano-reference.zip"
    drawing = "https://content.arduino.cc/assets/arduino_nano_size.pdf"
    datasheet =""
    source = "https://store.arduino.cc/collections/boards/products/arduino-nano"
    fritzing = ""
    arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source,fritzing])

    ###micro ((files not in right location need to be moved brd and sch))
    oompID = "PROJ-ARDU-MICRO-STAN-01"
    eagleFiles = "https://content.arduino.cc/assets/Micro-reference-Eagle.zip"
    drawing = "http://arduino.cc/documents/dimensioniMicro.dxf"
    datasheet =""
    source = "https://store.arduino.cc/collections/boards/products/arduino-micro"
    fritzing = "https://content.arduino.cc/assets/Arduino%20Micro%20%28Rev3%29.fzpz"
    arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source,fritzing])
    ###nano0 every
    oompID = "PROJ-ARDU-NANO-EVERY-01"
    eagleFiles = "https://content.arduino.cc/assets/NanoEveryV30.zip"
    drawing = ""
    datasheet =""
    source = "https://store.arduino.cc/collections/boards/products/arduino-nano-every-with-headers"
    fritzing = "https://content.arduino.cc/assets/Arduino%20Nano%20Every.fzpz"
    arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source,fritzing])


    for projectDetails in arduinoProjects:
        downloadArduinoProject(projectDetails)

def downloadArduinoProject(projectDetails):
    oompID = projectDetails[0]
    eagleFiles = projectDetails[1]
    drawing = projectDetails[2]
    datasheet = projectDetails[3]
    source = projectDetails[4]
    if len(projectDetails) > 5:
        fritzing = projectDetails[5]
    directory = "oomlout_OOMP_projects/" + oompID + "/"
    oomMakeDir(directory)
    tempDir = "oomlout_OOMP_projects/sourceFiles/tempT/"
    oomMakeDir(tempDir)
    ######  unzip board files
    url = eagleFiles
    saveFile = tempDir + "board.zip"
    oomSaveUrl(url,saveFile)
    filename = saveFile
    dirName = tempDir
    oomUnzip(filename,dirName,deleteZip=True)
    boardFile = ""
    schematicFile = ""
    files = [f for f in os.listdir(tempDir)]   
    for file in files:
        print(file)
        if ".brd" in file.lower():                
            print("        Found Board")
            boardFile = tempDir+file
        if ".sch" in file.lower():
            print("        Found Schematic")
            schematicFile = tempDir+file
    ###### datasheet
    if datasheet != "":
        url = datasheet
        saveFile = directory + "datasheet.pdf"
        oomSaveUrl(url,saveFile)
    ###### drawing        
    if drawing != "":
        url = drawing
        saveFile = ""
        if ".dxf" in url:
            saveFile = directory + "diagram.dxf"
        else:
            saveFile = directory + "diagram.pdf"    
        oomSaveUrl(url,saveFile)
    ###### fritzing        
    if fritzing != "":
        url = fritzing
        saveFile = directory + "fritzing.fzpz"
        oomSaveUrl(url,saveFile)
    ######  copy files        
    if boardFile != "":
        oomCopyFile(boardFile, directory + "boardEagle.brd")
    if schematicFile != "":            
        oomCopyFile(schematicFile, directory + "schematicEagle.sch")

    ############ Making OOMP file
    oomp = oompID.split("-")
    oompType = oomp[0]
    oompSize = oomp[1]
    oompColor = oomp[2]
    oompDesc = oomp[3]
    oompIndex = oomp[4] 
    hexID = "PRAR" + oompDesc   
    directory = "oomlout_OOMP_projects/" + oompType + "-"  + oompSize + "-"  + oompColor + "-"  + oompDesc + "-"  + oompIndex + "/"
    oomMakeDir(directory)  

    fileName = directory + "details.py"
    f = open(fileName,"w")
    f.write(OOMP.getFileOpening(hexID,oompType,oompSize,oompColor,oompDesc,oompIndex))
    ###### extra details
    f.write(OOMP.getAddTagLine("sources","All source files from " + source))
    f.write(OOMP.getAddTagLine("linkBuyPage",source))

    f.write("\n")
    f.write(OOMP.getFileEnding())
    f.close()



    oomDeleteDirectory(tempDir, safety=False)        


##################
######  Sparkfun Section

def harvestProjectsSparkfun():
    srcDir = "oomlout_OOMP_projects\sourceFiles/sparkfun/"
    print("Harvesting Sparkfun!")
    directory = srcDir
    for dir in os.listdir(directory):
        if(os.path.isdir(directory)):
            print("    Harvesting: " + srcDir + dir)
            processProjectDirSparkfun(srcDir + dir + "/")
            

def processProjectDirSparkfun(directory):
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
                index = stringBetween(readme,"https://www.sparkfun.com/products/",")")
                if not index.isnumeric():
                    index = stringBetween(readme,'href="https://www.sparkfun.com/products/','">')   
                if not index.isnumeric():
                    index = stringBetween(readme,'href="https://www.sparkfun.com/products/','">')   
                if not index.isnumeric():
                    ###### for debugging skipped repositories
                    c=0    
                
                print ("            Index: " + str(index))

        ###### Hardware Folder
        files = [f for f in os.listdir(hardwareDir)]   
        for file in files:
            print(file)
            if ".brd" in file.lower():                
                print("        Found Board")
                boardFile = hardwareDir+file
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
            directory = "oomlout_OOMP_projects/" + oompType + "-"  + oompSize + "-"  + oompColor + "-"  + oompDesc + "-"  + oompIndex + "/"
            oomMakeDir(directory)  

            fileName = directory + "details.py"
            f = open(fileName,"w")
            name = name
            f.write(OOMP.getFileOpening(hexID,oompType,oompSize,oompColor,oompDesc,oompIndex,name))
            ###### extra details
            f.write(OOMP.getAddTagLine("sources","All source files from https://github.com/sparkfun/" + name.replace(" ","_") + " (source licence details in srcLicense.md)"))
            f.write(OOMP.getAddTagLine("linkBuyPage","https://www.sparkfun.com/products/" + str(index)))

            f.write("\n")
            f.write(OOMP.getFileEnding())
            f.close()


            ############ Moving Files
            if readmeFile != "":
                oomCopyFile(readmeFile, directory + "srcReadme.md")
            if boardFile != "":
                oomCopyFile(boardFile, directory + "boardEagle.brd")
            if schematicFile != "":            
                oomCopyFile(schematicFile, directory + "schematicEagle.sch")
            if licenseFile != "":    
                oomCopyFile(licenseFile, directory + "srcLicense.md")

    else:
        print("SKIPING")
            #delay(1)
                            
