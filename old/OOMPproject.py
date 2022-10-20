from oomBase import *
from OOMPeda import *
import OOMP
import OOMPprojectHarvest
import OOMPprojectParts
import os
import shutil
import subprocess

    ##################
    ######  Projects Harvesting Stuff

def harvestEagleBoardToKicad(file,directory,overwrite=False):
    ######  open kicad launch window and place in topleft corner 
    # need a blank project loaded 
    dirKicad =   OOMP.baseDir + directory + "kicad/"
    oomMakeDir(dirKicad)
    boardKicad = dirKicad + "boardKicad.kicad_pcb"
    boardEagle = OOMP.baseDir + "boardEagle.brd"
    print(    "HarvestEagleBoardToKicad: " + file)
    if (overwrite or not os.path.exists(boardKicad)) and os.path.exists(boardEagle):
        oomLaunchKicad()
        oomDelay(10)
        oomMouseClick(pos=kicadActive,delay=5)       
        oomMouseClick(pos=kicadFile,delay=5)       
        #oomSendAltTab(1,delay=3)
        #oomSendAltTab(1,delay=3)


        #oomMouseMove(pos=kicadFootprintMiddle,delay=2)         
        #oomMouseClick(pos=kicadActive,delay=2)       
        #oomMouseMove(pos=kicadFootprintMiddle,delay=2)         
        #oomSendAltKey("v",10)
        #oomSendLeft(1,delay=2)
        oomSendDown(8,delay=2)
        oomSendRight(1,delay=2)
        oomSendDown(1,delay=2)
        oomSendEnter(delay=5)
        ###### filedialog box open
        filename = (OOMP.baseDir + file).replace("/","\\")
        oomSend(filename,5)
        oomSendEnter(10)
        ######  set temp folder
        tempDir = OOMP.baseDir + "oomlout_OOMP_projects/sourceFiles/tempB/"
        
        
        oomDeleteDirectory(tempDir + "boardEagle.pretty/", safety=False)
        oomDeleteDirectory(tempDir + "boardEagle-backups/", safety=False)        
        #oomDeleteDirectory(tempDir, safety=False)
        oomMakeDir(tempDir)
        oomSend(tempDir.replace("/","\\"),2)
        oomSendEnter(5)        
        oomSendEnter(10)
        oomSend("y",10)
        ######  match layers dialog
        oomSendTab(6,5)
        oomSendEnter(2)
        oomSendTab(1,2)
        oomSendEnter(10)
        oomSendEsc(2)
        oomSendEsc(2)
        oomSendEsc(2)
        oomDelay(15)
        oomMouseClick(pos=kicadFootprintMiddle,delay=2)
        oomSendEsc(delay=2)
        #fill zones
        oomSend("b",15)
        ######  save board
        #oomSendAltKey("f",2)
        oomMouseClick(pos=kicadFile,delay=5)
        oomSendDown(2,delay=2)
        oomSendEnter(delay=5)
        oomSend(boardKicad.replace("/","\\").replace("\\\\","\\"),2)
        oomSendEnter(delay=10)
        oomSend("y",2)
        oomSendEnter(delay=2)
        ###### close project
        kicadClosePcb(False)
    else:
        print("        SKIPPING")


def harvestEagleSchemToKicad(file,directory,overwrite=False):
    ######  open kicad launch window and place in topleft corner 
    # need a blank project loaded 
    dirKicad =   OOMP.baseDir + directory + "kicad/"
    oomMakeDir(dirKicad)
    boardKicad = dirKicad + "schematicKicad.kicad_sch"
    boardEagle = OOMP.baseDir + directory + "schematicEagle.sch"
    print(    "HarvestEagleSchematicToKicad: " + file)
    if (overwrite or not os.path.exists(boardKicad)) and os.path.exists(boardEagle):
        oomMouseClick(pos=kicadActive,delay=5)       
        oomMouseClick(pos=kicadFile,delay=5)       
        oomSendDown(8,delay=2)
        oomSendRight(1,delay=2)
        oomSendDown(1,delay=2)
        oomSendEnter(delay=5)
        ###### filedialog box open
        filename = (OOMP.baseDir + file).replace("/","\\")
        oomSend(filename,5)
        oomSendEnter(10)
        ######  set temp folder
        tempDir = OOMP.baseDir + "oomlout_OOMP_projects/sourceFiles/tempB/"
        
        
        oomDeleteDirectory(tempDir + "boardEagle.pretty/", safety=False)
        oomDeleteDirectory(tempDir + "boardEagle-backups/", safety=False)        
        #oomDeleteDirectory(tempDir, safety=False)
        oomMakeDir(tempDir)
        oomSend(tempDir.replace("/","\\"),2)
        oomSendEnter(5)        
        oomSendEnter(10)
        oomSend("y",10)
        
        ######  save board
        #oomSendAltKey("f",2)
        oomMouseClick(pos=kicadFile,delay=5)
        oomSendDown(2,delay=2)
        oomSendEnter(delay=5)
        oomSend(boardKicad.replace("/","\\").replace("\\\\","\\"),2)
        oomSendEnter(delay=10)
        oomSend("y",2)
        oomSendEnter(delay=2)
        ###### close project
        kicadClosePcb(False)
    else:
        print("        SKIPPING")  
        

def kicadClosePcb(noSave=True):
    #oomSendAltKey("f",2)
    oomMouseClick(pos=kicadFile,delay=5)
    oomSendUp(delay=2)
    oomSendEnter(delay=2)
    if noSave:
        oomSendRight(delay=2)
    oomSendEnter(delay=20)




#### 285 seconds per (12 an hour) (1000 in 80 hours) (33 days for 10000)
def harvestKicadBoardFile(file="",directory="",part="",overwrite=False,filter="projects"):
    
    boardKicad = ""
    dirKicad = ""
    if part != "":
        boardKicad = part.getFilename("boardKicad")
        dirKicad = part.getFilename("dirKicad")
        directory = part.getDir()
    else:
        dirKicad =   OOMP.baseDir + directory + "kicad/"
        boardKicad = dirKicad + "boardKicad.kicad_pcb"
    print("Harvesting Kicad Board File: " + boardKicad)
    if os.path.isfile(boardKicad) and (overwrite or True):
        if overwrite or not os.path.isfile(directory + "kicadPcb3d.png"):
            oomLaunchPopen("pcbnew.exe " + boardKicad,10)
            oomMouseMove(pos=kicadFootprintMiddle,delay=2)
            oomSend("b",10)
            oomMouseClick(pos=kicadActive,delay=5)    
            filename = OOMP.baseDir + directory + "kicad/"
            oomMakeDir(filename)
            if filter == "projects":
                kicadExport(filename,"bom",overwrite=overwrite)
            if filter == "projects":    
                kicadExport(filename,"pos",overwrite=overwrite)                
            kicadExport(filename,"svg",overwrite=overwrite)            
            kicadExport(filename,"wrl",overwrite=overwrite)
            kicadExport(filename,"step",overwrite=overwrite)
            filename = OOMP.baseDir + directory
            kicadExport(filename,"3dRender",overwrite=overwrite)
        

            kicadClosePcb()

def harvestKicadSchemFile(file="",directory="",part="",overwrite=False,filter="projects"):
    
    boardKicad = ""
    dirKicad = ""
    if part != "":
        boardKicad = part.getFilename("schemKicad")
        dirKicad = part.getFilename("dirKicad")
        directory = part.getDir()

    else:
        dirKicad =   OOMP.baseDir + directory + "kicad/"
        boardKicad = dirKicad + "schematicKicad.kicad_sch"
    imageFile = directory + "kicadSchem.png"
    print("Harvesting Kicad Board File: " + boardKicad)
    if os.path.isfile(boardKicad) and (overwrite or True):
        if overwrite or not os.path.isfile(imageFile):
            oomLaunchPopen("eeschema.exe " + boardKicad,10)
            oomMouseMove(pos=kicadFootprintMiddle,delay=2)
            oomMouseMove(pos=kicadActive,delay=2)
            oomMouseMove(pos=kicadFootprintMiddle,delay=2)
            oomMouseMove(pos=kicadActive,delay=2)
            oomMouseMove(pos=kicadFootprintMiddle,delay=2)
            oomMouseMove(pos=kicadActive,delay=2)
            oomMouseMove(pos=kicadFootprintMiddle,delay=2)
            oomMouseClick(pos=kicadActive,delay=5)    
            
            #oomSendAltKey("f",delay=2)            
            oomMouseClick(pos=kicadFile,delay=5)   
            oomSend("e",1)
            oomSendEnter(delay=2)
            oomClipboardSaveImage(imageFile)



            kicadClosePcb()
            oomSendEsc(delay=5)

def harvestEagleSchematicFile(file,directory,overwrite=False):
    dxfFile = OOMP.baseDir + directory + "eagleImage.dxf"
    imageFile = OOMP.baseDir + directory + "eagleSchemImage.png"
    partFile = OOMP.baseDir + directory + "eagleBOM.csv"
    #if overwrite or not os.path.exists(dxfFile):
    #if overwrite or not os.path.exists(pngFile):
    print("Harvesting Eagle Schematic: " + file)
    if(os.path.exists(file)):
        if overwrite or  (not os.path.exists(partFile) or not os.path.exists(imageFile)):
            oomLaunchEagle(OOMP.baseDir + file)
            oomDelay(45)
            ##### no back annotation message
            oomSendEnter(delay=2)  
            ##### no back annotation message
            oomSendEnter(delay=2)    
                
            oomSendMaximize()
            oomDelay(2)
            oomSendMaximize()
            oomDelay(2)
            #oomMouseClick(pos=kicadActive,delay=5)            
            oomSendControl("o",delay=5)
            #oomSendAltKey("f",2)
            #oomSend("o",1)
            #oomSend("b",1)
            
            fullFile = OOMP.baseDir + file
            oomSend(fullFile.replace("/","\\"),delay=3)
            oomSendEnter(2)
            oomSendEnter(2)
            oomSend("n",10)
            #maybe close warning window
            oomMouseClick(pos=eagleCloseText,delay=5)            
            

            ###### BOM
            filename = partFile
            if overwrite or not os.path.exists(filename):
                print("        " + filename)
                eagleExport(filename,6,overwrite=overwrite)
            ###### Image
            filename = imageFile
            if overwrite or not os.path.exists(filename):
                print("        " + filename)
                eagleExport(filename,5,overwrite=overwrite)

            oomSendAltKey("x")
        

def harvestEagleBoardFile(file,directory,overwrite=False):
    dxfFile = OOMP.baseDir + directory + "eagleImage.dxf"
    pngFile = OOMP.baseDir + directory + "eagleImage.png"
    partFile = OOMP.baseDir + directory + "eagleParts.txt"
    netFile = OOMP.baseDir + directory + "eagleNetlist.txt"
    pinFile = OOMP.baseDir + directory + "eaglePinlist.txt"
    imageFile = OOMP.baseDir + directory + "eagleImage.png"
    #if overwrite or not os.path.exists(dxfFile):
    #if overwrite or not os.path.exists(pngFile):
    print("Harvesting Eagle Board: " + file)
    if(os.path.exists(file)):
        if overwrite or not (os.path.exists(partFile) or os.path.exists(netFile) or os.path.exists(pinFile) or os.path.exists(imageFile)):
            oomLaunchEagle(OOMP.baseDir + file)
            oomDelay(45)
            ##### no back annotation message
            oomSendEnter(delay=2)    
            ##### no back annotation message
            oomSendEnter(delay=2)    
            oomSendMaximize()
            oomDelay(2)
            oomSendMaximize()
            oomDelay(2)
            #oomMouseClick(pos=kicadActive,delay=5)            
            oomSendControl("o",delay=5)
            #oomSendAltKey("f",2)
            #oomSend("o",1)
            #oomSend("b",1)
            

            fullFile = OOMP.baseDir + file
            oomSend(fullFile.replace("/","\\"),delay=3)
            oomSendEnter(2)        
            oomSend("n",10)
            oomSendEnter(delay=2)
            #maybe close warning window
            oomMouseClick(pos=eagleCloseText,delay=5)            
            

            ###### Part List
            filename = OOMP.baseDir + directory + "eagleParts.txt"
            if overwrite or not os.path.exists(filename):
                print("        " + filename)
                eagleExport(filename,1,overwrite=overwrite)
            ###### Net List
            filename = OOMP.baseDir + directory + "eagleNetlist.txt"
            if overwrite or not os.path.exists(filename):
                print("        " + filename)
                eagleExport(filename,0,overwrite=overwrite)
            ###### Pin List
            filename = OOMP.baseDir + directory + "eaglePinlist.txt"
            if overwrite or not os.path.exists(filename):
                print("        " + filename)
                eagleExport(filename,2,overwrite=overwrite)
            ###### image
            ###### set export to 1200
            filename = OOMP.baseDir + directory + "eagleImage.png"
            
            if overwrite or not os.path.exists(filename):
                print("        " + filename)
                eagleExport(filename,3,overwrite=overwrite)

            #close eagle
            oomSendAltKey("x")
            oomSendEsc(delay=2)


def kicadExport(filename,type,overwrite=False):
    if type.lower() == "bom":        
        bomFile = filename + "boardKicadBom.csv"
        if overwrite or not os.path.isfile(bomFile):
            print("    Making bom file")
            #oomSendAltKey("f",2)
            oomMouseClick(pos=kicadFile,delay=5)       
            oomSend("f",2)
            oomSend("b",2)
            oomSend(bomFile.replace("/","\\"),5)
            oomSendEnter(2)
            oomSend("y",2)
    if type.lower() == "pos":
        bomFile = filename + "boardKicad.pos"
        if overwrite or not os.path.isfile(bomFile):
            print("    Making bom file")
            #oomSendAltKey("f",2)
            oomMouseClick(pos=kicadFile,delay=5)       
            oomSend("f",2)
            oomSend("c",2)
            oomSend(filename.replace("/","\\"),5)
            oomSendShiftTab(2)
            oomSendEnter(2)   
            oomSendEsc(2)         
    if type.lower() == "svg":
        if overwrite or not os.path.isfile(filename + "boardKicad-B_Cu.svg"):
            print("    Making svg files")
            #oomSendAltKey("f",2)
            oomMouseClick(pos=kicadFile,delay=5)       
            oomSend("e",2)
            oomSend("ss",2)
            oomSendEnter(delay=2)
            oomSend(filename,5)
            oomSendShiftTab(2,delay=2)
            oomSendEnter(delay=10)
            oomSendEsc(5)
    if type.lower() == "wrl":
        if overwrite or not os.path.isfile(filename + "boardKicad.wrl"):
            print("    Making wrl file")
            oomMouseClick(pos=kicadFile,delay=5)       
            oomSend("e",2)
            oomSend("v",5)
            oomSendShiftTab(2,delay=2)
            oomSendEnter(delay=2)
            oomSend("y",8)
            oomSendEsc(5)
    if type.lower() == "step":
        if overwrite or not os.path.isfile(filename + "boardKicad.step"):
            print("    Making step file")
            oomMouseClick(pos=kicadFile,delay=5)       
            oomSend("e",2)
            oomSend("s",5)
            oomSendEnter(delay=2)
            oomSendShiftTab(4,delay=2)
            oomSendEnter(delay=10)
            oomSendAltKey('f4',5)
            oomSendEsc(5)
    if type.lower() == "3drender":
        if overwrite or not os.path.isfile(filename + "kicadPcb3d.png"):

            oomMouseMove(pos=kicadFootprintMiddle,delay=2)
            oomSendAltKey("3",5)
            ###### zoom
            oomMouseClick(pos=kicad3dView,delay=1)
            oomSend("z")
            oomSendEnter(delay=1)
            ######  front
            currentFile = filename + "kicadPcb3dFront.png"
            oomMouseClick(pos=kicadFile,delay=5) 
            oomSend("e",2)
            oomSendEnter(delay=2)
            oomSend(currentFile.replace("/","\\"),2)
            oomSendEnter(delay=2)
            oomSend("y",2)
            ######  back
            currentFile = filename + "kicadPcb3dBack.png"
            oomMouseMove(pos=kicadFootprintMiddle,delay=2)
            oomMouseRight(1)
            oomSend("vv",0.5)
            oomSendEnter(2)

            
            ###### zoom
            oomMouseClick(pos=kicad3dView,delay=1)
            oomSend("z")
            oomSendEnter(delay=1)
            oomMouseClick(pos=kicadFile,delay=5) 
            oomSend("e",2)
            oomSendEnter(delay=2)
            oomSend(currentFile.replace("/","\\"),2)
            oomSendEnter(delay=2)
            oomSend("y",2)
            ######  ortho
            oomMouseMove(pos=kicadFootprintMiddle,delay=2)
            oomMouseRight(1)
            oomSend("v",0.5)
            oomSendEnter(2)
            ###### zoom
            oomMouseClick(pos=kicad3dView,delay=1)
            oomSend("z")
            oomSendEnter(delay=1)            
            #yaxis
            times = 3
            for x in range(times):
                oomMouseClick(pos=kicad3dView,delay=1)
                oomSend("rr")
                oomSendEnter(delay=1)
            #zaxis    
            times = 2
            for x in range(times):
                oomMouseClick(pos=kicad3dView,delay=1)
                oomSend("rrrrrrr")
                oomSendEnter(delay=1)

            currentFile = filename + "kicadPcb3d.png"
            oomMouseClick(pos=kicadFile,delay=5) 
            oomSend("e",2)
            oomSendEnter(delay=2)
            oomSend(currentFile.replace("/","\\"),2)
            oomSendEnter(delay=2)
            oomSend("y",2)
            ###### close
            oomMouseClick(pos=kicadFile,delay=5) 
            oomSend("c",2)

            


def eagleExport(filename,downs,overwrite=False):
    if overwrite or not os.path.exists(filename):
        oomSendAltKey("f",2)
        oomSend("e",2)
        oomSendDown(downs,2)
        oomSendEnter(5)
        if "BOM" in filename:
            oomSendTab(3,1)
            oomSendDown(times=2,delay=1)            
            oomSendTab(1,1)
            oomSendRight(times=1,delay=1)                        
            oomSendSpace()
            oomDelay(2)
        oomSend(filename.replace("/","\\"),2)
        if ".png" in filename:
            oomSendTab(4,delay=2)
            oomSend("300",delay=1)
        oomSendEnter(5)
        if "BOM" in filename:
            oomSendEsc(2)
        if ".dxf" in filename:
            oomSendRight()
            oomDelay(2)
        oomSend("y",5)
        if downs == 5:
            oomDelay(10)

def makeInteractiveHtmlBom(project,overwrite=False):
    kicadPython = "C:/Program Files/KiCad/6.0/bin/python.exe"
    interactiveBom = '"C:/GH/oomlout_OOMP/sourceFiles/InteractiveHtmlBom/InteractiveHtmlBom/generate_interactive_bom.py" --no-browser'
    projectFile = project.getFilename("boardkicad",relative = "full")
    bomFile = project.getFilename("bomInteractive",relative="full")
    if os.path.isfile(projectFile): 
        if overwrite or not os.path.isfile(bomFile):
            launchString = '"' + kicadPython + '" ' + interactiveBom + ' "' + projectFile + '"'
            launchString = launchString.replace("/","\\")
            print("Generating Interactive BOM: " + projectFile)
            process = subprocess.Popen(launchString, shell=True, stdout=subprocess.PIPE)
            process.wait()
            print("    Result: " + str(process.returncode))

def makeInteractiveHtmlBomImages(project,overwrite=False):                   
    print("Harvesting Bom Image for: " + project.getID())                 
    filename = project.getFilename("bomInteractive",relative="full")
    frontimage = project.getFilename("bomInteractiveFront")
    backimage = project.getFilename("bomInteractiveBack")
    bom = project.getFilename("bomInteractiveCSV")
    bomDownload = "C:/Users/aaron/Downloads/boardKicad.txt" 
    frontimageDownload = "C:/Users/aaron/Downloads/boardKicad.F.png" 
    backimageDownload = "C:/Users/aaron/Downloads/boardKicad.B.png" 
    if os.path.exists(filename):
        if not os.path.exists(frontimage) or not os.path.exists(backimage) or not os.path.exists(bom) or overwrite:
            #oomLaunchWebsite(filename)
            oomLaunchOpen(filename)
            oomDelay(10)
            menuButton = [1160,120]
            frontimagePos = [950,250]
            backimagePos = [1100,250]
            bomPos = [955,410]
            oomDeleteFile(frontimageDownload)
            oomDeleteFile(backimageDownload)
            oomMouseClick(pos=menuButton,delay=2)
            oomMouseClick(pos=menuButton,delay=2)
            oomMouseClick(pos=frontimagePos,delay=3)
            oomMouseClick(pos=backimagePos,delay=3)
            oomMouseClick(pos=bomPos,delay=3)
            
            try:
                oomCopyFile(frontimageDownload,frontimage)
                oomCopyFile(backimageDownload,backimage)
                oomCopyFile(bomDownload,bom)
            except:
                frontimageDownload = "C:/Users/aaron/Downloads/boardKicad.2.F.png" 
                backimageDownload = "C:/Users/aaron/Downloads/boardKicad.2.B.png" 
                oomCopyFile(frontimageDownload,frontimage)
                oomCopyFile(backimageDownload,backimage)
                oomCopyFile(bomDownload,bom)                
                oomDeleteFile(frontimageDownload)
                oomDeleteFile(backimageDownload)

            oomSendControl("w")
        else:
            print("        SKIPPING")
    else:
        print("        SKIPPING NO BOM")



#PCBDRAW
####### kicad command prompt
####### pip install pyvirtualdisplay
####### pip install PcbDraw
####### C:\Program Files\KiCad\6.0\bin\kicad-cmd.bat
####### pcbdraw plot "C:/GH/oomlout_OOMP/oomlout_OOMP_projects/PROJ-ADAF-1032-STAN-01/kicad/boardKicad.kicad_pcb test.svg"
####### start cmd /C ""C:\Program Files\KiCad\6.0\bin\kicad-cmd.bat"&pcbDraw plot "C:\GH\oomlout_OOMP\oomlout_OOMP_projects\PROJ-ADAF-1032-STAN-01\kicad\boardKicad.kicad_pcb" "C:\GH\oomlout_OOMP\oomlout_OOMP_projects\PROJ-ADAF-1032-STAN-01\pcbdraw.svg""
####### -l Eagle-export
####### --remap "C:\\GH\\oomlout_OOMP\\pcbDrawRemap.json"
def renderPcbDraw(project,overwrite):
    ###### need to  pip install pcbdraw in kicad consile and pip install pyvirtualdisplay, and Pillow
    oompID = project.getID()
    print("Making PCB Draw for: "  + oompID  )
    filename = project.getFilename("boardKicad",relative="full").replace("/","\\")
    pcbDrawFile = project.getFilename("pcbdraw",relative="full").replace("/","\\")
    pcbDrawBackFile = project.getFilename("pcbdrawback",relative="full").replace("/","\\")
    pcbDrawFilePng = project.getFilename("pcbdraw",relative="full",extension = "png").replace("/","\\")
    pcbDrawBackFilePng = project.getFilename("pcbdrawback",relative="full",extension = "png").replace("/","\\")
    
    if os.path.exists(filename):
        filesize = os.stat(filename).st_size ## pcbdraw fails on empty boards
        if overwrite or not os.path.exists(pcbDrawFile) and filesize > 5000:
            kicadCmd = '"C:\\Program Files\\KiCad\\6.0\\bin\\kicad-cmd.bat"'
            pcbString = 'pcbDraw plot "' + filename + '" "' + pcbDrawFile + '"'
            pcbStringBack = 'pcbDraw plot --side back "' + filename + '" "' + pcbDrawBackFile + '"'
            launchString = 'start cmd /C "' + kicadCmd + "&" + pcbString + '"'
            print("       Launch String: " + launchString)
            launchStringBack = 'start cmd /C "' + kicadCmd + "&" + pcbStringBack + '"'
            print("       Launch String Back: " + launchStringBack)            
            #subprocess.Popen(launchString,shell=True)
            os.system(launchString)
            oomDelay(20)
            os.system(launchStringBack)
            oomDelay(20)
            oomMakePNG(pcbDrawFile,pcbDrawFilePng)
            oomMakePNG(pcbDrawBackFile,pcbDrawBackFilePng)

        else:
            print("    SKIPPING")
    else:
        print("      No PCB File")