import OOMP
import OOMP_modules


#OOMP.makePickle()
OOMP.loadPickle()


section = OOMP_modules

#OOMP_task_BASE.all(make=Trus,create=True)
#OOMP_task_BASE.one(section)
#section.makeAll()    
section.createAll()
#section.generateAll()
#section.harvestAll()

itemID = "MODULE-POWE-KLD1117-SO223-V33D"

item = OOMP.items[itemID]
itemDir = OOMP.getFileItem(item,"",relative="full").replace("/","\\")
print(itemDir)
#section.make(item)    
#section.create(item)
#section.generate(item)
#section.harvest(item)


import OOMP_summaries
section = OOMP_summaries
section.generate(item)


######## TESTING

