import OOMP_footprints
import OOMP_footprints_BASE
import OOMP_base
import OOMP
import OOMP_parts


#OOMP_footprints.make()
#OOMP_footprints_BASE.gitPull()
OOMP_footprints_BASE.createAllFootprints()
#OOMP_footprints_BASE.createFootprintLibraries()  

###### old

###### if you change a symbol need to run this before everything is fixed
def generateChanges():
    #OOMP_base.loadPickle()
    OOMP.loadFast()
    OOMP_parts.make()
    OOMP.loadFast()
    OOMP_footprints.make()
    OOMP.loadFast()
    OOMP_summaries.document(filter="parts")


#OOMP_base.makePickle()
#OOMP_base.loadPickle()

#OOMP_footprints.make()

#OOMP_footprints.harvest()

#generateChanges()


###### shouldn't use

#OOMP_base.loadPickle()
#OOMP_footprints_BASE.createFootprintLibraries()  