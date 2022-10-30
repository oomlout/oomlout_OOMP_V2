import OOMP

import OOMP_migrate_BASE

OOMP.loadPickle()

itemID = "PROJ-ADAF-1032-STAN-01"
#itemID = "CAPC-0402-X-NF100-V16"
itemID = "FOOTPRINT-kicad-kicad-footprints-Button_Switch_THT-KSA_Tactile_SPST"
itemID = "LEDS-0603-R-STAN-01"
item = OOMP.items[itemID]
OOMP_migrate_BASE.migrateFiles(item)


for item in OOMP.items:
    pass
    #OOMP_migrate_BASE.migrateFiles(OOMP.items[item])