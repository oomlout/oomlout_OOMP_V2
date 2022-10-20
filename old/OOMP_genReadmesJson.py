import OOMP
import OOMPgenerate
import OOMPinkscapeGenerate
import OOMPeda
from oomBase import *


#OOMP.loadParts("all")

OOMP.loadParts("pickle")


print(OOMP.getReport())

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")

OOMP.getItems("load",cache=False)

filter = "all"
#filter = "projects"
#filter = "nofootprints"
######  Readmesm
OOMPgenerate.generateAll(readmes=True,json=True,overwrite=True,filter=filter)
