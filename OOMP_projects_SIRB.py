import OOMP
import OOMP_projects_BASE

def createProjects():
    projects = []

    count = 1
    base = {}
    base["oompType"] = "PROJ"
    base["oompSize"] = "SIRB"
    base["format"] = "kicad"
    
    base["github"] = "https://github.com/sirboard/"

    d = breakoutDict(base.copy(),"CR1220",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"CR2031",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"ESP-12F",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"MicroSD",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"MicroSD_DualVoltage",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"MicroUSB",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"MiniUSB",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"QFN16",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"QFN20",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"SOIC16",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"SOIC20",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"SOIC24",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"SOIC28",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"SOT6",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"TQFP32",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"TQFP44",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"TQFP48",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"TQFP64",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"USB_C",count);projects.append(d.copy());count = count + 1
    d = breakoutDict(base.copy(),"WROOM02",count);projects.append(d.copy());count = count + 1
    
    ###### Sir Tiny's
    d = sirTinyDict(base.copy(),"ATTiny85",count);projects.append(d.copy());count = count + 1
    d = sirTinyDict(base.copy(),"ATTinyX12",count);projects.append(d.copy());count = count + 1
    d = sirTinyDict(base.copy(),"ATTinyX14",count);projects.append(d.copy());count = count + 1
    d = sirTinyDict(base.copy(),"ATTinyX16",count);projects.append(d.copy());count = count + 1
    d = sirTinyDict(base.copy(),"ATTinyX17",count);projects.append(d.copy());count = count + 1

    ######  Sir Nano
    d = nanoDict(base.copy(),"SirNanoV2",count,version="02");projects.append(d.copy())
    d = nanoDict(base.copy(),"SirNanoV3",count,version="03");projects.append(d.copy());count = count + 1    

    ######  Sir USB
    d = sirUsbDict(base.copy(),"CH330N",count);projects.append(d.copy());count = count + 1
    d = sirUsbDict(base.copy(),"CH340E",count);projects.append(d.copy());count = count + 1
    d = sirUsbDict(base.copy(),"CH340G",count);projects.append(d.copy());count = count + 1
    d = sirUsbDict(base.copy(),"CP2102N_20",count);projects.append(d.copy());count = count + 1
    d = sirUsbDict(base.copy(),"FT230V2",count,version="02");projects.append(d.copy());count = count + 1
    d = sirUsbDict(base.copy(),"FT231V2",count,version="02");projects.append(d.copy());count = count + 1
    



    for d in projects:
        OOMP_projects_BASE.makeProjectNew(d)

    count = count +1

def breakoutDict(d,bName,count):
    #### Manual
    d["name"] = bName + " Breakout Board (sirboard)"
    d["repo"] = "BreakoutBoards"
    d["file"] = bName + "/" + bName
    #### Auto
    d["count"] = count
    return d

def nanoDict(d,bName,count,version="01"):
    #### Manual
    d["name"] = bName + " SirNano"
    d["repo"] = "SirNano"
    d["file"] = bName + "/" + bName
    d["oompIndex"] = version
    #### Auto
    d["count"] = count

    return d

    
def sirTinyDict(d,bName,count):
    #### Manual
    d["name"] = bName + " SirTiny"
    d["repo"] = "SirTiny"
    d["file"] = bName + "/" + bName
    #### Auto
    d["count"] = count
    return d

def sirUsbDict(d,bName,count,version="01"):
    #### Manual
    d["name"] = bName + " SirUSB"
    d["repo"] = "SirUSB"
    d["file"] = bName + "/" + bName
    d["oompIndex"] = version
    #### Auto
    d["count"] = count

    return d
