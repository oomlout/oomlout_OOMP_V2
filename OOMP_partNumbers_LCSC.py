
import OOMP_parts_JLCC
import OOMP_partNumbers_BASE as onp
import OOMP
from oomBase import *
import csv

def loadPartNumbers():
    #inFile = "sourceFiles/partNumberTest.csv"
    inFile = "sourceFiles/megaList.csv" ###need to open in notepad++ and sewitch charachter set then convert to UTF 8
    f = open(inFile, mode="r",encoding="utf-8")
    #print(f)
    csvIn = csv.DictReader(f)
    distributorCode = "C-LCSC"
    count = 0
    #max = 10000
    max = 10000000000000000000
    for row in csvIn:
        ping(10000)
        
        manuCode = onp.getCompanyCode(row) 
        manuNum = row["MFR.Part"]
        mpnKey = "MPN-" + str(manuCode) + "-" + str(manuNum)
        
        if "C-VO" not in manuCode: ##### skip manufacturers with unicode part numbers
            onp.MPN[mpnKey] = {}
            onp.MPN[mpnKey]["MPNKEY"] = mpnKey
            onp.MPN[mpnKey]["MANUFACTURER"] = row["Manufacturer"]
            onp.MPN[mpnKey]["MANUCODE"] = manuCode
            onp.MPN[mpnKey]["MPN"] = manuNum
            oompD = row.copy()
            oompD = OOMP_parts_JLCC.matchPart(oompD)
            oompID = oompD["oompType"] + "-" + oompD["oompSize"] + "-" + oompD["oompColor"] + "-" + oompD["oompDesc"] + "-" + oompD["oompIndex"]
            onp.MPN[mpnKey]["OOMPIDPARTIAL"] = oompID
            onp.MPN[mpnKey]["OOMPID"] = ""
            onp.MPN[mpnKey]["LINK"] = ""
            onp.MPN[mpnKey]["DESCRIPTION"] = ""
            tags = []
            stock  = row["Stock"]
            if oompID == "RESE-0603-X-O103-01":
                pass
            if int(stock) > 1000000:
                tags.append("STOCK:1000K")
            elif int(stock) > 100000:
                tags.append("STOCK:100K")
            elif int(stock) > 10000:
                tags.append("STOCK:10K")
            elif int(stock) > 1000:
                tags.append("STOCK:1K")
            priceLine = row["Price"]
            prices = priceLine.split(",")
            volume = prices[0].split(":")[0]
            if ":" in prices:
                price = prices[0].split(":")[1]
                if float(price) > 1:
                    tags.append("PRICE:1")
                elif float(price) > 0.1:
                    tags.append("PRICE:0.1")
                elif float(price) > 0.01:
                    tags.append("PRICE:0.01")
                elif float(price) > 0.001:
                    tags.append("PRICE:0.001")
                elif float(price) > 0.0001:
                    tags.append("PRICE:0.0001")
            onp.MPN[mpnKey]["TAGS"] = tags
            if "UNMATCHED" not in oompID:
                onp.MPN[mpnKey]["OOMPID"] = oompID
                onp.MATCHED[mpnKey] = onp.MPN[mpnKey]
            #onp.MPN[mpnKey]["DESC"] = row["Description"]            
            dpn = row["LCSC Part"]
            dpnKey =  "DPN-" + distributorCode + "-" + dpn
            onp.DPN[dpnKey] = {}
            onp.DPN[dpnKey]["dpnKey"] = dpnKey
            onp.DPN[dpnKey]["DISTRIBUTOR"] = "LCSC"
            onp.DPN[dpnKey]["DISTRCODE"] = distributorCode
            onp.DPN[dpnKey]["DPN"] = dpn 
            onp.DPN[dpnKey]["MPN"] = mpnKey 
            onp.DPN[dpnKey]["TAGS"] = tags
            onp.DPN[dpnKey]["LINK"] = ""
            if distributorCode == "C-LCSC":
                onp.DPN[dpnKey]["LINK"] = "https://www.lcsc.com/product-detail/" + dpn + ".html"
            onp.DPN[dpnKey]["OOMPID"] = onp.MPN[mpnKey]["OOMPID"]
            count = count + 1
            if count > max:
                break
            
            


            pass
