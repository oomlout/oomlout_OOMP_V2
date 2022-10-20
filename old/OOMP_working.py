import OOMP
import OOMPgenerate
import OOMPsummaries
import OOMPtags
import OOMPproject
import OOMPinkscapeGenerate
import OOMPeda
from oomBase import *
import json


#OOMP.loadParts("parts")
#OOMP.exportPickle()


OOMP.loadParts("pickle")

print(OOMP.getReport())

#OOMP.printParts()
OOMP.setBaseDir("C:/GH/oomlout_OOMP/")

###### Redirtects
#OOMPsummaries.generateRedirect()

######  Readmes
#item = OOMP.parts[28250]
#item = OOMP.getPartByID("FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-C0402")
#print(item.fullString())
#https://github.com/oomlout/oomlout_OOMP_eda/tree/main/footprints/eagle/Adafruit-Eagle-Library/adafruit/C0402
#C:\GH\oomlout_OOMP\oomlout_OOMP_eda\footprints\eagle\Adafruit-Eagle-Library\adafruit\C0402

#item = OOMP.getPartByID("RESE-0603-X-O103-01")
#item = OOMP.getPartByID("BREB-P400-C-STAN-01")
print(OOMP.parts.__dict__)
item = OOMP.parts["BREB-P400-C-STAN-01"]
print(item.fullString())
#https://github.com/oomlout/oomlout_OOMP_parts/tree/main/RESE-0603-X-O103-01
#C:\GH\oomlout_OOMP\oomlout_OOMP_parts\RESE-0603-X-O103-01


#print(item.fullString())
#https://github.com/oomlout/oomlout_OOMP_projects/tree/main/PROJ-ADAF-1032-STAN-01
#C:\GH\oomlout_OOMP\oomlout_OOMP_projects\PROJ-ADAF-1032-STAN-01
item = OOMP.getPartByID("PROJ-ADAF-1032-STAN-01")


######  Reports
tags = ["name","hexID"]
filename = "sourceFiles/reports/tagReport.csv"
#OOMPtags.genReport(filename,tags)
tags = ["allParts"]
filename = "sourceFiles/reports/footprintReport.csv"
OOMPtags.genReport(filename,tags,multi=True,filter="projects")
#OOMPtags.genReport(filename,tags,multi=True,filter="projects")


print(item.fullString())
#OOMPgenerate.generateItem(item, labels=False,scads=False,renders=False,readmes=True,json=True,diagrams=False,diagRenders=False,images=False,overwrite=True)

#OOMPgenerate.generateAll(redirects=True)



######  Projects

#OOMPproject.harvestProjectsSparkfun()
#OOMPproject.harvestProjectsAdafruit()






















############ OLD

#for part in OOMP.parts:
    #print(part)
#print(OOMP.getPartByHex("H03R"))





## Generate

#OOMPgenerate.generateAll(labels=True,scads=False,renders=False,readmes=True,json=True,diagrams=False,diagRenders=False,images=True,overwrite=False)


#OOMPgenerate.generateAll(labels=False,scads=False,renders=False,readmes=True,json=True,diagrams=False,diagRenders=False,images=False,overwrite=True)


#OOMPgenerate.generateAll(labels=True,scads=True,renders=True,readmes=True,diagrams=True,diagRenders=True,images=True,overwrite=False)

#item = OOMP.parts[28250]
#OOMPgenerate.generateItem(item, labels=False,scads=False,renders=False,readmes=True,json=True,diagrams=False,diagRenders=False,images=False,overwrite=True)

#print(item)

#OOMPinkscapeGenerate.generateDiagram(item)

#OOMPinkscapeGenerate.generateDiagrams()

        
######  KICAD AND EAGLE THINGS

#oomDelay(5)

### ### Single is for doing default libraries
#OOMPeda.harvestEagleLibraries(footprint=True,files=True,single=False, overwrite=False)
#OOMPeda.harvestEagleLibraries(footprint=True,files=True,single=True, overwrite=False)


#OOMPeda.eagleSetLibrary("19inch")
#OOMPeda.eagleResetLibrary()

#import OOMP_genPickle

#OOMPeda.harvestKicadLibraries()

#owner = "kicad-footprints"
#OOMPEDA.harvestKicadFootprintImages(owner)
#library="C:/EAGLE 9.6.2/cache/lbr/pinhead.lbr"
#libraryName="pinhead"
#OOMPeda.harvestEagleFootprint(library,libraryName,footprint=False,files=True)

#OOMPeda.harvestEagleLibraries(footprint=False,files=True)

# search
## image.png -imageZ1 -imageZ2 -imageZ3 -imagez4 -imagez5 -imagez6 -imagez7 -imagez8 -imagez9
#OOMPeda.harvestEagleLibraries()

#oomDelay(2)
#oomMouseScrollWheel(movement=-50)


#oomScreenCapture("temp1.png",crop=[560,105,900,900])


#json testing
#item = OOMP.parts[517]

#print(json.dumps(item,default=lambda o: o.__dict__, sort_keys=True, indent=4))
#print(item.__dict__)