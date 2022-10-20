md sourceFiles
cd sourceFiles

git clone https://github.com/openscopeproject/InteractiveHtmlBom
cd InteractiveHtmlBom
git pull
cd..
git clone https://github.com/sparkfun/SparkFun-Eagle-Libraries
cd SparkFun-Eagle-Libraries
git pull
cd..
git clone https://github.com/adafruit/Adafruit-Eagle-Library
cd Adafruit-Eagle-Library
git pull
cd..
git clone https://gitlab.com/kicad/libraries/kicad-footprints
cd kicad-footprints
git pull
cd..
git clone https://gitlab.com/kicad/libraries/kicad-symbols
cd kicad-symbols
git pull
cd..
git clone https://github.com/ContextualElectronics/CE_KiCadLib
cd CE_KiCadLib
git pull
REM Ned to move .pretty files up one directory
cd..
cd..