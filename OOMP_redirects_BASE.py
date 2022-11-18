import OOMP

from oomBase import *

def generateRedirect():
    redirectLimit = 10000
    print("Generating redirect file")
    fileNum = 1
    oomMakeDir("redirects/")
    filename = "redirects/redirects"
    f = open(filename + str(fileNum) + ".csv","w+")
    x = 0
    
    for item in OOMP.items:
        item = OOMP.items[item]
        oompID = item["oompID"][0]
        hexID = item["hexID"][0]
        longLink = OOMP.getFileItem(item,"",relative="github")
        try:
            if oompID != "":     
                f.write(longLink + "," + oompID.lower() + "\n")
            if hexID != "":            
                f.write(longLink + "," + hexID.lower() + "\n")
        except:
            print("ERROR" + str(item))
        x = x + 1
        if x % redirectLimit == 0:
            f.close()
            fileNum = fileNum + 1
            f = open(filename + str(fileNum) + ".csv","w+")
            print(".",end="")