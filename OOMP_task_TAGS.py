import OOMP
import OOMP_tags


#OOMP.makePickle()
OOMP.loadPickle()


section = OOMP_tags

#OOMP_task_BASE.all(make=Trus,create=True)
#OOMP_task_BASE.one(section)

#section.preMakeAll()
#section.makeAll()    
#section.createAll()
#OOMP.makePickle()
section.generateAll()
#section.harvestAll()

