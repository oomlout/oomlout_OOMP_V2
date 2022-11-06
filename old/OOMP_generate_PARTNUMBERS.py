


import OOMP

import OOMP_partNumbers_BASE

OOMP.loadPickle()

#OOMP_partNumbers_BASE.loadPartNumbers()
#OOMP_partNumbers_BASE.dictToCsv()
#OOMP_partNumbers_BASE.savePickle()



OOMP_partNumbers_BASE.loadPickle()
itemID = "RESE-0603-X-O103-01"
itemID = "HEAD-JSTSH-X-PI04-SM"
item = OOMP.items[itemID]
overwrite = True

#OOMP_partNumbers_BASE.loadOompMpn()
OOMP_partNumbers_BASE.loadMpnDpn(item)




#mpns = OOMP_partNumbers_BASE.getMpn(item)
#dpns = OOMP_partNumbers_BASE.getDpn(item)
#item["manufacturerPartNumber"] = mpns
#item["distributorPartNumber"] = dpns
#OOMP.exportTagsItem(item,"detailspartNumbers",["manufacturerPartNumber","distributorPartNumber"])

pass