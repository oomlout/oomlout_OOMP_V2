import OOMP
import OOMP_projects_BASE
import OOMP_projects_ADAF_generated


def farmProjects():
    OOMP_projects_BASE.farmProjects(users=["adafruit"],code="ADAF")

def makeBaseProjects():
    OOMP_projects_BASE.makeBaseProjects(company="adafruit",code="ADAF")


def createProjects():
    OOMP_projects_ADAF_generated.createProjects()
    
    projects = []
    base = {}
    base["oompType"] = "PROJ"
    base["oompSize"] = "ADAF"
    base["format"] = "eagle"
    base["github"] = "https://github.com/adafruit/"
    
    
    d = base.copy()
    d["hexID"] = "PRA1231A"
    d["repo"] = "Adafruit_ADXL345_PCB"
    d["name"] = "ADXL345 - Triple-Axis Accelerometer (+-2g/4g/8g/16g) Rev A"
    d["file"] = "Adafruit_ADXL345"
    d["count"] = "1231"
    d["oompIndex"] = "0A"    
    projects.append(d)
    

    
    
    d = base.copy()
    d["hexID"] = "PRA1231C"
    d["repo"] = "Adafruit_ADXL345_PCB"
    d["name"] = "ADXL345 - Triple-Axis Accelerometer (+-2g/4g/8g/16g) Rev C"
    d["file"] = "ADXL345 STEMMA QT"
    d["count"] = "1231"
    d["oompIndex"] = "0C"    
    projects.append(d)    

    
    for d in projects:
        OOMP_projects_BASE.makeProjectNew(d) 
