import OOMP

import OOMP_modules_OOML

from oomBase import *



def makeAllModules():
    OOMP_modules_OOML.makeModules()

def makeModule(d):
    type = d["oompType"]
    size = d["oompSize"]
    color = d["oompColor"]
    desc = d["oompDesc"]
    index = d["oompIndex"]
    
    try:
        name = d["name"]
    except:
        pass

    hexID = d["hexID"]

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
    oompSlashes = oompID.replace("-","/")

    inputFile = "templates/partsTemplate.py"
    outputDir = OOMP.baseDir + OOMP.getDir("modules") + oompSlashes + "/"
    oomMakeDir(outputDir)
    oomMakeDir(outputDir + "src/")
    outputFile = outputDir + "details.py"

    print("Making: " + outputFile)

    contents = oomReadFileToString(inputFile)
    contents = contents.replace("TYPEZZ",type)
    contents = contents.replace("SIZEZZ",size)
    contents = contents.replace("COLORZZ",color)
    contents = contents.replace("DESCZZ",desc)
    contents = contents.replace("INDEXZZ",index)
    contents = contents.replace("HEXZZ",hexID)

    extraTags = []
    tagString = ""
    for tag in extraTags:
        tagString = tagString + OOMP.getPythonLine(tagName=tag[0],tagValue=tag[1]) + "\n"

    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)



def harvestModules():
    oomLaunchKicad()
    for project in OOMP.getItems("modules"):
        test = project.getTag("gitRepo").value
        test = "GO"
        if test != "":
            harvestModule(project,all=True)

