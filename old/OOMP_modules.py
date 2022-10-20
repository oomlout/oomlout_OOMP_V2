import OOMP
import OOMP_modules_BASE
import OOMP_projects_BASE

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")
#OOMP.loadParts("pickle")


def working():
    OOMP_modules_BASE.createAllModules()
    #OOMP_modules_BASE.harvestModules()

#working()

def make():
    OOMP_modules_BASE.createAllModules()

def harvest():
    OOMP_modules_BASE.harvestModules()

