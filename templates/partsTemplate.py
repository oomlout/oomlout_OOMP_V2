
######  Auto translated oomp file

def load(newPart):
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
    newPart['oompID'].append(oompID)

EXTRAZZ

    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

