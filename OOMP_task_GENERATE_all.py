import OOMP
import OOMP_task_BASE

from oomBase import *

oomRuntime(mode="start")

#make = True
make = False

if make:
    OOMP.makePickle()
else:
    OOMP.loadPickle()



def all():
    OOMP_task_BASE.all(preMake=False,make=True,create=True,generate=True,harvest=False,fast=False)
    
    #OOMP_task_BASE.all(preMake=True,make=True,create=True,generate=True,harvest=False,fast=False)
#OOMP_task_BASE.all(preMake=False,make=False,create=False,generate=True,harvest=False,fast=False)

def partsAndProjects():
    import OOMP_parts
    import OOMP_projects
    import OOMP_summaries
    listOfRuns=[]
    listOfRuns.append(OOMP_parts)
    listOfRuns.append(OOMP_projects)
    listOfRuns.append(OOMP_summaries)
    OOMP_task_BASE.all(listOfRuns=listOfRuns,preMake=False,make=True,create=True,generate=True,harvest=False,fast=False)

#all()
OOMP_task_BASE.generate()
#all()
#partsAndProjects()



###### Fast skips 
    #OOMP_partNUmbers.make
    #OOMP_footprints.create
#OOMP_task_BASE.all(preMake=False,make=True,create=True,generate=True,harvest=False,fast=True)

#OOMP_task_BASE.all(preMake=False,make=False,create=False,generate=True,harvest=False) 0


print(oomRuntime())