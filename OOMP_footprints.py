import OOMP
import OOMP_footprints_BASE
name = "OOMP_footprints_BASE"

import OOMP_automation_KICAD_footprints

def makeAll(overwrite=False):
    print("Make all for: " + name)
    OOMP_footprints_BASE.gitPull()
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        item = OOMP.items[itemID]
        make(item,overwrite)

def make(item,overwrite=False):    
    pass

def createAll(overwrite=False):
    print("Create all for: " + name)
    OOMP_footprints_BASE.createAllFootprints()    
    print("Create all for: " + name)
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        item = OOMP.items[itemID]
        create(item,overwrite)    

def create(item,overwrite=False):
    pass

def generateAll(overwrite=False):
    print("Generate all for: " + name)
    #for itemID in OOMP.items:
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        item = OOMP.items[itemID]
        generate(item,overwrite)
    OOMP_footprints_BASE.createFootprintLibraries()
    

def generate(item,overwrite=False):
    pass

def harvestAll(overwrite=False):
    print("Harvest all for: " + name)
    #for itemID in OOMP.items:
    for itemID in OOMP.itemsTypes["eda"]["items"]:
        item = OOMP.items[itemID]
        harvest(item,overwrite)

def harvest(item,overwrite=False):
    type = item["oompType"][0]
    if type == "FOOTPRINT":
        OOMP_automation_KICAD_footprints.harvestKicadFootprint(item)