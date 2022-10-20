import OOMP
import OOMPgenerate
import OOMPinkscapeGenerate
import OOMPeda
from oomBase import *

#OOMP.printParts()
OOMP.setBaseDir("C:/GH/oomlout_OOMP/")

#for part in OOMP.parts:
    #print(part)
#print(OOMP.getPartByHex("H03R"))


## Generate

#OOMPgenerate.generateAll(labels=False,scads=False,renders=False,readmes=False,diagrams=False,diagRenders=False,images=True)


OOMPgenerate.generateAll(labels=True,scads=True,renders=True,readmes=True,diagrams=True,diagRenders=True,images=True,overwrite=False)

#item = OOMP.parts[2]
#OOMPgenerate.generateItem(item, labels=False,scads=False,renders=False,readmes=False,diagrams=True,diagRenders=False,images=False)

#print(item)

#OOMPinkscapeGenerate.generateDiagram(item)

#OOMPinkscapeGenerate.generateDiagrams()

        
######  KICAD AND EAGLE THINGS

#OOMPeda.harvestEagleLibraries()
#OOMPeda.harvestKicadLibraries()


#library="C:/EAGLE 9.6.2/cache/lbr/pinhead.lbr"
#libraryName="pinhead"
#OOMPeda.harvestEagleFootprint(library,libraryName)

# search
## image.png -imageZ1 -imageZ2 -imageZ3 -imagez4 -imagez5 -imagez6 -imagez7 -imagez8 -imagez9
#OOMPeda.harvestEagleLibraries()

#oomDelay(2)
#oomMouseScrollWheel(movement=-50)


#oomScreenCapture("temp1.png",crop=[560,105,900,900])


