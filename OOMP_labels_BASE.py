import OOMP

import os
import re
import subprocess

def generateLabels(item,overwrite=False):
    oompID = item["oompID"][0]
    print("Generating labels for:" + oompID)
    templates = []
    templates.append({"template" : "templates/label/OOMP-label-inventory.tmpl.svg", "fileType" :"labelInventory"})

    for template in templates:
        generateLabel(item,template,overwrite)


def generateLabel(item,template,overwrite):
    oompID = item["oompID"][0]
    #inventory label
    output = OOMP.getFileItem(item,template["fileType"],extension = "svg")
    outputPDF = OOMP.getFileItem(item,template["fileType"],extension = "pdf")
    outputPNG = OOMP.getFileItem(item,template["fileType"],extension = "png") 
    if not os.path.isfile(output) or overwrite:    
        print("    Generating Label " + output)
        oompSearchAndReplace(template["template"], output, item)
        oompMakePDF(output,outputPDF)
        oompMakePDF(output,outputPNG)
    
def oompSearchAndReplace(inFile,outFile,item):
    oompID = item["oompID"][0]
    
    f = open(inFile, "r")
    template = f.read()
    f.close()

    template = template.replace("%%ID%%", oompID)

    
    splitters = ["@1","@@"]
    for y in splitters:
        delim = y
        ##matches = re.findall(r'@1.+?@1',template)
        matches = re.findall(delim + '.+?' + delim,template)

        ##  CODE
        ##  @@@1%%ID%%,oompPart.oompID,oompDesc@1,oompDesc.code,name@@

        ##  PART DETAIL
        ##  @@%%ID%%,oompPart.oompID,name@@

        for x in matches:
##            print(x)
            #remove deliminator
            orig = x
            x = x.replace(delim,"")
            #split replace
            splitTag = x.split(",")
            if len(splitTag) > 1:
                style = splitTag[1]
                tag = splitTag[2]
                if "oompPart" in style:
                    part = item
                    ##print(part)
                    replaceValue = part[tag][0]
##                    print("        Replacing: " + x + " with -- " + replaceValue )
                    template = template.replace(orig,replaceValue)
                else: ##detail
                    cat = ""
                    if "oompType" in style:
                        cat = "type"
                    elif "oompSize" in style:
                        cat = "size"
                    elif "oompColor" in style:
                        cat = "color"
                    elif "oompDesc" in style:
                        cat = "desc"
                    elif "oompIndex" in style:
                        cat = "index"                    
                    #replaceValue = OOMP.getDetailByCode(cat,splitTag[0]).name
                    replaceValue = OOMP.tagDetails[cat][splitTag[0]]["name"]
##                    print("        Replacing: " + x + " in " + cat + " with -- " + replaceValue )
                    template = template.replace(orig,replaceValue)
                
    
    f = open(outFile, "w+")
    f.write(template)
    f.close

def oompMakePDF(inFile,outFile):
    executeString = "inkscape.exe --export-filename=\"" + outFile + "\" \"" + inFile + "\""
    print("                Converting to : " + outFile)
    subprocess.call(executeString)
