import OOMP
import os
import glob

from oomBase import *

kicadActive =[515,14]
kicadFile = [80,35]
kicadFootprintMiddle = [945,545] 
kicad3dView = [145,35]

def convertAllEagleToKicad(overwrite=False):
    print("Converting all eagleBoard.brd files to kicad")
    filter = "eagleBoard.brd"
    print("     Getting glob of files")
    files = glob.glob("**\\" + filter,recursive=True)
    for file in files:
        convertEagleToKicad(file,style="brd",overwrite=overwrite)    
    print("Converting all eagleSchematic.sch files to kicad")
    filter = "eagleSchem.sch"
    print("     Getting glob of files")
    files = glob.glob("**\\" + filter,recursive=True)
    for file in files:
        convertEagleToKicad(file,style="sch",overwrite=overwrite)    


def convertEagleToKicad(filename,style="brd",overwrite=False):
    filename = OOMP.baseDir + filename 
    dir = os.path.dirname(os.path.realpath(filename)) + "\\"
    dir = dir.replace("\\","/")
    if style == "brd":
        kicadBoard = dir + "kicadBoard.kicad_pcb"
    if style == "sch":
        kicadBoard = dir + "kicadBoard.kicad_sch"
    
    boardEagle = filename
    print(    "HarvestEagleBoardToKicad: " + filename)
    if (overwrite or not os.path.exists(kicadBoard)) and os.path.exists(boardEagle):
        oomLaunchKicad()
        oomDelay(10)
        oomMouseClick(pos=kicadActive,delay=5)       
        oomMouseClick(pos=kicadFile,delay=5)       
        oomSendDown(8,delay=2)
        oomSendRight(1,delay=2)
        oomSendDown(1,delay=2)
        oomSendEnter(delay=5)
        ###### filedialog box open
        filename = boardEagle.replace("/","\\")
        oomSend(filename,5)
        oomSendEnter(10)
        ######  set temp folder
        tempDir = OOMP.baseDir + "sourceFiles/tempB/"
        oomMakeDir(tempDir)        
        oomDeleteDirectory(tempDir + "boardEagle.pretty/", safety=False)
        oomDeleteDirectory(tempDir + "boardEagle-backups/", safety=False)        
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
        oomMouseClick(pos=kicadFile,delay=5)
        oomSendDown(2,delay=2)
        oomSendEnter(delay=5)
        oomSend(kicadBoard.replace("/","\\").replace("\\\\","\\"),2)
        oomSendEnter(delay=10)
        oomSend("y",2)
        oomSendEnter(delay=2)
        ###### close project
        kicadClosePcb(False)
    else:
        print("        SKIPPING")
    



def harvestAllKicad(overwrite=False):
    print("Harvesting All Kicad Boards")
    filter = "kicadBoard.kicad_pcb"
    print("     Getting glob of files")
    files = glob.glob("**\\" + filter,recursive=True)
    for file in files:
        harvestKicadBoard(file,overwrite=overwrite)    
    print("Harvesting all Kicad Schematics")
    filter = "kicadBoard.kicad_sch"
    print("     Getting glob of files")
    files = glob.glob("**\\" + filter,recursive=True)
    for file in files:
        harvestKicadSchem(file,overwrite=overwrite) 

def harvestKicadBoard(filename="",overwrite=False):    
    filename = OOMP.baseDir + filename 
    dir = os.path.dirname(os.path.realpath(filename)) + "\\"
    dir = dir.replace("\\","/")
    dirBase = dir.replace("src/","")
    kicadBoard = filename
    print("Harvesting Kicad Board File: " + kicadBoard)
    if os.path.isfile(kicadBoard):
        if overwrite or not os.path.isfile(dirBase + "kicadPcb3d.png"):
            oomLaunchPopen("pcbnew.exe " + kicadBoard,10)
            oomMouseMove(pos=kicadFootprintMiddle,delay=2)
            oomSend("b",10)
            oomMouseClick(pos=kicadActive,delay=5)    
            filename = dir
            oomMakeDir(filename)
            kicadExport(filename,"bom",overwrite=overwrite)
            kicadExport(filename,"pos",overwrite=overwrite)                
            kicadExport(filename,"svg",overwrite=overwrite)            
            kicadExport(filename,"wrl",overwrite=overwrite)
            kicadExport(filename,"step",overwrite=overwrite)
            filename = dirBase
            kicadExport(filename,"3dRender",overwrite=overwrite)
            kicadClosePcb()

def harvestKicadSchem(file="",directory="",part="",overwrite=False,filter="projects"):
    
    kicadBoard = ""
    dirKicad = ""
    if part != "":
        kicadBoard = part.getFilename("schemKicad")
        dirKicad = part.getFilename("dirKicad")
        directory = part.getDir()

    else:
        dirKicad =   OOMP.baseDir + directory + "kicad/"
        kicadBoard = dirKicad + "schematicKicad.kicad_sch"
    imageFile = directory + "kicadSchem.png"
    print("Harvesting Kicad Board File: " + kicadBoard)
    if os.path.isfile(kicadBoard) and (overwrite or True):
        if overwrite or not os.path.isfile(imageFile):
            oomLaunchPopen("eeschema.exe " + kicadBoard,10)
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



###################### general kicad routines
def kicadClosePcb(noSave=True):
    #oomSendAltKey("f",2)
    oomMouseClick(pos=kicadFile,delay=5)
    oomSendUp(delay=2)
    oomSendEnter(delay=2)
    if noSave:
        oomSendRight(delay=2)
    oomSendEnter(delay=20)

def kicadExport(filename,type,overwrite=False):
    if type.lower() == "bom":        
        bomFile = filename + "kicadBoardBom.csv"
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
        bomFile = filename + "kicadBoard.pos"
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
        if overwrite or not os.path.isfile(filename + "kicadBoard-B_Cu.svg"):
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
        if overwrite or not os.path.isfile(filename + "kicadBoard.wrl"):
            print("    Making wrl file")
            oomMouseClick(pos=kicadFile,delay=5)       
            oomSend("e",2)
            oomSend("v",5)
            oomSendShiftTab(2,delay=2)
            oomSendEnter(delay=2)
            oomSend("y",8)
            oomSendEsc(5)
    if type.lower() == "step":
        if overwrite or not os.path.isfile(filename + "kicadBoard.step"):
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
