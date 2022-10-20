import OOMP

import OOMP_parts_BASE

import OOMP_parts_EDA

def working():
    OOMP.loadParts("pickle")
    OOMP_parts_BASE.createAllParts()

    OOMP_parts_EDA.matchFootprintsSymbols()


def make():    
    OOMP_parts_BASE.createAllParts()    
    OOMP_parts_EDA.matchFootprintsSymbols() ##### adds a symbol or footprint file detailFootprintsOOMP
    pass

def harvest():
    pass
