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
    current = "hexID"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "BASE"
    tn[current]["name"] = "Hex ID (short code)"
    tn[current]["description"] = "Hex ID (short code)"

###### Part Numbers
    current = "manufacturerPartNumber"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "PARTNUMBER"
    tn[current]["name"] = "Part Number (Manufacturer)"
    tn[current]["description"] = "A part number from a manufacturer. (Fields: code,name,partID,partName)"
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
    tn[current]["description"] = "Extrracted details from a kicad footprint"
    current = "symbolKicad"
    tn[current] = {}
    tn[current]["code"] = current
    tn[current]["category"] = "EDA"
    tn[current]["name"] = "Symbol Kicad"
    tn[current]["description"] = "An OOMP code for a matching symbol"
