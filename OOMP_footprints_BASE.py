import OOMP
from oomBase import *

import OOMP_symbols_BASE

import OOMP_footprints_KICAD
import OOMP_footprints_EAGLE

from kiutils.footprint import Footprint

footprintGits = {}
#####
git = 'digikey-kicad-library'

footprintGits[git] = {}
footprintGits[git]["code"] = git
footprintGits[git]["type"] = "kicad"
footprintGits[git]["url"] = 'https://github.com/Digi-Key/digikey-kicad-library'
footprintGits[git]["name"] = "Digikey's Footprints"
footprintGits[git]["description"] = "Digikey's kicad footprint library."
######
git = 'oomlout_OOMP_kicad'
footprintGits[git] = {}
footprintGits[git]["code"] = git
footprintGits[git]["type"] = "kicad"
footprintGits[git]["url"] = 'https://github.com/oomlout/oomlout_OOMP_kicad'
footprintGits[git]["name"] = "Oomlout's Footprints"
footprintGits[git]["description"] = "Oomlout's kicad footprint library."
######
git = 'kicad-footprints'
footprintGits[git] = {}
footprintGits[git]["code"] = git
footprintGits[git]["type"] = "kicad"
footprintGits[git]["url"] = 'https://gitlab.com/kicad/libraries/kicad-footprints'
footprintGits[git]["name"] = "Kicad Default Footprints"
footprintGits[git]["description"] = "Kicad's default footprint library."

############  Eagle Footprints
######
git = 'Adafruit-Eagle-Library'
footprintGits[git] = {}
footprintGits[git]["code"] = git
footprintGits[git]["type"] = "eagle"
footprintGits[git]["url"] = 'https://github.com/adafruit/Adafruit-Eagle-Library'
footprintGits[git]["name"] = "Adafruit's Eagle Footprints"
footprintGits[git]["description"] = "Adafruit's footprint library."

######
git = 'Adafruit-Eagle-Library'
footprintGits[git] = {}
footprintGits[git]["code"] = git
footprintGits[git]["type"] = "eagle"
footprintGits[git]["url"] = 'https://github.com/adafruit/Adafruit-Eagle-Library'
footprintGits[git]["name"] = "Adafruit's Eagle Footprints"
git = 'SparkFun-Eagle-Libraries'
footprintGits[git] = {}
footprintGits[git]["code"] = git
footprintGits[git]["type"] = "eagle"
footprintGits[git]["url"] = 'https://github.com/sparkfun/SparkFun-Eagle-Libraries'
footprintGits[git]["name"] = "SparkFun's Eagle Footprints"
footprintGits[git]["description"] = "SparkFun's footprint library."
git = 'eagle-default'
footprintGits[git] = {}
footprintGits[git]["code"] = git
footprintGits[git]["type"] = "eagle"
footprintGits[git]["url"] = ''
footprintGits[git]["name"] = "Eagle Default Footprints"
footprintGits[git]["description"] = "Eagle's default footprint library."

def gitPull():
    gits= []
    
    
    
    for git in footprintGits:        
        dir = "sourceFiles/git/" + footprintGits[git]["type"] + "Footprints/"
        oomMakeDir(dir)
        if footprintGits[git]["url"] != "":
            oomGitPullNew(footprintGits[git]["url"],dir)

import os

def harvest3DModel(item):
    footprintFile = OOMP.getFileItem(item,"kicadFootprint")
    if os.path.exist(footprintFile):
        pass
    
def createAllFootprints():
    initializeFootprintFile()
    OOMP_footprints_EAGLE.createFootprints()
    OOMP_footprints_KICAD.createFootprints()
    oomCloseFileUtf()

def harvestAllFootprints():
    OOMP_footprints_KICAD.harvestFootprints()    

def createFootprintLibraries():
    createFootprintLibrary()
    createFootprintLibrary(directory="oomlout_OOMP_kicad_V2/oomlout_OOMP_JLCC_Basic.pretty/",style="JLCC")

from kiutils.board import Board
from kiutils.footprint import Footprint
from kiutils.items.common import Position
from kiutils.items.fpitems import FpText

def createFootprintBoardFile(item):
    footprintFile = OOMP.getFileItem(item,"kicadFootprint")
    if os.path.isfile(footprintFile):
        try:
            outFile = OOMP.getFileItem(item,"kicadBoardFootprint")
            oomMakeDir(OOMP.getFileItem(item,"")+ "src/")
            oomMakeDir(OOMP.getFileItem(item,"")+ "src/sourceFiles/")
            templateFile = "templates/empty100.kicad_pcb"
            projectFile = "templates/empty100.kicad_pro"
            projectFileOut = OOMP.getFileItem(item,"")+ "src/sourceFiles/kicadBoard.kicad_pro"
            oomCopyFile(projectFile,projectFileOut)
            board = Board().from_file(templateFile)
        
        
            footprint = Footprint().from_file(footprintFile)
            footprint.position = Position(X=50, Y=50)
            
            # Change identifier to C105
            for itemA in footprint.graphicItems:
                if isinstance(itemA, FpText):
                    if itemA.type == 'reference':
                        itemA.text = item["hexID"][0]
            board.footprints.append(footprint)
        


    
            board.to_file(outFile)
        except UnicodeDecodeError:
            print("       Unicode Error: " + item["oompID"])

def createFootprintLibrary(directory="oomlout_OOMP_kicad_V2/oomlout_OOMP_parts.pretty/",style=""):
    outDir = directory
    print("    Creating foortprint library: " + outDir)
    oomMakeDir(outDir)
    for partID in OOMP.itemsTypes["parts"]["items"]:
        part = OOMP.items[partID]
        oompID = part["oompID"][0]
        hexID = part["hexID"][0]
        footprints = part["footprintKicad"]
        if len(footprints) > 0:
            #print("    Writing footprint:" + oompID)
            ping()
            try:
                footprint = OOMP.items[footprints[0]]
                footprintID = footprint
                include = False
                extra= ""
                if style == "":
                    include = True
                    extra = "-" + hexID
                elif style == "JLCC":
                        opl = part["oplPartNumber"]
                        for o in opl:
                            if o["code"] == "C-JLCC":
                                extra = "-" + hexID +"-" + o["partID"]
                                include = True 
                            
                            
                if footprintID != "----" and include:
                    footprintFile = OOMP.getFileItem(footprint,"kicadFootprint")
                    outFile = outDir + oompID + extra + ".kicad_mod"
                    footIn = Footprint().from_file(footprintFile)
                    ###### description not currently generated
                    footIn.description = OOMP_symbols_BASE.getDesc(part) + " " + footIn.description
                    footIn.libraryLink = oompID + extra
                    ###### change the name on the board
                    for item in footIn.graphicItems:
                        try:
                            if item.type == "reference":
                                item.text = hexID + "REF**"
                            if item.type == "value":
                                item.text = hexID
                        except:
                            pass
                    footIn.to_file(outFile)
                    pass
                else:
                    ping()
                    #print("        Skipping")
            except KeyError:
                pass
                #print("Footprint not found" + oompID)




def initializeFootprintFile():
    outputFile = OOMP.getDir("eda") + "details.py"
    oomOpenFileUtf(outputFile)

    contents = """
import OOMP

def load(newpart, it):
    pass
    
    
"""
    oomAddToOpenFileUtf(contents)

def makeFootprint(d):
    type = d["oompType"]
    size = d["oompSize"]
    color = d["oompColor"]
    desc = d["oompDesc"]   
    index = d["oompIndex"]

    d["name"] = desc + " : " + index

    hexID = d["hexID"]

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index

    #print("    Making Footprint")
    ping()

    oompSlashes = type + "/" + size + "/" + color + "/" + desc + "/" + index + "/"

    inputFile = "templates/edaTemplate.py"
    outputDir = OOMP.getDir("eda") + oompSlashes
    #outputFile = outputDir + "details.py"
    outputFile = OOMP.getDir("eda") + "details.py"

    #print("Making: " + outputFile) n

    contents = oomReadFileToString(inputFile)
    contents = contents.replace("TYPEZZ",type)
    contents = contents.replace("SIZEZZ",size)
    contents = contents.replace("COLORZZ",color)
    contents = contents.replace("DESCZZ",desc)
    contents = contents.replace("INDEXZZ",index)
    contents = contents.replace("HEXZZ",hexID)

    repoName = ""

    skipTags = ["oompType","oompSize","oompColor","oompDesc","oompIndex","FOOTPRINT","hexID"]

    extraTags = []
    for tag in d:
        if tag not in skipTags:
            if isinstance(d[tag],str):
                d[tag] = d[tag].replace("'","\\'")
            extraTags.append([tag,d[tag]])        
    tagString = ""
    for tag in extraTags:
        tagString = tagString + OOMP.getPythonLine(tagName=tag[0],tagValue=tag[1],indent="    ") + "\n"

    contents = contents.replace("EXTRAZZ",tagString)

    #oomWriteToFile(outputFile,contents)
    #oomAddLineToFileUtf(outputFile,contents)
    oomAddToOpenFileUtf(contents)
    pass

    

def gitFullPull():
    dir = "sourceFiles/git/kicadStuff/"
    oomMakeDir(dir)

    gits = []

    gits.append('git://smisioto.eu/kicad_libs.git')
    gits.append('https://github.com/1Bitsy/1bitsy-hardware-lib')
    gits.append('https://github.com/4ms/4ms-kicad-lib')
    gits.append('https://github.com/50an6xy06r6n/keyboard_reversible.pretty')
    gits.append('https://github.com/aaarsene/MX_19mm.pretty')
    gits.append('https://github.com/aaronw2/Torex_Semi.pretty')
    gits.append('https://github.com/AcheronProject/acheron_Components.pretty')
    gits.append('https://github.com/AcheronProject/acheron_Connectors.pretty')
    gits.append('https://github.com/AcheronProject/acheron_EC.pretty')
    gits.append('https://github.com/AcheronProject/acheron_Graphics.pretty')
    gits.append('https://github.com/AcheronProject/acheron_Hardware.pretty')
    gits.append('https://github.com/AcheronProject/acheron_Logos.pretty')
    gits.append('https://github.com/AcheronProject/acheron_MountingHoles.pretty')
    gits.append('https://github.com/AcheronProject/acheron_MX_PlateSlots.pretty')
    gits.append('https://github.com/AcheronProject/acheron_MX.pretty')
    gits.append('https://github.com/AcheronProject/acheron_MXH_metalrings.pretty')
    gits.append('https://github.com/AcheronProject/acheron_MXH.pretty')
    gits.append('https://github.com/AcheronProject/acheron_MXO.pretty')
    gits.append('https://github.com/adamgreig/agg-kicad')
    gits.append('https://github.com/adamjvr/ESP32-kiCAD-Footprints')
    gits.append('https://github.com/adamjvr/KiCAD-OnHand-Lib')
    gits.append('https://github.com/aesora/aesora.pretty.git')
    gits.append('https://github.com/aewallin/awallinKiCadFootprints.pretty.git')
    gits.append('https://github.com/ai03-2725/Molex-0548190589.pretty')
    gits.append('https://github.com/ai03-2725/MX_Alps_Hybrid.pretty')
    gits.append('https://github.com/ai03-2725/random-keyboard-parts.pretty')
    gits.append('https://github.com/ai03-2725/Type-C.pretty')
    gits.append('https://github.com/AkiyukiOkayasu/Kicad_Akiyuki_Footprint.pretty')
    gits.append('https://github.com/AlasEyrd/hitek725.pretty')
    gits.append('https://github.com/AlasEyrd/nec.pretty')
    gits.append('https://github.com/Alasofia/hitek725.pretty')
    gits.append('https://github.com/Alasofia/MXMountLP.pretty')
    gits.append('https://github.com/Alasofia/nec.pretty')
    gits.append('https://github.com/alchy/spacestudio_components.pretty.git')
    gits.append('https://github.com/alozewski/al-kicad-lib.pretty')
    gits.append('https://github.com/altLab/altlab-footprints.pretty.git')
    gits.append('https://github.com/ANDnXOR/ANDnXOR-Kicad.pretty.git')
    gits.append('https://github.com/andresmanelli/TOROID-KiCad.pretty.git')
    gits.append('https://github.com/angustrau/MHS_Robotics.pretty')
    gits.append('https://github.com/aniline/akn_misc.pretty.git')
    gits.append('https://github.com/aniline/akn_transformers.pretty.git')
    gits.append('https://github.com/antonchromjak/kicad_subory.pretty')
    gits.append('https://github.com/apexelectrix/apex-fuses.pretty.git')
    gits.append('https://github.com/apexelectrix/apex-pin-connectors.pretty.git')
    gits.append('https://github.com/apexelectrix/apex-pin-headers.pretty.git')
    gits.append('https://github.com/apexelectrix/apex-screw-terminals.pretty.git')
    gits.append('https://github.com/apexelectrix/apex-smd-capacitors.pretty.git')
    gits.append('https://github.com/apexelectrix/apex-smd-connectors.pretty.git')
    gits.append('https://github.com/apexelectrix/apex-smd-crystals.pretty.git')
    gits.append('https://github.com/apexelectrix/apex-smd-diode.pretty.git')
    gits.append('https://github.com/apexelectrix/apex-smd-resistors.pretty.git')
    gits.append('https://github.com/apexelectrix/apex-smd-wire-pads.pretty.git')
    gits.append('https://github.com/apexelectrix/apex-smd.pretty.git')
    gits.append('https://github.com/apexelectrix/Apex.pretty.git')
    gits.append('https://github.com/ariejan/ariejan.pretty.git')
    gits.append('https://github.com/ashtonchase/Battery_Holders.pretty')
    gits.append('https://github.com/ASoftTech/CAD.KiCad.Libs')
    gits.append('https://github.com/asukiaaa/asukiaaa-kicad-footprints.pretty')
    gits.append('https://github.com/asukiaaa/my-kicad-footprints.pretty')
    gits.append('https://github.com/asutp/strygin_TO.pretty.git')
    gits.append('https://github.com/audrentis/MX_Plate_Footprints.pretty')
    gits.append('https://github.com/av-p/Avp.pretty')
    gits.append('https://github.com/axello/kicad')
    gits.append('https://github.com/aylons/safety_pin.pretty.git')
    gits.append('https://github.com/barafael/sdp8xx.pretty')
    gits.append('https://github.com/BCN3D/BCN3D-Kicad-library')
    gits.append('https://github.com/benkev/myLib.pretty')
    gits.append('https://github.com/blackb3ar/kicadprints.pretty')
    gits.append('https://github.com/boul51/boul51.pretty')
    gits.append('https://github.com/brunoeagle/kicad-open-modules')
    gits.append('https://github.com/bsakatu/kicad_parts_bsakatu.pretty')
    gits.append('https://github.com/bveenema/USB.pretty')
    gits.append('https://github.com/c-base/kicad-cbase.pretty.git')
    gits.append('https://github.com/candykingdom/homebrew.pretty')
    gits.append('https://github.com/CarnivalBen/custom-kicadlib.pretty')
    gits.append('https://github.com/celeritous/KiCad.pretty.git')
    gits.append('https://github.com/cepr/Bluetooth_Modules.pretty')
    gits.append('https://github.com/chenchiel/BGA.pretty.git')
    gits.append('https://github.com/ChristianLerche/LercheTech_KiCAD')
    gits.append('https://github.com/chriswags/KiCad')
    gits.append('https://github.com/cmos-droner/KiCAD-SDIY.pretty')
    gits.append('https://github.com/coddingtonbear/coddingtonbear-kicad-lib')
    gits.append('https://github.com/codemercenary-os/kicad.pretty.git')
    gits.append('https://github.com/ContextualElectronics/CE_KiCadLib')
    gits.append('https://github.com/coredump-ch/particle.pretty.git')
    gits.append('https://github.com/cormoran/kicad.pretty.git')
    gits.append('https://github.com/cosmikwolf/Zetaohm.pretty.git')
    gits.append('https://github.com/cpavlina/kicad-pcblib')
    gits.append('https://github.com/cschopfer/digipict-kicad-footprint.pretty')
    gits.append('https://github.com/cuzdaori/KiCad.pretty.git')
    gits.append('https://github.com/cvra/kicad-lib')
    gits.append('https://github.com/Cylindric3D/KicadComponents.pretty.git')
    gits.append('https://github.com/d3philip/kicadprints.pretty')
    gits.append('https://github.com/daprice/keyboard_accessories.pretty')
    gits.append('https://github.com/daprice/keyswitches.pretty')
    gits.append('https://github.com/dchwebb/Custom_Footprints.pretty')
    gits.append('https://github.com/descampsa/arduino.pretty')
    gits.append('https://github.com/descampsa/CreativeCommon.pretty')
    gits.append('https://github.com/descampsa/fuse.pretty')
    gits.append('https://github.com/descampsa/LEDs.pretty')
    gits.append('https://github.com/descampsa/molex.pretty')
    gits.append('https://github.com/devbisme/RPi_Hat.pretty')
    gits.append('https://github.com/digikey/digikey-kicad-library')
    gits.append('https://github.com/digikey/digikey-partner-kicad-library')
    gits.append('https://github.com/diypinball/PinballParts.pretty.git')
    gits.append('https://github.com/DonutCables/donutbrary.pretty')
    gits.append('https://github.com/dqmcdonald/DQM_kicad_new.pretty')
    gits.append('https://github.com/dragonmux/rhais_bourns.pretty')
    gits.append('https://github.com/dragonmux/rhais_button-smd.pretty')
    gits.append('https://github.com/dragonmux/rhais_cherry.pretty')
    gits.append('https://github.com/dragonmux/rhais_coilcraft.pretty')
    gits.append('https://github.com/dragonmux/rhais_connector-jack.pretty')
    gits.append('https://github.com/dragonmux/rhais_connector-lumberg.pretty')
    gits.append('https://github.com/dragonmux/rhais_connector-multicomp.pretty')
    gits.append('https://github.com/dragonmux/rhais_connector-optical.pretty')
    gits.append('https://github.com/dragonmux/rhais_connector-te.pretty')
    gits.append('https://github.com/dragonmux/rhais_diode.pretty')
    gits.append('https://github.com/dragonmux/rhais_diodes_inc.pretty')
    gits.append('https://github.com/dragonmux/rhais_led.pretty')
    gits.append('https://github.com/dragonmux/rhais_osc.pretty')
    gits.append('https://github.com/dragonmux/rhais_package-qfn.pretty')
    gits.append('https://github.com/dragonmux/rhais_package-smd.pretty')
    gits.append('https://github.com/dragonmux/rhais_package-to.pretty')
    gits.append('https://github.com/dragonmux/rhais_package-vishay.pretty')
    gits.append('https://github.com/dragonmux/rhais_rcl.pretty')
    gits.append('https://github.com/dragonmux/rhais_relay.pretty')
    gits.append('https://github.com/dragonmux/rhais_switch-cherry.pretty')
    gits.append('https://github.com/dragonmux/rhais_switch.pretty')
    gits.append('https://github.com/dragonmux/rhais_usb.pretty')
    gits.append('https://github.com/Drc3p0/Prototyping_Workshop')
    gits.append('https://github.com/DrMacak/ELI_HW_KiCad.pretty.git')
    gits.append('https://github.com/DX-MON/rhais_button-smd.pretty')
    gits.append('https://github.com/DX-MON/rhais_led.pretty')
    gits.append('https://github.com/DX-MON/rhais_osc.pretty')
    gits.append('https://github.com/DX-MON/rhais_package-qfn.pretty')
    gits.append('https://github.com/DX-MON/rhais_package-smd.pretty')
    gits.append('https://github.com/DX-MON/rhais_rcl.pretty')
    gits.append('https://github.com/DX-MON/rhais_usb.pretty')
    gits.append('https://github.com/ebastler/kicad-keyboard-parts.pretty')
    gits.append('https://github.com/eblanton/kicad-footprints.pretty.git')
    gits.append('https://github.com/egladman/keebs.pretty.git')
    gits.append('https://github.com/ElectronicCats/ComponentLibrariesKicadWurthElektronik')
    gits.append('https://github.com/emilytrau/MHS_Robotics.pretty')
    gits.append('https://github.com/ep092/library_toni.pretty.git')
    gits.append('https://github.com/esden/pretty-kicad-libs')
    gits.append('https://github.com/espressif/kicad-libraries')
    gits.append('https://github.com/F6ITU/Kicad_Modules')
    gits.append('https://github.com/farizno/KicadFootprints.pretty')
    gits.append('https://github.com/FateNozomi/Fate_Parts.pretty')
    gits.append('https://github.com/freetronics/freetronics_kicad_library')
    gits.append('https://github.com/fruchti/fruchtilib/')
    gits.append('https://github.com/fudge01010/fudge-kicad-footprints.pretty')
    gits.append('https://github.com/garrettsworkshop/stdpads.pretty')
    gits.append('https://github.com/Gigahawk/Gigahawk.pretty')
    gits.append('https://github.com/Gijsco/Kicad_Footprint_Connectors.pretty')
    gits.append('https://github.com/Gijsco/Kicad_Footprint_Modules.pretty')
    gits.append('https://github.com/Gijsco/Kicad_Footprint_Packages.pretty')
    gits.append('https://github.com/GodenX/KiCAD_MyLib.pretty')
    gits.append('https://github.com/gorbachev/KiCad-SSD1306-0.91-OLED-4pin-128x32.pretty')
    gits.append('https://github.com/granskog/DGS_Connectors.pretty.git')
    gits.append('https://github.com/granskog/DGS_Devices.pretty.git')
    gits.append('https://github.com/granskog/DGS_Modules.pretty.git')
    gits.append('https://github.com/granskog/DGS_Switches.pretty.git')
    gits.append('https://github.com/granskog/DGS_Symbols.pretty.git')
    gits.append('https://github.com/graycatlabs/GrayCatLabs.pretty.git')
    gits.append('https://github.com/graycatlabs/OSD335x.pretty.git')
    gits.append('https://github.com/greatscottgadgets/gsg-kicad-lib')
    gits.append('https://github.com/GSMCustomEffects/Kicad_GSM_Footprint.pretty.git')
    gits.append('https://github.com/gutierrezps/gtrzps.pretty')
    gits.append('https://github.com/hairymnstr/Nathan_Mechanical.pretty.git')
    gits.append('https://github.com/hairymnstr/Nathan_SMD.pretty.git')
    gits.append('https://github.com/hairymnstr/Nathan_SMT_Conn.pretty.git')
    gits.append('https://github.com/hairymnstr/Nathan_SMT_Other.pretty.git')
    gits.append('https://github.com/hairymnstr/Nathan_SMT_Passive.pretty.git')
    gits.append('https://github.com/hairymnstr/Nathan_SMT_Semis.pretty.git')
    gits.append('https://github.com/hairymnstr/Nathan_THT_Conn.pretty.git')
    gits.append('https://github.com/hairymnstr/Nathan_THT_Other.pretty.git')
    gits.append('https://github.com/hairymnstr/Nathan_THT_Passive.pretty.git')
    gits.append('https://github.com/hairymnstr/Nathan_THT.pretty.git')
    gits.append('https://github.com/haru-ake/millmax-mxalps.pretty')
    gits.append('https://github.com/hiroieee/kicad-lib.pretty.git')
    gits.append('https://github.com/HiZLabs/KiCad_Footprints.pretty.git')
    gits.append('https://github.com/hormigaAzul/libs.pretty.git')
    gits.append('https://github.com/hoskinstech/bjh-kicad-connector-fp.pretty.git')
    gits.append('https://github.com/hoskinstech/bjh-kicad-ic-fp.pretty.git')
    gits.append('https://github.com/hoskinstech/bjh-kicad-logo-fp.pretty.git')
    gits.append('https://github.com/hoskinstech/bjh-kicad-modules-fp.pretty.git')
    gits.append('https://github.com/hoskinstech/bjh-kicad-mountingholes-fp.pretty.git')
    gits.append('https://github.com/hoskinstech/bjh-kicad-rcld-fp.pretty.git')
    gits.append('https://github.com/hoskinstech/bjh-kicad-relays.pretty.git')
    gits.append('https://github.com/hoskinstech/bjh-kicad-switches-fp.pretty.git')
    gits.append('https://github.com/hoskinstech/bjh-kicad-transistor-fp.pretty.git')
    gits.append('https://github.com/Icenowy/KiCad_Ingress_Biocard.pretty')
    gits.append('https://github.com/imciner2/KiCad-Libraries')
    gits.append('https://github.com/imrehg/kicalopl')
    gits.append('https://github.com/imuli/Connectors_Anderson.pretty')
    gits.append('https://github.com/jaka/connectors.pretty')
    gits.append('https://github.com/jakobkg/footprints.pretty')
    gits.append('https://github.com/jdunmire/kicad-ESP8266')
    gits.append('https://github.com/Jeff-Russ/Kicad.pretty')
    gits.append('https://github.com/JEON-KS/Kicad_Footprint.pretty')
    gits.append('https://github.com/jerkey/kicad-jerry.pretty.git')
    gits.append('https://github.com/jerome-labidurie/d1_mini_kicad')
    gits.append('https://github.com/jmding8/keebee.pretty')
    gits.append('https://github.com/jnedbal/jakub.pretty.git')
    gits.append('https://github.com/JoanTheSpark/KiCAD')
    gits.append('https://github.com/joem/jwm_kicad_footprints_misc.pretty')
    gits.append('https://github.com/johaa1993/KiCad-Dev.pretty.git')
    gits.append('https://github.com/johslarsen/2.54mm_Pin_Headers.pretty.git')
    gits.append('https://github.com/johslarsen/Connectors.pretty.git')
    gits.append('https://github.com/johslarsen/Integrated_Circuits.pretty.git')
    gits.append('https://github.com/johslarsen/Misc.pretty.git')
    gits.append('https://github.com/johslarsen/Power_Module_SMD_Cyntec_MUN12AD.pretty')
    gits.append('https://github.com/johslarsen/SMD.pretty.git')
    gits.append('https://github.com/johslarsen/Switches.pretty.git')
    gits.append('https://github.com/JonasNorling/Footprints.pretty.git')
    gits.append('https://github.com/jp3cyc/KiCadLibrary')
    gits.append('https://github.com/Junes-PhD/kicad_arbitrary_pad_example')
    gits.append('https://github.com/ka2hiro/kagizaraya-parts.pretty')
    gits.append('https://github.com/Kazu-zamasu/kicad-test.pretty.git')
    gits.append('https://github.com/keebio/Keebio-Parts.pretty')
    gits.append('https://github.com/kicad-harryr/rx-viper.pretty')
    gits.append('https://github.com/kicad-rleh/D-Sub-HD.pretty')
    gits.append('https://github.com/kicad-rleh/D-Sub.pretty')
    gits.append('https://github.com/kicad-rleh/DFN-12-2EP_3.3x5mm_Pitch0.65mm.pretty')
    gits.append('https://github.com/kicad-rleh/Housings_VQFN.pretty.git')
    gits.append('https://github.com/kicad-rleh/L_Coilcraft.pretty')
    gits.append('https://github.com/kicad-rleh/LW_G6SP.pretty')
    gits.append('https://github.com/kicad-rleh/Measurement_Point_Round-SMD-Pad_Smaller.pretty')
    gits.append('https://github.com/kicad-rleh/resistor-power-shunt.pretty.git')
    gits.append('https://github.com/kicad-rleh/rleh-oscillators.pretty.git')
    gits.append('https://github.com/kicad-rleh/TI_TO-PMOD.pretty.git')
    gits.append('https://github.com/kicad-rleh/USB_Mikro_SMD_China.pretty.git')
    gits.append('https://github.com/kicad-rleh/WCSP-8_1.6x1.6mm_P0.5mm.pretty')
    gits.append('https://github.com/kicad-rleh/WE-SLx.pretty')
    gits.append('https://github.com/KiCad/Air_Coils_SML_NEOSID.pretty/')
    gits.append('https://github.com/KiCad/Buttons_Switches_SMD.pretty/')
    gits.append('https://github.com/KiCad/Buttons_Switches_ThroughHole.pretty/')
    gits.append('https://github.com/KiCad/Buzzers_Beepers.pretty/')
    gits.append('https://github.com/KiCad/Capacitors_SMD.pretty/')
    gits.append('https://github.com/KiCad/Capacitors_Tantalum_SMD.pretty/')
    gits.append('https://github.com/KiCad/Capacitors_ThroughHole.pretty/')
    gits.append('https://github.com/KiCad/Choke_Axial_ThroughHole.pretty/')
    gits.append('https://github.com/KiCad/Choke_Common-Mode_Wurth.pretty/')
    gits.append('https://github.com/KiCad/Choke_Radial_ThroughHole.pretty/')
    gits.append('https://github.com/KiCad/Choke_SMD.pretty/')
    gits.append('https://github.com/KiCad/Choke_Toroid_ThroughHole.pretty/')
    gits.append('https://github.com/KiCad/Connect.pretty/')
    gits.append('https://github.com/KiCad/Connectors_JST.pretty/')
    gits.append('https://github.com/KiCad/Connectors_Molex.pretty/')
    gits.append('https://github.com/KiCad/Connectors_Multicomp.pretty/')
    gits.append('https://github.com/KiCad/Converters_DCDC_ACDC.pretty/')
    gits.append('https://github.com/KiCad/Crystals.pretty/')
    gits.append('https://github.com/KiCad/Diodes_SMD.pretty/')
    gits.append('https://github.com/KiCad/Diodes_ThroughHole.pretty/')
    gits.append('https://github.com/KiCad/Discret.pretty/')
    gits.append('https://github.com/KiCad/Display.pretty/')
    gits.append('https://github.com/KiCad/Displays_7-Segment.pretty/')
    gits.append('https://github.com/KiCad/Divers.pretty/')
    gits.append('https://github.com/KiCad/EuroBoard_Outline.pretty/')
    gits.append('https://github.com/KiCad/Fiducials.pretty/')
    gits.append('https://github.com/KiCad/Filters_HF_Coils_NEOSID.pretty/')
    gits.append('https://github.com/KiCad/Fuse_Holders_and_Fuses.pretty/')
    gits.append('https://github.com/KiCad/Hall-Effect_Transducers_LEM.pretty/')
    gits.append('https://github.com/KiCad/Heatsinks.pretty/')
    gits.append('https://github.com/KiCad/Housings_DFN_QFN.pretty/')
    gits.append('https://github.com/KiCad/Housings_DIP.pretty/')
    gits.append('https://github.com/KiCad/Housings_QFP.pretty/')
    gits.append('https://github.com/KiCad/Housings_SIP.pretty/')
    gits.append('https://github.com/KiCad/Housings_SOIC.pretty/')
    gits.append('https://github.com/KiCad/Housings_SSOP.pretty/')
    gits.append('https://github.com/KiCad/Inductors_NEOSID.pretty/')
    gits.append('https://github.com/KiCad/Inductors.pretty/')
    gits.append('https://github.com/KiCad/IR-DirectFETs.pretty/')
    gits.append('https://github.com/KiCad/kicad-footprints/')
    gits.append('https://github.com/KiCad/Labels.pretty/')
    gits.append('https://github.com/KiCad/LEDs.pretty/')
    gits.append('https://github.com/KiCad/Measurement_Points.pretty/')
    gits.append('https://github.com/KiCad/Measurement_Scales.pretty/')
    gits.append('https://github.com/KiCad/Mechanical_Sockets.pretty/')
    gits.append('https://github.com/KiCad/Microwave.pretty/')
    gits.append('https://github.com/KiCad/Mounting_Holes.pretty/')
    gits.append('https://github.com/KiCad/NF-Transformers_ETAL.pretty/')
    gits.append('https://github.com/KiCad/Oddities.pretty/')
    gits.append('https://github.com/KiCad/Opto-Devices.pretty/')
    gits.append('https://github.com/KiCad/Oscillators.pretty/')
    gits.append('https://github.com/KiCad/PFF_PSF_PSS_Leadforms.pretty/')
    gits.append('https://github.com/KiCad/Pin_Headers.pretty/')
    gits.append('https://github.com/KiCad/Potentiometers.pretty/')
    gits.append('https://github.com/KiCad/Power_Integrations.pretty/')
    gits.append('https://github.com/KiCad/Relays_ThroughHole.pretty/')
    gits.append('https://github.com/KiCad/Resistors_SMD.pretty/')
    gits.append('https://github.com/KiCad/Resistors_ThroughHole.pretty/')
    gits.append('https://github.com/KiCad/Resistors_Universal.pretty/')
    gits.append('https://github.com/KiCad/RF_Modules.pretty/')
    gits.append('https://github.com/KiCad/SMD_Packages.pretty/')
    gits.append('https://github.com/KiCad/Socket_Strips.pretty/')
    gits.append('https://github.com/KiCad/Sockets_BNC.pretty/')
    gits.append('https://github.com/KiCad/Sockets_Mini-Universal.pretty/')
    gits.append('https://github.com/KiCad/Sockets_MOLEX_KK-System.pretty/')
    gits.append('https://github.com/KiCad/Sockets_WAGO734.pretty/')
    gits.append('https://github.com/KiCad/Sockets.pretty/')
    gits.append('https://github.com/KiCad/Symbols.pretty/')
    gits.append('https://github.com/KiCad/Terminal_Blocks.pretty/')
    gits.append('https://github.com/KiCad/TO_SOT_Packages_SMD.pretty/')
    gits.append('https://github.com/KiCad/TO_SOT_Packages_THT.pretty/')
    gits.append('https://github.com/KiCad/Transformers_CHK.pretty/')
    gits.append('https://github.com/KiCad/Transformers_SMPS_ThroughHole.pretty/')
    gits.append('https://github.com/KiCad/Transistors_OldSowjetAera.pretty/')
    gits.append('https://github.com/KiCad/Valves.pretty/')
    gits.append('https://github.com/KiCad/Varistors.pretty/')
    gits.append('https://github.com/KiCad/Wire_Connections_Bridges.pretty/')
    gits.append('https://github.com/KiCad/Wire_Pads.pretty/')
    gits.append('https://github.com/kichMan/JDY-08')
    gits.append('https://github.com/kikaiken/kicad_conn.pretty.git')
    gits.append('https://github.com/kikaiken/kicad_dip.pretty.git')
    gits.append('https://github.com/kikaiken/kicad_others.pretty.git')
    gits.append('https://github.com/kikaiken/kicad_smd.pretty.git')
    gits.append('https://github.com/kiu/kiu-footprint.pretty')
    gits.append('https://github.com/kleusbalut/kleus_kicad_library.pretty.git')
    gits.append('https://github.com/kohhat540750/kohhatsKicadFootPrint.pretty.git')
    gits.append('https://github.com/konspyre/kicad-footprints')
    gits.append('https://github.com/KozueNakano/KiCADKozueLib.pretty.git')
    gits.append('https://github.com/kubiX89/kiCAD.pretty')
    gits.append('https://github.com/Kujimoto/fujimoto.pretty.git')
    gits.append('https://github.com/kuresaru/KiCAD-Connector_KF301.pretty')
    gits.append('https://github.com/KUT-KiCad/KUT_CommIC.pretty.git')
    gits.append('https://github.com/KUT-KiCad/KUT_Connector.pretty.git')
    gits.append('https://github.com/KUT-KiCad/KUT_Device.pretty.git')
    gits.append('https://github.com/KUT-KiCad/KUT_DriveIC.pretty.git')
    gits.append('https://github.com/KUT-KiCad/KUT_Passive.pretty.git')
    gits.append('https://github.com/KUT-KiCad/KUT_Sensor.pretty.git')
    gits.append('https://github.com/KUT-KiCad/KUT_Switch.pretty.git')
    gits.append('https://github.com/KUT-KiCad/KUT_uController.pretty.git')
    gits.append('https://github.com/lab6-ifma/LAB6-LIB.pretty.git')
    gits.append('https://github.com/labitat/labitat_kicad_footprints.pretty.git')
    gits.append('https://github.com/LacieUnlam/Poncho_Esqueleto.pretty.git')
    gits.append('https://github.com/LacieUnlam/Poncho_Modelos.pretty.git')
    gits.append('https://github.com/leptun/leptunKicadLib.pretty')
    gits.append('https://github.com/LibreSolar/KiCad-footprints')
    gits.append('https://github.com/LosNarfos/Kicad_Libraries')
    gits.append('https://github.com/m-byte/aesora.pretty')
    gits.append('https://github.com/macmade/XS.pretty.git')
    gits.append('https://github.com/MacroFab/EDALibraries')
    gits.append('https://github.com/madworm/Bluetooth.pretty.git')
    gits.append('https://github.com/madworm/Capacitors.pretty.git')
    gits.append('https://github.com/madworm/DC-DC-modules.pretty.git')
    gits.append('https://github.com/madworm/DIL-Headers.pretty.git')
    gits.append('https://github.com/madworm/Fuses-polyswitch.pretty.git')
    gits.append('https://github.com/madworm/Heatsinks.pretty.git')
    gits.append('https://github.com/madworm/KiCad-Footprints.pretty.git')
    gits.append('https://github.com/madworm/micro-MaTch.pretty.git')
    gits.append('https://github.com/madworm/Nichia-LEDs.pretty.git')
    gits.append('https://github.com/madworm/Panelization.pretty.git')
    gits.append('https://github.com/madworm/Potentiometers.pretty.git')
    gits.append('https://github.com/madworm/RC-Battery-Connectors.pretty.git')
    gits.append('https://github.com/madworm/Resonators.pretty.git')
    gits.append('https://github.com/madworm/Rotary-Encoders.pretty.git')
    gits.append('https://github.com/madworm/SIL-Headers.pretty.git')
    gits.append('https://github.com/madworm/Switches.pretty.git')
    gits.append('https://github.com/madworm/WiFi.pretty.git')
    gits.append('https://github.com/madworm/WS2812B.pretty.git')
    gits.append('https://github.com/mamiksik/kicad-components.pretty')
    gits.append('https://github.com/marf41/MF-conn.pretty')
    gits.append('https://github.com/marf41/railtec.pretty')
    gits.append('https://github.com/mcous/kicad-lib')
    gits.append('https://github.com/MDHSweden/KiCad-MDH-Connectors.pretty')
    gits.append('https://github.com/MDHSweden/KiCad-MDH-IC.pretty')
    gits.append('https://github.com/MechChurch/MechChurch-parts.pretty')
    gits.append('https://github.com/mhorimoto/HOLLY.pretty')
    gits.append('https://github.com/micliv/LivaModules.pretty')
    gits.append('https://github.com/mitaroThanken/Connector_Audio_Mod.pretty')
    gits.append('https://github.com/mkleinschmidt/Connectors_Phoenix.pretty.git')
    gits.append('https://github.com/mkleinschmidt/Mundorf.pretty.git')
    gits.append('https://github.com/mkudlacek/Inductors_Bourns.pretty')
    gits.append('https://github.com/mmmspatz/mspatz_RFlab_Kicad_footprints.pretty.git')
    gits.append('https://github.com/mmmspatz/RFLab_KiCad_Libs.pretty.git')
    gits.append('https://github.com/monostable/CommonPartsLibrary.pretty')
    gits.append('https://github.com/mrmoje/mojes-kicad-footprints.pretty.git')
    gits.append('https://github.com/mron/kicad_footprints.pretty.git')
    gits.append('https://github.com/mvbasov/MVB.pretty')
    gits.append('https://github.com/myelin/myelin-kicad.pretty')
    gits.append('https://github.com/NathanielPerkins/NPFootprints.pretty.git')
    gits.append('https://github.com/Nathanjp91/NPFootprints.pretty')
    gits.append('https://github.com/natsfr/kicad-components')
    gits.append('https://github.com/naturesyouth/Footprints.pretty')
    gits.append('https://github.com/naturesyouth/meastro_gnss.pretty')
    gits.append('https://github.com/nebs/eurocad/')
    gits.append('https://github.com/nellump/Connectors_Powerpole.pretty')
    gits.append('https://github.com/newAM/newam.pretty')
    gits.append('https://github.com/nickgagnon/Kicad_footprint.pretty')
    gits.append('https://github.com/nightmechanic/nightmechanic_pcb.pretty.git')
    gits.append('https://github.com/Ninjaneer7/KiCADLib.pretty.git')
    gits.append('https://github.com/NorbotNorway/NorBotKiCadFootprints.pretty.git')
    gits.append('https://github.com/notmart/eurorack.pretty')
    gits.append('https://github.com/notsockx/kiboard.pretty')
    gits.append('https://github.com/nppc/KiCadCustomLibs')
    gits.append('https://github.com/nqbit/NQBit.pretty')
    gits.append('https://github.com/nqbit/nqbit.pretty')
    gits.append('https://github.com/nutbolt/WS2852.pretty.git')
    gits.append('https://github.com/nxmq/animegirlsare.pretty')
    gits.append('https://github.com/ohdsp/KiCad-Libs')
    gits.append('https://github.com/ohporter/beaglebone_cape.pretty.git')
    gits.append('https://github.com/ojousima/logos.pretty.git')
    gits.append('https://github.com/ojousima/SMD_Diodes.pretty.git')
    gits.append('https://github.com/ojousima/SMD_Packages.pretty.git')
    gits.append('https://github.com/ojousima/SMD_Passives.pretty.git')
    gits.append('https://github.com/ojousima/Switches_buttons.pretty.git')
    gits.append('https://github.com/ojousima/Terminal_blocks.pretty.git')
    gits.append('https://github.com/ojousima/Test_points.pretty.git')
    gits.append('https://github.com/OLIMEX/KiCAD')
    gits.append('https://github.com/OpenMusicKontrollers/omk.pretty.git')
    gits.append('https://github.com/OssiconeLabs/Ossicone_Labs_Footprints.pretty.git')
    gits.append('https://github.com/panicjp/KiCad_Mod.pretty.git')
    gits.append('https://github.com/patiqs/KicadLib.pretty.git')
    gits.append('https://github.com/PatrickBaus/footprints.pretty')
    gits.append('https://github.com/pbrook/Parts.pretty.git')
    gits.append('https://github.com/PCSmithy/744272471.pretty')
    gits.append('https://github.com/PCSmithy/Capstone_FP.pretty')
    gits.append('https://github.com/PCSmithy/CAS-D20TA.pretty')
    gits.append('https://github.com/PCSmithy/CL-SB-12B.pretty')
    gits.append('https://github.com/PCSmithy/custom.pretty')
    gits.append('https://github.com/PCSmithy/DB15_Female_Right_Angle.pretty')
    gits.append('https://github.com/PCSmithy/ESP32-footprints-Lib.pretty')
    gits.append('https://github.com/PCSmithy/logos.pretty')
    gits.append('https://github.com/PCSmithy/MCX.pretty')
    gits.append('https://github.com/PCSmithy/NeoPixel_FP.pretty')
    gits.append('https://github.com/PCSmithy/PA4332_222NLT.pretty')
    gits.append('https://github.com/PCSmithy/PCA9685PW_FP.pretty')
    gits.append('https://github.com/PCSmithy/PCB_Banana_Jack.pretty')
    gits.append('https://github.com/PCSmithy/phoenix_push_term_block.pretty')
    gits.append('https://github.com/PCSmithy/S8411-45R.pretty')
    gits.append('https://github.com/PCSmithy/SF_JCA10.pretty')
    gits.append('https://github.com/PCSmithy/VIA_FP.pretty')
    gits.append('https://github.com/peekpt/kicad_smisioto')
    gits.append('https://github.com/pelrun/libKiCad')
    gits.append('https://github.com/phigleaf/kicadprints.pretty')
    gits.append('https://github.com/q61org/kicad_nixie.pretty.git')
    gits.append('https://github.com/quinkennedy/chillpizza.pretty')
    gits.append('https://github.com/rascalmicro/rascalmicro-kicad-footprints.pretty.git')
    gits.append('https://github.com/rchojetzki-kicad/footprints.pretty')
    gits.append('https://github.com/rchojetzki-kicad/kicad-footprints-rchojetzki.pretty')
    gits.append('https://github.com/rchojetzki/rchojetzki-kicad-footprints-lib.pretty')
    gits.append('https://github.com/rdeterre/misc.pretty.git')
    gits.append('https://github.com/re-innovation/kicad_reinnovation')
    gits.append('https://github.com/realthunder/Connectors_Amass.pretty.git')
    gits.append('https://github.com/realthunder/Misc.pretty.git')
    gits.append('https://github.com/recursinging/kxmx/')
    gits.append('https://github.com/rigidus/kicad_my_library.pretty')
    gits.append('https://github.com/rocketman768/nu9j-footprints.pretty.git')
    gits.append('https://github.com/rocketscream/RocketScreamKicadLibrary.git')
    gits.append('https://github.com/rodibot/RoDI.pretty.git')
    gits.append('https://github.com/rohbotics/IPC7351-Nominal.pretty.git')
    gits.append('https://github.com/RomaVis/connect-minifit.pretty.git')
    gits.append('https://github.com/rudiloos/kilibs.pretty')
    gits.append('https://github.com/ruriwo/GND_via.pretty')
    gits.append('https://github.com/ruriwo/KiCad_Ceralock.pretty.git')
    gits.append('https://github.com/ruriwo/KiCad_CherryMx.pretty.git')
    gits.append('https://github.com/ruriwo/KiCad_MicroUSB.pretty.git')
    gits.append('https://github.com/ruriwo/KiCad_MoutingHole.pretty.git')
    gits.append('https://github.com/ruriwo/KiCad_Switches.pretty.git')
    gits.append('https://github.com/russellmcc/eurorack_kicad/')
    gits.append('https://github.com/russellmcc/russell_kicad')
    gits.append('https://github.com/ruuvi/kicad-library')
    gits.append('https://github.com/s-light/CONN_RJ45_MagJack_POEp.pretty.git')
    gits.append('https://github.com/S-SINKER/KiCad_Footprint.pretty.git')
    gits.append('https://github.com/samdolt/kicad-fp.pretty.git')
    gits.append('https://github.com/sasaplus1/kicad-footprints.pretty')
    gits.append('https://github.com/schemu/Housings_CDFP_RUS.pretty')
    gits.append('https://github.com/Seeed-Studio/OPL_Kicad_Library')
    gits.append('https://github.com/septillion-git/septillion_device.pretty.git')
    gits.append('https://github.com/sergiu46/KiCadParts.pretty')
    gits.append('https://github.com/servomouse/servomouse.pretty')
    gits.append('https://github.com/shelaf-dygma/raise_fp.pretty')
    gits.append('https://github.com/sherifeid/RoboLib.pretty.git')
    gits.append('https://github.com/shozaburo-shimada/KiCADfootprint.pretty')
    gits.append('https://github.com/simontretter/mediaarchitectu.re.pretty.git')
    gits.append('https://github.com/soburi-org/kicad_share_repository.pretty')
    gits.append('https://github.com/sparkfun/SparkFun-KiCad-Libraries')
    gits.append('https://github.com/stanleyseow/SVTmaker.pretty')
    gits.append('https://github.com/StefanHamminga/SH_Antennas.pretty')
    gits.append('https://github.com/StefanHamminga/SH_Audio.pretty')
    gits.append('https://github.com/StefanHamminga/SH_Batteries.pretty')
    gits.append('https://github.com/StefanHamminga/SH_BGA.pretty')
    gits.append('https://github.com/StefanHamminga/SH_Capacitors.pretty')
    gits.append('https://github.com/StefanHamminga/SH_Connectors.pretty')
    gits.append('https://github.com/StefanHamminga/SH_Crystals_Oscillators.pretty')
    gits.append('https://github.com/StefanHamminga/SH_Diodes.pretty')
    gits.append('https://github.com/StefanHamminga/SH_Filters.pretty')
    gits.append('https://github.com/StefanHamminga/SH_IC_Custom.pretty')
    gits.append('https://github.com/StefanHamminga/SH_Inductors.pretty')
    gits.append('https://github.com/StefanHamminga/SH_Jumper_Pins.pretty')
    gits.append('https://github.com/StefanHamminga/SH_Mechanical.pretty')
    gits.append('https://github.com/StefanHamminga/SH_Modules.pretty')
    gits.append('https://github.com/StefanHamminga/SH_QFN_QFP.pretty')
    gits.append('https://github.com/StefanHamminga/SH_Resistors.pretty.git')
    gits.append('https://github.com/StefanHamminga/SH_Shielding_Protection.pretty.git')
    gits.append('https://github.com/StefanHamminga/SH_SOD_SON_SOT.pretty.git')
    gits.append('https://github.com/StefanHamminga/SH_Solder_Pads.pretty.git')
    gits.append('https://github.com/StefanHamminga/SH_Switches_Buttons.pretty.git')
    gits.append('https://github.com/StefanHamminga/SH_Test_Points_Fiducials.pretty.git')
    gits.append('https://github.com/stormbard/Keyboard.pretty')
    gits.append('https://github.com/stormbard/Keyboard.pretty.git')
    gits.append('https://github.com/stubbyone/kicad-footprints.pretty.git')
    gits.append('https://github.com/suf-KiCAD/suf_capacitor.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_choke_smd.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_connector_misc.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_connector_ncw.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_connector_RJ.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_connector_usb.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_diode_bridge.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_dpak.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_fuse.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_housings_TO.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_led_display.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_led.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_module.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_power_module.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_relay.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_sob.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_sot.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_switch.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_terminal_block.pretty')
    gits.append('https://github.com/suf-KiCAD/suf_transformer.pretty')
    gits.append('https://github.com/svarmo/kicadParts.pretty')
    gits.append('https://github.com/TahuTech/tahutech.pretty')
    gits.append('https://github.com/TakeshiOnagawa/Kicad_GSM_Footprint.pretty')
    gits.append('https://github.com/tamu21131/mymod.pretty')
    gits.append('https://github.com/TDHolmes/KiCadCustomFootprints')
    gits.append('https://github.com/theFork/Solderjumpers.pretty.git')
    gits.append('https://github.com/theFork/uMIDI.pretty.git')
    gits.append('https://github.com/Tinkerforge/kicad-libraries')
    gits.append('https://github.com/tmandic/HCBT_Aclass.pretty')
    gits.append('https://github.com/tmk/keyboard_parts.pretty.git')
    gits.append('https://github.com/toka-eisos/Transformers_WurthElektronik.pretty')
    gits.append('https://github.com/tommueller/KiCAD-SDIY.pretty.git')
    gits.append('https://github.com/Toroid-io/toroid-kicad.pretty')
    gits.append('https://github.com/tristan-smith/HA_KicadLibraries')
    gits.append('https://github.com/tsunderu/nRF51822-modules.pretty.git')
    gits.append('https://github.com/twam/Connectors_Amphenol.pretty.git')
    gits.append('https://github.com/twam/Connectors_FCI.pretty.git')
    gits.append('https://github.com/twam/Connectors_Samtec.pretty.git')
    gits.append('https://github.com/twam/Connectors_Sullins.pretty.git')
    gits.append('https://github.com/twam/Connectors_TE.pretty.git')
    gits.append('https://github.com/twam/Connectors_Wuerth.pretty.git')
    gits.append('https://github.com/twam/Crystal_Oscillators.pretty.git')
    gits.append('https://github.com/tylercrumpton/CrumpPrints.pretty.git')
    gits.append('https://github.com/tylercrumpton/CrumpPrintSymbols.pretty.git')
    gits.append('https://github.com/UgoesSky/kicad_test.pretty.git')
    gits.append('https://github.com/UMONS-GFA/kicad-gfa.pretty.git')
    gits.append('https://github.com/UofSSpaceDesignTeam/USST-footprints.pretty')
    gits.append('https://github.com/UofSSpaceTeam/USST-footprints.pretty')
    gits.append('https://github.com/ViktorKicad/mystuff.pretty.git')
    gits.append('https://github.com/vivitainc/KiCADfootprint.pretty')
    gits.append('https://github.com/vontrapp/vontrapp.pretty.git')
    gits.append('https://github.com/voxel-dot-at/voxel_KiCad.pretty')
    gits.append('https://github.com/Wallbraker/Amiga.pretty')
    gits.append('https://github.com/wiebus/SOT23_SOT143_SOT143R_TSOT6_MK06A_SC70-6_Housing_14Mar2014.pretty.git')
    gits.append('https://github.com/WurthElectronics/Transformers_WurthElektronik.pretty')
    gits.append('https://github.com/wykys/kicad')
    gits.append('https://github.com/XenGi/kailh_big_series.pretty')
    gits.append('https://github.com/XenGi/teensy.pretty')
    gits.append('https://github.com/xesscorp/RPi_Hat.pretty.git')
    gits.append('https://github.com/xesscorp/xess.pretty')
    gits.append('https://github.com/ZaneKaminski/primarypoints.pretty.git')
    gits.append('https://github.com/Zetaohm/Zetaohm.pretty.git')
    gits.append('https://github.com/ziteh/key-switches.pretty')
    gits.append('https://gitlab.com/kicad/libraries/kicad-footprints')


    for gitLoc in gits:
        oomGitPull(gitLoc,dir)




