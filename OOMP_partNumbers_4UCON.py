
import OOMP_parts_JLCC
import OOMP_partNumbers_BASE as onp
import OOMP
from oomBase import *
import csv

def loadPartNumbers():
    #inFile = "sourceFiles/partNumberTest.csv"
    inFile = "csv/C-4UCON-part.csv" ###need to open in notepad++ and sewitch charachter set then convert to UTF 8
    f = open(inFile, mode="r",encoding="utf-8")
    #print(f)
    csvIn = csv.DictReader(f)
    #distributorCode = "C-LCSC"
    count = 0
    #max = 10000
    max = 10000000000000000000
    for row in csvIn:
        ping()
        
        manuCode = "C-4UCON"
        manuNum = row["partNumber"]
        mpnKey = "MPN-" + str(manuCode) + "-" + str(manuNum)
        description = row["description"]
        onp.MPN[mpnKey] = {}
        onp.MPN[mpnKey]["MPNKEY"] = mpnKey
        onp.MPN[mpnKey]["MANUFACTURER"] = "4Ucon Online Connectors"
        onp.MPN[mpnKey]["MANUCODE"] = manuCode
        onp.MPN[mpnKey]["MPN"] = manuNum
        oompD = row.copy()
        oompD = matchPart(oompD)
        #oompID = oompD["oompType"] + "-" + oompD["oompSize"] + "-" + oompD["oompColor"] + "-" + oompD["oompDesc"] + "-" + oompD["oompIndex"]
        oompID = oompD["oompID"]
        onp.MPN[mpnKey]["OOMPIDPARTIAL"] = oompID
        onp.MPN[mpnKey]["OOMPID"] = ""
        onp.MPN[mpnKey]["LINK"] = "https://www.4uconnector.com/online/SearchPro.asp?s_keyword=" + manuNum
        onp.MPN[mpnKey]["DESCRIPTION"] = description
        tags = []
        onp.MPN[mpnKey]["TAGS"] = tags
        if "UNMATCHED" not in oompID:
            onp.MATCHED[mpnKey] = onp.MPN[mpnKey]

def matchPart(part):
    part["oompID"] = ""
    return part