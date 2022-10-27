import OOMP

import OOMP_collections_BASE

def working():
    OOMP.loadParts("pickle")

    #OOMP_collections_BASE.generateCollections()

    OOMP_collections_BASE.generatCollectionsPages()

#working()

def make():
    OOMP_collections_BASE.makeAllCollections()

def create():
    OOMP_collections_BASE.createAllCollections()