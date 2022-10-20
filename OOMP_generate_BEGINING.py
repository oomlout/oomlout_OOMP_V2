

runFootprints = False
runParts = False
runProjects = True
runSymbols = False
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
if runSymbols:    
    pass
    #OOMP_projects_IBBC.createProjects()
    #OOMP_projects_ADAF.createProjects()    
    #OOMP_projects_DANP.createProjects()    
    #OOMP_projects_ELLA.createProjects()
    #OOMP_projects_SEED.createProjects()
    #OOMP_projects_SIRB.createProjects()
    #OOMP_projects_SOPA.createProjects()
    #OOMP_projects_SPAR.createProjects()   


########################################
######  SYMBOLS
import OOMP_symbols
import OOMP_symbols_BASE
#OOMP_symbols.make()
if True:
    OOMP_symbols_BASE.gitPull()
    OOMP_symbols_BASE.createAllSymbols()
    #OOMP_symbols_BASE.createSymbolLibraries()


