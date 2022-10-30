import OOMP
import OOMP_summaries_BASE as osb


######  Pages

def generateReadmeFootprint(item, mdFile):
    pass

def generateReadmePart(item, mdFile):
    addFootprintList(item,mdFile)
    addSymbolList(item,mdFile)
    addOOMPInstancesList(item,mdFile)
    pass


def generateReadmeProject(item, mdFile):
    addIbom(item,mdFile)
    addOOMPPartsList(item,mdFile)
        
        
######  Helpers

###### PARTS
def addFootprintList(item,mdFile):
    mdFile.new_header(level=2, title='Footprints')
    tags = []
    try:
        thingName = "footprintKicad"
        things = item[thingName]
        ####### extra things to add
        things.extend(item["footprintEagle"])
        for thing in things:
            try:
                part = OOMP.items[thing]
                link = OOMP.getFileItem(part,"",relative="github")
            except KeyError:
                part= ""
                link = ""
            image= osb.getImageItem(part,"image",link=False)
            text= thing
            designators = ""
            tags.append(osb.getLink(image+ "<br>" + text,link) )
        osb.addDisplayTable(mdFile,tags,4,align="left")
    except IndexError:
        print("       Skipping because it's a block")

def addOOMPInstancesList(item,mdFile):
    mdFile.new_header(level=2, title='OOMP Instances')
    tags = []
    try:
        thingName = "oompInstances"
        things = item[thingName]
        ####### extra things to add
        things.extend(item["symbolEagle"])
        for thing in things:
            try:
                project = OOMP.items[thing["PROJECT"]]
                link = OOMP.getFileItem(project,"",relative="github")
            except KeyError:
                part= ""
                link = ""            
            text= project["name"][0] + "<br>"  + project["oompID"][0] + "<br>" + thing["ID"]
            tags.append(osb.getLink(text,link))
        osb.addDisplayTable(mdFile,tags,4,align="left")
    except IndexError:
        print("       Skipping because it's a block")

def addSymbolList(item,mdFile):
    mdFile.new_header(level=2, title='Symbols')
    tags = []
    try:
        thingName = "symbolKicad"
        things = item[thingName]
        ####### extra things to add
        things.extend(item["symbolEagle"])
        for thing in things:
            try:
                part = OOMP.items[thing]
                link = OOMP.getFileItem(part,"",relative="github")
            except KeyError:
                part= ""
                link = ""
            image= osb.getImageItem(part,"image",link=False)
            text= thing
            designators = ""
            tags.append(osb.getLink(image,link) + "<br>" + text)
        osb.addDisplayTable(mdFile,tags,4,align="left")
    except IndexError:
        print("       Skipping because it's a block")
###### PROJECTS

def addIbom(item,mdFile):
    mdFile.new_header(level=2, title='I BOM')
    oompID = item["oompID"][0]
    osb.addLine(mdFile,osb.getLink("iBom.html","https://htmlpreview.github.io/?https://github.com/oomlout/oomlout_OOMP_projects/blob/main/" + oompID.replace("-","/") + "ibom.html"))


def addOOMPPartsList(item,mdFile):
    mdFile.new_header(level=2, title='OOMP Parts')
    tags = []
    tags.append("Image")    
    tags.append("OOMP ID")
    tags.append("Designators")
    try:
        oompParts = item["oompParts"][0]
        uniqueParts = []
        
        for part in oompParts:
            if oompParts[part] not in uniqueParts:
                uniqueParts.append(oompParts[part])
        for partID in uniqueParts:
            try:
                part = OOMP.items[partID]
                link = OOMP.getFileItem(part,"",relative="github")
            except KeyError:
                part= ""
                link = ""
            image= osb.getImageItem(part,"image",link=False)
            text= partID
            designators = ""
            for testPart in oompParts:
                if oompParts[testPart] == partID:
                    designators = designators + testPart + ","
            tags.append(osb.getLink(image,link))
            tags.append(osb.getLink(text,link))
            tags.append(osb.getLink(designators,link))
        osb.addDisplayTable(mdFile,tags,3,align="left")
    except IndexError:
        print("       Skipping because it's a block")