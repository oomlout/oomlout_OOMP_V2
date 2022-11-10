#TYPEZZ-SIZEZZ-COLORZZ-DESCZZ-INDEXZZ
newPart = {}
newPart = OOMP.preloadItem(newPart)
newPart['oompType'].append("TYPEZZ")
newPart['oompSize'].append("SIZEZZ")
newPart['oompColor'].append("COLORZZ")
newPart['oompDesc'].append("DESCZZ")
newPart['oompIndex'].append("INDEXZZ")
newPart['hexID'].append("HEXZZ")
oompID = "TYPEZZ" + "-" + "SIZEZZ" + "-" + "COLORZZ" + "-" + "DESCZZ" + "-" + "INDEXZZ"
newPart['oompID'].append(oompID)

EXTRAZZ

OOMP.items[oompID] = newPart
OOMP.itemsHex["HEXZZ"] = newPart

