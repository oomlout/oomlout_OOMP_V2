import OOMP
import OOMP_symbols_BASE

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")
#OOMP.loadParts("pickle")

def working():
    #OOMP_symbols_BASE.createAllSymbols()

    OOMP_symbols_BASE.createSymbolLibraries()


def make():
    OOMP_symbols_BASE.createAllSymbols()
    OOMP_symbols_BASE.createSymbolLibraries()

def harvest():
    pass

#working
#make()
