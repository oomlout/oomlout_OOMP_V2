import os
import PIL
from PIL import Image
PIL.Image.MAX_IMAGE_PIXELS = 933120000
                             

def generateResolutions(item,overwrite=False):
    oompID = item.getTag("oompID").value
    print("Resolution Check for: " + oompID)
    #if("FOOTPRINT" in oompID):
    if True:
        
        res = [140,450,600]        
        images = item.getFilename("allImagesNames")
        for image in images:
            if "pcbdraw" in image:
                pass
            if item.ifFileExists(image) or item.ifFileExists(image, extension = "png"):
                inFile=item.getFilename(image)
                extension = ""
                if not "jpg" in inFile and not "png" in inFile:
                    extension = "png"
                    inFile=item.getFilename(image, extension="png")                                        
                for r in res:    
                    basewidth=r            
                    outFile = item.getFilename(image, resolution = r, extension=extension)                    
                    if not os.path.isfile(outFile) or overwrite: 
                        try:                     
                            print("        Generating: " + outFile)
                            img = Image.open(inFile)
                            wpercent = (basewidth / float(img.size[0]))
                            hsize = int((float(img.size[1]) * float(wpercent)))
                            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
                            img.save(outFile)
                        except:
                            print("Missing File: " + inFile)
        

