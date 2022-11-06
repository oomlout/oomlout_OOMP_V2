import OOMP
import OOMP_projects_partsMatch
import OOMP_projects

#OOMP.makePickle()
OOMP.loadPickle()

itemID = "PROJ-ADAF-1032-STAN-01"
item = OOMP.items[itemID]
itemDir = OOMP.getFileItem(item,"",relative="full").replace("/","\\")
print(itemDir)
OOMP_projects.generate(item)

