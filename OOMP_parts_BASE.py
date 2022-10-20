import OOMP
from oomBase import *

import OOMP_parts_OOML
import OOMP_parts_JLCC

import urllib.request


def createAllParts():
    OOMP_parts_OOML.createParts()
    OOMP_parts_JLCC.createParts()


def makePart(type="",size="",color="",desc="",index="",hexID="",extraTags=[],dict=""):
    if dict != "":
        type = dict["type"]
        size = dict["size"]
        color = dict["color"]
        desc = dict["desc"]
        index = dict["index"]
        hexID = dict["hexID"]
        try:
            extraTags = dict["extraTags"]
        except:
            pass

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
    oompSlashes = oompID.replace("-","/")
    print("Making part: " + oompID)

    inputFile = "templates/partsTemplate.py"
    outputDir = OOMP.baseDir + OOMP.getDir("parts") + oompSlashes + "/"
    oomMakeDir(outputDir)
    outputFile = outputDir + "details.py"

    datasheet = ""
    if dict != "":
        try:
            datasheet = dict["datasheet"]
        except:
            pass
    if datasheet != "":
        if "http" in datasheet:
            if True:   
                download_url = datasheet
                filename = outputDir + "datasheet"
                if not os.path.exists(filename + ".pdf"): ######
                    print("        Downloading datasheet: " + datasheet)
                    response = urllib.request.urlopen(download_url)    
                    file = open(filename + ".pdf", 'wb')
                    file.write(response.read())
                    file.close()            
                else:
                    print("        Skipping datasheet (already exists): " + datasheet)
                pass            

        else:
            oomCopyFile(datasheet,outputDir + "datasheet.pdf" )


    print("Making: " + outputFile)

    contents = oomReadFileToString(inputFile)
    contents = contents.replace("TYPEZZ",type)
    contents = contents.replace("SIZEZZ",size)
    contents = contents.replace("COLORZZ",color)
    contents = contents.replace("DESCZZ",desc)
    contents = contents.replace("INDEXZZ",index)
    contents = contents.replace("HEXZZ",hexID)
    
    tagString = ""
    for tag in extraTags:
        tagString = tagString + OOMP.getPythonLine(tagName=tag[0],tagValue=tag[1]) + "\n"

    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)


