import OOMP

import OOMP_collections
import OOMP_footprints
import OOMP_modules
import OOMP_parts
import OOMP_projects
import OOMP_summaries
import OOMP_symbols

def makePickle():
    OOMP.loadParts("all")
    print(OOMP.getReport())

def loadPickle():
    OOMP.loadParts("pickle")
    print(OOMP.getReport())


def all(load=False,reload=False,make=False,harvest=False,document=False):
    if load:
        makePickle
    else:
        loadPickle()
    
    #OOMP.loadParts(filter)
    print(OOMP.getReport())
    ###### Make everything
    list = [OOMP_collections, OOMP_footprints, OOMP_modules, OOMP_parts, OOMP_projects, OOMP_summaries, OOMP_symbols]

    if make:        
        for l in list:
            l.make()
            if reload:
                makePickle()

    if harvest:
        for l in list:
            l.harvest()
            if reload:
                makePickle()

    if document:
        OOMP_summaries.document()

def allAll():
    loadPickle()
    all(load=False,reload=False,make=True,harvest=False,document=True)
    makePickle()
    all(load=False,reload=False,make=True,harvest=False,document=True)
    makePickle()
    all(load=False,reload=False,make=True,harvest=False,document=True)

    input("ALL DONE")