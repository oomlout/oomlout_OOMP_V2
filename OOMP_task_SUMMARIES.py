import OOMP
import OOMP_summaries


OOMP.makePickle()
#OOMP.loadPickle()


section = OOMP_summaries

#OOMP_task_BASE.all(make=Trus,create=True)
#OOMP_task_BASE.one(section)
#section.makeAll()    
#section.createAll()
#OOMP.makePickle()
section.generateAll()
#OOMP.makePickle()
#section.harvestAll()

itemID = "VREG-SO223-X-KLD1117-V33D"
itemID = "VREG-SO235-X-KMIC5225-V25D"
itemID = "FOOTPRINT-kicad-kicad-footprints-Connector_PinHeader_2.54mm-PinHeader_2x03_P2.54mm_Vertical_SMD"
itemID = "PROJ-ADAF-1032-STAN-01"
itemID = "HEAD-I01-X-PI04-01"

item = OOMP.items[itemID]
itemDir = OOMP.getFileItem(item,"",relative="full").replace("/","\\")
print(itemDir)
#section.make(item)    
#section.create(item)
#### stage where it gets matched with a footprint
section.generate(item)
#section.harvest(item)


######## TESTING

