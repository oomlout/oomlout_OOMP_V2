import OOMP

import OOMP_symbols_BASE
import OOMP_hex_FOOTPRINTS
from oomBase import *

import os

from kiutils.symbol import SymbolLib

def createSymbols():  
    print("Creating Kicad Symbols")  
    for git in OOMP_symbols_BASE.symbolGits:
        owner = OOMP_symbols_BASE.symbolGits[git]["code"]
        print("    Creating for: " + owner)
        print("        Getting Names")
        symbols = getKicadSymbolNames(owner)  
        print("        Making Symbols")      
        for symbol in symbols: 
            d = {}
            d["oompType"] =  "SYMBOL"
            d["oompSize"] =  "kicad"
            d["oompColor"] =  owner
            d["oompDesc"] =  symbol[0]
            d["SYMBOL"] = symbol[1]
            loadSymbolDict(d)
            OOMP_symbols_BASE.makeSymbol(d)




def loadSymbolDict(d):
    
    origDict = d
    symbol = d["SYMBOL"]

    d= {}
    #print(symbol)
    """
Property(key='Reference', value='U', id=0, position=Position(X=-7.62, Y=19.05, angle=0, unlocked=False), effects=Effects(font=Font(face=None, height=1.27, width=1.27, thickness=None, bold=False, italic=False, lineSpacing=None), justify=Justify(horizontally=None, vertically=None, mirror=False), hide=False))
1:
Property(key='Value', value='14529', id=1, position=Position(X=-7.62, Y=-21.59, angle=0, unlocked=False), effects=Effects(font=Font(face=None, height=1.27, width=1.27, thickness=None, bold=False, italic=False, lineSpacing=None), justify=Justify(horizontally=None, vertically=None, mirror=False), hide=False))
    """

    try:
        d["kicadSymbol" + "Extends"] = symbol.extends
    except:
        print("        Symbol does not extend another")

    for property in symbol.properties:
        #print(property)
        d["kicadSymbol" + property.key] = property.value.replace("'","")

    ###### grab pin names from first example only
    try:
        for unit in symbol.units:
            pins = unit.pins  
            if len(pins) > 0:
                break

        for pin in pins:
            #print(pin)
            d["kicadSymbolPin" + pin.number + "Name"] = pin.name 
            d["kicadSymbolPin" + pin.number + "ElectricalType"] = pin.name 
            d["kicadSymbolPin" + pin.number + "Position"] = '"' + pin.position + '"' 
            d["kicadSymbolPin" + pin.number + "Length"] = '"' +  pin.length  + '"'
    except:
        print("        Unable to capture pins")



    origDict["oompIndex"] = d["kicadSymbolValue"]
    oompID = origDict["oompType"] + "-" + origDict["oompSize"] + "-" + origDict["oompColor"] + "-" + origDict["oompDesc"] + "-" + origDict["oompIndex"]
    origDict["hexID"] = OOMP_hex_FOOTPRINTS.getFootprintHex(oompID)
    ###### Copy source symbol to OOMP directory
    if True:        
        destDir = OOMP.getDir("eda") + "SYMBOL/kicad/" + origDict["oompColor"] + "/" + origDict["oompDesc"] + "/" 
        oomMakeDir(destDir)
        destDir = destDir +   origDict["oompIndex"] + "/"
        oomMakeDir(destDir)
        destFile = destDir + "symbol.kicad_sym"
        destFileOOMP = destDir + oompID + ".kicad_sym"
        destFileOOMPShort = destDir + origDict["oompIndex"] + ".kicad_sym"
        ###### open library
        filename = "templates/oomlout_OOMP_partsTEMPLATE.kicad_sym"
        sym = SymbolLib().from_file(filename)
        ###### add symbol to library
        sym.symbols.append(symbol)
        sym.to_file(destFile)
        sym.to_file(destFileOOMP)
        sym.to_file(destFileOOMPShort)
    origDict["symbolKicadDetails"] = []
    origDict["symbolKicadDetails"].append(d)
    return origDict

def getKicadSymbolNames(owner):
    directory = "sourceFiles/git/kicadSymbols/" + owner + "/"        
    filter= "" ###### for debugging
    symbols = []
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            filename = subdir +"" + file
            if("kicad_sym" in file):   
                if(filter in filename):                             
                    #print("Working on File: "  + filename)
                    
                    try:
                        sym = SymbolLib().from_file(filename)
                    except:
                        print("    ERROR Unable to parse file into kiutils")
                    for symbol in sym.symbols:
                        ping()
                        symbols.append([file.replace(".kicad_sym",""),symbol])
    return symbols    