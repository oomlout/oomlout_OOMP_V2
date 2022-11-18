import OOMP

import time

startTime= time.time()



##########################
######  Section Import
##########################
sections = []
import OOMP_collections
sections.append(OOMP_collections)
import OOMP_csv
sections.append(OOMP_csv)
import OOMP_footprints
sections.append(OOMP_footprints)
import OOMP_qrCode
sections.append(OOMP_qrCode)
import OOMP_migrate
sections.append(OOMP_migrate)
import OOMP_redirects
sections.append(OOMP_redirects)
import OOMP_projects
sections.append(OOMP_projects)
import OOMP_parts
sections.append(OOMP_parts)
import OOMP_symbols
sections.append(OOMP_symbols)
import OOMP_labels
sections.append(OOMP_labels)
import OOMP_partNumbers
sections.append(OOMP_partNumbers)
import OOMP_summaries
sections.append(OOMP_summaries)
import OOMP_json
sections.append(OOMP_json)
import OOMP_images
sections.append(OOMP_images)
import OOMP_modules
sections.append(OOMP_modules)


###########################
######  Routines
###########################
def all(listOfRuns = sections,preMake = False,make=True,create=True,generate=True,harvest=False,fast=False):
    
    if preMake:
        OOMP_projects.preMakeAll()
    ###### makeAll
    ######    Everything needed to get things in line for creating
    if make:
        fastSkip = [OOMP_partNumbers]
        for section in listOfRuns:
            pass
            if not fast or section not in fastSkip:
                section.makeAll()
        if not fast:
            OOMP.makePickle()    
    ###### createAll
    ######     Makes the details files and directories
    if create:
        fastSkip = [OOMP_footprints,OOMP_projects,OOMP_partNumbers]
        for section in listOfRuns:
            pass
            if not fast or section not in fastSkip:
                section.createAll()
        if not fast:                
            OOMP.makePickle()    
    ###### generateAll
    ######   All the steps to add details and files
    if generate:
        fastSkip = [OOMP_migrate]
        for section in listOfRuns:
            pass
            if not fast or section not in fastSkip:
                section.generateAll()
    ###### harvestAll
    ######   Things that require a gui automation
    if harvest:
        for section in listOfRuns:
            pass
            section.harvestAll()

def generate():
    for section in sections:
        section.generateAll()
        
def harvest():
    for section in sections:
        section.harvestAll()


def make():
    for section in sections:
        section.makeAll()



def one(section):
    ###### makeAll
    ######    Everything needed to get things in line for creating
    section.makeAll()    
    ###### createAll
    ######     Makes the details files and directories
    section.createAll()
    ###### generateAll
    ######   All the steps to add details and files
    section.generateAll()
    ###### harvestAll
    ######   Things that require a gui automation
    #section.harvestAll()



#########################
#####  Section launch
#########################
#########################
#########################

OOMP.loadPickle()

#sectiosbsn = OOMP_collections
section = OOMP_csv
#section = OOMP_parts
#section = OOMP_projects
#section = OOMP_summaries
#section = OOMP_json
#section = OOMP_images
one(section)
#section.makeAll()    
#section.createAll()
#section.generateAll()
#section.harvestAll()


#all()
#multiple()

