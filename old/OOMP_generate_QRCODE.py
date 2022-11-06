import OOMP_qrCode_BASE
import OOMP


OOMP.loadPickle()

for itemID in OOMP.itemsTypes["parts"]["items"]:
    item = OOMP.items[itemID]
    OOMP_qrCode_BASE.createCode(item)
