import OOMP
from oomBase import *

import OOMP_symbols_KICAD
from kiutils.symbol import SymbolLib


symbolGits = {}
git = 'oomlout_OOMP_kicad'
symbolGits[git] = {}
symbolGits[git]["code"] = git
symbolGits[git]["url"] = 'https://github.com/oomlout/oomlout_OOMP_kicad'
symbolGits[git]["name"] = "Oomlout's Symbols"
symbolGits[git]["description"] = "Oomlout's kicad symbol library."
######
git = 'kicad-symbols'
symbolGits[git] = {}
symbolGits[git]["code"] = git
symbolGits[git]["url"] = 'https://gitlab.com/kicad/libraries/kicad-symbols'
symbolGits[git]["name"] = "Kicad Default Symbols"
symbolGits[git]["description"] = "Kicad's default symbol library."

def gitPull():
    gits= []
    dir = "sourceFiles/git/kicadSymbols/"
    oomMakeDir(dir)
    for git in symbolGits:
        oomGitPullNew(symbolGits[git]["url"],dir)

def createAllSymbols():
    initializeSymbolFile()
    OOMP_symbols_KICAD.createSymbols()
    oomCloseFileUtf()

def initializeSymbolFile():
    outputFile = OOMP.getDir("eda") + "details2.py"
    oomOpenFileUtf(outputFile)

    contents = """
import OOMP

def load(newpart, it):
    pass
    
    
"""
    oomAddToOpenFileUtf(contents)

def makeSymbol(d):
    type = d["oompType"]
    size = d["oompSize"]
    color = d["oompColor"]
    desc = d["oompDesc"]   
    index = d["oompIndex"]

    d["name"] = desc + " : " + index

    hexID = d["hexID"]

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index

    #print("Making symbol: " + oompID)
    ping()

    oompSlashes = type + "/" + size + "/" + color + "/" + desc + "/" + index + "/"

    inputFile = "templates/edaTemplate.py"
    outputDir = OOMP.baseDir + OOMP.getDir("eda") + oompSlashes
    oomMakeDir(outputDir)
    #outputFile = outputDir + "details.py"
    outputFile = OOMP.getDir("eda") + "details.py"

    #print("Making: " + outputFile)
    ping()

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
            extraTags.append([tag,d[tag]])        
    tagString = ""
    for tag in extraTags:
        tagString = tagString + OOMP.getPythonLine(tagName=tag[0],tagValue=tag[1],indent="    ") + "\n"

    contents = contents.replace("EXTRAZZ",tagString)

    #oomWriteToFile(outputFile,contents)
    oomAddToOpenFileUtf(contents)
    pass

def createSymbolLibraries():
    createSymbolLibrary()
    libraryName="oomlout_OOMP_kicad_V2/oomlout_OOMP_JLCC_Basic.kicad_sym"
    style="JLCC"
    createSymbolLibrary(libraryName=libraryName,style=style)

def createSymbolLibrary(templateFile="templates/oomlout_OOMP_partsTEMPLATE.kicad_sym",libraryName="oomlout_OOMP_kicad_V2/oomlout_OOMP_parts.kicad_sym",style=""):
    filename = templateFile
    outFile = libraryName
    symLib = SymbolLib().from_file(filename)
    for partID in OOMP.itemsTypes["parts"]["items"]:
        part = OOMP.items[partID]
        oompID = part["oompID"][0]
        hexID = part["hexID"][0]
        symbols = part["symbolKicad"]
        if len(symbols) > 0:
            symbolID = symbols[0]
            try:
                #keys = OOMP.items.keys() 
                #for key in keys:
                #    print(key)
                symbol = OOMP.items[symbolID]
                symbolID = symbol["oompID"][0]
                if symbolID != "----":
                    include = False
                    symbolFile = OOMP.getFileItem(symbol,"kicadSymbol")
                    if style == "":
                        extra = "-" + hexID
                        include = True
                    elif style == "JLCC":
                        opl = part["oplPartNumber"]
                        for o in opl:
                            if o["code"] == "C-JLCC":
                                extra = "-" + hexID +"-" + o["partID"]
                                include = True

                    if include:
                        symIn = SymbolLib().from_file(symbolFile)
                        inSymbol = symIn.symbols[0]
                        oldID = inSymbol.id
                        ###### changing ID
                        if "VREG-SO235" in oompID:
                            pass
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
                        #print("    Adding Symbol: " + oompID)
                        ping()
                        #symLib.to_file(outFile)
                        pass
                    
                else:
                    pass
                #print("Missing symbol: " + symbols[0].value)
            except KeyError as e:
                #raise e
                print("symbol not found: " + symbolID)
    symLib.to_file(outFile)

def getDesc(part):    
    
    hexID = part["hexID"][0]
    oompID = part["oompID"][0]
    name = part["name"][0]
    desc = "oompID: " + oompID + ";" + "name: " + name + ";" + "hexID: " + hexID + ";"
    tags = part["oplPartNumber"]
    if len(tags) > 0:
        for x in range(0,min(len(tags),3)):
            desc = desc + str(tags[x])
    tags = part["distributorPartNumber"]
    if len(tags) > 0:
        for x in range(0,min(len(tags),3)):
            desc = desc + str(tags[x])
    tags = part["manufacturerPartNumber"]
    if len(tags) > 0:        
        for x in range(0,min(len(tags),3)):
            desc = desc + str(tags[x])
    return desc