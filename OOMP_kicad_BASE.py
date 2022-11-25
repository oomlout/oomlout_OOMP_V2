import OOMP
import os
import glob

import OOMP_kicad_CLI

from oomBase import *

kicadActive =[515,14]
kicadFile = [80,35]
kicadFootprintMiddle = [945,545] 
kicad3dView = [145,35]

def makeInteractiveHtmlBom(project,overwrite=False):
    kicadPython = "C:/Program Files/KiCad/6.0/bin/python.exe"
    ###### git clone https://github.com/openscopeproject/InteractiveHtmlBom
    interactiveBom = '"C:/GH/oomlout_OOMP/sourceFiles/InteractiveHtmlBom/InteractiveHtmlBom/generate_interactive_bom.py" --no-browser'
    projectFile = OOMP.getFileItem(project,"kicadBoard",relative = "full")
    bomFile = OOMP.getFileItem(project,"ibom",relative="full")
    if os.path.isfile(projectFile): 
        if overwrite or not os.path.isfile(bomFile):
            launchString = '"' + kicadPython + '" ' + interactiveBom + ' "' + projectFile + '"'
            launchString = launchString.replace("/","\\")
            #print("Generating Interactive BOM: " + projectFile)
            process = subprocess.Popen(launchString, shell=True, stdout=subprocess.PIPE)
            process.wait()

            #print("    Result: " + str(process.returncode))

def makeInteractiveHtmlBomImages(project,overwrite=False):                   
    #print("Harvesting Bom Image for: " + project.getID())  
    item = project               
    filename = OOMP.getFileItem(item,"ibom",relative="full")
    frontimage = OOMP.getFileItem(item,"ibomFront")
    backimage = OOMP.getFileItem(item,"ibomBack")
    frontimageDownload = "C:/Users/aaron/Downloads/boardKicad.F.png" 
    backimageDownload = "C:/Users/aaron/Downloads/boardKicad.B.png" 
    if os.path.exists(filename):
        if not os.path.exists(frontimage) or not os.path.exists(backimage) or overwrite:
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
            #oomMouseClick(pos=bomPos,delay=3)
            
            try:
                oomCopyFile(frontimageDownload,frontimage)
                oomCopyFile(backimageDownload,backimage)
                #oomCopyFile(bomDownload,bom)
            except:
                try:
                    frontimageDownload = "C:/Users/aaron/Downloads/boardKicad.2.F.png" 
                    backimageDownload = "C:/Users/aaron/Downloads/boardKicad.2.B.png" 
                    oomCopyFile(frontimageDownload,frontimage)
                    oomCopyFile(backimageDownload,backimage)
                    #oomCopyFile(bomDownload,bom)                
                    oomDeleteFile(frontimageDownload)
                    oomDeleteFile(backimageDownload)
                except:
                    downloadDirectory = "C:/Users/aaron/Downloads/"
                    list_of_files = glob.glob(downloadDirectory + "/*.F*")
                    oomMouseClick(pos=menuButton,delay=2)
                    oomMouseClick(pos=frontimagePos,delay=5)
                    latestFile = max(list_of_files, key=os.path.getctime)
                    oomCopyFile(latestFile,frontimage)
                    oomDeleteFile(latestFile)
                    oomMouseClick(pos=menuButton,delay=2)
                    oomMouseClick(pos=backimagePos,delay=5)
                    list_of_files = glob.glob(downloadDirectory + "/*.B*")                    
                    latestFile = max(list_of_files, key=os.path.getctime)
                    oomCopyFile(latestFile,backimage)
                    oomDeleteFile(latestFile)
                    oomDelay(45)

            oomSendControl("w")
        else:
            pass
            #print("        SKIPPING")
    else:
        pass
        #print("        SKIPPING NO BOM")


def renderPcbDraw(project,overwrite):
    item = project
    ###### need to  pip install pcbdraw in kicad consile and pip install pyvirtualdisplay, and Pillow
    oompID = project["oompID"][0]
    include = True
    skips = ["ADAF-0723","ADAF-3501","ADAF-4991","ADAF-5100","SOPA-0010","SOPA-0012","SPAR-10412","SPAR-11013","SPAR-11259","SPAR-11260","SPAR-12634","SPAR-11013","SPAR-13328","SPAR-14130","SPAR-16653","SPAR-9565"]
    for s in skips:
        if s in oompID:
            include = False
    if include:
        ping()
        filename = OOMP.getFileItem(item,"kicadBoard",relative="full").replace("/","\\")
        pcbDrawFile = OOMP.getFileItem(item,"pcbdraw",relative="full").replace("/","\\")
        pcbDrawBackFile = OOMP.getFileItem(item,"pcbdrawBack",relative="full").replace("/","\\")
        pcbDrawFilePng = OOMP.getFileItem(item,"pcbdraw",relative="full",extension = "png").replace("/","\\")
        pcbDrawBackFilePng = OOMP.getFileItem(item,"pcbdrawBack",relative="full",extension = "png").replace("/","\\")
        
        if os.path.exists(filename):
            filesize = os.stat(filename).st_size ## pcbdraw fails on empty boards
            if overwrite or not os.path.exists(pcbDrawBackFilePng) and filesize > 5000:
                print("Making PCB Draw for: "  + oompID  )
                kicadCmd = '"C:\\Program Files\\KiCad\\6.0\\bin\\kicad-cmd.bat"'
                pcbString = 'pcbDraw plot "' + filename + '" "' + pcbDrawFile + '"'
                pcbStringBack = 'pcbDraw plot --side back "' + filename + '" "' + pcbDrawBackFile + '"'
                launchString = 'start cmd /C "' + kicadCmd + "&" + pcbString + '"'
                #print("       Launch String: " + launchString)
                launchStringBack = 'start cmd /C "' + kicadCmd + "&" + pcbStringBack + '"'
                #print("       Launch String Back: " + launchStringBack)            
                #subprocess.Popen(launchString,shell=True)
                os.system(launchString)
                oomDelay(20)
                os.system(launchStringBack)
                oomDelay(20)
                oomMakePNG(pcbDrawFile,pcbDrawFilePng)
                oomMakePNG(pcbDrawBackFile,pcbDrawBackFilePng)

            else:
                pass
                #print("    SKIPPING")
        else:
            pass
            #print("      No PCB File")

def convertAllEagleToKicad(overwrite=False):
    print("Converting all eagleBoard.brd files to kicad")
    filter = "eagleBoard.brd"
    print("     Getting glob of files")
    files = glob.glob(OOMP.getDir("projects") + "\\**\\" + filter,recursive=True)
    
    for file in files:
        convertEagleToKicad(file,style="brd",overwrite=overwrite)    
    print("Converting all eagleSchematic.sch files to kicad")
    filter = "eagleSchem.sch"
    print("     Getting glob of files")
    files = glob.glob(OOMP.getDir("projects") + "**\\" + filter,recursive=True)
    
    skips = ["ADAF\\0000","ADAF\\0014","ADAF\\0073","ADAF\\0089","ADAF\\0091","ADAF\\0194","ADAF\\0789","ADAF\\0795","ADAF\\0801","ADAF\\0802","SPAR\\0716","SPAR\\0717","SPAR\\0747","SPAR\\10406","SPAR\\10507","SPAR\\10547","SPAR\\10618","SPAR\\10701","SPAR\\10930"]
    for file in files:
        include = True            
        for skip in skips:
            if skip in file:
                include = False
        if include:
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
    ping()
    if (overwrite or not os.path.exists(kicadBoard)) and os.path.exists(boardEagle):
        print(    "HarvestEagleBoardToKicad: " + filename)

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
    



def harvestAllKicad(overwrite=False,eda=False,fpFilter=[""]):
    print("Harvesting All Kicad Boards")
    filter = "kicadBoard.kicad_pcb"
    print("     Getting glob of files")
    files = []
    if eda:
        pass
        files.extend(glob.glob(OOMP.getDir("eda") + "**\\" + filter,recursive=True)    )        
    else:
        pass
        files.extend(glob.glob(OOMP.getDir("projects") + "**\\" + filter,recursive=True))
        files.extend(glob.glob(OOMP.getDir("modules") + "**\\" + filter,recursive=True)    )
    skips = ["SOPA\\0010"]
    for file in files:
        fileSize = os.stat(file).st_size
        if fileSize > 3000:
            include = True
            for skip in skips:
                if skip in file:
                    include = False
            if include:                
                if any(ext in file for ext in fpFilter):
                    print("Harverting Kicad Board: " + file)
                    
                    harvestKicadBoard(file,overwrite=overwrite,eda=eda)    
    print("Harvesting all Kicad Schematics")
    filter = "kicadBoard.kicad_sch"
    print("     Getting glob of files")
    files = []
    files = glob.glob(OOMP.getDir("projects") + "**\\" + filter,recursive=True)
    files.extend(glob.glob(OOMP.getDir("modules") + "**\\" + filter,recursive=True))
    skips = []
    for file in files:
        fileSize = os.stat(file).st_size
        if fileSize > 2000:
            include = True            
            for skip in skips:
                if skip in file:
                    include = False
            if include:
                print("Harvesting Kicad Schem: " + file)
                harvestKicadSchem(file,overwrite=overwrite) 

def harvestKicadBoard(filename="",overwrite=False,eda=False):    
    filename = OOMP.baseDir + filename 
    dir = os.path.dirname(os.path.realpath(filename)) + "\\"
    dir = dir.replace("\\","/")
    dirBase = dir.replace("src/sourceFiles/","")
    dirBase = dirBase.replace("src/","")
    kicadBoard = filename
    print("Harvesting Kicad Board File: " + kicadBoard)
    if os.path.isfile(kicadBoard):
        ###### add frameless kicad pro
        inFile = "templates/kicadBoard.kicad_pro"
        outFile = filename.replace("kicadBoard.kicad_pcb","kicadBoard.kicad_pro")
        oomCopyFile(inFile,outFile)
        run = False
        if eda:
            fileTest = dirBase + "src/kicadBoardSvg.svg"
            run = overwrite or not os.path.isfile(fileTest)
        else:
            run = overwrite or not os.path.isfile(dirBase + "kicadPcb3d.png")  or not os.path.isfile(dirBase + "src/kicadBoardBom.csv")
        if run:
            oomLaunchPopen("pcbnew.exe " + kicadBoard,10)
            oomMouseMove(pos=kicadFootprintMiddle,delay=2)
            oomSend("b",10)
            oomMouseClick(pos=kicadActive,delay=5)    
            filename = dir
            oomMakeDir(filename)
            if not eda:
                kicadExport(filename,"bom",overwrite=overwrite)
                kicadExport(filename,"pos",overwrite=overwrite)                
            kicadExport(filename,"svg",overwrite=overwrite)            
            if not eda:
                kicadExport(filename,"wrl",overwrite=overwrite)
                kicadExport(filename,"step",overwrite=overwrite)
                filename = dirBase
                kicadExport(filename,"3dRender",overwrite=overwrite)
            kicadClosePcb(eda=eda)    

import svgutils.transform as st

def svgKicadBoard(item,overwrite = False):
    pass
    kicadSVGBoard = OOMP.getFileItem(item,"kicadBoardSvg")
    kicadSVGBoardSimple = OOMP.getFileItem(item,"kicadBoardSvgSimple")
    if overwrite or not os.path.isfile(kicadSVGBoardSimple):
        pass
        base = OOMP.getFileItem(item,"") + "src/kicadBoard"
        first = "-B_Cu.svg"
        if not os.path.isfile(base + first):
            base = OOMP.getFileItem(item,"") + "src/sourceFiles/kicadBoard"
        if os.path.isfile(base + first):
            ###### FULL
            start = base+first
            template = st.fromfile(start)            
            layers = ["-B_Adhesive.svg","-B_Courtyard.svg","-B_Fab.svg","-B_Mask.svg","-B_Paste.svg","-B_Silkscreen.svg","-Edge_Cuts.svg","-F_Adhesive.svg","-F_Courtyard.svg",
            "-F_Fab.svg","-F_Mask.svg","-F_Paste.svg","-F_Silkscreen.svg","-Margin.svg","-F_Cu.svg"]
            for layer in layers:
                try:
                    layerFile = base + layer
                    second_svg = st.fromfile(layerFile)
                    template.append(second_svg.root)                
                except:
                    print("Missing Layer in: " + item["oompID"][0] + " " + layer)
            template.save(kicadSVGBoard)
            kicadPNGBoard = OOMP.getFileItem(item,"kicadBoardSvg",extension="png")
            kicadPDFBoard = OOMP.getFileItem(item,"kicadBoardSvg",extension="pdf")
            oomMakePNG(kicadSVGBoard,kicadPNGBoard)
            oomMakePDF(kicadSVGBoard,kicadPDFBoard)
            ###### SIMPLE
            start = base+first
            template = st.fromfile(start)            
            layers = ["-B_Courtyard.svg","-F_Courtyard.svg","-F_Cu.svg"]
            for layer in layers:
                try:
                    layerFile = base + layer
                    second_svg = st.fromfile(layerFile)
                    template.append(second_svg.root)                
                except:
                    print("Missing Layer in: " + item["oompID"][0] + " " + layer)
            template.save(kicadSVGBoardSimple)
            kicadPNGBoard = OOMP.getFileItem(item,"kicadBoardSvgSimple",extension="png")
            kicadPDFBoard = OOMP.getFileItem(item,"kicadBoardSvgSimple",extension="pdf")
            oomMakePNG(kicadSVGBoardSimple,kicadPNGBoard)
            oomMakePDF(kicadSVGBoardSimple,kicadPDFBoard)

        else:
            pass
            #print("     svgKicadBoard: svg files not found")


def harvestKicadSchem(file="",directory="",part="",overwrite=False,filter="projects"):
    
    kicadBoard = ""
    dirKicad = ""
    if part != "":
        kicadBoard = part.getFilename("schemKicad")
        dirKicad = part.getFilename("dirKicad")
        directory = part.getDir()

    else:
        if directory == "":
            directory = os.path.dirname(file) + "/"
        #dirKicad =   OOMP.baseDir + directory + "kicad/"
        kicadBoard = directory + "schematicKicad.kicad_sch"
        if not os.path.isfile(kicadBoard):
            kicadBoard = directory + "kicadBoard.kicad_sch"

    imageFile = directory + "kicadSchem.png"
    print("Harvesting Kicad Board File: " + kicadBoard)
    if os.path.isfile(kicadBoard) and (overwrite or True):
        if overwrite or not os.path.isfile(imageFile):
            ###### add frameless kicad pro
            inFile = "templates/kicadBoard.kicad_pro"
            outFile = kicadBoard.replace("kicadBoard.kicad_sch","kicadBoard.kicad_pro")
            oomCopyFile(inFile,outFile)
            
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
def kicadClosePcb(noSave=True,eda=False):
    #oomSendAltKey("f",2)
    oomMouseClick(pos=kicadFile,delay=5)
    oomSendUp(delay=2)
    oomSendEnter(delay=2)
    if noSave:
        oomSendRight(delay=2)
    if eda:
        oomSendEnter(delay=5)
    else:
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
