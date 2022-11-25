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
    for itemID in OOMP.itemsTypes["eda"]["items"]:
        item = OOMP.items[itemID]
        generate(item,overwrite)
    OOMP_footprints_BASE.createFootprintLibraries()
    
import OOMP_kicad_BASE
from oomBase import *
def generate(item,overwrite=False):
    ping()
    OOMP_footprints_BASE.createFootprintBoardFile(item)
    OOMP_kicad_BASE.svgKicadBoard(item,overwrite=overwrite)

def harvestAll(overwrite=False):
    print("Harvest all for: " + name)
    #for itemID in OOMP.items:
    for itemID in OOMP.itemsTypes["eda"]["items"]:
        item = OOMP.items[itemID]
        harvest(item,overwrite)

def harvest(item,overwrite=False):
    type = item["oompType"][0]
    skips = ["CBI-RIGHT-ANGLE-PTH","PI_HAT_SPECIFICATION"]
    if type == "FOOTPRINT":
        include = True
        oompID = item["oompID"][0]
        for s in skips:
            if s.upper() in oompID.upper():
                include = False
        if include:
            OOMP_automation_KICAD_footprints.harvestKicadFootprint(item)