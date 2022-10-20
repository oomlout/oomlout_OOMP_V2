import OOMP
import os
import json

def generateJson(item,overwrite):
    print("        JSON for: " + item.getTag("oompID").value)
    oompID = item.getTag("oompID").value
    name = item.getTag("name").value
    index = item.getTag("index").value

    item.addTag("oompID", oompID)
    item.addTag("name", name)
    removes = ["index","oompIDslashes"]
    for remove in removes:
        item.removeTag(remove) 
    jsonFile = item.getFolder() + "json.json"
    if not "TEMPLATE" in oompID and (not os.path.isfile(jsonFile) or overwrite):
        jsonText = json.dumps(item,default=lambda o: o.__dict__, sort_keys=True, indent=4)
        f = open(jsonFile,"w")
        f.write(jsonText)
        f.close()

    item.addTag("index", index)
    item.removeTag("oompID")    
    item.removeTag("name")    