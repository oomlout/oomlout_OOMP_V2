from oomBase import *

#"https://www.aliexpress.com/wholesale?SearchText=1117"

searchList = ["https://www.avnet.com/shop/us/search/",
                "https://www.digikey.com/en/products?keywords=",
                "https://www.lcsc.com/search?q=",
                "https://uk.farnell.com/search?st=",
                "https://www.mouser.com/c/?q="
]
 
def searchDistFor(keyword):
    for s in searchList:
        searchString = s + keyword
        oomLaunchWebsite(searchString)


keyword="ATTINY84 SSU"
searchDistFor(keyword)        