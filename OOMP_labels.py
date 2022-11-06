import OOMP
import OOMP_labels_BASE
name = "OOMP_labels_BASE"

def makeAll(overwrite=False):
    print("Make all for: " + name)
    pass

def make(item,overwrite=False):
    pass

def createAll(overwrite=False):
    print("Create all for: " + name)
    pass

def create(item,overwrite=False):
    pass

def generateAll(overwrite=False):
    print("Generate all for: " + name)
    for itemID in OOMP.itemsTypes["parts"]["items"]:
        generate(OOMP.items[itemID],overwrite)

def generate(item,overwrite=False):
    OOMP_labels_BASE.generateLabels(item,overwrite)

def harvestAll(overwrite=False):
    print("Harvest all for: " + name)
    pass

def harvest(item,overwrite=False):
    pass