import OOMP
import OOMP_projects_BASE

def createProjects():
    projects = []
    
    count = 1
    base = {}
    base["oompSize"] = "SOPA"
    base["format"] = "kicad"
    base["github"] = "https://github.com/solderparty/"
    base["oompIndex"] = "01"    ###### default to rev 01

    #############################################################
    #############################################################    

    projectStrings = []
    projectStrings.append("rp2040_stamp_hw")
    projectStrings.append(["bbq20kbd_hw","bbq20_keyboard"])
    projectStrings.append("rp2040_stamp_carrier_hw")
    projectStrings.append("keyboard_featherwing_hw")
    projectStrings.append("type-c_plug_cp2102")
    projectStrings.append("type-c_plug_lipo")
    projectStrings.append("rp2040_stamp_photolight_hw")
    projectStrings.append("rp2040_stamp_macropad_hw")
    projectStrings.append("rp2040_stamp_console_hw")
    projectStrings.append(["rp2040_stamp_round_carrier_hw","rp2040_stamp_round"])
    projectStrings.append(["pmod_to_qwiic_adapter","pmod_to_qwiic"])
    projectStrings.append("rp2040_stamp_jig_hw")



    #############################################################
    for item in projectStrings:
        if isinstance(item, list):
            repo = item[0]
            file = item[1]
        else:
            repo = item
            file = item

        d = base.copy()    
        d["repo"] = repo
        d["file"] = file.replace("_hw","")    
        d["name"] = file.replace("_hw","").replace("_"," ").capitalize
        d["count"] = count; count = count + 1
        projects.append(d)

    for d in projects:
        OOMP_projects_BASE.makeProjectNew(d)

    """
    #### Massaging of details
    if True:
        ind = ind + 1
        d["name"] = name + rev
        d["oompColor"] = str(ind).zfill(4)
        d["oompIndex"] = rev.zfill(2)
        d["hexID"] = "PR" + d["oompSize"][0:2] + str(ind)    
        if style == "eagle":
            d["eagleBoard"] = filename + ".brd"
            d["eagleSchem"] = d["eagleBoard"].replace(".brd",".sch")
        if style == "kicad":
            d["kicadBoard"] = filename + ".kicad_pcb"
            d["kicadSchem"] = d["kicadBoard"].replace(".kicad_pcb",".kicad_sch")
            
    OOMP_projects_BASE.makeProject(d)
    
    #############################################################
    #############################################################
    rev = "1"
    style = "kicad"
    #style = "eagle"
    name = "BBQ20KBD"
    filename = "bbq20_keyboard"
    d["gitRepo"] = "https://github.com/solderparty/bbq20kbd_hw"
      
    #### Massaging of details
    if True:
        ind = ind + 1
        d["name"] = name + rev
        d["oompColor"] = str(ind).zfill(4)
        d["oompIndex"] = rev.zfill(2)
        d["hexID"] = "PR" + d["oompSize"][0:2] + str(ind)    
        if style == "eagle":
            d["eagleBoard"] = filename + ".brd"
            d["eagleSchem"] = d["eagleBoard"].replace(".brd",".sch")
        if style == "kicad":
            d["kicadBoard"] = filename + ".kicad_pcb"
            d["kicadSchem"] = d["kicadBoard"].replace(".kicad_pcb",".kicad_sch")
            
    OOMP_projects_BASE.makeProject(d)

    #############################################################
    #############################################################
    rev = "1"
    style = "kicad"
    #style = "eagle"
    name = "The RP2040 Stamp Carrier"
    filename = "rp2040_stamp_carrier"
    d["gitRepo"] = "https://github.com/solderparty/rp2040_stamp_carrier_hw"
      
    #### Massaging of details
    if True:
        ind = ind + 1
        d["name"] = name + rev
        d["oompColor"] = str(ind).zfill(4)
        d["oompIndex"] = rev.zfill(2)
        d["hexID"] = "PR" + d["oompSize"][0:2] + str(ind)    
        if style == "eagle":
            d["eagleBoard"] = filename + ".brd"
            d["eagleSchem"] = d["eagleBoard"].replace(".brd",".sch")
        if style == "kicad":
            d["kicadBoard"] = filename + ".kicad_pcb"
            d["kicadSchem"] = d["kicadBoard"].replace(".kicad_pcb",".kicad_sch")
            
    OOMP_projects_BASE.makeProject(d)


    #############################################################
    #############################################################
    rev = "1"
    style = "kicad"
    #style = "eagle"
    name = "Raspberry Pi Zero Adapter for the Keyboard FeatherWing"
    filename = "kfw_rpi_adapter"
    d["gitRepo"] = "https://github.com/solderparty/keyboard_featherwing_zero_adapter"
      
    #### Massaging of details
    if True:
        ind = ind + 1
        d["name"] = name + rev
        d["oompColor"] = str(ind).zfill(4)
        d["oompIndex"] = rev.zfill(2)
        d["hexID"] = "PR" + d["oompSize"][0:2] + str(ind)    
        if style == "eagle":
            d["eagleBoard"] = filename + ".brd"
            d["eagleSchem"] = d["eagleBoard"].replace(".brd",".sch")
        if style == "kicad":
            d["kicadBoard"] = filename + ".kicad_pcb"
            d["kicadSchem"] = d["kicadBoard"].replace(".kicad_pcb",".kicad_sch")
            
    OOMP_projects_BASE.makeProject(d)
    """
