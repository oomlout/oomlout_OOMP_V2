import OOMP
import OOMP_projects_BASE

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")
#OOMP.loadParts("pickle")

#print(OOMP.getReport())

companies = {}


comps = ["SPAR","ADAF","OOML","DANP","ELLA","IBBC","SEED","SIRB","SOPA","SPAR"]
companies = {}
for comp in comps:
    companies[comp] = {}
    companies[comp]["code"] = comp

#OOMP.loadParts("nofootprints")
#import oomlout_OOMP_projects.test


def create():
    make()

def all(filter="",exclusions="NONE"):
    OOMP_projects_BASE.harvestProjects()
    OOMP.loadParts("all")
    OOMP_projects_BASE.harvestProjects()
    OOMP.loadParts("all")
    OOMP_projects_BASE.harvestProjects()


def single(oompid):
    d = {"all" :False,
        "gitPull" : False,
        "copyBaseFiles" : False,
        "harvestEagle" : False,
        "harvestKicad" : False,
        "matchParts" : True,
    }
    overwrite = True

    #overwrite = False
    project = OOMP.getPartByID(oompid)
    testID = project.getID()
    if testID != "----":
        #OOMP_projects_BASE.harvestProject(project,overwrite=overwrite, dict={"all" : True} )
        OOMP_projects_BASE.harvestProject(project,dict=d,overwrite=overwrite)
    else:
        print("No Project Found")

def working():

    #create()

    #OOMP.loadParts("projects")
    #OOMP.loadParts("nofootprints")

    #filter = ""
    #filter = "DANP"  
    #exclusions = "NONE" ## not working yet
    #exclusions = "ADAF" ## not working yet
    #all(filter,exclusions)

    oompID="PROJ-SPAR-15932-STAN-01"
    single(oompID)


def preMake():
    OOMP_projects_BASE.preMakeAllProjects()

def make():
    OOMP_projects_BASE.createAllProjects()

def harvest():    
    OOMP_projects_BASE.harvestProjects()


