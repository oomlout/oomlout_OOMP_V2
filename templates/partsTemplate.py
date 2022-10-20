
import OOMP 

######  Auto translated oomp file

newPart = {}
newpart = OOMP.preloadItem(newPart)

oType = "TYPEZZ"
oSize = "SIZEZZ"
oColor = "COLORZZ"
oDesc = "DESCZZ"
oIndex = "INDEXZZ"
hexID = "HEXZZ"

newPart['oompType'].append(oType)
newPart['oompSize'].append(oSize)
newPart['oompColor'].append(oColor)
newPart['oompDesc'].append(oDesc)
newPart['oompIndex'].append(oIndex)
oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

EXTRAZZ

######  Common
newPart['hexID'].append(hexID)

######  Housekeeping
#OOMPtags.addTags(newPart,oompId)

OOMP.items[oompID] = newPart
OOMP.itemsHex[hexID] = newPart
