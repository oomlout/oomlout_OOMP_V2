#import OOMP
from oomBase import *


def migrateOompFiles():
    directory = "C:/GH/OLD01-oomlout-OOMP/parts/"
    fileFilter = ".oomp"
    for subdir, dirs, files in os.walk(directory):
            for file in files:
                if(fileFilter in file):
                    filename = subdir + "/" + file                    
                    
                    migrateFile(subdir,file)
                    

def migrateFile(subdir,file):
    
    infile = subdir + "/" + file                    
    outfolder = subdir.replace("C:/GH/OLD01-oomlout-OOMP/parts","test/")
    oomMakeDir(outfolder)
    outfile= outfolder + "/details.py"
    print("Migrating from:" + infile + "  to  "  + outfile)
    inf = open(infile,"r")
    contents = inf.read()
    inf.close()
    outf = open(outfile,"w")

    removeList = []
    removeList.append("<xml>")
    removeList.append("</xml>")
    removeList.append("<oompPart>")
    removeList.append("</oompPart>")
    #removeList.append("\t")
    removeList.append("<xml>")
    for remove in removeList:
        contents = contents.replace(remove,"")

    removeBetweenList = []
    removeBetweenList.append("sourceList")
    removeBetweenList.append("oplList")
    removeBetweenList.append("oompStatCount")
    removeBetweenList.append("oompStatPercent")

    contents = contents.replace("\n","WWAW67H8")

    for between in removeBetweenList:
        removeBit = stringBetween(contents,"\<" + between + "\>","\</" + between + "\>")
        start = "<" + between + ">"
        end = "</" + between + ">"
        contents = contents.replace(start + removeBit + end,"")


    ##### diagrams
    diagTypes = ["oompSchem","oompDiag","oompBbls","oompIden","oompSimp"]

    for type in diagTypes:
        bits = stringBetween(contents,"\<" + type + "\>","\</" + type + "\>")
        newBits = bits
        
        contents= contents.replace("<" + type + ">","")
        contents= contents.replace("</" + type + ">","")
        newBits = newBits.replace("drawItem",type)
        contents= contents.replace(bits,newBits)

        
    ###### variables
    variableNames = [["ooPitch","pitch"],["ooNumPins","pins"]]
    
    variables = ""
    variablesLine = ""
    for variable in variableNames:
        value = stringBetween(contents,"\<" + variable[0] + "\>","\</" + variable[0] + "\>")
        value = value.replace("mm","")
        value = value.replace("2X0","2*")
        value = value.replace("2X","2*")
        if value != "":
            variables = variables + variable[1] + " = " + value + "\n"
            variablesLine = variablesLine + "," + variable[1] + " = " + value

    contents = contents.replace("WWAW67H8","\n")

    ###### tags
    tagList = stringsBetween(contents,"<",">")
    tagList = list(dict.fromkeys(tagList))
    tags = ""

    hexID = ""
    type = ""
    size = ""
    color = ""
    desc = ""
    index = ""

    for tag in tagList:
        if not "/" in tag:
            values = stringsBetween(contents,"<" + tag + ">","\</" + tag + ">")
            for value in values:
                if value == "oompType":
                    type = value
                if value == "oompSize":
                    size = value
                if value == "oompColor":
                    color = value
                if value == "oompDesc":
                    desc = value
                if value == "oompIndex":
                    index = value
                line = "newPart.addTag('" + tag + "','" + value.replace("'","&#39") + "')"
                tags = tags + line + "\n"

    ###### oompTags line
    #newPart = OOMPtags.addTags(newPart,"HEAD-I01-X-X-X",pins=pins)
    idList = ["oompType","oompSize","oompColor","oompDesc","oompIndex"]
    id = []
    for i in idList:
        id.append(stringBetween(contents,"\<" + i + "\>","\</" + i + "\>"))
    if id[4] == 1:
        id[4] = "01"
    oompID = id[0] + "-" +id[1].zfill(2) + "-" +id[2] + "-" +id[3] + "-" + id[4].zfill(2)

    variablesLine = variablesLine + ",hexID=" + hexID + ",oompType=" + type + ",oompSize=" + size + ",oompColor=" + color + ",oompDesc=" + desc + ",oompIndex=" + index
    partLine = 'newPart = OOMPtags.addTags(newPart,"' + oompID + '"' + variablesLine + ')\n'


    outf.write("import OOMP \n")
    outf.write("import OOMPtags \n")
    outf.write("\n")
    outf.write("######  Auto translated oomp file\n")
    outf.write("\n")
    outf.write("newPart = OOMP.oompItem()\n")
    outf.write(variables)
    outf.write(tags)
    outf.write(partLine)
    outf.write("OOMP.parts.append(newPart)\n")
    contents= contents.replace("\t","")
    #outf.write(contents)
    
    


    outf.close()


migrateOompFiles()                    