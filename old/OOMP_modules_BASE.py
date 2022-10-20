import OOMP
import OOMPproject
import OOMPprojectParts

import OOMP_projects_partsMatch

import OOMP_modules_OOML

from oomBase import *


def make():
    OOMP_modules_OOML.createModules()

def createAllModules():
    make()

def harvest():
    harvestModules()

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

    inputFile = "templates/projectsTemplate.py"
    outputDir = "C:/GH/oomlout_OOMP/oomlout_OOMP_modules/" + oompID + "/"
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
    try:
        for tag in d["extraTags"]:
            extraTags.append(OOMP.oompTag(tag[0],tag[1]))        
    except:
        print("no extra tags")

    tagString = ""
    for tag in extraTags:
        tagString = tagString + tag.getPythonLine() + "\n"

    



    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)


def harvestModules():
    oomLaunchKicad()
    for project in OOMP.getItems("modules"):
        test = project.getTag("gitRepo").value
        test = "GO"
        if test != "":
            harvestModule(project,all=True)

def harvestModule(project,all=False,gitPull=False,copyBaseFiles=False,harvestEagle=False,harvestKicad=False,overwrite=False):
    oompID = project.getID()
    print("Harvesting Project: " + oompID)

    if all or gitPull:
        pass
        #gitPullProject(project)
    if all or copyBaseFiles:
        pass
        #copyBaseFilesProject(project)
    if all or harvestEagle:        
        pass
        #harvestEagleProject(project,overwrite)
    if all or harvestKicad:
        pass
        harvestKicadProject(project,overwrite)


def harvestKicadProject(project,overwrite=False):
    print("    Harvesting Kicad Files ")
    ###### Convert to kicad
    kicadBoardFile = project.getFilename("boardkicad")    
    kicadSchemFile = project.getFilename("schemkicad")
    
    projectDir = project.getFolder()
    ###### get files out
    #  of kicad
    OOMPproject.harvestKicadBoardFile(part=project,overwrite=overwrite)
    OOMPproject.harvestKicadSchemFile(part=project,overwrite=overwrite)
    ###### interactive BOM
    OOMPproject.makeInteractiveHtmlBom(project,overwrite)
    ###### currently broken for kicad files
    OOMPprojectParts.harvestParts(project,overwrite=overwrite)
    OOMP_projects_partsMatch.matchParts(project)

    OOMPproject.renderPcbDraw(project,overwrite)
    if False:
        for part in OOMP.getItems("parts"):
                part.exportTags("detailsInstancesOomp",["oompInstances"]) 

