import OOMP
import OOMP_footprints
import OOMP_footprints_BASE
import OOMP_kicad_BASE

#OOMP.makePickle()
OOMP.loadPickle()


section = OOMP_footprints

#OOMP_task_BASE.all(make=Trus,create=True)
#OOMP_task_BASE.one(section)
#section.makeAll()    b
#section.createAll()
section.generateAll()
#section.harvestAll()

itemID = "FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-SOT-23"

item = OOMP.items[itemID]
itemDir = OOMP.getFileItem(item,"",relative="full").replace("/","\\")
print(itemDir)
#section.make(item)    
#section.create(item)
#section.generate(item)
#section.harvest(item)


######## TESTING
#OOMP_footprints_BASE.createFootprintBoardFile(item)
#OOMP_kicad_BASE.svgKicadBoard(item,overwrite=True)
#OOMP_kicad_BASE.harvestAllKicad(overwrite=False,eda=True)