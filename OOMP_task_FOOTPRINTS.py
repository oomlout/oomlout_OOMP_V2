import OOMP
import OOMP_footprints


#OOMP.makePickle()
OOMP.loadPickle()


section = OOMP_footprints

#OOMP_task_BASE.all(make=Trus,create=True)
#OOMP_task_BASE.one(section)
#section.makeAll()    
section.createAll()
#section.generateAll()
#section.harvestAll()

itemID = "RESE-0603-X-O103-01"

item = OOMP.items[itemID]
itemDir = OOMP.getFileItem(item,"",relative="full").replace("/","\\")
print(itemDir)
#section.make(item)    
#section.create(item)
#section.generate(item)
#section.harvest(item)


######## TESTING
