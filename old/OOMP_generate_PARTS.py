import OOMP
import OOMP_parts
import OOMP_parts_BASE
import OOMP_parts_OOML
import OOMP_parts_EDA
import OOMP_parts_INSTANCES


#OOMP.makePickle()   ###### make no changes 40 seconds 1600 items
                    ###### from compiled? 24 seconds 1600 items
                    ###### make from blank 72 seconds 1600 items
                    ###### Full load of parts and eda
                    ############  From blank 
                    # 
                    # 
OOMP.loadPickle()


#OOMP_parts_EDA.matchFootprintsSymbols()
items = OOMP.items
#item = items["HEAD-I01-X-PI2X03-01"]
#OOMP_parts_INSTANCES.loadAllInstances()

OOMP_parts_OOML.createParts()

pass
