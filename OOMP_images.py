import OOMP
import OOMP_images_BASE
name = "OOMP_images_BASE"

def makeAll(overwrite=False):
    print("Make all for: " + name)
    for item in OOMP.items:
    #for item in OOMP.itemsTypes["parts"]["items"]:
        make(item,overwrite)


def make(item,overwrite=False):
    pass

def createAll(overwrite=False):
    print("Create all for: " + name)
    for itemID in OOMP.itemsTypes["collections"]["items"]:
        item = OOMP.items[itemID]
        create(item,overwrite)
        
def create(item,overwrite=False):
    pass

def generateAll(overwrite=False):
    print("Generate all for: " + name)
    OOMP_images_BASE.generateAllResolutions()
    for itemID in OOMP.items:
    #for item in OOMP.itemsTypes["parts"]["items"]:
        item = OOMP.items[itemID]
        generate(item,overwrite)

def generate(item,overwrite=False):
    pass

def harvestAll(overwrite=False):
    print("Harvest all for: " + name)
    for item in OOMP.items:
    #for item in OOMP.itemsTypes["parts"]["items"]:
        harvest(item,overwrite)

def harvest(item,overwrite=False):
    pass