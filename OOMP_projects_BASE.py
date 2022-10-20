import OOMP
import OOMPproject
import OOMPprojectParts
from oomBase import *

import OOMP_projects_partsMatch

import re
import json
from urllib.request import urlopen

######  Company Files
import OOMP_projects_ADAF
import OOMP_projects_DANP
import OOMP_projects_ELLA
import OOMP_projects_IBBC
import OOMP_projects_SEED
import OOMP_projects_SIRB
import OOMP_projects_SOPA
import OOMP_projects_SPAR

def createAllProjects():
    OOMP_projects_IBBC.createProjects()
    OOMP_projects_ADAF.createProjects()    
    OOMP_projects_DANP.createProjects()    
    OOMP_projects_ELLA.createProjects()
    OOMP_projects_SEED.createProjects()
    OOMP_projects_SIRB.createProjects()
    OOMP_projects_SOPA.createProjects()
    OOMP_projects_SPAR.createProjects()

def getRepos(user):
    print("    Farming repos for: " + user)
    repos = []
    for page in range(0,100):
    #for page in range(0,1):
        print("        Page: " + str(page) + " current repos: " + str(len(repos)))
        url = "https://api.github.com/users/" + user + "/repos?per_page=100&page=" + str(page)
        response  = urlopen(url)
        oomDelay(2)
        result = json.loads(response.read())
        for item in result:
            try:
                repos.append(item["clone_url"])
            except:
                pass
        if len(result) == 0:
            break


    return repos



def makeProject(d):
    type = d["oompType"]
    size = d["oompSize"]
    color = d["oompColor"]
    desc = d["oompDesc"]
    index = d["oompIndex"]

    hexID = d["hexID"]

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index

    inputFile = "templates/projectsTemplate.py"
    outputDir = "C:/GH/oomlout_OOMP/oomlout_OOMP_projects/" + oompID + "/"
    outputFile = outputDir + "details.py"

    print("Making: " + outputFile)

    contents = oomReadFileToString(inputFile)
    contents = contents.replace("TYPEZZ",type)
    contents = contents.replace("SIZEZZ",size)
    contents = contents.replace("COLORZZ",color)
    contents = contents.replace("DESCZZ",desc)
    contents = contents.replace("INDEXZZ",index)
    contents = contents.replace("HEXZZ",hexID)

    repoName =""
    try:
        sp = d["gitRepo"].split("/")
        repoName = sp[len(sp)-1]
    except:
        pass

    extraTags = []
    tagString = ""
    extraTags.append(["name",d["name"]])
    try:
        extraTags.append(["gitRepo",d["gitRepo"]])
    except:
        pass
    extraTags.append(["gitName",repoName])
    try:
        extraTags.append(["eagleBoard",d["eagleBoard"]])
    except:
        pass
    try:
        extraTags.append(["kicadBoard",d["kicadBoard"]])
    except:
        pass
    try:
        extraTags.append(["eagleSchem",d["eagleSchem"]])
    except:
        pass
    try:
        extraTags.append(["kicadSchem",d["kicadSchem"]])
    except:
        pass
    for tag in extraTags:
        tagString = tagString + tag.getPythonLine() + "\n"

    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)

def makeProjectNew(d):
    type = d["oompType"]
    size = d["oompSize"]


    color = str(d["count"]).zfill(4)
    desc = "STAN"
    index = "01"
    try:
        index = d["oompIndex"]
    except:
        pass


    hexID = "PR" + type[0:2] + str(d["count"])

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index

    inputFile = "templates/projectsTemplate.py"
    outputDir = OOMP.baseDir + "/oomlout_OOMP_projects/" + oompID + "/"
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
    extraTags.append(["name",d["name"]])
    extraTags.append(["gitRepo",d["github"] + d["repo"]])
    extraTags.append(["gitName",d["repo"]])
    if d["format"].lower() == "eagle":
        extraTags.append(["eagleBoard",d["file"] + ".brd"])
        extraTags.append(["eagleSchem",d["file"] + ".sch"])
    elif d["format"].lower() == "kicad":
        extraTags.append(["kicadBoard",d["file"] + ".kicad_pcb"])
        extraTags.append(["kicadSchem",d["file"] + ".kicad_sch"])

    for tag in extraTags:
        tagString = tagString + OOMP.getPythonLine(tagName=tag[0],tagValue=tag[1]) + "\n"

    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)

def harvestProjects(filter="",exclusions="NONE"):
    neverString = "nnmmkjkjoijlknlkzzzz"
    if exclusions == "NONE":
        exclusions= neverString
    oomLaunchKicad()
    for project in OOMP.itemsTypes["projects"]:
        oompID = project.getID()
        test = project.getTag("gitRepo").value
        test =  "GO"
        skip = ["PROJ-SEED-20054-STAN-01"]
        if test != "" and oompID not in skip:
            testID = project.getID()
            if filter in testID and exclusions not in testID:
                harvestProject(project,all=True)
    for part in OOMP.getItems("parts"):
        part.exportTags("detailsInstancesOomp",["oompInstances"]) 
   

def harvestProject(project,all=False,dict="",overwrite=False):
    oompID = project.getID()
    print("Harvesting Project: " + oompID)

    if dict != "":
        if dict["all"]:
            all = True

    if all or dict["gitPull"]:
        pass
        gitPullProject(project)
    if all or dict["copyBaseFiles"]:
        pass
        copyBaseFilesProject(project)
    if all or dict["harvestEagle"]:        
        pass
        harvestEagleProject(project,overwrite)
    if all or dict["harvestKicad"]:
        pass
        harvestKicadProject(project,overwrite)
    if all or dict["matchParts"]:
        pass
        OOMP_projects_partsMatch.matchParts(project)

def gitPullProject(project):
    print("    Pulling or cloning project ")
    gitRepo = project.getTag("gitRepo").value
    if gitRepo == "":
        print("        No Git Repo Found")
        #raise Exception("No git repo for project")
    else:
        pass
        oomGitPullNew(gitRepo,"sourceFiles/projects/")

def copyBaseFilesProject(project):
    print("    Copying Base Files ")
    type = "Board"
    filename = project.getTag("eagle" + type).value    
    outFile = project.getFilename(type + "Eagle")
    outDir = ""
    inFile = ""
    if filename != "":
        inFile = "sourceFiles/git/" + project.getTag("gitName").value + "/" + filename
    else:
        filename = project.getTag("kicad" + type).value
        if filename != "":
            inFile = "sourceFiles/git/" + project.getTag("gitName").value + "/" + filename
            outFile = project.getFilename(type + "Kicad")
            outDir = project.getFilename("dirkicad")
        else:
            #raise Exception("No source board file found")
            print("        No Board File Found")
    if os.path.exists(inFile):
        if outDir != "":
            oomMakeDir(outDir)
        oomCopyFile(inFile,outFile)


    type = "Schem"
    filename = project.getTag("eagle" + type).value    
    outFile = project.getFilename(type + "Eagle")
    outDir = ""
    if filename != "":
        inFile = "sourceFiles/git/" + project.getTag("gitName").value + "/" + filename
    else:
        filename = project.getTag("kicad" + type).value
        if filename != "":
            inFile = "sourceFiles/git/" + project.getTag("gitName").value + "/" + filename
            outFile = project.getFilename(type + "Kicad")
            outDir = project.getFilename("dirkicad")
        else:
            #raise Exception("No source board file found")
            print("        No Schematic File Found")
    if os.path.exists(inFile):
        if outDir != "":
            oomMakeDir(outDir)
 
  
        oomCopyFile(inFile,outFile)   
    
def harvestEagleProject(project,overwrite=False):
    print("    Harvesting Eagle Files ")
    eagleBoardFile = project.getFilename("boardeagle")
    projectDir = project.getFolder()
    eagleBoardFileFull = project.getFilename("boardeagle",relative="full")
    OOMPproject.harvestEagleBoardFile(eagleBoardFile,projectDir,overwrite=overwrite)

    OOMPproject.harvestEagleSchematicFile(eagleBoardFile.replace("boardEagle.brd","schematicEagle.sch"),projectDir,overwrite=overwrite)
    #oomSendAltKey("x",delay=5)
    #oomSendAltKey("x",delay=5)

def harvestKicadProject(project,overwrite=False):
    print("    Harvesting Kicad Files ")
    ###### Convert to kicad
    kicadBoardFile = project.getFilename("boardkicad")    
    kicadSchemFile = project.getFilename("schemkicad")    
    eagleBoardFile = project.getFilename("boardeagle")
    eagleSchemFile = project.getFilename("schemeagle")
    
    projectDir = project.getFolder()
    OOMPproject.harvestEagleBoardToKicad(eagleBoardFile,projectDir,overwrite=overwrite)
    ###### projects that cause errors
    skips = ["PROJ-ADAF-196-STAN-01","PROJ-ADAF-1980-STAN-01","PROJ-ADAF-2200-STAN-01","PROJ-ADAF-2566-STAN-01","PROJ-ADAF-91-STAN-01","PROJ-ADAF-259-STAN-01","PROJ-ADAF-269-STAN-01","PROJ-ADAF-280-STAN-01","PROJ-ADAF-284-STAN-01","PROJ-ADAF-292-STAN-01","PROJ-ADAF-326-STAN-01","PROJ-ADAF-358-STAN-01","PROJ-ADAF-364-STAN-01","PROJ-ADAF-376-STAN-01","PROJ-ADAF-390-STAN-01","PROJ-ADAF-391-STAN-01","PROJ-ADAF-395-STAN-01","PROJ-ADAF-466-STAN-01","PROJ-ADAF-512-STAN-01","PROJ-ADAF-572-STAN-01","PROJ-ADAF-659-STAN-01","PROJ-ADAF-661-STAN-01","PROJ-ADAF-684-STAN-01","PROJ-ADAF-714-STAN-01","PROJ-ADAF-723-STAN-01","PROJ-ADAF-757-STAN-01","PROJ-ADAF-782-STAN-01","PROJ-ADAF-795-STAN-01","PROJ-ADAF-801-STAN-01","PROJ-ADAF-802-STAN-01","PROJ-ADAF-815-STAN-01","PROJ-ADAF-878-STAN-01","PROJ-ADAF-904-STAN-01","PROJ-SPAR-10103-STAN-01","PROJ-SPAR-10182-STAN-01","PROJ-SPAR-10406-STAN-01","PROJ-SPAR-10507-STAN-01","PROJ-SPAR-10547-STAN-01","PROJ-SPAR-10618-STAN-01","PROJ-SPAR-10701-STAN-01","PROJ-SPAR-10864-STAN-01","PROJ-SPAR-10878-STAN-01","PROJ-SPAR-10888-STAN-01","PROJ-SPAR-10889-STAN-01","PROJ-SPAR-10899-STAN-01","PROJ-SPAR-10901-STAN-01","PROJ-SPAR-10914-STAN-01","PROJ-SPAR-10920-STAN-01","PROJ-SPAR-10930-STAN-01","PROJ-SPAR-10936-STAN-01","PROJ-SPAR-10940-STAN-01","PROJ-SPAR-10941-STAN-01","PROJ-SPAR-10967-STAN-01","PROJ-SPAR-10968-STAN-01","PROJ-SPAR-10995-STAN-01","PROJ-SPAR-11007-STAN-01","PROJ-SPAR-11008-STAN-01","PROJ-SPAR-11013-STAN-01","PROJ-SPAR-11018-STAN-01","PROJ-SPAR-11028-STAN-01","PROJ-SPAR-11040-STAN-01","PROJ-SPAR-11043-STAN-01","PROJ-SPAR-12081-STAN-01","PROJ-SPAR-544-STAN-01","PROJ-SPAR-716-STAN-01","PROJ-SPAR-9110-STAN-01","PROJ-SPAR-9266-STAN-01","PROJ-SPAR-9267-STAN-01","PROJ-SPAR-9346-STAN-01","PROJ-SPAR-9363-STAN-01","PROJ-SPAR-9607-STAN-01","PROJ-SPAR-9612-STAN-01","PROJ-SPAR-9814-STAN-01","PROJ-SPAR-9947-STAN-01","PROJ-SPAR-9954-STAN-01","PROJ-SPAR-9964-STAN-01","PROJ-SPAR-9981-STAN-01","PROJ-DANP-0002-STAN-V0A","PROJ-DANP-0002-STAN-V1A","PROJ-DANP-0002-STAN-V25","PROJ-DANP-0002-STAN-V2A","PROJ-DANP-0002-STAN-V3","PROJ-DANP-0002-STAN-V35C","PROJ-DANP-0002-STAN-V36A","PROJ-DANP-0002-STAN-V4E"]
    if not project.getID() in skips:
        OOMPproject.harvestEagleSchemToKicad(eagleSchemFile,projectDir,overwrite=overwrite)
    ###### get files out
    #  of kicad
    OOMPproject.harvestKicadBoardFile(kicadBoardFile,projectDir,overwrite=overwrite)

    OOMPproject.harvestKicadSchemFile(kicadSchemFile,projectDir,overwrite=overwrite)
    ###### interactive BOM
    OOMPproject.makeInteractiveHtmlBom(project,overwrite)
    ###### currently broken for kicad files
    if os.path.exists(eagleBoardFile):
        OOMPproject.makeInteractiveHtmlBomImages(project,overwrite)
    OOMPprojectParts.harvestParts(project,overwrite=overwrite)
    ###### now standalone
    #OOMP_projects_partsMatch.matchParts(project)
    skips = ["PROJ-ADAF-391-STAN-01","PROJ-ADAF-4991-STAN-01","PROJ-ADAF-3501-STAN-01","PROJ-ADAF-5100-STAN-01","PROJ-ADAF-723-STAN-01","PROJ-SPAR-10402-STAN-01","PROJ-SPAR-10412-STAN-01","PROJ-SPAR-11013-STAN-01","PROJ-SPAR-11259-STAN-01","PROJ-SPAR-11260-STAN-01","PROJ-SPAR-12634-STAN-01","PROJ-SPAR-13328-STAN-01","PROJ-SPAR-14130-STAN-01","PROJ-SPAR-16653-STAN-01","PROJ-SPAR-9565-STAN-01"]
    if not project.getID() in skips:
        OOMPproject.renderPcbDraw(project,overwrite)
    if False:
        for part in OOMP.getItems("parts"):
                part.exportTags("detailsInstancesOomp",["oompInstances"]) 