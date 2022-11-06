import OOMP_footprints
import OOMP_footprints_BASE
import OOMP
import OOMP_parts
import OOMP_automation_KICAD_footprints


#OOMP.makePickle()
#OOMP.loadPickle()
#OOMP_footprints.make()
#OOMP_footprints_BASE.gitPull()
OOMP_footprints_BASE.createAllFootprints()
#OOMP_footprints_BASE.createFootprintLibraries()  



###### copy over 3d model
itemID = "PROJ-ADAF-1032-STAN-01"
itemID = "LEDS-0603-R-STAN-01"
#itemID = "RESE-0603-X-O100-01"
#itemID = "HEAD-JSTSH-X-PI04-RS"
itemID = "CAPC-0603-X-NF100-V50"
item = OOMP.items[itemID]
#OOMP_footprints_BASE.harvest3DModel(item)

###### old

###### if you change a symbol need to run this before everything is fixed
def generateChanges():
    #OOMP_base.loadPickle()
    OOMP.loadFast()
    OOMP_parts.make()
    OOMP.loadFast()
    OOMP_footprints.make()
    OOMP.loadFast()
    OOMP_summaries.document(filter="parts")


#OOMP.makePickle()
#OOMP_base.loadPickle()

#OOMP_footprints.make()
if True:
    #OOMP_footprints_BASE.gitPull()
    #OOMP_footprints_BASE.createAllFootprints()  
    #OOMP_footprints_BASE.createFootprintLibraries()  
    pass

OOMP.loadPickle()

itemID = "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-1X01"
item = OOMP.items[itemID]

#OOMP_automation_KICAD_footprints.harvestKicadFootprint(item)

#OOMP_footprints.harvest()

#generateChanges()


###### shouldn't use

#OOMP_base.loadPickle()
#OOMP_footprints_BASE.createFootprintLibraries()  