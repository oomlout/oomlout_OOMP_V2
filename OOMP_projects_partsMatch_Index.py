import OOMP
import OOMP_projects_partsMatch

def matchIndex(project,part,oompType="",oompSize="",oompColor="",oompDesc="",oompIndex=""):
    global PART, VALUE, DEVICE, PACAKGE, DESC, BOM    
    rv= "01"
    partID = oompType + "-" + oompSize + "-" + oompColor + "-" + oompDesc
    partDict = OOMP_projects_partsMatch.loadPartDict(part,project)   

    ######  Cap\acitor Voltage matching
    ###### V50
    list = []
    v = "CA"
    list.append(["LEDS-2121-RGB-STAN",v])
    v = "RS"
    list.append(["HEAD-01-X-PI04",v])
    
    v = "V33D"
    list.append(["VREG-SO235-X-KAP2112K",v])
    list.append(["VREG-SO235-X-KLP298XS",v])
    list.append(["VREG-SO235-X-KMIC5225",v])
    v= "V63D"
    list.append(["CAPC-0402-X-NF47D",v])
    list.append(["CAPC-0402-X-UF1",v])
    list.append(["CAPC-0402-X-UF10",v])
    list.append(["CAPC-0402-X-UF47D",v])
    list.append(["CAPC-0603-X-UF10",v])
    list.append(["CAPC-0805-X-UF22",v])
    list.append(["CAPC-1206-X-UF100",v])
    list.append(["CAPE-05-X-UF1",v])
    list.append(["CAPE-05-X-UF22D",v])
    list.append(["CAPE-05-X-UF47D",v])
    list.append(["CAPT-1206-X-UF47D",v])
    list.append(["CAPT-2917-X-UF470",v])
    v = "V10"
    list.append(["CAPC-0402-X-NF100",v])
    list.append(["CAPC-0402-X-UF1",v])
    list.append(["CAPC-0603-X-UF10",v])
    list.append(["CAPC-0603-X-UF22D",v])
    list.append(["CAPC-0603-X-UF47D",v])
    list.append(["CAPC-0805-X-UF10",v])
    list.append(["CAPT-1206-X-UF10",v])
    list.append(["CAPT-1206-X-UF22",v])
    list.append(["CAPT-1210-X-UF10",v])
    list.append(["CAPT-1210-X-UF100",v])
    list.append(["CAPT-1210-X-UF22",v])
    list.append(["CAPT-1210-X-UF47",v])
    list.append(["CAPT-2312-X-UF100",v])
    list.append(["CAPT-3216-X-UF10",v])

    v = "V16"
    list.append(["CAPC-0402-X-NF100",v])
    list.append(["CAPC-0402-X-NF220",v])
    list.append(["CAPE-05-X-UF100",v])
    list.append(["CAPE-05-X-UF47",v])
    list.append(["CAPE-S63D-X-UF220",v])
    list.append(["CAPT-1206-X-UF10",v])
    list.append(["CAPT-1206-X-UF47D",v])
    list.append(["CAPT-1210-X-UF10",v])
    list.append(["CAPT-1210-X-UF22",v])
    list.append(["CAPT-2312-X-UF100",v])
    list.append(["CAPT-2312-X-UF47",v])

    v = "V25"
    list.append(["CAPC-0402-X-NF100",v])
    list.append(["CAPC-0402-X-NF47",v])
    list.append(["CAPC-0603-X-NF220",v])
    list.append(["CAPC-0603-X-UF1",v])
    list.append(["CAPC-0805-X-UF1",v])
    list.append(["CAPC-0805-X-UF10",v])
    list.append(["CAPC-0805-X-UF22D",v])
    list.append(["CAPC-0805-X-UF47D",v])
    list.append(["CAPC-1206-X-UF10",v])
    list.append(["CAPE-05-X-UF10",v])
    list.append(["CAPE-05-X-UF22",v])
    list.append(["CAPE-10-X-UF470",v])
    list.append(["CAPE-63D-X-UF100",v])
    list.append(["CAPE-S63D-X-UF47",v])
    list.append(["CAPT-2312-X-UF22",v])

    v = "V50"
    list.append(["CAPC-0603-X-NF100",v])
    list.append(["CAPC-0805-X-NF100",v])    
    list.append(["CAPC-0402-X-NF1",v])
    list.append(["CAPC-0402-X-NF10",v])
    list.append(["CAPC-0402-X-NF22",v])
    list.append(["CAPC-0402-X-NF22D",v])
    list.append(["CAPC-0402-X-NF47D",v])
    list.append(["CAPC-0402-X-PF05D",v])
    list.append(["CAPC-0402-X-PF06D",v])
    list.append(["CAPC-0402-X-PF1",v])
    list.append(["CAPC-0402-X-PF10",v])
    list.append(["CAPC-0402-X-PF100",v])
    list.append(["CAPC-0402-X-PF12",v])
    list.append(["CAPC-0402-X-PF15",v])
    list.append(["CAPC-0402-X-PF15D",v])
    list.append(["CAPC-0402-X-PF18",v])
    list.append(["CAPC-0402-X-PF22",v])
    list.append(["CAPC-0402-X-PF220",v])
    list.append(["CAPC-0402-X-PF22D",v])
    list.append(["CAPC-0402-X-PF27",v])
    list.append(["CAPC-0402-X-PF33",v])
    list.append(["CAPC-0402-X-PF390",v])
    list.append(["CAPC-0402-X-PF47",v])
    list.append(["CAPC-05-X-NF100",v])
    list.append(["CAPC-0603-X-NF1",v])
    list.append(["CAPC-0603-X-NF10",v])
    list.append(["CAPC-0603-X-NF100",v])
    list.append(["CAPC-0603-X-NF22",v])
    list.append(["CAPC-0603-X-NF22D",v])
    list.append(["CAPC-0603-X-NF33",v])
    list.append(["CAPC-0603-X-NF47D",v])
    list.append(["CAPC-0603-X-PF10",v])
    list.append(["CAPC-0603-X-PF100",v])
    list.append(["CAPC-0603-X-PF12",v])
    list.append(["CAPC-0603-X-PF15",v])
    list.append(["CAPC-0603-X-PF22",v])
    list.append(["CAPC-0603-X-PF27",v])
    list.append(["CAPC-0603-X-PF39",v])
    list.append(["CAPC-0603-X-PF47D",v])
    list.append(["CAPC-0603-X-PF82D",v])
    list.append(["CAPC-0805-X-NF10",v])
    list.append(["CAPC-0805-X-NF100",v])
    list.append(["CAPC-45D-X-NF10",v])
    list.append(["CAPC-55D-X-PF22",v])
    list.append(["CAPT-36D-X-NF100",v])
    v = "V100"
    list.append(["CAPC-1206-X-NF100",v])






    for l in list:
        if l[0] == partID:
            return l[1]
       

    list = []
    list.append(["MIC52055V","V5"])
    
    for l in list:
        if l[0] == partDict["VALUE"]:
            return l[1]

    if oompType.startswith("CAP"):
        list = []
        list.append(["25V","V25"])
        list.append(["6.3V","V63D"])        
                
        for l in list:
            if l[0] in partDict["VALUE"]:
                return l[1]

        ################### DEBUG
    if partDict["PART"] == "PC1":
        pass    


    return rv        

