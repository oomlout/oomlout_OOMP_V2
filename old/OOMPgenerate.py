import OOMP
import OOMPscad
import OOMPdiagrams
import OOMPjson
import OOMPimages
import OOMPlabels
import OOMPsummaries
import OPSC as opsc



def generateAll(filter="all",labels=False,scads=False,renders=False,readmes=False,diagrams=False,diagRenders=False,images=False,json=False,redirects=False,overwrite=False):

    print("Generating for " + str(len(OOMP.parts)) + " items")
  

    if labels:
        print("     Generating Labels:")
        if filter == "all" or filter == "parts":
            for item in OOMP.getItems("parts",cache=True):
                OOMPlabels.generateLabel(item,overwrite)

    if scads:        
        print("     Generating SCADs: Parts")
        for item in OOMP.getItems(filter,cache=True):
            OOMPscad.generateScad(item,renders,overwrite)

    if redirects:
        #for item in OOMP.getItems(cache=True):
        #    OOMPsummaries.generateRedirect(item,overwrite) 
        OOMPsummaries.generateRedirect() 


    if readmes:
        print("     Generating Readmes:")
        OOMPsummaries.generateReadmeIndex()
        for item in OOMP.getItems(filter,cache=True):
            OOMPsummaries.generateReadme(item,overwrite)

    if json:
        print("     Generating jsons:")
        for item in OOMP.getItems(filter,cache=True):
                OOMPjson.generateJson(item,overwrite)

    if diagrams or diagRenders:
        
        if filter == "all" or filter == "parts":
            print("     Generating Diagrams: " + filter)
            for item in OOMP.getItems("parts",cache=True):
                OOMPdiagrams.generateDiagrams(item, diagrams=diagrams, renders=diagRenders,overwrite=overwrite)
            OOMPdiagrams.genAllDiagramsFile()

    if images:
        print("     Generating Image Resolutions: All")
        for item in OOMP.getItems(filter,cache=True):
            OOMPimages.generateResolutions(item,overwrite)

def generateItem(item, labels=False,scads=False,renders=False,readmes=False,diagrams=False,diagRenders=False,images=False,json=False,redirects=False,overwrite=False):

    if labels:
        OOMPlabels.generateLabel(item,overwrite=overwrite)

    if scads:
        OOMPscad.generateScad(x,renders,overwrite=overwrite)

    if readmes:
        OOMPsummaries.generateReadme(item,overwrite=overwrite)
    
    if json:
        OOMPjson.generateJson(item,overwrite=overwrite)

    if diagrams or diagRenders:
        OOMPdiagrams.generateDiagrams(item, diagrams=diagrams, renders=diagRenders,overwrite=overwrite)

    if images:
        OOMPimages.generateResolutions(item,overwrite=overwrite)

    if redirects:
        OOMPsummaries.generateRedirect(item,overwrite) 


