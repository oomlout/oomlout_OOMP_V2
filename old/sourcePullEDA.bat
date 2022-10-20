REM  Pull in the required source files into sourceFiles/ folder

md sourceFiles
cd sourceFiles

REM Eagle Libraries
git clone https://github.com/adafruit/Adafruit-Eagle-Library
git clone https://github.com/DangerousPrototypes/Eagle_Part_Library
del DangerousPrototypes-Eagle-Library
ren Eagle_Part_Library DangerousPrototypes-Eagle-Library
git clone https://github.com/Seeed-Studio/OPL_Eagle_Library
git clone https://github.com/pimoroni/eagle 
del Pimoroni-Eagle-Library
ren eagle Pimoroni-Eagle-Library
git clone https://github.com/sparkfun/SparkFun-Eagle-Libraries
git clone https://github.com/watterott/Eagle-Libs
del Eagle-Libs
ren Eagle-Libs Watterot-Eagle-Libraries


REM Kicad libraries
git clone https://github.com/ContextualElectronics/CE_KiCadLib
git clone https://gitlab.com/kicad/libraries/kicad-symbols
git clone https://gitlab.com/kicadpersus/kicad-footprints

cd ..

REM need to manually add each library to Eagle