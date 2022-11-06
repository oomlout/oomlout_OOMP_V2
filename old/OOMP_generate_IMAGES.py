import OOMP_images_BASE

#OOMP.loadPickle()

inFile = "C:/GH/oomlout_OOMP_V2/oomlout_OOMP_eda_V2/FOOTPRINT/kicad/kicad-footprints/Button_Switch_THT/KSA_Tactile_SPST/image.png"
#OOMP_images_BASE.generateResolutions(inFile)


OOMP_images_BASE.generateAllResolutions(inFile)
#for item in OOMP.items:
    #OOMP_migrate_BASE.migrateFiles(OOMP.items[item])