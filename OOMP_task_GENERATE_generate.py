import OOMP
import OOMP_task_BASE


OOMP.makePickle()
#OOMP.loadPickle()
OOMP_task_BASE.generate()


repeats = 3
for x in range(0,repeats):
    OOMP.makePickle()
    OOMP_task_BASE.generate()