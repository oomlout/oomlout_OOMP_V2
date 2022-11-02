import csv
from oomBase import *
import re
import pickle
import OOMP

import OOMP_partNumbers_LCSC
import OOMP_partNumbers_JSTT
import OOMP_partNumbers_4UCON

MPN = {}
OOMPMPN = {}
MATCHED = {}
DPN = {}
OOMPDPN = {}


def loadOompMpn():
    global OOMPMPN
    print("Loading OOMP MPN")
    for mpnID in MPN:
        #ping()
        mpn = MPN[mpnID]
        if mpn["OOMPID"] != "":
            oompID = mpn["OOMPID"]
            try:
                OOMPMPN[oompID].append(MPN[mpnID])
            except:
                OOMPMPN[oompID] = [MPN[mpnID]]
    loadOompDpn()

def loadOompDpn():
    global OOMPDPN
    print("Loading OOMP DPN")
    for dpnID in DPN:
        #ping()
        dpn = DPN[dpnID]
        if dpn["OOMPID"] != "":
            oompID = dpn["OOMPID"]
            try:
                OOMPDPN[oompID].append(DPN[dpnID])
            except:
                OOMPDPN[oompID] = [DPN[dpnID]]
    pass

def loadMpnDpn(item):
    mpns = getMpn(item)
    dpns = getDpn(item)
    item["manufacturerPartNumber"] = mpns
    item["distributorPartNumber"] = dpns
    OOMP.exportTagsItem(item,"detailspartNumbers",["manufacturerPartNumber","distributorPartNumber"])
    #loadOompMpn()

def getMpn(item):
    rv = []
    oompID = item["oompID"][0]
    try:
        return OOMPMPN[oompID]
    except:
        return []

    #for mpnID in MPN:
    #    testID = MPN[mpnID]["OOMPID"]
    #    #print(testID)
    #    if testID == oompID:
    #        rv.append(MPN[mpnID])
    #return rv

def getDpn(item):
    rv = []
    oompID = item["oompID"][0]
    for dpnID in DPN:
        testID = DPN[dpnID]["OOMPID"]
        if testID == oompID:
            rv.append(DPN[dpnID])
    return rv

mpnPickle = "sourceFiles/mpnPickle.pickle"
dpnPickle = "sourceFiles/dpnPickle.pickle"
matchPickle =  "sourceFiles/matchPickle.pickle"

def savePickle():
    pickle.dump(MPN,open(mpnPickle, "wb"))
    pickle.dump(DPN,open(dpnPickle, "wb"))
    pickle.dump(MATCHED,open(matchPickle, "wb"))
    #oomWriteToFile(dpnPickle,json.dumps(DPN))
    #oomWriteToFile(matchPickle,json.dumps(MATCHED))

def loadPickle():
    print("Loading Part Number and Distributor Number from Pickle")
    global MPN,DPN,MATCHED 
    MPN = pickle.load(open(mpnPickle,"rb"))
    DPN = pickle.load(open(dpnPickle,"rb"))
    MATCHED = pickle.load(open(matchPickle,"rb"))
    #DPN = json.loads(dpnPickle)
    #MATCHED = json.loads(matchPickle)
    loadOompMpn()
    pass


def loadPartNumbers():
    MPN = {}
    DPN = {}
    MATCHED = {}
    #loadPickle()
    OOMP_partNumbers_JSTT.loadPartNumbers()
    OOMP_partNumbers_LCSC.loadPartNumbers()    
    OOMP_partNumbers_4UCON.loadPartNumbers()
    loadOompMpn()
def dictToCsv():
    global MATCHED,MPN,DPN
    mpnFile = ["oomlout_OOMP_partNUmbers_V2/sourceFiles/oomlout_PartNumbers_V2_mpn.csv",MPN]
    dpnFile = ["oomlout_OOMP_partNUmbers_V2/sourceFiles/oomlout_PartNumbers_V2_dpn.csv",DPN]
    matchFile = ["oomlout_OOMP_partNUmbers_V2/oomlout_PartNumbers_V2_mpn_MATCHED.csv",MATCHED]

    files = [mpnFile,dpnFile,matchFile]
    for file in files:
        f = open(file[0],mode = "w+",encoding = "utf-8")    
        dic = file[1]        
        try:
            first = dic[next(iter(dic))]
            csvF = csv.DictWriter(f,first.keys(),lineterminator="\n")
            csvF.writeheader()
            for id in dic:
                line = dic[id]
                csvF.writerow(line)
        except StopIteration:
            print("Empty Dict")

    f.close()

def getCompanyCode(row):
    mystring = row["Manufacturer"]
    manu = re.sub('[^A-Za-z0-9]+', '', mystring)
    
    manu = manu[0:6].upper()    
    return "C-" + manu