import OOMP

import time

startTime= time.time()

makePickle = False
runCollections = False
runFootprints = False
runModules = False
runParts = False
runProjects = False
runSymbols = False

runCSV = False
runHarvest = False
runMatching = False
runMigrating = False
runImages = False
runSummaries = True

###### gui ones
convertToKicad=False
harvestKicad=False

########################################
######  Make Pickle
if makePickle:
    print("Making pickle")
    OOMP.makePickle()

########################################
######  COLLECTIONS
import OOMP_collections
import OOMP_collections_BASE

if runCollections:
    print("Running Collections")
    #OOMP_colelctions.make()
    OOMP.loadPickle()
    OOMP_collections_BASE.makeAllCollections()
    #OOMP_collections.create()
    #OOMP.makePickle()
    #OOMP_collections_BASE.createAllCollections()


########################################
######  FOOTPRINTS
import OOMP_footprints
import OOMP_footprints_BASE
#OOMP_footprints.make()
if runFootprints:
    OOMP_footprints_BASE.gitPull()
    OOMP_footprints_BASE.createAllFootprints()
    #OOMP_footprints_BASE.createFootprintLibraries()

########################################
######  MODULES
import OOMP_modules
import OOMP_modules_BASE

if runModules:
    print("Running Modules")
    #OOMP_modules.make()
    #OOMP.loadPickle()
    OOMP_modules_BASE.makeAllModules()
    

########################################
######  PARTS
import OOMP_parts
import OOMP_parts_BASE
import OOMP_parts_EDA
#OOMP_parts.make()
if runParts:
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
    OOMP_symbols_BASE.gitPull()
    OOMP_symbols_BASE.createAllSymbols()
    #OOMP_symbols_BASE.createSymbolLibraries()







#######################################
######  CSV

import OOMP_csv
import OOMP_csv_BASE

if runCSV:
    print("Running CSV")
    OOMP.loadPickle()
    
    #OOMP_csv.make()
    OOMP_csv_BASE.makeCSVSummaries()
    for item in OOMP.items:
        OOMP_csv_BASE.makeCSVFile(OOMP.items[item])

#######################################
######  HARVEST PARTS

import OOMP_projects_partsHarvest_BASE

if runHarvest:
    print("Running Harvest Parts")
    OOMP.loadPickle()
    
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        OOMP_projects_partsHarvest_BASE.harvestParts(OOMP.items[itemID])
    for itemID in OOMP.itemsTypes["modules"]["items"]:
        OOMP_projects_partsHarvest_BASE.harvestParts(OOMP.items[itemID])  


#######################################
######  MATCH PARTS

import OOMP_projects_partsMatch

if runMatching:
    print("Running Match Parts")
    OOMP.loadPickle()
    
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        OOMP_projects_partsMatch.matchParts(OOMP.items[itemID])
    #for itemID in OOMP.itemsTypes["modules"]["items"]:
        #OOMP_projects_partsMatch.matchParts(OOMP.items[itemID])


#######################################
######  MIGRATING

import OOMP_migrate_BASE

if runMigrating:
    OOMP.loadPickle()
    for item in OOMP.items:
    #for item in OOMP.itemsTypes["projects"]["items"]:
        OOMP_migrate_BASE.migrateFiles(OOMP.items[item])

#######################################
######  IMAGES
import OOMP_images_BASE

if runImages:
    OOMP_images_BASE.generateAllResolutions()

#######################################
######  SUMMARIES
import OOMP_summaries_BASE
if runSummaries:
    #OOMP.makePickle()
    OOMP.loadPickle()
    for item in OOMP.items:
    #for item in OOMP.itemsTypes["projects"]["items"]:
        OOMP_summaries_BASE.createSummary(OOMP.items[item],overwrite=True)





################################################################################
################################################################################
######  GUI ONES

#######################################
######  EAGLE CONVERT TO KICAD
import OOMP_kicad_BASE
if convertToKicad:
    OOMP_kicad_BASE.convertAllEagleToKicad(overwrite=False)

#######################################
######  HARVESTING KICAD
if harvestKicad:
    OOMP_kicad_BASE.harvestAllKicad(overwrite=False)








print("")
print("Time to execute: " + str(round(time.time()-startTime)) + " sec")

