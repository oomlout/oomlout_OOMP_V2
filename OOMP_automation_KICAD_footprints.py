from oomBase import *
import OOMP

###### kicad mousepoints
X = 0
Y = 0
kicadActive =[515,14]
kicadFootprintFilter =[145,114]
kicadFootprintFirstResult = [145,185]
kicadFootprintMiddle = [945,545] 
kicadFootprintMiddlePlus = [950,550] 
kicadFootprintTopLeft = [365,86] 
kicadSymbolMiddle = [1105,555] 
kicadSymbolMiddlePlus = [1110,560] 

kicadFile = [80,35]
kicad3dView = [145,35]


kicadLibraryTop = [210,115]

def harvestFootprints(overwrite=False,copySourceFiles=False,harvestFootprintImages=False):        
    for footprint in OOMP.getItems("footprints"):
        type =  footprint.getTag("oompFootprintType").value
        if type.lower() == "kicad":
            harvestFootprint(footprint,all=True,copySourceFiles=copySourceFiles,harvestFootprintImages=harvestFootprintImages,overwrite=overwrite)

def harvestFootprint(footprint,all=False,copySourceFiles=False,harvestFootprintImages=False,overwrite=False):
    print("Working on: " + footprint.getID())
    if all or copysourceFiles:
        pass
        #copySourceFile(footprint,overwrite)
    if all or harvestFootprintImages:
        harvestKicadFootprint(footprint)

def harvestKicadFootprint(footprint,overwrite=False):
    print("    Harvesting files")

    oompID = footprint["oompID"][0]
    oompFileName = OOMP.getFileItem(footprint,"image",relative="full")
    oompFileName3D = OOMP.getFileItem(footprint,"kicadPcb3d",relative="full")
    oompFileName3Dfront = OOMP.getFileItem(footprint,"kicadPcb3dFront",relative="full")
    oompFileName3Dback = OOMP.getFileItem(footprint,"kicadPcb3dBack",relative="full")
    footprintFilename = OOMP.getFileItem(footprint,"kicadFootprint",relative="full")

    #if overwrite or not os.path.isfile(oompFileName) :
    if overwrite or not os.path.isfile(oompFileName3D) :
        shortDelay = 1
        longDelay = 3
        footprintName = footprint["oompIndex"][0]
        footprintDir = footprint["oompDesc"][0]
        print("Capturing :" + str(footprint))
        oomMouseClick(pos=kicadActive)
        oomDelay(shortDelay)
        ##apply filter
        oomMouseClick(pos=kicadFootprintFilter)
        oomDelay(shortDelay)
        oomSendCtrl("a")
        oomDelay(shortDelay)
        oomSend(footprintName + " " + footprintDir)
        oomDelay(longDelay)
        oomMouseDoubleClick(pos=kicadFootprintFirstResult)
        oomDelay(longDelay)
        #### Discard Changes
        oomSendRight()
        oomDelay(shortDelay)
        oomSendEnter()
        oomDelay(longDelay)
        #### Export PNG
        file = oompFileName.replace("/","\\")
        if not os.path.exists(file):
            oomSendAltKey("f",2)
            oomSend("e",1)
            oomSend("p",2)
            oomSend(file,3)
            oomSendEnter(delay=1)
            oomSend("y",2)
        #### Export Footprint
        oomMouseClick(pos=kicadFootprintFilter)
        file = footprintFilename.replace("/","\\")
        if not os.path.exists(file):        
            oomSendAltKey("f",2)
            oomSend("e",1)
            oomSend("f",2)
            oomSend(file,3)
            oomSendEnter(delay=1)
            oomSend("y",2)
            oomSendEnter(delay=1)
        #### 3d 
        oomMouseClick(pos=[153,36],delay=1)
        oomSendDown(times=2,delay=1)
        oomSendEnter(delay=5)
        oomSendWindowsKey("up")
        ##### raytracing
        #if "_BALL" not in oompID.upper() and "_FLG" not in oompID.upper():
        #    oomSendAltKey("p",1)
        #    oomSendEnter(2)
        #    oomDelay(10)
        #### front
        oomSendAltKey("f",2)
        oomSendEnter(delay=1)
        oomSend(oompFileName3Dfront.replace("/","\\"),3)
        oomSendEnter(delay=1)
        oomSend("y",2)
        oomMouseClick(pos=[595,60],delay=5)
        oomMouseClick(pos=[818,536],delay=5) ###### click middle
        oomSend("Z",2)       
        #### back        
        oomDelay(10)
        oomSendAltKey("f",2)
        oomSendEnter(delay=1)
        oomSend(oompFileName3Dback.replace("/","\\"),3)
        oomSendEnter(delay=1)
        oomSend("y",2)  
        oomMouseClick(pos=[818,536],delay=5) ###### click middle
        oomSend("r",2)       
        #### ortho
        #oomMouseClick(pos=[595,60],delay=5)  
        # Needs hotkey setting rotate x clockwise to a, z counter clockwise to d 
        oomSend("aaaa",2)
        # for b in range(0,4):
        #     oomSendAltKey("v",delay=0.5)
        #     oomSendDown(4,delay=1)  
        #     oomSendEnter(delay=1)   
        oomSend("dd",2)
        oomDelay(10)
        # for b in range(0,2):
        #     oomSendAltKey("v",delay=0.5)
        #     oomSendDown(9,delay=1)  
        #     oomSendEnter(delay=1)      
        oomMouseClick(pos=[818,536],delay=5) ###### click middle
        oomSendAltKey("f",2)
        oomSendEnter(delay=1)
        oomSend(oompFileName3D.replace("/","\\"),3)
        oomSendEnter(delay=1)
        oomSend("y",2)
        oomMouseClick(pos=[818,536],delay=5) ###### click middle
        ##### close
        oomSendAltKey("f",delay=1)
        oomSendUp(delay=1)
        oomSendEnter(delay=3)







        oomDelay(longDelay)    

        oomDelay(5)


