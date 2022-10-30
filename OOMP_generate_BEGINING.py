import OOMP

import time

startTime= time.time()
mode = "all"
#mode = "regular"
#mode = "parts"
#mode = "projects"
#mode = "regular"
#mode = "none"

###### Setting Base Level
OOMP.loadPickle()
items = OOMP.items
makePickle = runCollections = runFootprints = runModules = runParts = runProjects = runSymbols = makePickle2 = runCSV = runHarvestProjects = runMatching = runInstances = runMigrating = runImages = runJson = runSummaries = False

###### gui ones
convertToKicad=False
harvestKicad=False

if mode == "regular":
    makePickle = False
    runCollections = False
    runFootprints = False
    runModules = False
    runParts = True
    runProjects = False
    runSymbols = False

    makePickle2 = False

    runCSV = False
    runHarvestProjects = False
    runMatching = False
    runInstances = False
    runMigrating = False
    runImages = False
    runJson = False
    runSummaries = False


###### run subset


    #items = OOMP.itemsTypes["parts"]["items"]



##### All
#makePickle = False
if mode == "all":    
    runCollections = False
    runFootprints = runModules =runParts = runProjects = runSymbols = makePickle2 = runCSV = runHarvestProjects = runMatching = runInstances = runMigrating = runImages = runJson = runSummaries = True
##### Make Parts, make pickle, make csv etc
if mode == "parts":
    runParts = makePickle = makePickle2 = runCSV = runInstances = runMigrating = runImages = runJson =runSummaries = True
    items = OOMP.itemsTypes["parts"]["items"]
##### Make Projects, make pickle, make csv etc
if mode == "projects":
    runProjects =  makePickle =  runImages = False
    makePickle2 = runCSV = runHarvestProjects = runMatching = runMigrating =  runJson = runSummaries = True    
    items = OOMP.itemsTypes["projects"]["items"]




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
    OOMP_parts_EDA.matchFootprintsSymbols() ##### adds a symbol or footprint file detailFootprintsOOMP    

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



########################################
######  Make Pickle
if makePickle2:
    print("Making pickle")
    OOMP.makePickle()




#######################################
######  CSV

import OOMP_csv
import OOMP_csv_BASE

if runCSV:
    print("Running CSV")
    OOMP.loadPickle()
    
    #OOMP_csv.make()
    OOMP_csv_BASE.makeCSVSummaries()
    for item in items:
        OOMP_csv_BASE.makeCSVFile(OOMP.items[item])

#######################################
######  HARVEST PARTS

import OOMP_projects_partsHarvest_BASE

if runHarvestProjects:
    print("Running Harvest Parts")
    OOMP.loadPickle()
    
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        OOMP_projects_partsHarvest_BASE.harvestParts(OOMP.items[itemID])
    for itemID in OOMP.itemsTypes["modules"]["items"]:
        OOMP_projects_partsHarvest_BASE.harvestParts(OOMP.items[itemID])  
    OOMP.makePickle()        


#######################################
######  MATCH PARTS

import OOMP_projects_partsMatch

if runMatching:
    print("Running Match Parts")
    OOMP.loadPickle()
    
    for itemID in OOMP.itemsTypes["projects"]["items"]:
        OOMP_projects_partsMatch.matchParts(OOMP.items[itemID])
    OOMP_projects_partsMatch.partReport()    
    OOMP.makePickle()        

#######################################
######  MATCH INSTANCES

import OOMP_parts_INSTANCES

if runInstances:
    print("Running Instances")
    OOMP.loadPickle()    
    OOMP_parts_INSTANCES.loadAllInstances()


#######################################
######  MIGRATING

import OOMP_migrate_BASE

if runMigrating:
    OOMP.loadPickle()
    for item in items:
    #for item in OOMP.itemsTypes["projects"]["items"]:
        OOMP_migrate_BASE.migrateFiles(OOMP.items[item])

#######################################
######  IMAGES
import OOMP_images_BASE

if runImages:
    OOMP_images_BASE.generateAllResolutions()

#######################################
######  JSON
import OOMP_json_BASE
if runJson:
    OOMP.loadPickle()
    
    
    for item in items:
        OOMP_json_BASE.makeJson(OOMP.items[item],overwrite=True)

#######################################
######  SUMMARIES
import OOMP_summaries_BASE
import OOMP_summaries_INDEXES
if runSummaries:
    OOMP.makePickle()

    #OOMP.loadPickle()
    
    
    
    for item in items:
        OOMP_summaries_BASE.createSummary(OOMP.items[item],overwrite=True)
    OOMP_summaries_INDEXES.generatePartsIndex()
    OOMP_summaries_INDEXES.generateCollectionsIndex()




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

