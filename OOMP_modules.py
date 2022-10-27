import OOMP
import OOMP_modules_BASE
import OOMP_projects_BASE

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")
#OOMP.loadParts("pickle")


def working():
    OOMP_modules_BASE.createModules()
    #OOMP_modules_BASE.harvestModules()

#working()

def make():
    OOMP_modules_BASE.makeAllModules()

def create():
    pass
def harvest():
    pass

