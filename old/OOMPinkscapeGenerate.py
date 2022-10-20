import OOMP
import OOMPdiagrams
#import pyautogui
import time
import os.path

def generateDiagrams():
    time.sleep(5)
    for part in OOMP.parts:
        generateDiagram(part)

def generateDiagram(part):
    oompID = part.getTag("oompID").value
    if not "TEMPLATE" in oompID:
        print("Generating: " + oompID )
        for type in OOMPdiagrams.types:
            fileName = OOMP.getDir("parts",base=True) + oompID + "/diag" + type.upper() + ".py"
            if(os.path.exists(fileName)):
                #print("    Making: " + fileName)
                genFileName(fileName)
        

def sendAltKey(st):
    print("                Sending Alt " + st)
    pyautogui.keyDown('alt')
    time.sleep(.01)
    pyautogui.press(st)
    time.sleep(.01)
    pyautogui.keyUp('alt')
    time.sleep(2)

def sendKeyShift(st, times=1):
    print("        Sending: " + st + " " + str(times) + " times")
    
    pyautogui.keyDown('shift')
    
    for t in range(times):
        time.sleep(.25)
        pyautogui.press(st)
        time.sleep(.25)
    pyautogui.keyUp('shift')
    time.sleep(1.75)

def sendKeyCtrl(st, times=1):
    print("        Sending: " + st + " " + str(times) + " times")
    for t in range(times):
        pyautogui.keyDown('ctrl')
        time.sleep(.01)
        pyautogui.press(st)
        time.sleep(.01)
        pyautogui.keyUp('ctrl')
        time.sleep(2)
        time.sleep(0.25)    
    time.sleep(1.75)

def sendKey(st, times=1):
    print("        Sending: " + st + " " + str(times) + " times")
    for t in range(times):
        pyautogui.press(st)
        time.sleep(0.25)    
    time.sleep(1.75)


def sendKeys(st, times=1):
    print("        Sending: " + st + " " + str(times) + " times")
    for t in range(times):
        for s in st:
            pyautogui.press(s)
            time.sleep(0.05)    
    time.sleep(1.75)



def genFileName(fileName):
    sendAltKey("n")
    sendKey("down",12)
    time.sleep(3)
    sendKey("right")
    sendKey("up",4)
    sendKey("enter")
    time.sleep(10)
    sendKey("tab",2)
    sendKeys(fileName)
    time.sleep(2)
    sendKeyShift("tab",2) 
    sendKey("enter")
    time.sleep(10)    
    sendKey("tab")
    sendKey("enter")
    sendKey("esc")
    sendKeyCtrl("a")
    time.sleep(10) 
    sendKey("del")
    time.sleep(10) 



        


def genTest():
    fileName = "C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD_I01_X_PI03_01/diagBBLS.py"
    f = open(fileName)
    exec(f.read())
    f.close()
    


