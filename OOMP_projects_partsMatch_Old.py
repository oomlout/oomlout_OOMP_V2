import OOMP
from OOMP_projects_partsMatch import *

def matchPartOld(project,part):

    PART = 0
    VALUE = 1
    PACKAGE = 2
    LIBRARY = 3

    oompType = "UNMATCHED"
    oompSize = "UNMATCHED"
    oompColor = "UNMATCHED"
    oompDesc = "UNMATCHED"
    oompIndex = "UNMATCHED"                

    oompColor = "X"
    oompIndex= "01"


    partLetter = "".join([i for i in part[PART] if not i.isdigit()])
    partNumber = "".join([i for i in part[PART] if not i.isalpha()])
    valueLetter = "".join([i for i in part[VALUE] if not i.isdigit()])
    valueNumber = "".join([i for i in part[VALUE] if not i.isalpha()])
    packageLetter = "".join([i for i in part[PACKAGE] if not i.isdigit()]).replace("-","")
    packageNumber = "".join([i for i in part[PACKAGE] if not i.isalpha()]).replace("-","")

    valueNumber = valueNumber.replace("+","")

    ###### TYPE

    if partLetter == "C":
        try:
            if float(valueNumber) < 20:
                oompType = "CAPC"
            else:
                oompType = "CAPE"    
        except:
            c=0

    if partLetter == "R":
        oompType = "RESE"

    ####### skip test

    skipList = [
        ["fid","SKIP"],
        ["mountinghole","SKIP"],
        ["fiducial","SKIP"],
        ["gator","SKIP"],
        ["wpj","SKIP"],
        ["test","SKIP"],
        ["solder","SKIP"],
        ["pad-jumper","SKIP"],
        ["sewtap","SKIP"],
        ["sewingtap","SKIP"],
        ["tp","SKIP"],
        ["sj","SKIP"]
    ]

    for skip in skipList:
        if skip[0] in part[PART].lower() :
            oompType = skip[1]
        if skip[0] in part[PACKAGE].lower() :
            oompType = skip[1]
    

    ######  SIZE

    sizeList = [
        ["0805","0805"],
        ["805","0805"], 
        ["0805-","0805"],
        ["_0805","0805"],
        ["0603","0603"],
        ["603","0603"], 
        ["0603-","0603"],
        ["_0603","0603"],
        ["0402","0402"],
        ["402","0402"], 
        ["0402-","0402"],
        ["_0402","0402"],
        ["1210","1210"]
    ]

    for swap in sizeList:
        if part[PACKAGE].lower() == swap[0]:
            oompSize = swap[1]
        if packageNumber.lower() == swap[0]:
            oompSize = swap[1]    

    ###### headerss

    headIncludeList =[["1x","HEAD" ]
    ]

    headExcludeList =["mm","jst", "fiducial", "mil", "screw"]


    package = part[PACKAGE].lower()
    value = part[VALUE].lower()
    name = part[PART].lower()


    if "jp" in name:
        for swap in headIncludeList:
            if swap[0] in package or swap[0] in name:
                include = True
                for skip in headExcludeList:
                    if skip in package or skip in name:
                        include =False
                    if include:
                        oompType = "HEAD"
                        oompSize = "I01"
                        packageSan = packageNumber.replace("_76","").replace("_70","").replace("-","").replace("_","")
                        oompDesc = "PI" + packageSan.zfill(2)[1:]


    ###### LEDs

    ledList =[["led","LEDS" ]
            ]
    if part[PART].lower() == "l":
        oompType = "LEDS"

    for swap in ledList:

        if part[PART].lower() == swap[0]:
            oompType = swap[1]
            if "2812" in part[PACKAGE] or "APA" in part[PACKAGE] or  "2811" in part[PACKAGE] or  "RGB" in part[PACKAGE]:
                oompColor = "RGB"
            elif "red" in part[VALUE].lower():
                oompColor = "R"
            elif "green" in part[VALUE].lower():
                oompColor = "G"
            elif "blue" in part[VALUE].lower():
                oompColor = "L"
            elif "white" in part[VALUE].lower():
                oompColor = "W"
            elif "yellow" in part[VALUE].lower():
                oompColor = "Y"
            else:
                oompColor = "G"
    ###### common capacitor values

    descList = [["0.01uf","NF10" ],
                ["2.2pf","PF22D" ],
                ["1000pf","NF1" ],
                ["2.2nf","NF22D" ],
                ["2200pf","NF22D" ],
                [".47uf","NF470" ],
                [".01uf","NF10" ],
                [".01uf","NF10" ],
                ["0.01uf","NF10" ],
                ["0.1uf","NF100" ],
                ["0.1u","NF100" ],
                ["0.22uf","NF220" ],
                [".22uf","NF220" ],
                ["0.33uf","NF330" ],
                [".33uf","NF330" ],
                ["0.39uf","NF390" ],
                [".39uf","NF390" ],
                ["0.47uf","NF470" ],
                [".47uf","NF470" ],
                ["0.5uf","NF500" ],
                [".5uf","NF500" ],
                ["0.68uf","NF680" ],
                [".68uf","NF680" ],
                ["0.75uf","NF750" ],
                [".75uf","NF750" ],
                ["0.8uf","NF800" ],
                [".8uf","NF800" ],
                ["2.2uf","UF22D" ],
                ["1000uf","UF1000"],
                ["100/6vuf","UF100"],
    ]

    values  = ["p","n","u"]
    steps = 999
    for value in values:
        for step in range(steps):
            descList.append([str(step) + value,value.upper() + "F" + str(step) ])
            descList.append([str(step) + "f" + value,value.upper() + "F" + str(step) ])
            descList.append([str(round(step,1)) + "f" + value,value.upper() + "F" + str(step) ])



    for swap in descList:
        if part[VALUE].replace("+","").replace("/10V","").replace("/16V","").replace("-25V","").replace("/50V","").replace("/2kV","").lower() == swap[0]:
            oompDesc = swap[1]


    oompID = oompType + "-" + oompSize + "-" + oompColor + "-" + oompDesc + "-" + oompIndex

    if oompType == "CAPC" and oompDesc == "NF100":
        oompIndex = "V50"
    ###### default to v50 for small 0603 value caps    
    if oompType == "CAPC" and oompSize == "0603" and ("NF" in oompDesc or "PF" in oompDesc)  :
        oompIndex = "V50"        
    if oompType == "CAPC" and oompDesc == "UF10":
        oompIndex = "V25"


    ###### common resistor values
    if oompType == "RESE":
        descList = [
            ["10K","O103"],
            ["1K","O102"],
            ["2K","O202"],
            ["3K","O302"],
            ["4K","O402"],
            ["5K","O502"],
            ["6K","O602"],
            ["7K","O702"],
            ["8K","O802"],            
            ["9K","O902"],
            ["100K","O104"],
            ["22K","O223"],
            ["2.2K","O222"],
            ["1M","O105"],
            ["2M","O205"],
            ["3M","O305"],
            ["4M","O405"],
            ["5M","O505"],
            ["6M","O605"],
            ["7M","O705"],
            ["8M","O805"],
            ["9M","O905"],
            ["220","O221"],
            ["330","O331"]
        ]

        first = 99
        zeros=6
        for zero in range(3,zeros):
            for num in range(10,first):
                if zero < 2:
                    test = num * pow(10,zero)
                elif zero < 5:
                    test = str(round(num * pow(10,zero-3),1)) + "k"
                else:
                    test = str(round(num * pow(10,zero-6),1)) + "M"   
                result = "O" + str(num) + str(zero)
                descList.append([test , result])

        for swap in descList:
            if part[VALUE].replace("+","").replace("/10V","").replace("/16V","").replace("-25V","").replace("/50V","").replace("/2kV","").lower() == swap[0]:
                oompDesc = swap[1]
            if valueNumber == swap[0]:
                oompDesc = swap[1]

    rv = oompType + "-" + oompSize + "-" + oompColor + "-" + oompDesc + "-" + oompIndex
    return rv


def harvestPartsOld(item,overwrite = False):
    print("#############################################################")
    print("#############################################################")
    print("#############################################################")
    print("#############################################################")
    print("######  SHOULDN'T BE BEING USED ANYMORE  #######")
    print("######  harvestPartsOld(item,overwrite = False):  #######")
    eagleParts = item.getFilename("eagleParts")
    partsPython = item.getFilename("pythonParts")
    if overwrite or not os.path.exists(partsPython): 
        print("Harvesting Parts For: " + str(item))
        parts = oomReadFileToString(eagleParts)
        lines = parts.splitlines()    
        process = False
        parts = []
        oompParts = []
        multiplier = 1
        for line in lines:
            line = line.replace("µ","u").replace("�","").replace('"',"").replace("'","").replace("±","+/-").replace("�","")
            ######  skip"'" until getting to part line
            if process:
                if line != "":
                    parts.append(line.split())
            if "Part " in line:
                process = True  
                if "(inch)" in line:
                    multiplier = 25.4              
        for part in parts:
            ######missing value
            if len(part) == 6:
                part = [part[0],"",part[1],part[2],part[3],part[4],part[5]]
            if len(part) > 4:

                    ##### oompID, part, x, y, rotation
                oompID = matchPart(item,part)
                try:                    
                    partName = part[0]
                    x = part[4].replace("(","")
                    y = part[5].replace(")","")
                    rotation = part[6].replace("R","")

                    oompParts.append([oompID,partName,float(x)*multiplier,float(y)*multiplier,rotation])
                except:
                    print("harvest parts error " + str(part))
                    oompParts.append(["ERROR",part[0] + " " + part[1] + " " + part[2],0,0,0])


        if len(oompParts) > 0:
            makePartsFile(item,oompParts,parts)

        #oomDelay(30)        
