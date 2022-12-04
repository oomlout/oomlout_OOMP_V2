import OOMP
import OOMP_summaries_BASE as osb

import re

def createTagMDs():
    print("Making Tag Summary Readme")
    outFile = "readmeCodes.md"
    mdFile = osb.newReadme(outFile)
    osb.addHeader(mdFile,"OOMP Codes Described",1)
    line= """A part's ID has five parts

    TYPE-SIZE-COLOR-DESCRIPTION-INDEX

	* TYPE - This defines the part type (Ex. HEAD - Header, LEDS - LED)
	* SIZE - This is the size category or package of a part (Ex.  I01 - 0.1", W04 - 1.4 Watt Resistor, 0603 - 0603 (SMD))
	* COLOR - This is the parts color or material (Ex. R - Red, M - Metal ) (Default X)
	* DESCRIPTION - This is a defining charachteristic of the part and is the same across a type (Ex. (HEAD) PI03 - 3 Pins, (RESE) O561 - 560 Ohms) (Default XXXX)
	* INDEX - This is an additional piece of information that differentiates a part and can change within type (Ex. 67 - 1% tolerance, RA - right angle) (Default 01)
"""
    osb.addLine(mdFile,line)
    osb.addHeader(mdFile,"OOMP Tag Summary",2)
    tagTypes = ["type","size","color","desc","index"]
    for tt in tagTypes:
        tags = OOMP.tagDetails[tt]
        osb.addHeader(mdFile,tt + "Tags",3)
        tagList = ["Code", "Name", "Description"]
        for tag in tags:
            normal = True
            regexList = ["[A]\d","[PI]\d","[O]\d","[L]\d","[MZ]\d","[PF]\d","[V]\d","[NF]\d","[UF]\d","^[0-9]+$","\d[D]","\d[W]","\d[P]"]
            for reg in regexList:
                if tt == "size" and reg == "^[0-9]+$":  ## leave SMD sizes but remove mm
                    if "mm" in tags[tag]["name"]:
                        normal = False
                else:
                    test = re.search(reg,tag)
                    if test != None:
                        normal = False
            if tag == "":
                normal = False
            if normal:
                tagList.append(tags[tag]["code"])
                tagList.append(tags[tag]["name"])
                tagList.append(tags[tag]["description"])
            else:
                pass
        if tt == "type":
            pass
        if tt == "size":
            tagList.append(["###"])
            tagList.append(["### mm"])
            tagList.append(["### mm"])
            pass
        if tt == "color":
            pass
        if tt == "desc":
            tagList.append(["MZ###"])
            tagList.append(["### MHz"])
            tagList.append(["### MHz"])
            tagList.append(["UF###"])
            tagList.append(["### Uf"])
            tagList.append(["### Uf"])
            tagList.append(["NF###"])
            tagList.append(["### nf"])
            tagList.append(["### nf"])
            tagList.append(["PF###"])
            tagList.append(["### pf"])
            tagList.append(["### pf"])
            tagList.append(["V###"])
            tagList.append(["### v"])
            tagList.append(["### v"])
            tagList.append(["PI###"])
            tagList.append(["### pins"])
            tagList.append(["### pins"])
            tagList.append(["O###"])
            tagList.append(["### Ohms"])
            tagList.append(["3 digit code for Ohms, (ie 103 10k,102 1k)"])
        if tt == "index":
            pass
        osb.addDisplayTable(mdFile,tagList,3)



    osb.addToc(mdFile)
    osb.saveReadme(mdFile)

