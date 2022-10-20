from xmlrpc.client import FastMarshaller
import OOMP
import OOMPgenerate
import OOMPinkscapeGenerate
import OOMPeda
from oomBase import *



######  Choose part load method
OOMP.loadParts("pickle")


print(OOMP.getReport())

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")

OOMP.getItems("load",cache=False)



filter = "all"
#filter = "nofootprints"
#filter = "footprints"
#filter = "symbols"
#filter="projects"

OOMP.getItems("load",cache=False)

OOMP.parts 

item = OOMP.getPartByID("HEAD-I01-X-PI02-01")
#item = OOMP.getPartByID("BUTA-06-X-STAN-01")
#C:\GH\oomlout_OOMP\oomlout_OOMP_parts\HEAD-I01-X-PI18-01
item = OOMP.getPartByID("CAPC-0603-X-NF100-V50")
#item = OOMP.getPartByID("PROJ-ADAF-1231-STAN-01")
item = OOMP.getPartByID("PROJ-ELLA-0001-STAN-01")
#C:\GH\oomlout_OOMP\oomlout_OOMP_projects\PROJ-ADAF-1032-STAN-01
#item = OOMP.getPartByID("FOOTPRINT-eagle-eagle-default-atmel-SO24W")
#C:\GH\oomlout_OOMP\oomlout_OOMP_eda\footprints\eagle\eagle-default\atmel\SO24W

overwrite=True

labels=False

scads=False
renders=False
readmes=True
diagrams=False
redirects=False
diagRenders=False
images=False
json=False

OOMPgenerate.generateItem(item, labels=labels,scads=scads,renders=renders,readmes=readmes,diagrams=diagrams,diagRenders=diagRenders,images=images,json=json,redirects=redirects,overwrite=overwrite)

