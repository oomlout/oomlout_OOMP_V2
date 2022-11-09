import OOMP
import pyqrcode
import os
from oomBase import *


def createCode(item,overwrite = False):
    hexID = item["hexID"][0]
    oompID = item["oompID"][0]
    #print("    Making qr code for: " + oompID)
    ping()
    
    qrCodeName = OOMP.getFileItem(item,"qrCode")
    if not os.path.exists(qrCodeName) or overwrite:
        qr = pyqrcode.create("YX" + str(hexID))
        qr.png(qrCodeName, scale=12)