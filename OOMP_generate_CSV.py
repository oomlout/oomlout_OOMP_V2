import OOMP_csv_BASE

import OOMP

#OOMP.makePickle()
OOMP.loadPickle()


itemID = "PROJ-ADAF-1032-STAN-01"
#C:\GH\oomlout_OOMP_V2\oomlout_OOMP_projects_V2\PROJ\ADAF\1032\STAN\01
item = OOMP.items[itemID]
#OOMP_csv_BASE.makeCSVFile(item)


OOMP_csv_BASE.makeCSVSummaries()
#for item in OOMP.items:
#    OOMP_csv_BASE.makeCSVFile(OOMP.items[item])
