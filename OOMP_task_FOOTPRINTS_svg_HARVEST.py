import OOMP
import OOMP_footprints
import OOMP_footprints_BASE
import OOMP_kicad_BASE

#OOMP.makePickle()
OOMP.loadPickle()

import OOMP_task_FOOTPRINTS_svg


######## TESTING
filter = ["Connector_PinHeader_2.54mm","Resistor_SMD","Resistor_THT","Capacitor_SMD","Capacitor_THT","Capacitor_Tantalum_SMD","Package_TO_SOT_SMD","Package_TO_SOT_SMD","Package_SO"]
filter = [""]
OOMP_kicad_BASE.harvestAllKicad(overwrite=False,eda=True,fpFilter=filter)






