import OOMP
import pyqrcode


def createCode(item):
    hexID = item["hexID"][0]
    oompID = item["oompID"][0]
    print("    Making qr code for: " + oompID)
    
    qrCodeName = OOMP.getFileItem(item,"qrCode")
    qr = pyqrcode.create("YX" + str(hexID))
    qr.png(qrCodeName, scale=12)