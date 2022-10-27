def load(tn):
    ###### BASE
    current = "oompType"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "BASE"
    tn[current]["name"] = "OOMP Type"
    tn[current]["description"] = "OOMP Type"
    current = "oompSize"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "BASE"
    tn[current]["name"] = "OOMP Size"
    tn[current]["description"] = "OOMP Size"
    current = "oompColor"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "BASE"
    tn[current]["name"] = "OOMP Color"
    tn[current]["description"] = "OOMP Color"
    current = "oompDesc"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "BASE"
    tn[current]["name"] = "OOMP Description"
    tn[current]["description"] = "OOMP Description"
    current = "oompIndex"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "BASE"
    tn[current]["name"] = "OOMP Index"
    tn[current]["description"] = "OOMP Index"
    current = "oompID"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "BASE"
    tn[current]["name"] = "Full OOMP ID"
    tn[current]["description"] = "Full OOMP ID"
    current = "hexID"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "BASE"
    tn[current]["name"] = "Hex ID (short code)"
    tn[current]["description"] = "Hex ID (short code)"

###### Main ones
    category = "MAIN"
    current = "name"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = category
    tn[current]["name"] = current
    tn[current]["description"] = current
    current = "description"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = category
    tn[current]["name"] = current
    tn[current]["description"] = current
    current = "code"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = category
    tn[current]["name"] = current
    tn[current]["description"] = current

###### Collection Ones
    category = "COLLECTION"
    current = "collection"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = category
    tn[current]["name"] = current
    tn[current]["description"] = current
    
###### Project Ones
    current = "gitRepo"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "PROJECT"
    tn[current]["name"] = current
    tn[current]["description"] = current
    current = "gitName"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "PROJECT"
    tn[current]["name"] = current
    tn[current]["description"] = current
    current = "eagleBoard"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "PROJECT"
    tn[current]["name"] = current
    tn[current]["description"] = current
    current = "eagleSchem"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "PROJECT"
    tn[current]["name"] = current
    tn[current]["description"] = current
    current = "kicadBoard"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "PROJECT"
    tn[current]["name"] = current
    tn[current]["description"] = current
    current = "kicadSchem"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "PROJECT"
    tn[current]["name"] = current
    tn[current]["description"] = current

###### Part Numbers
    current = "manufacturerPartNumber"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "PARTNUMBER"
    tn[current]["name"] = "Part Number (Manufacturer)"
    tn[current]["description"] = "A part number from a manufacturer. (Fields: code,name,partID,partName,partLink)"
    ######
    current = "distributorPartNumber"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "PARTNUMBER"
    tn[current]["name"] = "Part Number (Distributor)"
    tn[current]["description"] = "A part number from a distributor. (Fields:  (Fields: code,name,partID,partName)"
    ######
    current = "oplPartNumber"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "PARTNUMBER"
    tn[current]["name"] = "Part Number (OPL)"
    tn[current]["description"] = "A part number from an open parts library. (Fields:  (Fields: code,name,partID,partName))"


######  EDA
    current = "footprintKicad"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "EDA"
    tn[current]["name"] = "Footprint Kicad"
    tn[current]["description"] = "An OOMP code for a matching footprint"
    current = "footprintKicadDetails"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "EDA"
    tn[current]["name"] = "Footprint Kicad"
    tn[current]["description"] = "Extracted details from a kicad footprint"
    current = "symbolKicad"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "EDA"
    tn[current]["name"] = "Symbol Kicad"
    tn[current]["description"] = "An OOMP code for a matching symbol"
    current = "symbolKicadDetails"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "EDA"
    tn[current]["name"] = "Symbol Kicad Details"
    tn[current]["description"] = "Extracted details from a kicad footprint"

######  Parts
    current = "oompParts"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "PARTS"
    tn[current]["name"] = "OOMP Parts List"
    tn[current]["description"] = "List of OOMP matched parts (Designator,OOMPID)"
    current = "oompInstances"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "PARTS"
    tn[current]["name"] = "OOMP Instances"
    tn[current]["description"] = "List of OOMP projects the part is in (Designator,Project)"
    current = "rawParts"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "PARTS"
    tn[current]["name"] = "Parts as pulled from a BOM"
    tn[current]["description"] = "List of OOMP matched parts (eagleBom,kicadBom)(each entry in BOM has Part,Value,Device,Package,Description,BOM)"
    