
def load(fn):

    ###### BASE
    cType = "BASE"
    current = "details"
    fn[current] = {}
    fn[current]["filename"] = "details.py"
    fn[current]["type"] = cType
    fn[current]["generated"] = True
    current = "detailspartsRaw"
    fn[current] = {}
    fn[current]["filename"] = "detailspartsRaw.py"
    fn[current]["type"] = cType
    fn[current]["generated"] = True
    current = "detailsPartsOomp"
    fn[current] = {}
    fn[current]["filename"] = "detailsPartsOomp.py"
    fn[current]["type"] = cType
    fn[current]["generated"] = True
    current = "detailsInstancesOomp"
    fn[current] = {}
    fn[current]["filename"] = "detailsInstancesOomp.py"
    fn[current]["type"] = cType
    fn[current]["generated"] = True
    current = "detailsFootprintsOomp"
    fn[current] = {}
    fn[current]["filename"] = "detailsFootprintsOomp.py"
    fn[current]["type"] = cType
    fn[current]["generated"] = True
    current = "detailspartNumbers"
    fn[current] = {}
    fn[current]["filename"] = "detailsPartNumbers.py"
    fn[current]["type"] = cType
    fn[current]["generated"] = True



    
    current = ""
    fn[current] = {}
    fn[current]["filename"] = ""
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    current = "readme"
    fn[current] = {}
    fn[current]["filename"] = "README.md"
    fn[current]["type"] = cType
    fn[current]["generated"] = True
    current = "mpnList"
    fn[current] = {}
    fn[current]["filename"] = "MPNLIST.md"
    fn[current]["type"] = cType
    fn[current]["generated"] = True
    current = "collection"
    fn[current] = {}
    fn[current]["filename"] = "COLLECTION.md"
    fn[current]["type"] = cType
    fn[current]["generated"] = True
    
    current = "jsonBasic"
    fn[current] = {}
    fn[current]["filename"] = "basic.json"
    fn[current]["type"] = cType
    fn[current]["generated"] = True
    current = "jsonFull"
    fn[current] = {}
    fn[current]["filename"] = "full.json"
    fn[current]["type"] = cType
    fn[current]["generated"] = True
    current = "csv"
    fn[current] = {}
    fn[current]["filename"] = "details.csv"
    fn[current]["type"] = cType
    fn[current]["generated"] = True
    


    fn[cType] = []
    for file in fn:
        try:
            if fn[file]["type"] == cType:
                fn[cType].append(file)
        except:
            pass
    ###### images
    cType = "IMAGE"

    ######  Photographs
    current = "image"
    fn[current] = {}
    fn[current]["filename"] = "image&&res&&.&&ext&&"
    fn[current]["filenameV1"] = ["oomlout_OOMP_parts/&&oompID&&/image.jpg"]
    fn[current]["defaultExtension"] = "jpg"
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    current = "imagePng"
    fn[current] = {}
    fn[current]["filename"] = "image&&res&&.&&ext&&"
    
    fn[current]["defaultExtension"] = "png"
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    current = "imageBottom"
    fn[current] = {}
    fn[current]["filename"] = "image_BOTTOM&&res&&.&&ext&&"
    fn[current]["filenameV1"] = ["oomlout_OOMP_parts/&&oompID&&/image_BOTTOM.jpg"]
    fn[current]["defaultExtension"] = "jpg"
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    current = "imageRe"
    fn[current] = {}
    fn[current]["filename"] = "image_RE&&res&&.&&ext&&"
    fn[current]["filenameV1"] = ["oomlout_OOMP_parts/&&oompID&&/image_RE.jpg"]
    fn[current]["defaultExtension"] = "jpg"
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    
    ###### eagle images
    current = "eagleImage"
    fn[current] = {}
    fn[current]["filename"] = current + "&&res&&.png"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/" + current + ".png"]
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    current = "eagleSchemImage"
    fn[current] = {}
    fn[current]["filename"] = current + "&&res&&.png"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/" + current + ".png"]
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    
    ######  Kicad images
    current = "kicadPcb3dFront"
    fn[current] = {}
    fn[current]["filename"] = "kicadPcb3dFront&&res&&.png"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/" + current + ".png"]
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    current = "kicadPcb3dBack"
    fn[current] = {}
    fn[current]["filename"] = "kicadPcb3dBack&&res&&.png"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/" + current + ".png"]
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    current = "kicadPcb3d"    
    fn[current] = {}
    fn[current]["filename"] = "kicadPcb3d&&res&&.png"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/" + current + ".png"]
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    current = "bomBack"    
    fn[current] = {}
    fn[current]["filename"] = current + "&&res&&.png"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/" + current + ".png"]
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    current = "bomFront"    
    fn[current] = {}
    fn[current]["filename"] = current + "&&res&&.png"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/" + current + ".png"]
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    current = "pcbdraw"    
    fn[current] = {}
    fn[current]["filename"] = current + "&&res&&.&&ext&&"
    fn[current]["defaultExtension"] = "svg"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/" + current + ".svg"]
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    current = "pcbdrawBack"    
    fn[current] = {}
    fn[current]["filename"] = current + "&&res&&.&&ext&&"
    fn[current]["defaultExtension"] = "svg"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/" + current + ".svg"]
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    current = "pcbdrawFront"    
    fn[current] = {}
    fn[current]["filename"] = current + "&&res&&.&&ext&&"
    fn[current]["defaultExtension"] = "svg"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/" + current + ".svg"]
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    current = "qrCode"    
    fn[current] = {}
    fn[current]["filename"] = current + "&&res&&.&&ext&&"
    fn[current]["defaultExtension"] = "png"
    fn[current]["type"] = cType
    fn[current]["generated"] = False
    
    fn[cType] = []
    for file in fn:
        try:
            if fn[file]["type"] == cType:
                fn[cType].append(file)
        except:
            pass
    ###### EDA
    cType = "EDA"
    current = "eagleBoard"
    fn[current] = {}
    fn[current]["filename"] = "src/eagleBoard.&&ext&&"
    fn[current]["defaultExtension"] = "brd"
    fn[current]["generated"] = False
    current = "eagleSchem"
    fn[current] = {}
    fn[current]["filename"] = "src/eagleSchem.&&ext&&"
    fn[current]["defaultExtension"] = "sch"
    fn[current]["generated"] = False
    current = "kicadBoard"
    fn[current] = {}
    fn[current]["filename"] = "src/kicadBoard.&&ext&&"
    fn[current]["defaultExtension"] = "kicad_pcb"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/kicad/" + "boardKicad" + ".kicad_pcb"]
    fn[current]["generated"] = False
    current = "kicadSchem"
    fn[current] = {}
    fn[current]["filename"] = "src/kicadSchem.&&ext&&"
    fn[current]["defaultExtension"] = "kicad_sch"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/kicad/" + "schematicKicad" + ".kicad_sch"]
    fn[current]["generated"] = False
    current = "kicadFootprint"
    fn[current] = {}
    fn[current]["filename"] = "footprint.&&ext&&"
    fn[current]["defaultExtension"] = "kicad_mod"
    fn[current]["generated"] = False
    

    ###### generated eagle files
    current = "eagleBOM"
    fn[current] = {}
    fn[current]["filename"] = "src/" + current + ".&&ext&&"
    fn[current]["defaultExtension"] = "csv"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/" + current + ".csv"]
    fn[current]["generated"] = False
    current = "eagleParts"
    fn[current] = {}
    fn[current]["filename"] = "src/" + current + ".&&ext&&"
    fn[current]["defaultExtension"] = "txt"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/" + current + ".txt"]
    fn[current]["generated"] = False
    current = "eaglePinlist"
    fn[current] = {}
    fn[current]["filename"] = "src/" + current + ".&&ext&&"
    fn[current]["defaultExtension"] = "txt"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/" + current + ".txt"]
    fn[current]["generated"] = False

    ###### generated kicad files
    current = "ibom"
    fn[current] = {}
    fn[current]["filename"] = "/" + current + ".&&ext&&"
    fn[current]["defaultExtension"] = "html"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/kicad/bom/" + current + ".html"]
    fn[current]["generated"] = False
    current = "kicadBOM"
    fn[current] = {}
    fn[current]["filename"] = "src/" + "kicadBoardBom" + ".&&ext&&"
    fn[current]["defaultExtension"] = "csv"
    fn[current]["filenameV1"] = ["oomlout_OOMP_projects/&&oompID&&/kicad/kicadBoardBom.csv"]
    fn[current]["generated"] = False
    
    ###### labels
    current = "labelInventory"
    fn[current] = {}
    fn[current]["filename"] = "/" + current + ".&&ext&&"
    fn[current]["defaultExtension"] = "pdf"
    fn[current]["generated"] = True
    

    fn[cType] = []
    for file in fn:
        try:
            if fn[file]["type"] == cType:
                fn[cType].append(file)
        except:
            pass
