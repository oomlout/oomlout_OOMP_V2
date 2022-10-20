import OOMP
import OOMPtags #### hex for footprint
import OOMP_symbols_BASE
from oomBase import *

import os

from kiutils.symbol import SymbolLib

def createSymbols():
    owners = ["kicad-symbols"]
    for owner in owners:
        symbols = getKicadSymbolNames(owner)        
        for symbol in symbols: 
            d = {}
            d["oompType"] =  "SYMBOL"
            d["oompSize"] =  "kicad"
            d["oompColor"] =  owner
            d["oompDesc"] =  symbol[0]
            d["SYMBOL"] = symbol[1]
            loadSymbolDict(d)
            makeSymbol(d)


def makeSymbol(d):
    type = d["oompType"]
    size = d["oompSize"]
    color = d["oompColor"]
    desc = d["oompDesc"]   
    index = d["oompIndex"]

    hexID = d["hexID"]

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index

    print("Making symbol: " + oompID)

    oompSlashes = type + "/" + size + "/" + color + "/" + desc + "/" + index + "/"

    inputFile = "templates/projectsTemplate.py"
    outputDir = "C:/GH/oomlout_OOMP/oomlout_OOMP_eda/" + oompSlashes
    oomMakeDir(outputDir)
    outputFile = outputDir + "details.py"

    print("Making: " + outputFile)

    contents = oomReadFileToString(inputFile)
    contents = contents.replace("TYPEZZ",type)
    contents = contents.replace("SIZEZZ",size)
    contents = contents.replace("COLORZZ",color)
    contents = contents.replace("DESCZZ",desc)
    contents = contents.replace("INDEXZZ",index)
    contents = contents.replace("HEXZZ",hexID)

    repoName = ""

    skipTags = ["oompType","oompSize","oompColor","oompDesc","oompIndex","SYMBOL","hexID"]

    extraTags = []
    for tag in d:
        if tag not in skipTags:
            extraTags.append(OOMP.oompTag(tag,d[tag]))        
    tagString = ""
    for tag in extraTags:
        tagString = tagString + tag.getPythonLine() + "\n"

    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)
    pass

def loadSymbolDict(d):
    symbol = d["SYMBOL"]
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
            d["kicadSymbolPin" + pin.number + "Position"] = pin.position 
            d["kicadSymbolPin" + pin.number + "Length"] = pin.length  
    except:
        print("        Unable to capture pins")



    d["oompIndex"] = d["kicadSymbolValue"]

    oompID = d["oompType"] + "-" + d["oompSize"] + "-" + d["oompColor"] + "-" + d["oompDesc"] + "-" + d["oompIndex"]
    d["hexID"] = OOMPtags.getFootprintHex(oompID)

    return d

def getKicadSymbolNames(owner):
    directory = "oomlout_OOMP_eda/sourceFiles/" + owner + "/"

    
    filter= "" ###### for debugging
    symbols = []
    count = 0
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            filename = subdir +"" + file
            if("kicad_sym" in file):   
                if(filter in filename):                             
                    print("Working on File: "  + filename)
                    try:
                        sym = SymbolLib().from_file(filename)
                    except:
                        print("    ERROR Unable to parse file into kiutils")
                    for symbol in sym.symbols:
                        symbols.append([file.replace(".kicad_sym",""),symbol])
                    count = count + 1
                    if count > 40:
                        pass
                    #break  ## For only one file
    return symbols    