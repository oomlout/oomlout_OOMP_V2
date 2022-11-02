import OOMP

from oomBase import *

import csv



def getCSVdetails(type="code"):
    headings = []
    for item in OOMP.tagNames:
        headings.append(OOMP.tagNames[item][type])
    return headings

def getCSVHead():
    contents = []
    headings = getCSVdetails(type="name")
    for head in headings:
            contents.append(head)
    return contents 

def getCSVLine(item):
    contents = []
    headings = getCSVdetails(type="code")
    for head in headings:
        extra = ""
        try:
            extra = '' + str(item[head][0]) + ''
        except:
            extra = ''
        contents.append(extra)
    return contents 


def makeCSVSummaries():
    for type in OOMP.typesNames:
        print("    Making CSV Summary for: " + type)
        filename = OOMP.getDir(type) + "/details" + type.capitalize() + ".csv"
        f = open(filename, "w+", encoding='utf-8')
        fcsv = csv.writer(f, delimiter=';', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
        #fcsv.writerow(["OOMP Summary file for " + type.capitalize() ])
        fcsv.writerow(getCSVHead())
        for itemID in OOMP.itemsTypes[type]["items"]:
            fcsv.writerow(getCSVLine(OOMP.items[itemID]))
        f.close

def makeCSVSummariesOld():
    for type in OOMP.typesNames:
        print("    Making CSV Summary for: " + type)
        filename = OOMP.getDir(type) + "/details" + type.capitalize() + ".csv"
        f = open(filename, "w+", encoding='utf-8')
        f.write("OOMP Summary file for " + type.capitalize() + "\n")
        f.write(getCSVHead() + "\n")
        for itemID in OOMP.itemsTypes[type]["items"]:
            f.write(getCSVLine(OOMP.items[itemID]) + "\n")
        f.close

    

def makeCSVFile(item):
    ping()
    filename = OOMP.getFileItem(item,"csv")
    
    f = open(filename, "w+", encoding='utf-8')
    fcsv = csv.writer(f, delimiter=';', quotechar='"', lineterminator='\n',quoting=csv.QUOTE_MINIMAL)
    #fcsv.writerow(["CSV Line for;" + item["oompID"][0] + ";" + item["name"][0]])
    fcsv.writerow(getCSVHead())
    fcsv.writerow(getCSVLine(item))
    f.close

