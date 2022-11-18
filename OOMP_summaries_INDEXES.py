import OOMP
import OOMP_summaries_BASE as osb

def generateCollectionsIndex(): 
    print("Generating Collection Index")  
    filename = OOMP.getDir("collections") + "/README.md"
    
    rFile = osb.newReadme(filename)
    osb.addHeader(rFile, title="Collections", level=1)
    
    parts = ["Collections"]
    for collectionID in OOMP.itemsTypes["collections"]["items"]:
        collection = OOMP.items[collectionID]
        name = collection["name"][0]
        description = collection["description"][0]    
        entry = ""
        entry = entry + osb.getLink(text = name,link = OOMP.getFileItem(collection,"readme",relative="noDir")) + "  <br>"
        entry = entry + description + ""
        
        parts.append(entry)
    osb.addDisplayTable(rFile,parts,1,align="left")       
    osb.saveReadme(rFile)

def generatePartsIndex():
    print("Generating Parts Index")  
    filename = OOMP.getDir("parts") + "/README.md"
    
    rFile = osb.newReadme(filename)
    osb.addHeader(rFile, title="Parts", level=1)
    
    types = OOMP.tagDetails["type"]
    sizes = OOMP.tagDetails["size"]
    
    for type in types:
        for size in sizes:
            indexes = [""]
            if(type == "HEAD" and size == "I01"):
                indexes = ["01","RS","SHRO","SM"]
            if(type == "HEAD" and size == "JSTSH"):
                indexes = ["RS","SM"]
            for index in indexes:
                if index == "":
                    oompStart = type + "-" + size + "-"
                    oompEnd = ""
                    title = type + ">" + size + "  (" + OOMP.tagDetails["type"][type]["name"] + ">" +  OOMP.tagDetails["size"][size]["name"] + ")"
                else:
                    oompStart = type + "-" + size + "-"
                    oompEnd = "-" + index
                    title = type + ">" + size + ">" + index +  "  (" + OOMP.tagDetails["type"][type]["name"] + ">" +  OOMP.tagDetails["size"][size]["name"]  + ">" +  OOMP.tagDetails["index"][index]["name"] + ")"
                entries = []
                for partID in OOMP.itemsTypes["parts"]["items"]:
                    if partID.startswith(oompStart) and partID.endswith(oompEnd):
                        part = OOMP.items[partID]
                        link = OOMP.getFileItem(part,"",relative="github")
                        image = osb.getImageItem(part,"image",link=False)
                        text = OOMP.getNameDisplay(part,br="<br>")
                        entry = osb.getLink(image + "<br>" + text,link)
                        entries.append(entry)
                if len(entries) > 0:
                    osb.addHeader(rFile, title=title, level=2)
                    osb.addDisplayTable(rFile,entries,5)       

    osb.addToc(rFile)
    osb.saveReadme(rFile)
