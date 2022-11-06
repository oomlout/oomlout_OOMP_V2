import OOMP

import time

startTime= time.time()

runFootprints = False
runCollections = True
runModules = False
runParts = False
runProjects = False
runSymbols = False
runMigrating = False
runImages = False
runSummaries = False
########################################
######  FOOTPRINTS
import OOMP_footprints
import OOMP_footprints_BASE
if runFootprints:
    print("Running Footprints")
    #OOMP_footprints.make()
    OOMP_footprints_BASE.gitPull()
    OOMP_footprints_BASE.createAllFootprints()
    #OOMP_footprints_BASE.createFootprintLibraries()

########################################
######  Collections
import OOMP_collections
import OOMP_collections_BASE

if runCollections:
    print("Running Collections")    
    #OOMP_collections.make()
    OOMP.loadPickle()
    OOMP_collections_BASE.makeAllCollections()
    #OOMP.makePickle()
    OOMP.loadPickle()
    #OOMP_collections.create()
    OOMP_collections_BASE.createAllCollections()

########################################
######  MODULES
import OOMP_modules
import OOMP_modules_BASE
#OOMP_modules.make()
if runModules:
    print("Running Modules")
    OOMP_modules_BASE.createAllModules()

########################################
######  PARTS
import OOMP_parts
import OOMP_parts_BASE
import OOMP_parts_EDA
#OOMP_parts.make()
if runParts:
    print("Running Parts")
    OOMP_parts_BASE.createAllParts()    
    #OOMP_parts_EDA.matchFootprintsSymbols() ##### adds a symbol or footprint file detailFootprintsOOMP    

########################################
######  PROJECTS
import OOMP_projects
import OOMP_projects_SPAR
import OOMP_projects_ADAF
###### projects
#OOMP_projects.preMake():
#OOMP_projects_BASE.preMakeAllProjects()
if runProjects:
        print("Running Projects")
        OOMP_projects_SPAR.farmProjects() ###### get repo list
        OOMP_projects_SPAR.makeBaseProjects() #go through all repos and pull git details and whether they are a project or not        
        OOMP_projects_SPAR.createProjects()
        
        OOMP_projects_ADAF.farmProjects() ###### get repo list
        OOMP_projects_ADAF.makeBaseProjects() #go through all repos and pull git details and whether they are a project or not        
        OOMP_projects_ADAF.createProjects()
#OOMP_projects.make()
#OOMP_projects_BASE.createAllProjects()


########################################
######  SYMBOLS
import OOMP_symbols
import OOMP_symbols_BASE
#OOMP_symbols.make()

if runSymbols:
    print("Running Symbols")
    OOMP_symbols_BASE.gitPull()
    OOMP_symbols_BASE.createAllSymbols()
    #OOMP_symbols_BASE.createSymbolLibraries()

#######################################
######  MIGRATING

import OOMP_migrate_BASE

if runMigrating:
    print("Running Migrating")
    OOMP.loadPickle()
    for item in OOMP.items:
        OOMP_migrate_BASE.migrateFiles(OOMP.items[item])

#######################################
######  IMAGES
import OOMP_images_BASE

if runImages:
    print("Running Images")
    OOMP_images_BASE.generateAllResolutions()

#######################################
######  SUMMARIES
import OOMP_summaries_BASE

if runSummaries:
    print("Running Summaries")
    OOMP.makePickle()
    #OOMP.loadPickle()
    for item in OOMP.items:
        OOMP_summaries_BASE.createSummary(OOMP.items[item],overwrite=True)

print("")
print("Time to execute: " + str(round(time.time()-startTime)) + " sec")
