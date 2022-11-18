import OOMP
import OOMP_projects_BASE
name = "OOMP_projects_BASE"
import OOMP_projects_SPAR
import OOMP_projects_ADAF

import OOMP_projects_partsHarvest_BASE
import OOMP_projects_partsMatch

import OOMP_projects_partsMatch_Special

import OOMP_kicad_BASE

def preMakeAll(overwrite=False):
    
    print("Pre make all for: " + name)
    OOMP_projects_SPAR.farmProjects() ###### get repo list
    OOMP_projects_ADAF.farmProjects() ###### get repo list
    OOMP.makePickle()    
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        item = OOMP.items[itemID]
        preMake(item,overwrite)

        
def preMake(item,overwrite=False):    
    OOMP_projects_BASE.gitPullProject(item)
    OOMP_projects_BASE.copyBaseFilesProject(item)
    

def makeAll(overwrite=False):
    print("Make all for: " + name)   
    #for itemID in OOMP.items: 
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        item = OOMP.items[itemID]
        make(item,overwrite)

def make(item,overwrite=False):    
        OOMP_projects_BASE.copyBaseFilesProject(item)

def createAll(overwrite=False):
    print("Create all for: " + name)
    OOMP_projects_BASE.createAllProjects()

def create(item,overwrite=False):
    pass

def generateAll(overwrite=False):
    print("Generate all for: " + name)
    #for itemID in OOMP.items:
    OOMP_projects_partsMatch_Special.loadMatches()
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        item = OOMP.items[itemID]
        generate(item,overwrite)
    OOMP_projects_partsMatch.partReport()

def generate(item,overwrite=False):
    OOMP_projects_partsHarvest_BASE.harvestParts(item)
    OOMP_projects_partsMatch.matchParts(item)
    
    

def harvestAll(overwrite=False):
    
    OOMP_kicad_BASE.convertAllEagleToKicad(overwrite=False)
    OOMP_kicad_BASE.harvestAllKicad(overwrite=False)
    
    print("Harvest all for: " + name)
    #for itemID in OOMP.items:
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        item = OOMP.items[itemID]
        harvest(item,overwrite)

def harvest(item,overwrite=False):
    OOMP_kicad_BASE.renderPcbDraw(item,overwrite)
    OOMP_kicad_BASE.makeInteractiveHtmlBom(item,overwrite)
    OOMP_kicad_BASE.makeInteractiveHtmlBomImages(item,overwrite)