import OOMP

from oomBase import *





def getCSVdetails(type="code"):
    headings = []
    for item in OOMP.tagNames:
        headings.append(OOMP.tagNames[item][type])
    return headings

def getCSVHead():
    contents = ""
    headings = getCSVdetails(type="name")
    for head in headings:
            contents = contents + head + ";"
    return contents 

def getCSVLine(item):
    contents = ""
    headings = getCSVdetails(type="code")
    for head in headings:
        extra = ""
        try:
            extra = '"' + str(item[head][0]) + '"'
        except:
            extra = ""
        contents = contents + extra + ";"            
    return contents 


def makeCSVSummaries():
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
    contents = "CSV Line for;" + item["oompID"][0] + ";" + item["name"][0] + "\n"
    contents = contents + getCSVHead() + "\n"
    contents = contents + getCSVLine(item)
    oomWriteToFile(filename,contents)
    
