import OOMP
import OOMP_footprints


OOMP.makePickle()
#OOMP.loadPickle()


section = OOMP_footprints

#OOMP_task_BASE.all(make=Trus,create=True)
#OOMP_task_BASE.one(section)
#section.makeAll()    
section.createAll()
OOMP.makePickle()
section.generateAll()
#section.harvestAll()

itemID = "RESE-0603-X-O103-01"
itemID = "FOOTPRINT-kicad-oomlout_OOMP_kicad-oomlout_OOMP_JLCC_Basic-CAPC-0402-X-NF2-V50-C4N2-C1532"
itemID = "FOOTPRINT-kicad-kicad-footprints-Connector_PinHeader_2.54mm-PinHeader_2x03_P2.54mm_Vertical_SMD"


item = OOMP.items[itemID]
itemDir = OOMP.getFileItem(item,"",relative="full").replace("/","\\")
print(itemDir)
section.make(item)    
section.create(item)
section.generate(item)
#section.harvest(item)

import OOMP_summaries
section = OOMP_summaries
section.generate(item)

######## TESTING

