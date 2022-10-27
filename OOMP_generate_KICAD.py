import OOMP

import OOMP_kicad_BASE



###### Conert files
filename = "oomlout_OOMP_projects_V2\\PROJ\\ADAF\\0000\\STAN\\01\\src\\eagleBoard.brd"

#OOMP_kicad_BASE.convertEagleToKicad(filename,overwrite=False)

#OOMP_kicad_BASE.convertAllEagleToKicad(overwrite=False)

###### harvest kicad board
filename = "oomlout_OOMP_projects_V2\\PROJ\\ADAF\\1032\\STAN\\01\\src\\kicadBoard.kicad_pcb"

#OOMP_kicad_BASE.harvestAllKicad(overwrite=False)

OOMP_kicad_BASE.harvestKicadBoard(filename,overwrite=False)