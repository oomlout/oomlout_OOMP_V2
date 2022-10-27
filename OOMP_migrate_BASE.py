import OOMP

from oomBase import *




def migrateFiles(item):
    ping()
    
    oompID = item["oompType"][0] + "-" + item["oompSize"][0] + "-" + item["oompColor"][0] + "-" + item["oompDesc"][0] + "-" + item["oompIndex"][0]
    ###### for projects
    #oompID = item["oompType"][0] + "-" + item["oompSize"][0] + "-" + str(int(item["oompColor"][0])) + "-" + item["oompDesc"][0] + "-" + item["oompIndex"][0]
    oompSlashes = item["oompType"][0] + "/" + item["oompSize"][0] + "/" + item["oompColor"][0] + "/" + item["oompDesc"][0] + "/" + item["oompIndex"][0]

    v1Base = "C:/GH/oomlout_OOMP/"

    for file in OOMP.filenames:
        if file == "kicadBoard":
            print(oompID)
            pass
        try:
            v1Files = OOMP.filenames[file]["filenameV1"]
        except KeyError:
            v1Files = ""
        except TypeError:
            v1Files = ""     
        if v1Files != "":
            for v1File in v1Files:
                v1FileDash = v1Base + v1File.replace("&&oompID&&",oompID)
                v1FileSlash = v1Base + v1File.replace("&&oompID&&",oompSlashes)
                v2File = OOMP.getFileItem(item,file)
                if os.path.exists(v1FileDash) and not os.path.exists(v2File):
                    
                    oomCopyFile(v1FileDash,v2File)
                    print("    Moving File: " + v2File)
                if os.path.exists(v1FileSlash) and not os.path.exists(v2File):
                    oomCopyFile(v1FileSlash,v2File)
                    print("    Moving File: " + v2File)



    pass
