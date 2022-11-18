import OOMP
from oomBase import *


#OOMP.makePickle()
OOMP.loadPickle()


def delFiles(item,list):
    for file in list:
        filename = OOMP.getFileItem(item,file)
        oomDeleteFile(filename)
        if ".svg" in filename:
            resolutions = ["140","450","600"]            
            extensions = ["png","pdf","svg"]
            for extension in extensions:
                filename = OOMP.getFileItem(item,file,extension=extension)
                oomDeleteFile(filename)
                if extension == "png":
                    for res in resolutions:
                        filename = OOMP.getFileItem(item,file,extension=extension,resolution=res)
                        oomDeleteFile(filename)
                

                
fileList = []
fileList = ["kicadBoardSvg"]

itemID = "FOOTPRINT-kicad-oomlout_OOMP_kicad-oomlout_OOMP_JLCC_Basic-CAPC-0402-X-NF2-V50-C4N2-C1532"
itemID = "FOOTPRINT-kicad-kicad-footprints-Connector_PinHeader_2.54mm-PinHeader_2x03_P2.54mm_Vertical_SMD"

item = OOMP.items[itemID]
itemDir = OOMP.getFileItem(item,"",relative="full").replace("/","\\")
print(itemDir)
delFiles(item,fileList)
        