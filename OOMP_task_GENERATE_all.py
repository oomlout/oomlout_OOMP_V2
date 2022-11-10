import OOMP
import OOMP_task_BASE


make = True
#make = False
if make:
    OOMP.makePickle()
else:
    OOMP.loadPickle()

OOMP_task_BASE.all(preMake=False,make=True,create=True,generate=True,harvest=False,fast=False)

###### Fast skips 
    #OOMP_partNUmbers.make
    #OOMP_footprints.create
#OOMP_task_BASE.all(preMake=False,make=True,create=True,generate=True,harvest=False,fast=True)
#OOMP_task_BASE.all(preMake=False,make=False,create=False,generate=True,harvest=False) 0