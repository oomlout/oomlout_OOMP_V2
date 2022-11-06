import OOMP_projects
import OOMP_projects_BASE
import OOMP_projects_ADAF
import OOMP_projects_SPAR
import OOMP_projects_HYDR
import OOMP_projects_PDP7
import OOMP_projects_OSOB
import OOMP_projects_SOPA

import OOMP_summaries_BASE

import OOMP


OOMP.makePickle()
#OOMP.loadPickle()

#OOMP_projects.make()

#OOMP_projects.harvest()

#OOMP_projects.all()

#OOMP_projects_ADAF.farmProjects() ###### get repo list
#OOMP_projects_ADAF.makeBaseProjects() #go through all repos and pull git details and whether they are a project or not
#OOMP_projects_ADAF.createProjects()

#OOMP_projects_SPAR.farmProjects() ###### get repo list
#OOMP_projects_SPAR.makeBaseProjects() #go through all repos and pull git details and whether they are a project or not
#OOMP_projects_SPAR.createProjects()


import OOMP_projects_partsHarvest_BASE

itemID = "PROJ-ADAF-1032-STAN-01"
itemID = "PROJ-SPAR-13118-STAN-01"
item = OOMP.items[itemID]

#OOMP_projects_partsHarvest_BASE.harvestParts(item)


######  PARTS MATCH
#############################

import OOMP_projects_partsMatch

import OOMP_projects_partsMatch_Special

OOMP_projects_partsMatch_Special.loadMatches()
OOMP_projects_partsMatch.matchParts(item)
for itemID in OOMP.itemsTypes["projects"]["items"]:
        #OOMP_projects_partsMatch.matchParts(OOMP.items[itemID])
        pass
    

#OOMP_projects_partsMatch.partReport()


###### Base Projects


#OOMP_projects_SPAR.farmProjects()
#OOMP_projects_BASE.makeBaseProjects("sparkfun","SPAR")

itemID = "PROJ-SOPA-0001-STAN-01"
item = OOMP.items[itemID]
#OOMP_projects_SOPA.createProjects()
#OOMP_projects_PDP7.createProjects()
#OOMP_projects_HYDR.createProjects()
#OOMP_projects_OSOB.createProjects()
filter = "OSOB"

for item in OOMP.itemsTypes["projects"]["items"]:
        if filter in item:
                pass        
                #OOMP_projects_BASE.harvestProject(OOMP.items[item],all=True)