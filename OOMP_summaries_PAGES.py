import OOMP
import OOMP_summaries_BASE as osb
from oomBase import *

######  Pages

def generateReadmeFootprint(item, mdFile):
    pass

def generateReadmeCollection(item, mdFile):
    addCollectionList(item,mdFile)

def generateReadmePart(item, mdFile):
    addFootprintList(item,mdFile)
    addSymbolList(item,mdFile)
    addOOMPInstancesList(item,mdFile)
    addDPNSearch(item,mdFile)
    addDPNList(item,mdFile)
    addMPNList(item,mdFile)
    pass


def generateReadmeProject(item, mdFile):
    addIbom(item,mdFile)
    addOOMPPartsList(item,mdFile)
        
        
######  Helpers

###### COLLECTIONS
def addCollectionList(collection,mdFile):    
    oompID = collection["oompID"][0]  
    
    name = collection["name"][0]
    description = collection["description"][0]
    rFile = mdFile
    
    print("    Generating collection page for: " + oompID) 

    osb.addHeader(rFile,title="Items in Collection",level=2)
    osb.addLine(rFile,description)
    
    items = []
    for itemID in collection["collection"][0]["items"]:
        item = OOMP.items[itemID]
        string = osb.getPictureLink(item,resolution="140",link="")
        items.append(string)
    osb.addDisplayTable(rFile,items,3)
    

###### PARTS
def addFootprintList(item,mdFile):
    
    tags = ["Image","ID","Name"]
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
            
            designators = ""        
            id = thing
            try:
                name = OOMP.items[thing]["name"][0]
                tags.append(osb.getLink(image,link))
                tags.append(osb.getLink(id,link))
                tags.append(osb.getLink(name,link))
            except KeyError:
                tags.append("")
                tags.append(thing)
                tags.append("")
        if len(tags) > 3:
            osb.addHeader(mdFile, level=2, title='Footprints')
            osb.addDisplayTable(mdFile,tags,3,align="left")
    except IndexError:
        print("       Skipping because it's a block")

def addDPNSearch(item,mdFile): 
    osb.addHeader(mdFile, level=2, title='Distributor Searches')
    osb.addLine(mdFile, "Links to search for this item (using OOMP name) at various distributors")          
    ###### search links
    linkText = ""
    mpn = item["name"][0].replace(" ","+").replace("(","").replace(")","")
    ###### Aliexpress
    linkStart = "https://www.aliexpress.com/wholesale?SearchText=1117"
    link = linkStart + mpn
    text = "(Aliexpress) "
    linkText = linkText + osb.getLink(text,link) + "&nbsp;&nbsp;&nbsp;"
    ###### AVNET
    linkStart = "https://www.avnet.com/shop/us/search/"
    link = linkStart + mpn
    text = "(Avnet) "
    linkText = linkText + osb.getLink(text,link) + "&nbsp;&nbsp;&nbsp;"
    ###### Digikey
    linkStart = "https://www.digikey.co.uk/en/products/result?s="
    link = linkStart + mpn
    text = "(Digikey) "
    linkText = linkText + osb.getLink(text,link) + "&nbsp;&nbsp;&nbsp;"
    ###### LCSC
    linkStart = "https://www.lcsc.com/search?q="
    link = linkStart + mpn
    text = "(LCSC) "
    linkText = linkText + osb.getLink(text,link) + "&nbsp;&nbsp;&nbsp;"
    ###### Farnell
    linkStart = "https://uk.farnell.com/search?st="
    link = linkStart + mpn
    text = "(Farnell) "
    linkText = linkText + osb.getLink(text,link) + "&nbsp;&nbsp;&nbsp;"
    ###### Mouser
    linkStart = "https://www.mouser.com/c/?q="
    link = linkStart + mpn
    text = "(Mouser) "
    linkText = linkText + osb.getLink(text,link) + "&nbsp;&nbsp;&nbsp;"
    osb.addLine(mdFile, linkText)

def addDPNList(item,mdFile): 
    thingName = "distributorPartNumber"
    things = OOMP.getTag(item,thingName)
    if len(things) > 0:       
        tags = ["Distributor","DPN"]
        for thing in things:
            try:
                link = thing["LINK"]
            except:
                link = thing["partLink"]
            try:
                distributor = thing["DISTRIBUTOR"]
            except:
                distributor = "LCSC"
            try:
                dpn = thing["DPN"]
            except:
                dpn = thing["partID"]
            tags.append(osb.getLink(distributor,link))
            tags.append(osb.getLink(dpn,link))
        if len(tags) > 2:            
            osb.addHeader(mdFile, level=2, title='Distributor Part Numbers')          
            osb.addDisplayTable(mdFile,tags,2,align="left")

    
def addMPNList(item,mdFile):     
    ###### make extra file
    oompID = item["oompID"][0]
    ping(1000)
    filename = OOMP.getFileItem(item,"mpnList")
    thingName = "manufacturerPartNumber"
    things = OOMP.getTag(item,thingName)
    if len(things) > 0:       
        rFile = osb.newReadme(filename)
        hexID = item["hexID"][0]
        try:
            name = item["name"][0]
        except:
            name = ""
        osb.addHeader(rFile,level=1,title="MPN Summary For: " + hexID + " > " + name)
        tags = ["MPN","Direct Links","Search Links"]
        
        for thing in things:
            try:
                mpn = thing["MPN"]
                text = thing["MANUFACTURER"] + "<br>" + mpn
                tags.append(text)
                ###### direct links
                linkText = ""
                tags.append(linkText)
                ###### search links
                linkText = ""
                ###### AVNET
                linkStart = "https://www.avnet.com/shop/us/search/"
                link = linkStart + mpn
                text = "(AV) "
                linkText = linkText + osb.getLink(text,link)
                ###### Digikey
                linkStart = "https://www.digikey.co.uk/en/products/result?s="
                link = linkStart + mpn
                text = "(DK) "
                linkText = linkText + osb.getLink(text,link)
                ###### LCSC
                linkStart = "https://www.lcsc.com/search?q="
                link = linkStart + mpn
                text = "(LCSC) "
                linkText = linkText + osb.getLink(text,link)
                ###### Farnell
                linkStart = "https://uk.farnell.com/search?st="
                link = linkStart + mpn
                text = "(FA) "
                linkText = linkText + osb.getLink(text,link)
                ###### Mouser
                linkStart = "https://www.mouser.com/c/?q="
                link = linkStart + mpn
                text = "(MS) "
                linkText = linkText + osb.getLink(text,link)
                tags.append(linkText)     
            except:
                pass              
        if len(tags) > 3:            
            osb.addHeader(rFile, level=2, title='MPNs')          
            osb.addDisplayTable(rFile,tags,3,align="left")
    
        osb.saveReadme(rFile)
    ###### make display table     
    try:
        thingName = "manufacturerPartNumber"
        things = item[thingName]
        ####### extra things to add
        count = len(things)
        
        includes = []
        if count < 20:
            tagReason = ""
            includes = things
        else:
            ###### including highest stock level
            tagReason  = ""
            stocks = ["1000K","100K","10K"]
            for stock in stocks:
                if len(includes) < 1:
                    for thing in things:
                        tags = thing["TAGS"]
                        if len(tags) == 0:
                            pass
                        else:
                            for tag in tags:
                                if tag  == "STOCK:" + stock:
                                    tagReason = tag
                                    includes.append(thing)
        tags = ["MPN","Direct Links","Search Links"]
        for thing in includes:
            try: 
                mpn = thing["MPN"]
                text = thing["MANUFACTURER"] + "<br>" + mpn
                tags.append(text)
                ###### direct links
                linkText = ""
                tags.append(linkText)
                ###### search links
                linkText = ""
                ###### AVNET
                linkStart = "https://www.avnet.com/shop/us/search/"
                link = linkStart + mpn
                text = "(AV) "
                linkText = linkText + osb.getLink(text,link)
                ###### Digikey
                linkStart = "https://www.digikey.co.uk/products/en?keywords="
                link = linkStart + mpn
                text = "(DK) "
                linkText = linkText + osb.getLink(text,link)
                ###### LCSC
                linkStart = "https://www.lcsc.com/search?q="
                link = linkStart + mpn
                text = "(LCSC) "
                linkText = linkText + osb.getLink(text,link)
                ###### Farnell
                linkStart = "https://uk.farnell.com/search?st="
                link = linkStart + mpn
                text = "(FA) "
                linkText = linkText + osb.getLink(text,link)
                ###### Mouser
                linkStart = "https://www.mouser.com/c/?q="
                link = linkStart + mpn
                text = "(MO) "
                linkText = linkText + osb.getLink(text,link)
                tags.append(linkText)                   
            except KeyError:
                pass ###### skip over if no MPN
        if len(tags) > 3:            
            osb.addHeader(mdFile, level=2, title='MPNs')
            link = OOMP.getFileItem(item,"mpnList",relative="flat")
            if tagReason != "":
                osb.addLine(mdFile,"Number of MPNs: " + str(count) + "<br>Below is a subset included because: " + tagReason + " <br>Full list: " + osb.getLink("Full MPN List",link))
            else:
                osb.addLine(mdFile,"Number of MPNs: " + str(count))
            osb.addDisplayTable(mdFile,tags,3,align="left")
    except IndexError:
        pass
        #print("       Skipping because it's a block")



def addOOMPInstancesList(item,mdFile):    
    tags = ["Project ID","Project Name","Parts"]
    try:
        thingName = "oompInstances"
        things = item[thingName]
        ####### extra things to add
        
        projects = []
        for thing in things:
            try:
                #unique values
                projectID = thing["PROJECT"]
                if projectID not in projects:
                    projects.append(projectID)
            except KeyError:
                pass
        for projectID in projects:
            ids = ""
            for thing in things:
                try:
                    testID = thing["PROJECT"]
                    if projectID == testID:
                        ids = ids + thing["ID"] + ", "
                except KeyError:
                    pass
            if ids != "":
                ids = ids[0:len(ids)-2]
            project = OOMP.items[projectID]
            link = OOMP.getFileItem(project,"",relative="github")
            id = projectID
            name = project["name"][0]
            ids = ids
            tags.append(osb.getLink(id,link))
            tags.append(osb.getLink(name,link))
            tags.append(osb.getLink(ids,link))
        if len(tags) > 3:
            osb.addHeader(mdFile,level=2, title='OOMP Instances')
            osb.addDisplayTable(mdFile,tags,3,align="left")
    except IndexError:
        pass
        #print("       Skipping because it's a block")

def addSymbolList(item,mdFile):
    
    tags = ["Image","ID","Name"]
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
            id= thing
            try:
                name = OOMP.items[thing]["name"][0]
            except KeyError:
                name = ""
            designators = ""            
            tags.append(osb.getLink(image,link))
            tags.append(osb.getLink(id,link))
            tags.append(osb.getLink(name,link))
        if len(tags) > 3:
            osb.addHeader(mdFile,level=2, title='Symbols')
            osb.addDisplayTable(mdFile,tags,3,align="left")
    except IndexError:
        print("       Skipping because it's a block")
###### PROJECTS

def addIbom(item,mdFile):
    ibomFile = OOMP.getFileItem(item,"ibom")
    if os.path.exists(ibomFile):
        mdFile.new_header(level=2, title='iBom')
        oompID = item["oompID"][0]
        osb.addLine(mdFile,osb.getLink("iBom.html","https://htmlpreview.github.io/?https://github.com/oomlout/oomlout_OOMP_projects_V2/blob/main/" + oompID.replace("-","/") + "/ibom.html"))


def addOOMPPartsList(item,mdFile):
    mdFile.new_header(level=2, title='OOMP Parts')
    tags = []
    tags.append("Image")    
    tags.append("OOMP ID")
    tags.append("Designators")
    try:
        oompParts = item["oompParts"][0]
        if len(oompParts) > 0:
            uniqueParts = []
            
            for part in oompParts:
                if oompParts[part]["OOMPID"] not in uniqueParts:
                    uniqueParts.append(oompParts[part]["OOMPID"])
            uniqueParts.sort()
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
                    if oompParts[testPart]["OOMPID"] == partID:
                        designators = designators + testPart + ","
                if designators != "":
                    designators = designators[0:-1]
                tags.append(osb.getLink(image,link))
                tags.append(osb.getLink(text,link))
                tags.append(osb.getLink(designators,link))
            osb.addDisplayTable(mdFile,tags,3,align="left")
    except IndexError:
        print("       Skipping because it's a block")