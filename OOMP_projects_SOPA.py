import OOMP
import OOMP_projects_BASE

def createProjects():
    ind = 0
    d = {}
    d["oompType"] = "PROJ"
    d["oompSize"] = "SOPA"
    d["oompDesc"] = "STAN"
        

    #############################################################
    #############################################################    
    rev = "1"
    style = "kicad"
    #style = "eagle"
    name = "RP2040 Stamp"
    filename = "rp2040_stamp"
    d["gitRepo"] = "https://github.com/solderparty/rp2040_stamp_hw"
      
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

