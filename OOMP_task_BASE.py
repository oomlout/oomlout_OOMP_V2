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
import OOMP_labels
sections.append(OOMP_labels)
import OOMP_migrate
sections.append(OOMP_migrate)
import OOMP_projects
sections.append(OOMP_projects)
import OOMP_parts
sections.append(OOMP_parts)
import OOMP_partNumbers
sections.append(OOMP_partNumbers)
import OOMP_qr
sections.append(OOMP_qr)
import OOMP_summaries
sections.append(OOMP_summaries)
import OOMP_json
sections.append(OOMP_json)
import OOMP_images
sections.append(OOMP_images)


###########################
######  Routines
###########################
def all():
    ###### makeAll
    ######    Everything needed to get things in line for creating
    for section in sections:
        pass
        #section.makeAll()
    ###### createAll
    ######     Makes the details files and directories
    for section in sections:
        section.createAll()
    OOMP.makePickle()    
    ###### generateAll
    ######   All the steps to add details and files
    for section in sections:
        section.generateAll()
    ###### harvestAll
    ######   Things that require a gui automation
    for section in sections:
        pass
        #section.harvestAll()

def generate():
    for section in sections:
        section.generateAll()
        
def harvest():
    for section in sections:
        section.harvestAll()


def make():
    for section in sections:
        section.makeAll()



def multiple():
    ###### makeAll
    ######    Everything needed to get things in line for creating
    for section in sections:
        section.makeAll()
    ###### createAll
    ######     Makes the details files and directories
    for section in sections:
        section.createAll()
    OOMP.makePickle()    
    ###### generateAll
    ######   All the steps to add details and files
    for x in range(0,3):
        for section in sections:
            section.generateAll()
        OOMP.makePickle()            
    ###### harvestAll
    ######   Things that require a gui automation
    #for section in sections:
    #    section.harvestAll()

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

#sectiosbsn = OOMP_collections
#section = OOMP_parts
#section = OOMP_projects
#section = OOMP_summaries
#section = OOMP_json
section = OOMP_images
#one(section)
#section.makeAll()    
#section.createAll()
#section.generateAll()
#section.harvestAll()


#all()
#multiple()

