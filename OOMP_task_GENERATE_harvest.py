import OOMP
import OOMP_task_BASE


#OOMP.makePickle()
OOMP.loadPickle()


import OOMP_projects
import OOMP_modules


section = OOMP_projects

OOMP_projects.harvestAll()
OOMP_modules.harvestAll()

itemID = "PROJ-ADAF-1032-STAN-01"
itemID = "PROJ-DANP-0001-STAN-2A"
item = OOMP.items[itemID]
itemDir = OOMP.getFileItem(item,"",relative="full").replace("/","\\")
print(itemDir)

#section.harvest(item)












