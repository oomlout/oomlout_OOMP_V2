import OOMP
import OOMP_migrate_BASE
name = "OOMP_migrate_BASE"


def makeAll(overwrite=False):    
    #for itemID in OOMP.items:
    
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
    for itemID in OOMP.items:
    #for itemID in OOMP.itemsTypes["modules"]["items"]:
        item = OOMP.items[itemID]
        generate(item,overwrite)
    

def generate(item,overwrite=False):
    OOMP_migrate_BASE.migrateFiles(item)

def harvestAll(overwrite=False):
    OOMP_projects.harvestAll(overwrite)
    print("Harvest all for: " + name)
    for itemID in OOMP.items:
    #for item in OOMP.itemsTypes["parts"]["items"]:
        item = OOMP.items[itemID]
        harvest(item,overwrite)

def harvest(item,overwrite=False):
    pass