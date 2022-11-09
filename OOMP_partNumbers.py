import OOMP
import OOMP_partNumbers_BASE
name = "OOMP_partNumbers_BASE"


def makeAll(overwrite=False):  
    print("Make all for: " + name)
    #for itemID in OOMP.items:    
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        item = OOMP.items[itemID]
        make(item,overwrite)

def make(item,overwrite=False):    
        pass

def createAll(overwrite=False):
    print("Create all for: " + name)
    OOMP_partNumbers_BASE.loadPartNumbers()
    OOMP_partNumbers_BASE.dictToCsv()
    OOMP_partNumbers_BASE.savePickle()    
    #for itemID in OOMP.items:
    for itemID in OOMP.itemsTypes["modules"]["items"]:
        item = OOMP.items[itemID]
        create(item,overwrite)

def create(item,overwrite=False):
    pass

def generateAll(overwrite=False):
    print("Generate all for: " + name)
    OOMP_partNumbers_BASE.loadPickle()
    #for itemID in OOMP.items:
    for itemID in OOMP.itemsTypes["parts"]["items"]:
        item = OOMP.items[itemID]
        generate(item,overwrite)
    OOMP.makePickle() 
    

def generate(item,overwrite=False):
    OOMP_partNumbers_BASE.loadMpnDpn(item)

def harvestAll(overwrite=False):    
    print("Harvest all for: " + name)
    for itemID in OOMP.items:
    #for item in OOMP.itemsTypes["parts"]["items"]:
        item = OOMP.items[itemID]
        harvest(item,overwrite)

def harvest(item,overwrite=False):
    pass