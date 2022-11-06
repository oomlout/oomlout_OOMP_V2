import OOMP_task_BASE
import OOMP
from oomBase import *

oomRuntime("start")


sections = []
import OOMP_collections
import OOMP_csv
import OOMP_footprints
import OOMP_labels
import OOMP_migrate
import OOMP_partNumbers
import OOMP_parts
import OOMP_projects
import OOMP_qr
import OOMP_summaries
import OOMP_symbols
import OOMP_images
import OOMP_json

OOMP.loadPickle()
#OOMP.makePickle()

#section = OOMP_collections
#section = OOMP_csv
#section = OOMP_footprints
#section = OOMP_parts
#section = OOMP_projects
#section = OOMP_summaries
#section = OOMP_symbols

#section = OOMP_json
section = OOMP_images

OOMP_task_BASE.all()
#OOMP_task_BASE.one(section)
#section.makeAll()    
#section.createAll()
#section.generateAll()
#section.harvestAll()

print(oomRuntime())