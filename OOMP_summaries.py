import OOMP
import OOMP_summaries_BASE
import OOMP_summaries_INDEXES
name = "OOMP_summaries_BASE"

def makeAll(overwrite=False):
    print("Make all for: " + name)
    for item in OOMP.items:
    #for item in OOMP.itemsTypes["parts"]["items"]:
        make(item,overwrite)


def make(item,overwrite=False):
    pass

def createAll(overwrite=False):
    print("Create all for: " + name)
    types = ["parts","projects","collections","modules","eda"]
    for type in types:
        #print("    " + type)
        #for itemID in OOMP.items:
        for itemID in OOMP.itemsTypes[type]["items"]:
            create(OOMP.items[itemID],overwrite)
        
    
    

def create(item,overwrite=False):
    pass

def generateAll(overwrite=False):
    print("Generate all for: " + name)
    #for itemID in OOMP.items:
    types = ["parts","projects","collections","modules","eda"]
    for type in types:
        print("    " + type)
        #for itemID in OOMP.items:
        for itemID in OOMP.itemsTypes[type]["items"]:
            generate(OOMP.items[itemID],overwrite)
        print()
    OOMP_summaries_INDEXES.generatePartsIndex()
    OOMP_summaries_INDEXES.generateCollectionsIndex()
    
    OOMP_summaries_BASE.generateCollectionsIndex()
    

def generate(item,overwrite=False):
    OOMP_summaries_BASE.createSummary(item,overwrite=True)

def harvestAll(overwrite=False):
    print("Harvest all for: " + name)
    for item in OOMP.items:
    #for item in OOMP.itemsTypes["parts"]["items"]:
        harvest(item,overwrite)

def harvest(item,overwrite=False):
    pass