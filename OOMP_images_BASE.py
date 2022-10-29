import os
import PIL
from PIL import Image
PIL.Image.MAX_IMAGE_PIXELS = 933120000    
import glob      
from oomBase import *                

def generateAllResolutions(overwrite=False):
    skips = ["_140","_450","_600","sourceFiles"]  
    types = [".jpg", ".png"]
    files = []
    for type in types:
        print("    Getting all " + type + "files.")
        files.extend(glob.glob("**/*" + type,recursive=True))
    for file in files:
        process = True
        for r in skips:
            if r in file:
                process = False
        if process:
            generateResolutions(file,overwrite)      

def generateResolutions(inFile,overwrite=False):
    res = [140,450,600]        
    ping()
    for r in res:    
        basewidth=r            
        outFile = inFile.replace(".png","_" + str(r) + ".png").replace(".jpg","_" + str(r) + ".jpg")
        if not os.path.isfile(outFile) or overwrite:     
            print("        Generating: " + outFile)
            img = Image.open(inFile)
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            img.save(outFile)
        

