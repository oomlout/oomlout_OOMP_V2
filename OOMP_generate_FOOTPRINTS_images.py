import OOMP_footprints
import OOMP_footprints_BASE
import OOMP
import OOMP_parts
import OOMP_automation_KICAD_footprints


#OOMP.makePickle()
OOMP.loadPickle()

#OOMP_footprints_BASE.gitPull()

###### single
#itemID = "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-1X01"
#item = OOMP.items[itemID]
#OOMP_automation_KICAD_footprints.harvestKicadFootprint(item)


for itemID in OOMP.itemsTypes["eda"]["items"]:
    item = OOMP.items[itemID]
    type = item["oompType"][0]
    if type == "FOOTPRINT":
        OOMP_automation_KICAD_footprints.harvestKicadFootprint(item)
