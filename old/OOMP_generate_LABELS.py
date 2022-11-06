import OOMP
import OOMP_labels_BASE


OOMP.loadPickle()
itemID = "RESE-0603-X-O103-01"
item = OOMP.items[itemID]
overwrite = True
OOMP_labels_BASE.generateLabels(item,overwrite)

overwrite = False
for item in OOMP.itemsTypes["parts"]["items"]:
    OOMP_labels_BASE.generateLabels(OOMP.items[item],overwrite)