import OOMP
import OOMP_projects

import OOMP_kicad_BASE
import OOMP_projects_partsMatch_Special

#OOMP.makePickle()
OOMP.loadPickle()


section = OOMP_projects

#OOMP_task_BASE.all(make=Trus,create=True)
#OOMP_task_BASE.one(section)

#section.preMakeAll()
#section.makeAll()    
section.createAll()
#section.generateAll()
#section.harvestAll()

itemID = "PROJ-ADAF-1032-STAN-01"
itemID = "PROJ-SPAR-19921-STAN-01"
#itemID = "PROJ-ADAF-1431-STAN-01"
itemID = "PROJ-ELLA-0003-STAN-01"
itemID = "PROJ-PDP7-0001-STAN-01"
item = OOMP.items[itemID]
itemDir = OOMP.getFileItem(item,"",relative="full").replace("/","\\")
print(itemDir)
#section.make(item)    
#section.create(item)
OOMP_projects_partsMatch_Special.loadMatches()
section.generate(item)   ####run parts match
#section.harvest(item)

import OOMP_summaries
OOMP_summaries.generate(item)

######## TESTING

## ibom
#OOMP_kicad_BASE.makeInteractiveHtmlBom(item,True)
#OOMP_kicad_BASE.makeInteractiveHtmlBomImages(item,True)
## pcbDraw
##OOMP_kicad_BASE.renderPcbDraw(item,True)