import OOMP
import OOMP_modules_BASE
name = "OOMP_modules_BASE"

import OOMP_projects

import OOMP_projects_partsHarvest_BASE
import OOMP_projects_partsMatch

import OOMP_kicad_BASE

def makeAll(overwrite=False):    
    #for itemID in OOMP.items:
    OOMP_modules_BASE.makeAllModules()
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        item = OOMP.items[itemID]
        make(item,overwrite)

def make(item,overwrite=False):    
        pass

def createAll(overwrite=False):
    
    #for itemID in OOMP.items:
    for itemID in OOMP.itemsTypes["modules"]["items"]:
        item = OOMP.items[itemID]
        create(item,overwrite)

def create(item,overwrite=False):
    pass

def generateAll(overwrite=False):
    print("Generate all for: " + name)
    #for itemID in OOMP.items:
    for itemID in OOMP.itemsTypes["modules"]["items"]:
        item = OOMP.items[itemID]
        generate(item,overwrite)
    

def generate(item,overwrite=False):
    OOMP_projects_partsMatch.matchParts(item)

def harvestAll(overwrite=False):
    OOMP_projects.harvestAll(overwrite)
    print("Harvest all for: " + name)
    for itemID in OOMP.items:
    #for item in OOMP.itemsTypes["parts"]["items"]:
        item = OOMP.items[itemID]
        harvest(item,overwrite)

def harvest(item,overwrite=False):
    pass