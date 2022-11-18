import OOMP
import OOMP_parts


#OOMP.makePickle()
OOMP.loadPickle()


section = OOMP_parts

#OOMP_task_BASE.all(make=Trus,create=True)
#OOMP_task_BASE.one(section)
#section.makeAll()    

section.createAll()
OOMP.makePickle()
section.generateAll()
OOMP.makePickle()
#section.harvestAll()


itemID = "VREG-SO223-X-KLD1117-V5"
itemID = "XTAL-3225P4-X-MZ8-01"
itemID = "VREG-SO223-X-KLD1117-V12D"
itemID = "MCUU-SC14-84-ATTINY-01"
itemID = "HEAD-JSTSH-X-PI04-RS"
itemID = "HEAD-I01-X-PI04-01"

item = OOMP.items[itemID]
itemDir = OOMP.getFileItem(item,"",relative="full").replace("/","\\")
print(itemDir)
#section.make(item)    
#section.create(item)
#### stage where it gets matched with a footprint
#section.generate(item)
#section.harvest(item)

import OOMP_summaries
OOMP_summaries.generate(item)

######## TESTING

