import OOMP

import subprocess

def harvestKicadBoardCLI(item):
    oompID = item["oompID"][0]
    print("    Harvesting Kicad Board CLI: " + oompID)
    inFile = OOMP.getFileItem(item,"kicadBoard",relative="full")
    outFile = OOMP.getFileItem(item,"kicadBoard",extension="png",relative="full")
    outFile = ""
    kicadCLI(inFile,outFile,command="export",mode="pcb",format="png")

def kicadCLI(inFile,outFile="",command="export",mode="pcb",format="png"):
    if outFile == "":
        outFile = inFile.replace(".kicad_" + mode,"." + format)
    executeString = "kicad-cli.exe"
    executeString = executeString + " " + mode
    executeString = executeString + " " + command
    executeString = executeString + " -o " + outFile
    executeString = executeString + " " + inFile
    

    layers = "--layers F.Cu,F.Paste"

    print("                KICAD CLI: " + outFile)
    print(executeString)
    #subprocess.call(executeString)