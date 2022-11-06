import OOMP
import os
import json

from oomBase import *

def makeJson(item,overwrite,short=False):
    oompID = item["oompID"][0]
    basicJson = OOMP.getFileItem(item,"jsonBasic")
    #print("        JSON for: " + oompID)
    ping(1000)
    jsonFile = basicJson
    if not "TEMPLATE" in oompID and (not os.path.isfile(jsonFile) or overwrite):
        jsonText = json.dumps(item,default=lambda o: o.__dict__, sort_keys=True, indent=4)
        f = open(jsonFile,"w")
        f.write(jsonText)
        f.close()
    ###### fullJSON        
    fullJson = OOMP.getFileItem(item,"jsonFull")
    jsonFile = fullJson
    workingItem = item.copy()
    if short: ###### remove blank entries
        w2 = workingItem.copy()
        for tag in w2:
            if len(workingItem[tag]) == 0:
                del workingItem[tag]
        ###### FILES
    oompFiles = {}
    for file in OOMP.filenames:
        skips  =["BASE","IMAGE","EDA"]
        if file not in skips:
            testFile = OOMP.getFileItem(item,file)
        if os.path.exists(testFile):
            oompFiles[file] = [testFile]
    workingItem["oompFiles"] = oompFiles
    if not "TEMPLATE" in oompID and (not os.path.isfile(jsonFile) or overwrite):
        jsonText = json.dumps(workingItem,default=lambda o: o.__dict__, sort_keys=True, indent=4)
        f = open(jsonFile,"w")
        f.write(jsonText)
        f.close()
        pass        
