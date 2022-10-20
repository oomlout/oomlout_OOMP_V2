import OOMP
import OOMPgenerate
import OOMPinkscapeGenerate
import OOMPeda
from oomBase import *
import json
        
OOMP.loadParts("pickle")

print(OOMP.getReport())

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")

#oomDelay(5)

harvestKicadSymbolsFiles = False  
harvestKicadSymbolsImages = False   ### not quite finished
harvestKicadFootprintImages = True
harvestEagleLibraries = False
overwrite=True
overwrite=False
filter="all"
filter="symbols"
OOMPeda.doTasks(overwrite=overwrite,harvestKicadSymbolsFiles=harvestKicadSymbolsFiles, harvestKicadSymbolsImages=harvestKicadSymbolsImages,harvestEagleLibraries=harvestEagleLibraries)

