
import OOMP_partNumbers_BASE as onp
import OOMP
from oomBase import *

def loadPartNumbers():
    jstParts = []
    for itemID in OOMP.itemsTypes["parts"]["items"]:
        item = OOMP.items[itemID]
        oompID = item["oompID"][0]
        
        if oompID.startswith("HEAD-JST"):
            if len(item["footprintKicad"]) > 0:
                footprints = item["footprintKicad"]
                for footprint in footprints:
                    jstID = footprint
                    jstID = jstID.replace("FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_","")
                    classes = ["SH","PH","XH"]
                    for cl in classes:
                        jstID = jstID.replace(cl + "_","")
                    jstID = jstID[0:jstID.index("_")]
                    jstParts.append([jstID,oompID])
    for part in jstParts:       
        oompID = part[1]
        manuCode = "C-JSTSAL"
        manuNum = part[0]
        mpnKey = "MPN-" + str(manuCode) + "-" + str(manuNum)        
        onp.MPN[mpnKey] = {}
        onp.MPN[mpnKey]["MPNKEY"] = mpnKey
        onp.MPN[mpnKey]["MANUFACTURER"] = "Japan Solderless Terminals"
        onp.MPN[mpnKey]["MANUCODE"] = manuCode
        onp.MPN[mpnKey]["MPN"] = manuNum
        onp.MPN[mpnKey]["OOMPIDPARTIAL"] = oompID
        onp.MPN[mpnKey]["OOMPID"] = oompID
        onp.MPN[mpnKey]["LINK"] = ""
        onp.MPN[mpnKey]["DESCRIPTION"] = ""
        if "UNMATCHED" not in oompID:
            onp.MATCHED[mpnKey] = onp.MPN[mpnKey]
        onp.MPN[mpnKey]["TAGS"] = []
        ###### see if at LCSC
        for dpnKey in onp.DPN:
            if part[0] in onp.DPN[dpnKey]["MPN"]:
                onp.DPN[dpnKey]["OOMPID"] = onp.MPN[mpnKey]["OOMPID"]            
                onp.MPN[mpnKey]["TAGS"] = onp.DPN[dpnKey]["TAGS"]