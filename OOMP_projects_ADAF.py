import OOMP
import OOMP_projects_BASE

def createProjects():
    d = {}
    d["oompType"] = "PROJ"
    d["oompSize"] = "ADAF"
    d["oompColor"] = "1231"
    d["oompDesc"] = "STAN"
    d["oompIndex"] = "0A"
    
    d["hexID"] = "PRA1231A"

    d["name"] = "ADXL345 - Triple-Axis Accelerometer (+-2g/4g/8g/16g) Rev A"
    d["gitRepo"] = "https://github.com/adafruit/Adafruit_ADXL345_PCB"
    d["gitName"] = "Adafruit_ADXL345_PCB"
    d["eagleBoard"] = "Adafruit_ADXL345.brd"
    d["eagleSchem"] = d["eagleBoard"].replace(".brd",".sch")
    OOMP_projects_BASE.makeProject(d)

    d["oompIndex"] = "0B"
    d["hexID"] = "PRA1231B"
    d["name"] = "ADXL345 - Triple-Axis Accelerometer (+-2g/4g/8g/16g) Rev B"
    d["gitRepo"] = "https://github.com/adafruit/Adafruit_ADXL345_PCB"
    d["gitName"] = "Adafruit_ADXL345_PCB"
    d["eagleBoard"] = "Adafruit ADXL345 Triple-Axis Accelerometer.brd"
    d["eagleSchem"] = d["eagleBoard"].replace(".brd",".sch")
    OOMP_projects_BASE.makeProject(d)

    d["oompIndex"] = "0C"
    d["hexID"] = "PRA1231C"
    d["name"] = "ADXL345 - Triple-Axis Accelerometer (+-2g/4g/8g/16g) Rev C"
    d["gitRepo"] = "https://github.com/adafruit/Adafruit_ADXL345_PCB"
    d["gitName"] = "Adafruit_ADXL345_PCB"
    d["eagleBoard"] = "ADXL345 STEMMA QT.brd"
    d["eagleSchem"] = d["eagleBoard"].replace(".brd",".sch")
    OOMP_projects_BASE.makeProject(d)
