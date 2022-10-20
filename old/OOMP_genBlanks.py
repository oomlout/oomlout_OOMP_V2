import OOMP;import OOMPgenerate;import OOMPinkscapeGenerate;import OOMPeda;from oomBase import *

######  Choose part load method
OOMP.loadParts("pickle")

print(OOMP.getReport())

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")

filter = "all"
#filter = "parts"
#filter = "nofootprints"
#filter = "footprints"
#filter = "symbols"
#filter="projects"
#filter = "modules"

OOMP.getItems("load",cache=False)
######  Images
OOMPgenerate.generateAll(filter=filter,images=True,overwrite=False)
######  All but labels
OOMPgenerate.generateAll(filter =filter,scads=False,renders=True,readmes=True,diagrams=False,diagRenders=False,images=False,overwrite=False)
######  Labels
OOMPgenerate.generateAll(filter =filter,labels=True)
######  Overwrite Readme and JSON
OOMPgenerate.generateAll(filter =filter,readmes=True,json=True,overwrite=True)

#input("ALL DONE")