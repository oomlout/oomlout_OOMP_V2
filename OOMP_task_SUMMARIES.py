import OOMP
import OOMP_summaries


#OOMP.makePickle()
OOMP.loadPickle()


section = OOMP_summaries

#OOMP_task_BASE.all(make=Trus,create=True)
#OOMP_task_BASE.one(section)
#section.makeAll()    
#section.createAll()
section.generateAll()
#section.harvestAll()

itemID = "VREG-SO223-X-KLD1117-V33D"

item = OOMP.items[itemID]
itemDir = OOMP.getFileItem(item,"",relative="full").replace("/","\\")
print(itemDir)
#section.make(item)    
#section.create(item)
#### stage where it gets matched with a footprint
#section.generate(item)
#section.harvest(item)


######## TESTING

