import OOMP
import OOMP_json_BASE
name = "OOMP_json_BASE"

def makeAll(overwrite=False):
    print("Make all for: " + name)
    for item in OOMP.items:
    #for item in OOMP.itemsTypes["parts"]["items"]:
        make(item,overwrite)


def make(item,overwrite=False):
    pass

def createAll(overwrite=False):
    print("Create all for: " + name)
    for itemID in OOMP.items:
    #for item in OOMP.itemsTypes["parts"]["items"]:
        create(OOMP.items[itemID],overwrite)

    

def create(item,overwrite=False):
    OOMP_json_BASE.makeJson(item,overwrite=True,short=True)

def generateAll(overwrite=False):
    print("Generate all for: " + name)
    for item in OOMP.itemsTypes["parts"]["items"]:
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