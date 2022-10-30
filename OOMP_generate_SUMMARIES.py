import OOMP_summaries_BASE
import OOMP_summaries_PAGES
import OOMP_summaries_INDEXES

import OOMP

#OOMP.makePickle()
OOMP.loadPickle()


itemID = "PROJ-ADAF-1032-STAN-01"
itemID = "LEDS-0603-R-STAN-01"
#itemID = "RESE-0603-X-O100-01"
item = OOMP.items[itemID]
OOMP_summaries_BASE.createSummary(item,overwrite=True)


for item in OOMP.items:
    pass
    #OOMP_summaries_BASE.createSummary(OOMP.items[item],overwrite=True)

###### Indexes
#OOMP_summaries_INDEXES.generatePartsIndex()