import OOMP_summaries_BASE

import OOMP

#OOMP.makePickle()
OOMP.loadPickle()


itemID = "PROJ-ADAF-1032-STAN-01"
item = OOMP.items[itemID]
#OOMP_summaries_BASE.createSummary(item,overwrite=True)


for item in OOMP.items:
    OOMP_summaries_BASE.createSummary(OOMP.items[item],overwrite=True)
