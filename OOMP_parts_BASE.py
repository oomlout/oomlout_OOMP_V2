import OOMP
from oomBase import *

import OOMP_parts_OOML
import OOMP_parts_JLCC

import urllib.request


def createAllParts():
    OOMP_parts_OOML.createParts()
    OOMP_parts_JLCC.createParts()


def makePart(type="",size="",color="",desc="",index="",hexID="",extraTags=[],dict=""):
    if dict != "":
        type = dict["type"]
        size = dict["size"]
        color = dict["color"]
        desc = dict["desc"]
        index = dict["index"]
        hexID = dict["hexID"]
        try:
            extraTags = dict["extraTags"]
        except:
            pass

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
    oompSlashes = oompID.replace("-","/")
    #print("Making part: " + oompID)
    ping()

    inputFile = "templates/partsTemplate.py"
    outputDir = OOMP.baseDir + OOMP.getDir("parts") + oompSlashes + "/"
    oomMakeDir(outputDir)
    outputFile = outputDir + "details.py"

    datasheet = ""
    if dict != "":
        try:
            datasheet = dict["datasheet"]
        except:
            pass
    if datasheet != "" and datasheet != " " :
        if "http" in datasheet:
            if True:   
                download_url = datasheet
                filename = outputDir + "datasheet"
                if not os.path.exists(filename + ".pdf"): ######
                    #print("        Downloading datasheet: " + datasheet)
                    try:
                        response = urllib.request.urlopen(download_url, allow_redirects=True)    
                        file = open(filename + ".pdf", 'wb')
                        file.write(response.read())
                        file.close()            
                    except:
                        pass
                        print("         Error downloading datasheet")
                else:
                    pass
                    #print("        Skipping datasheet (already exists): " + datasheet)
                pass            

        else:
            try:
                oomCopyFile(datasheet,outputDir + "datasheet.pdf" )
            except:
                pass
                print("        datasheet not found: " + oompID + "  " + datasheet)


    #print("Making: " + outputFile)

    contents = oomReadFileToString(inputFile)
    contents = contents.replace("TYPEZZ",type)
    contents = contents.replace("SIZEZZ",size)
    contents = contents.replace("COLORZZ",color)
    contents = contents.replace("DESCZZ",desc)
    contents = contents.replace("INDEXZZ",index)
    contents = contents.replace("HEXZZ",hexID)
    
    tagString = ""
    for tag in extraTags:
        tagString = tagString + OOMP.getPythonLine(tagName=tag[0],tagValue=tag[1]) + "\n"

    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)


    ####### details 2 File
    outputFile = outputDir + "details2.py"
    if not os.path.exists(outputFile): ###### only make one if it doesn't alreadry exist
        inputFile = "templates/details2Template.py"
        outputDir = OOMP.baseDir + OOMP.getDir("parts") + oompSlashes + "/"
        oomMakeDir(outputDir)
        contents = oomReadFileToString(inputFile, encoding="utf-8")
        
        oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
        contents = contents.replace("OOMPIDZZ",oompID)
        oomWriteToFileUtf(outputFile,contents)

def getHexID(oompID):
    
    list = []
    list.append(["CAPC-","C"])
    list.append(["LEDS-","L"])
    list.append(["RESE-","R"])
    list.append(["HEAD-","H"])
    ######size
    list.append(["0201-","2"])
    list.append(["0402-","4"])
    list.append(["0603-","6"])
    list.append(["0805-","8"])
    list.append(["1206-","12"])
    list.append(["03-","3"])
    list.append(["05-","5"])
        ###### Headers
    list.append(["I01-",""])
    list.append(["JSTXH-","XH"])
    list.append(["JSTPH-","PH"])
    list.append(["JSTSH-","SH"])        
    
    ######desc
        ###### CAPC
    list.append(["PF","P"])
    list.append(["NF","N"])
    list.append(["UF","U"])

    list.append(["STAN",""])
        ###### HEAD
    list.append(["PI2X","2X"])        
    list.append(["PI",""])        

    ######index          
    if "CAPC" in oompID:  
        list.append(["-V50",""])  
        list.append(["-V25",""])  
    ###### HEAD
    list.append(["-RA","R"])
    list.append(["-RS","RS"])    
    list.append(["-SM","S"])    
    list.append(["-SHRO","SHR"])
    list.append(["-SHRR","SHRR"])
    
    list.append(["-V",""])
    list.append(["-D",""])
    list.append(["-01",""])
        
     ######color
    list.append(["X-",""])
    list.append(["R-","R"])
    list.append(["O-","O"])
    list.append(["Y-","Y"])
    list.append(["G-","G"])
    list.append(["L-","L"])
    list.append(["V-","V"])
    list.append(["B-","B"])
    list.append(["P-","P"])   
    list.append(["W-","W"])   

    for l in list:
        oompID = oompID.replace(l[0],l[1])
    return oompID
