import OOMP_symbols
import OOMP_symbols_BASE
import OOMP_parts
import OOMP


#OOMP_symbols_BASE.gitPull()
OOMP_symbols_BASE.createAllSymbols()

###### if you change a symbol need to run this before everything is fixed
def generateChanges():
    OOMP_base.loadPickle()
    OOMP.loadFast()
    OOMP_parts.make()
    OOMP.loadFast()
    OOMP_symbols.make()
    OOMP.loadFast()
    OOMP_summaries.document(filter="parts")

#OOMP_base.makePickle()
#OOMP_base.loadPickle()

#OOMP_symbols.make()

#OOMP_symbols.harvest()

#generateChanges()
