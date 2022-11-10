import OOMP
import OOMP_parts_BASE
name = "OOMP_parts_BASE"

import OOMP_parts_EDA
import OOMP_parts_INSTANCES

def makeAll(overwrite=False):  
    print("Make all for: " + name)
    for itemID in OOMP.items:
    #for item in OOMP.itemsTypes["parts"]["items"]:
        item = OOMP.items[itemID]
        make(item,overwrite)

def make(item,overwrite=False):    
        pass

def createAll(overwrite=False):   
    print("Create all for: " + name) 
    testID = "VREG-SO223-X-KLD1117-V12D"
    item2 = OOMP.items[testID]
    OOMP_parts_BASE.createAllParts()
    OOMP.makePickle()
    for itemID in OOMP.items:
        item2 = OOMP.items[testID]    
    #for item in OOMP.itemsTypes["parts"]["items"]:
        item = OOMP.items[itemID]
        create(item,overwrite)

def create(item,overwrite=False):    
    OOMP.exportTagsItem(item,"detailsFootprintsOomp",["footprintEagle","footprintKicad","symbolKicad"]) 

def generateAll(overwrite=False):
    print("Generate all for: " + name)
    #for itemID in OOMP.items:
    for itemID in OOMP.itemsTypes["parts"]["items"]:
        item = OOMP.items[itemID]
        generate(item,overwrite)
    ###### instances
    for partID in OOMP.itemsTypes["parts"]["items"]: ###### reset oomp instances
        OOMP.items[partID]["oompInstances"] = []
    OOMP_parts_INSTANCES.loadInstances()
    for partID in OOMP.itemsTypes["parts"]["items"]: ###### reset oomp instances
        try:
            item["oompInstances"] = OOMP_parts_INSTANCES.partInstances[itemID]
        except:
            pass
        OOMP.exportTagsItem(OOMP.items[partID],"detailsInstancesOomp",["oompInstances"])
    OOMP.makePickle()

    
def generate(item,overwrite=False):
    OOMP_parts_EDA.matchFootprint(item)
    OOMP.exportTagsItem(item,"detailsFootprintsOomp",["footprintEagle","footprintKicad","symbolKicad"]) 

def harvestAll(overwrite=False):
    print("Harvest all for: " + name)
    for itemID in OOMP.items:
    #for item in OOMP.itemsTypes["parts"]["items"]:
        item = OOMP.items[itemID]
        harvest(item,overwrite)

def harvest(item,overwrite=False):
    pass