import OOMP
import OOMP_collections_BASE
name = "OOMP_collections_BASE"


def makeAll(overwrite=False):    
    print("Make all for: " + name)
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        item = OOMP.items[itemID]
        make(item,overwrite)

def make(item,overwrite=False):    
    pass

def createAll(overwrite=False):
    print("Create all for: " + name)
    OOMP_collections_BASE.makeAllCollections()
    for itemID in OOMP.itemsTypes["collections"]["items"]:
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
    

def generate(item,overwrite=False):
    pass

def harvestAll(overwrite=False):
    print("Harvest all for: " + name)
    #for itemID in OOMP.items:
    for itemID in OOMP.itemsTypes["eda"]["items"]:
        item = OOMP.items[itemID]
        harvest(item,overwrite)

def harvest(item,overwrite=False):
    pass