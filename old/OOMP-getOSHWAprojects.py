import requests


#Initialize csv
output = "OOMP-oshwa.csv"
f = open(output,"w+",encoding="utf-8")

fields = ["oshwaUid",'responsibleParty','country', 'publicContact', 'projectName', 'projectWebsite', 'projectVersion','projectDescription', 'primaryType', 'projectKeywords', 'citations', 'documentationUrl', 'hardwareLicense','softwareLicense', 'documentationLicense', 'certificationDate']
for i in fields:
    f.write(i + ",")
f.write("\n")


for x in range(0,20):
    print("Fetching Pagination: " + str(x))

    offset = str(x * 100)
    url = "https://certificationapi.oshwa.org/api/projects?offset=" + offset

    payload = {}

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYzM2E5ZTlkMWMyNmJhMDAxOGFkMTIxZiIsImlhdCI6MTY2NDc4NjA3NywiZXhwIjoxNjczNDI2MDc3fQ.fX9-Kp5vVzzW_fNtZjUH6DqxMADTKTNuQPzeGjAmtU8'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    contents = response.text.encode('utf8')
    #print(response.text.encode('utf8'))
    import json

    d = json.loads(contents)


    for item in d["items"]:    
        for i in fields:
            try:
                if type(item[i]) == list:
                    for y in item[i]:
                        f.write(str(y).replace(","," ").replace("\n"," ").replace("\r"," ") + " ")
                        f.write(",")
                else:
                    f.write(item[i].replace("\n"," ").replace("\r"," ") + ",")            
            except KeyError:
                pass
        f.write("\n")



f.close()