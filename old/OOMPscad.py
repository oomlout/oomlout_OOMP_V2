import OOMP
import OPSC as opsc
from solid.objects import *
import os

def generateScad(part,renders=False,overwrite=False):
    
    oompID = part.getTag("oompID").value
    
    
    opsc.setMode("TRUE")
    item = opsc.item()
    item.addPos(insert("OOMP-" + oompID))
    #print(draw)
    #item.addPos(draw)
    #print("Is Empty:" + str(item.isEmpty()))
    if(not item.isEmpty()):
        #print("     MAKING")
        file = OOMP.getDir("parts") + oompID + "\\3dmodel.scad"
        if not os.path.isfile(file) or overwrite:
            print("Generating SCAD for: " + oompID)
            opsc.saveToScad(file, item.getPart())
            if(renders):
                opsc.saveToStl(file)
                opsc.saveToPng(file, extra="")
    else:
        c="SKIPPING"
        #print("      SKIPPING")


######  OOMP ROUTINES

    ######  BUTA
def oompButa06XX01(color):
    pinWidth = 3.25
    pinHeight = 2.5
    return oompButaXXX01(pinWidth,pinHeight,color)

def oompButa12XX01(color):
    pinWidth = 6.75
    pinHeight = 2.5
    return oompButaXXX01(pinWidth,pinHeight,color)

def oompButaXXX01(pinWidth,pinHeight,color):
    mode = opsc.getMode()

    posA = [-pinWidth,pinHeight,0.1]    
    posB = [pinWidth,pinHeight,0.1]    
    posC = [-pinWidth,-pinHeight,0.1]    
    posD = [pinWidth,-pinHeight,0.1]
    depth=5.1    

    part = opsc.item()
    part.addPos(insert("pinWide",pos=posA,depth=depth,color=color))
    part.addPos(insert("pinWide",pos=posB,depth=depth,color=color))
    part.addPos(insert("pinWide",pos=posC,depth=depth,color=color))
    part.addPos(insert("pinWide",pos=posD,depth=depth,color=color))

    if(mode=="3DPR"):
        clearanceGap = 1.2
        clearancePos = [0,0,-clearanceGap]
        clearanceSize = [18.36,10,depth-clearanceGap]

        part.addPos(insert("cubeRounded",pos=clearancePos,size=clearanceSize,rad=2.5,color=color))


    return part.getPart()

    ######  HEAD
def oompHeadtopClearance(pitch,pins,color):
    part = opsc.item()
    depth= 6 + 2.54
    clear=0.5
    part.addPos(insert("cube",pos=[pins-1*2.54,0,0],size=[(pins*pitch)+clear,pitch+clear,depth],color=color))


    return part.getPart()    

    ######  LEDS

def oompLeds10XX01(color):
    part = opsc.item()
    posA = [1.27,0,0.1]
    posB = [-posA[0],posA[1],posA[2]]
    size = [opsc.ooebPinWidth,opsc.ooebPinWidth,4.1]
    sizeLong = [opsc.ooebPinWidth,opsc.ooebPinWidth,6.1]

    color = opsc.colWire
    part.addPos(insert("pin",pos=posA,size=size,color=color))
    part.addPos(insert("cube",pos=posB,size=sizeLong,color=color))
    color = opsc.colLEDRed
    part.addPos(insert("cylinder",pos=[0,0,8.5],rad=5,depth=6.5,color=color))
    part.addPos(insert("cylinder",pos=[0,0,2.05],rad=5.5,depth=2,color=color))
    part.addPos(insert("sphere",pos=[0,0,8.5+5],rad=5,color=color))

    return part.getPart()

    ######  RESE

def oompReseW04XX01(color,value):
    part = opsc.item()
    
    dig = f"{value:03}"
    dig1 = dig[0]
    dig2 = dig[1]
    dig3 = dig[2]
    #print("Value: ",value," ",dig)
    pinSpacing = 3.81
    resLength = 6.8
    resRad = 2.5/2
    resBandSpacing = 1

    posA = [pinSpacing,0,0+resRad+opsc.ooebPinWidth/2]
    posB = [-posA[0],posA[1],posA[2]]
    size = [opsc.ooebPinWidth,opsc.ooebPinWidth,5+resRad+opsc.ooebPinWidth/2]

    color = opsc.colWire
    part.addPos(insert("cube",pos=posA,size=size,color=color))
    part.addPos(insert("cube",pos=posB,size=size,color=color))
    part.addPos(insert("cube",pos=[pinSpacing*2/2,0,resRad],size=[opsc.ooebPinWidth,opsc.ooebPinWidth,pinSpacing*2],rot=[0,90,0],color=color))

    color = opsc.colResistor
    resPos = [resLength/2,0,resRad+0.01]
    part.addPos(insert("cylinder",pos=resPos,depth=resLength,rad=resRad,rot=[90,0,90],color=color))
    
    ####bands
    bandRad=resRad+0.01
    bandDepth = 0.75
    band1Pos=[resPos[0]-1,resPos[1],resPos[2]]    
    band1Color = opsc.colRes[int(dig1)]
    part.addPos(insert("cylinder",pos=band1Pos,depth=bandDepth,rad=bandRad,rot=[90,0,90],color=band1Color))
    
    band2Pos=[band1Pos[0]-resBandSpacing,resPos[1],resPos[2]]    
    band2Color = opsc.colRes[int(dig2)]
    part.addPos(insert("cylinder",pos=band2Pos,depth=bandDepth,rad=bandRad,rot=[90,0,90],color=band2Color))
    
    band3Pos=[band2Pos[0]-resBandSpacing,resPos[1],resPos[2]]    
    band3Color = opsc.colRes[int(dig3)]
    part.addPos(insert("cylinder",pos=band3Pos,depth=bandDepth,rad=bandRad,rot=[90,0,90],color=band3Color))




    return part.getPart()

############  PROJECTS

def oompProjArdcShenStan01TopClearance(color,depth=4,clear=0.5):
    part = opsc.item()

    part.addPos(insert("cube",pos=[0,0,0],size=[7*2.54+clear,17*2.54+clear,depth],color=color))
    part.addPos(insert("cube",pos=[0,18.95,0],size=[3*2.54+clear,9.271+clear,depth],color=color))
    return part.getPart()


######  Insert Routines

def insert(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color=opsc.colDefault,alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):
    returnValue = ""
    if pos[0] != None:
        x=pos[0]
        y=pos[1]
        z=pos[2]
    if rot[0] != None:
        rotX=rot[0]
        rotY=rot[1]
        rotZ=rot[2]
    
    #print(item,x,y,z,rotX,rotY,rotZ)

    returnValue = translate((x,y,z))(
            rotate((rotX,rotY,rotZ))(
                OOEBInsertIf(item,pos,x,y,z,ex,size,length,rot,rotX,rotY,rotZ,width,height,depth,rad,rad2,color,alpha,OOwidth,OOheight,holes,negative,name)
            )
        )
    

    return returnValue

def OOEBInsertIf(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color=opsc.colDefault,alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):

    #print("    OOEBInsert item:" + str(item) + " at:[" + str(x) + "," + str(y) + "," + str(z) + "] size: [" + str(width) + "," + str(height) + "," + str(depth) + "]")

    #print(pos)

    if(item=="XXXX"):
        x=0
    ######  OOMP ITEMS
        ######  BASIC
    elif(item=="pin"):
        returnValue = opsc.insert("cube",[None,None,None],0,0,0,ex,size,length,[None,None,None],0,0,0,opsc.ooebPinWidth,opsc.ooebPinWidth,depth,rad,rad2,color,alpha,OOwidth,OOheight,holes,negative,name)    
    elif(item=="pinWide"):
        returnValue = opsc.insert("cube",[None,None,None],0,0,0,ex,size,length,[None,None,None],0,0,0,opsc.ooebPinWidth,opsc.ooebPinWidthWide,depth,rad,rad2,color,alpha,OOwidth,OOheight,holes,negative,name)    
        ######  BUTA
    elif(item=="OOMP-BUTA-06-X-X-01"):
        returnValue = oompButa06XX01(color)    
    elif(item=="OOMP-BUTA-12-X-X-01"):
        returnValue = oompButa12XX01(color)  
        ######  HEAD
    elif(item=="OOMP-HEAD-I01-X-PI02-01-topClearance"):          
        returnValue = oompHeadtopClearance(pitch=2.54,pins=2,color=color)
        ######  LEDS
    elif(item=="OOMP-LEDS-10-X-X-01"):
        returnValue = oompLeds10XX01(color)
    elif(item=="OOMP-LEDS-10-R-FROS-01"):
        returnValue = oompLeds10XX01(opsc.colLEDRed)        
        ######  RESE
    elif(item=="OOMP-RESE-W04-X-X-01"):
        returnValue = oompReseW04XX01(color,000)
    elif(item=="OOMP-RESE-W04-X-O561-01"):
        returnValue = oompReseW04XX01(color,561)
    ############  PROJECTS
    elif(item=="OOMP-PROJ-ARDC-SHEN-STAN-01-topClearance"):
        returnValue = oompProjArdcShenStan01TopClearance(color,depth=depth)    
    else:    
        returnValue = opsc.insert(item,[None,None,None],0,0,0,ex,size,length,[None,None,None],0,0,0,width,height,depth,rad,rad2,color,alpha,OOwidth,OOheight,holes,negative,name)
    return returnValue

