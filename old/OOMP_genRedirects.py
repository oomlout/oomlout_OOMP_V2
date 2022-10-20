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

######  Redirects
OOMPgenerate.generateAll(filter=filter,redirects=True,overwrite=True)
