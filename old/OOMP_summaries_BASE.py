import OOMP



import OOMPsummaries
import math

from oomBase import *

def createAllSummaries(all=False,overwrite=False,filter=""):
    par = OOMP.parts
    if filter == "parts":
        par =OOMP.getItems("parts")
        filter = ""
    for item in par:        
        if filter in item.getID():
            print("Summaries For:" + item.getID())
            createSummary(item=item,all=all,overwrite=overwrite)
    OOMPsummaries.generateReadmeIndex()
    


def createSummary(item,all=False,overwrite=False,filter=""):
    print("    Making Summary")
    OOMPsummaries.generateReadme(item,overwrite)




###### md helpers
def getLink(text,link):
    return "[" + text + "](" + link + ")"

def getImage(image,alt=""):
    return "![" + alt + "](" + image + ")"

def getPictureLink(item):    
    if item.getID() != "----":
        type = ""
        if item.ifFileExists("kicadPcb3d"):
            type = "kicadPcb3d"
        elif item.ifFileExists("image", extension = "jpg"):
            type = "image"

        if type != "":
            string = getImage(item.getFilename(type,relative="githubRaw",resolution="140")) + "<br>" + item.getName(br="<br>")
        else:
            string = item.getName(br="<br>")
        string = getLink(string,item.getFilename(filename="",relative="github"))
    else:
        string = "MISSING"
    return string

def addDisplayTable(mdFile,cells,width):
    mdFile.new_line()

    numCells = len(cells)
    rows = math.floor(numCells / width) + 1
    difference = rows * width - len(cells)

    for r in range(0,difference):
        cells.append("")

    #print("Table Test: " + str(len(cells)) + "    rows: " + str(rows)  + "    Cols: " + str(width))
    mdFile.new_table(columns=width, rows=rows, text=cells, text_align='center')                           