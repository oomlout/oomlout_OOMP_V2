import OOMP
import OOMPeda
from oomBase import *

import OOMP_symbols_KICAD
from kiutils.symbol import SymbolLib

def createAllSymbols():
    OOMP_symbols_KICAD.createSymbols()

def createSymbolLibraries():
    createSymbolLibrary()
    libraryName="oomlout_OOMP_kicad/oomlout_OOMP_JLCC_Basic.kicad_sym"
    style="JLCC"
    createSymbolLibrary(libraryName=libraryName,style=style)

def createSymbolLibrary(templateFile="templates/oomlout_OOMP_partsTEMPLATE.kicad_sym",libraryName="oomlout_OOMP_kicad/oomlout_OOMP_parts.kicad_sym",style=""):
    filename = templateFile
    outFile = libraryName
    symLib = SymbolLib().from_file(filename)
    for part in OOMP.getItems("parts"):
        oompID = part.getID()
        hexID = part.getHex()
        symbols = part.getTags("symbolKicad")
        if len(symbols) > 0:
            symbol = OOMP.getPartByID(symbols[0].value)
            symbolID = symbol.getID()
            if symbolID != "----":
                include = False
                symbolFile = symbol.getFilename("symbolkicad")
                if style == "":
                    extra = "-" + hexID
                    include = True
                elif style == "JLCC":
                    opl = part.getTags("oplPartNumber")
                    for o in opl:
                        if o.value["code"] == "C-JLCC":
                            extra = "-" + hexID +"-" + o.value["partID"]
                            include = True

                if include:
                    symIn = SymbolLib().from_file(symbolFile)
                    inSymbol = symIn.symbols[0]
                    oldID = inSymbol.id
                    ###### changing ID
                    inSymbol.id = oompID + extra
                    for unit in inSymbol.units:
                        unit.id = unit.id.replace(oldID,oompID + extra)
                    symLib.symbols.append(inSymbol)
                    ###### changing value
                    for property in inSymbol.properties:
                        if property.key == "Value":
                            property.value = oompID + extra
                        if property.key == "Footprint":
                            footprintID = "FOOTPRINT-kicad-oomlout_OOMP_kicad-oomlout_OOMP_parts-" + oompID + extra
                            property.value = "oomlout_OOMP_parts:" + oompID + extra
                        if property.key == "Datasheet":
                            property.value = "oom.lt/" + hexID
                        if property.key == "ki_description":
                            desc = getDesc(part)
                            property.value = desc + property.value
                    print("    Adding Symbol: " + oompID)
                    #symLib.to_file(outFile)
                    pass
                
            else:
                print("Missing symbol: " + symbols[0].value)
    symLib.to_file(outFile)

def getDesc(part):
    hexID = part.getHex()
    desc = "hexID: " + hexID + ";"
    tags = part.getTags("oplPartNumber")
    if len(tags) > 0:
        for tag in tags:
            desc = desc + "PARTL " + tag.value["code"] + ";" + tag.value["partID"] + ";"
    tags = part.getTags("distributerPartNumber")
    if len(tags) > 0:
        for tag in tags:
            desc = desc + "DISTR " + tag.value["code"] + ";" + tag.value["partID"] + ";"                            
    tags = part.getTags("manufacturerPartNumber")
    if len(tags) > 0:
        for tag in tags:
            if isinstance(tag.value,dict):
                desc = desc + "MANUF " + tag.value["code"] + ";" + tag.value["partID"] + ";"                            
            else:
                desc = desc + "MANUF " + "C-XXXX" + ";" + tag.value + ";"                            
    return desc