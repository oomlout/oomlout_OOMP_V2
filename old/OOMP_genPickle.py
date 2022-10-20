import OOMP

print("Generating Pickle Files:")


filter = "all"
#filter = "nofootprints"
#filter = "parts"
OOMP.loadParts(filter)


# OOMP.loadParts("modules")


#__import__("sourceFiles.oompLoad")  
#exportPickle() 


print(OOMP.getReport())

#import OOMP_genBlanks
import OOMP_genBlanks




input("ALL DONE")

for part in OOMP.parts:
    pass
    #print(part.getID())

                                  