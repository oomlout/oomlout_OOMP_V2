import OOMP
import OOMP_summaries_BASE as osb


######  Pages

def generateReadmeFootprint(item, mdFile):
    pass

def generateReadmeProject(item, mdFile):
    addOOMPPartsList(item,mdFile)
        
def generateReadmePart(item, mdFile):
    pass
        
######  Helpers

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