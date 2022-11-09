import OOMP
import OOMP_projects

import OOMP_kicad_BASE

#OOMP.makePickle()
OOMP.loadPickle()


section = OOMP_projects

#OOMP_task_BASE.all(make=Trus,create=True)
#OOMP_task_BASE.one(section)
#section.makeAll()    
#section.createAll()
#section.generateAll()
#section.harvestAll()

itemID = "PROJ-ADAF-1032-STAN-01"
itemID = "PROJ-SPAR-18077-STAN-01"
item = OOMP.items[itemID]
itemDir = OOMP.getFileItem(item,"",relative="full").replace("/","\\")
print(itemDir)
#section.make(item)    
#section.create(item)
#section.generate(item)
#section.harvest(item)


######## TESTING

## ibom
#OOMP_kicad_BASE.makeInteractiveHtmlBom(item,True)
#OOMP_kicad_BASE.makeInteractiveHtmlBomImages(item,True)
## pcbDraw
##OOMP_kicad_BASE.renderPcbDraw(item,True)