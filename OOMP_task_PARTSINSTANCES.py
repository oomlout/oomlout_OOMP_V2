import OOMP
import OOMP_parts_INSTANCES

#OOMP.makePickle()
OOMP.loadPickle()

itemID = "RESE-0603-X-O103-01"
item = OOMP.items[itemID]
itemDir = OOMP.getFileItem(item,"",relative="full").replace("/","\\")
print(itemDir)
item["oompInstances"] = []

OOMP_parts_INSTANCES.loadInstances()
item["oompInstances"] = OOMP_parts_INSTANCES.partInstances[itemID]
OOMP.exportTagsItem(item,"detailsInstancesOomp",["oompInstances"])
