import OOMP
from oomBase import *

import OOMP_projects_partsMatch
import OOMP_projects_partsHarvest_BASE
import OOMP_json_BASE

import re
import json
from urllib.request import urlopen

######  Company Files
import OOMP_projects_ADAF
import OOMP_projects_DANP
import OOMP_projects_ELLA
import OOMP_projects_IBBC
import OOMP_projects_HYDR
import OOMP_projects_OSOB
import OOMP_projects_PDP7
import OOMP_projects_SEED
import OOMP_projects_SIRB
import OOMP_projects_OOML
import OOMP_projects_SOPA
import OOMP_projects_SPAR

def preMakeAllProjects():
    pass
    raise Exception("Shouldn't have reached Here")

def createAllProjects():
    OOMP_projects_IBBC.createProjects()
    OOMP_projects_ADAF.createProjects()    
    OOMP_projects_DANP.createProjects()    
    OOMP_projects_ELLA.createProjects()
    OOMP_projects_HYDR.createProjects()
    OOMP_projects_OSOB.createProjects()
    OOMP_projects_PDP7.createProjects()
    #OOMP_projects_SEED.createProjects()
    OOMP_projects_SIRB.createProjects()
    OOMP_projects_OOML.createProjects()
    OOMP_projects_SOPA.createProjects()
    OOMP_projects_SPAR.createProjects()
    OOMP_projects_SPAR.makeBaseProjects() #go through all repos and pull git details and whether they are a project or not        
    OOMP_projects_ADAF.makeBaseProjects() #go through all repos and pull git details and whether they are a project or not        
    

def getRepos(user):
    print("    Farming repos for: " + user)
    repos = []
    for page in range(0,100):
    #for page in range(0,1):
        print("        Page: " + str(page) + " current repos: " + str(len(repos)))
        url = "https://api.github.com/users/" + user + "/repos?per_page=100&page=" + str(page)
        response  = urlopen(url)
        oomDelay(10)
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
    raise exception("Should no longer be used")
    
#### Per Company:
#   oompSize:  Company Code
#   format:     kicad or eagle
#   github:       base git address
#   #### Per Project
#       name:       Project Name
#       repo:       Repo name
#       file:       file name within the repo (no need for suffix)       
#       oompIndex:  Version code
#       count:      project ID
def makeProjectNew(d):
    type = "PROJ"
    size = d["oompSize"]

    try:
        color = str(d["count"]).zfill(4)
    except:
        color = str(d["oompColor"]).zfill(4)
    desc = "STAN"
    index = "01"
    try:
        index = d["oompIndex"]
    except:
        pass

    ind = 0000
    try:
        ind = str(d["count"]).zfill(4)
    except:
        ind = str(d["oompColor"])

    hexID = "PR" + type[0:2] + str(ind)

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
    oompSlashes = oompID.replace("-","/")

    inputFile = "templates/partsTemplate.py"
    outputDir = OOMP.baseDir + OOMP.getDir("projects") + oompSlashes + "/"
    oomMakeDir(outputDir)
    oomMakeDir(outputDir + "src/")
    outputFile = outputDir + "details.py"

    #print("Making: " + outputFile)
    ping()

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

def harvestProjects(filter="",exclusions="NONE",overwrite=False):
    neverString = "nnmmkjkjoijlknlkzzzz"
    if exclusions == "NONE":
        exclusions= neverString
    test = OOMP.items
    for projectID in OOMP.itemsTypes["projects"]["items"]:
        skip = ["PROJ-SEED-20054-STAN-01"]
        if projectID not in skip:
            if filter in projectID and exclusions not in projectID:
                harvestProject(OOMP.items[projectID],overwrite=overwrite)
    #for part in OOMP.getItems("parts"):
    #    pass
        #part.exportTags("detailsInstancesOomp",["oompInstances"]) 

def farmProjects(users,code):
    print("Farming Projects for :" + code)
    #genFile = "OOMP_projects_" + code + "_gen.py"
    repos = []
    for user in users:
        repos.extend(getRepos(user=user))
    print("    Found " + str(len(repos)) + " repos")
    oomMakeDir("json/")
    filename = "json/oomp_Projects_" + code + "_repoRaw.json"
    oomWriteToFile(filename,json.dumps(repos))



####### no longer used
def harvestProject(project,all=False,overwrite=False):
    oompID = project["oompID"][0]
    print("Harvesting Project: " + oompID)

    all = True
    if all or dict["easy"] or dict["gitPull"]:
        pass
        gitPullProject(project)
    if all or dict["easy"] or  dict["copyBaseFiles"]:
        pass
        copyBaseFilesProject(project)
    if all or dict["harvestParts"]:
        pass
        OOMP_projects_partsHarvest_BASE.harvestParts(project)
    if all or dict["matchParts"]:
        pass
        OOMP_projects_partsMatch.matchParts(project)
    if all or dict["easy"] or dict["makeJsons"]:
        pass
        OOMP_json_BASE.makeJson(project,overwrite)

def makeBaseProjects(company,code):

    print("Harvesting " + company + " Projects")

    repoString = ""
    filename = "json/oomp_Projects_" + code + "_repoRaw.json"
    repos = json.loads(oomReadFileToString(filename))
    projects = []
    exportFile = "OOMP_projects_" + code + "_generated.py"
    contents = ""
    contents = contents + """
###### THIS FILE IS GENERATED BY OOMP_projects_BASE.py
import OOMP_projects_BASE

def createProjects():
    projects = []    
    
"""
    oomWriteToFile(exportFile,contents)
    skips = ['https://github.com/sparkfunX/Arduino.git']
    for repo in repos:
        if repo not in skips:
            #print("    Harvesting: " + repo)
            ping()
            outDir = oomGitPullNew(repo,"sourceFiles/git/",onlyCreate=True)  
            base = {}
            base["oompType"] = "PROJ"
            base["oompSize"] = code
            base["format"] = "eagle"
            base["github"] = "https://github.com/" + company + "/"
            d = base.copy()
            d["repo"] = repo.replace("https://github.com/" + company + "/","").replace(".git","")
            d["repo"] = d["repo"].replace("https://github.com/" + company + "X/","").replace(".git","") ###### to fix sparkfun X repos
            d = processDir(outDir,d,company,code)
            if d != None:
                run = False
                try:   ###### exit if no count was found (project ID)
                    a = d["count"]
                    run = True
                except:
                    pass
                if run:
                    oomAddLineToFile(exportFile,"    projects.append(" + str(d) + ")")
                #OOMP_projects_BASE.makeProjectNew(d)
    contents = """

    for d in projects:
        OOMP_projects_BASE.makeProjectNew(d) 
    
    """
    oomAddLineToFile(exportFile,contents)

def processDir(directory,d,company,code):
    readmeFile = ""
    boardFile = ""
    schematicFile = ""
    licenseFile = ""
    index = 0

    ############ Finding Files
    ###### Test if it has a hardware path
    if True:
        files = [f for f in os.listdir(directory)]
        #print(files)
        filter = "*.brd"
        filter = "**/*.brd"
        files = glob.glob(directory + filter,recursive=True)
        if len(files) > 0:
            name = d["repo"].replace("_"," ").replace("-"," ")
            d["name"] = name 
            if len(files) > 1:
                pass
                #print("    More than one board file found")
            
            d["file"] = files[0].replace("sourceFiles/git/" + d["repo"].replace(".git",""),"").replace(".brd","").replace("\\","/")
            filter = "license.md"
            files = glob.glob(directory + filter)
            if len(files) > 0:
                licenseFile = files[0]
            filter = "readme.md"
            files = glob.glob(directory + filter)
            if len(files) > 0:
                readmeFile = files[0]
                extraTags = []
                if code == "SPAR":
                    if readmeFile != "":
                        #print("        Found Readme")
                        pass
                        readme = oomReadFileToString(readmeFile)
                        
                        index = stringBetween(readme,"https://www.sparkfun.com/products/","\\)")
                        if not index.isnumeric():
                            index = stringBetween(readme,'href="https://www.sparkfun.com/products/','">')   
                        if not index.isnumeric():
                            index = stringBetween(readme,'href="https://www.sparkfun.com/products/','">')   
                        if not index.isnumeric():
                            ###### for debugging skipped repositories
                            c=0    
                        d["count"] = index
                        #print ("            Index: " + str(index))
                        
                        extraTags.append(["sources","All source files from https://github.com/sparkfun/" + name.replace(" ","_") + " (source licence details in srcLicense.md)"])
                        extraTags.append(["linkBuyPage","https://www.sparkfun.com/products/" + str(index)])
                if code == "ADAF":
                    if readmeFile != "":
                        #print("        Found Readme")

                        readme = oomReadFileToString(readmeFile)
                        index = stringBetween(readme,'href="http://www.adafruit.com/products/','">')
                        d["count"] = index
                        #print ("            Index: " + str(index))                        
                if index != 0 and index != "":
                    ############ Making OOMP file
                    oompType = "PROJ"
                    oompSize = code
                    oompColor = str(index).zfill(4)
                    oompDesc = "STAN"
                    oompIndex = "01" 
                    hexID = "PRS" + index   
                    directory = OOMP.getDir("projects") + oompType + "/"  + oompSize + "/"  + oompColor + "/"  + oompDesc + "/"  + oompIndex + "/"
                    oomMakeDir(directory)  
                    ############ Moving Files
                    if readmeFile != "":
                        oomCopyFile(readmeFile, directory + "srcReadme.md")
                    if licenseFile != "":    
                        oomCopyFile(licenseFile, directory + "srcLicense.md")
                                   
                return d
            return None
        else:
            pass
            #print("SKIPING")
                #delay(1)
            return None



def gitPullProject(project):
    print("    Pulling or cloning project ")
    gitRepo = project["gitRepo"][0]
    if gitRepo == "":
        print("        No Git Repo Found")
        #raise Exception("No git repo for project")
    else:
        pass
        oomGitPullNew(gitRepo,"sourceFiles/git/")

def copyBaseFilesProject(project):
    #print("    Copying Base Files ")
    ping()
    for prog in ["kicad", "eagle"]:
        for type in ["Board","Schem"]:
            try:
                filename = project[prog + type][0]
            except:
                filename = ""
            outFile = OOMP.getFileItem(project, prog + type)
            if filename != "":
                inFile = "sourceFiles/git/" + project["gitName"][0] + "/" + filename
                if os.path.exists(inFile):
                    oomMakeDir(os.path.dirname(outFile))
                    oomCopyFile(inFile,outFile)

