import OOMP
import OOMP_projects_BASE

def createProjects():
    d = {}
    d["oompType"] = "PROJ"
    d["oompSize"] = "ELLA"
    d["oompColor"] = "0001"
    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01"
    
    d["hexID"] = "PRE1"

    d["name"] = "Zig A Zig Ah"
    d["gitRepo"] = "https://github.com/electrolama/zig-a-zig-ah"
    d["eagleBoard"] = "zzh/Revision A/zzh.brd"
    d["eagleSchem"] = "zzh/Revision A/zzh.sch"

    OOMP_projects_BASE.makeProject(d)

    ind = 2
    rev = "A"
    d["oompColor"] = str(ind).zfill(4)
    d["oompIndex"] = rev.zfill(2)
    d["hexID"] = "PRE" + str(ind)
    d["name"] = "Zoe Rev " + rev
    d["gitRepo"] = "https://github.com/electrolama/zoe"
    d["eagleBoard"] = "/Revision " + rev +"/pi-zigbee-poe-rtc.brd"
    d["eagleSchem"] = d["eagleBoard"].replace(".brd",".sch")
    OOMP_projects_BASE.makeProject(d)

    ind = ind
    rev = "B"
    d["oompColor"] = str(ind).zfill(4)
    d["oompIndex"] = rev.zfill(2)
    d["hexID"] = "PRE" + str(ind)
    d["name"] = "Zoe Rev " + rev
    d["gitRepo"] = "https://github.com/electrolama/zoe"
    d["eagleBoard"] = "/Revision " + rev +"/pi-zigbee-poe-rtc.brd"
    d["eagleSchem"] = d["eagleBoard"].replace(".brd",".sch")
    OOMP_projects_BASE.makeProject(d)

    ind = ind
    rev = "C"
    d["oompColor"] = str(ind).zfill(4)
    d["oompIndex"] = rev.zfill(2)
    d["hexID"] = "PRE" + str(ind)
    d["name"] = "Zoe Rev " + rev
    d["gitRepo"] = "https://github.com/electrolama/zoe"
    d["eagleBoard"] = "/Revision " + rev +"/pi-zigbee-poe-rtc.brd"
    d["eagleSchem"] = d["eagleBoard"].replace(".brd",".sch")
    OOMP_projects_BASE.makeProject(d)

    d["oompIndex"] = "01"

    ###### New Style
    projects = []

    count = ind
    base = {}
    base["oompType"] = "PROJ"
    base["oompSize"] = "ELLA"
    base["format"] = "eagle"
    base["github"] = "https://github.com/electrolama/"

    d = base.copy()
    d["name"] = "mcore h616 breakout"
    d["repo"] = "mcore-h616-breakout"
    d["file"] = "hardware/Revision A1/mcore-h616-breakout-RevA1"
    d["count"] = count = count + 1
    projects.append(d.copy())

    d = base.copy()
    d["name"] = "riscystick"
    d["repo"] = d["name"]
    d["file"] = "hardware/Revision A1/" + d["name"] + "-RevA1"
    d["count"] = count = count + 1
    projects.append(d.copy())


    d = base.copy()
    d["name"] = "minik"
    d["repo"] = d["name"]
    d["file"] = "hardware/Revision A2/" + d["name"] + "-RevA2"
    d["count"] = count = count + 1
    projects.append(d.copy())

    d = base.copy()
    d["name"] = "disaster01"
    d["repo"] = d["name"]
    d["file"] = d["name"]
    d["count"] = count = count + 1
    projects.append(d.copy())

    d = base.copy()
    d["name"] = "nandcat"
    d["repo"] = d["name"]
    d["file"] = "Revision A/nand-cat"
    d["count"] = count = count + 1
    projects.append(d.copy())

    d = base.copy()
    d["name"] = "pic16-usb-module"
    d["repo"] = d["name"]
    d["file"] = "pum"
    d["count"] = count = count + 1
    projects.append(d.copy())

    for d in projects:
        OOMP_projects_BASE.makeProjectNew(d)

"""
    d = base.copy()
    d["name"] = "minik"
    d["repo"] = d["name"] + "/"
    d["file"] = "hardware/Revision A1/" + d["name"] + "-RevA1"
    d["count"] = count = count + 1
    projects.append(d.copy())
"""
    
    