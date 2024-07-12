import requests
import pandas

host = "https://www.signia.net"

apiurl = "https://www.signia.net/api/shop-finder/GetShopsByProximity?latlng=36.204824,138.252924&country=JP&filterOnPreferred=false&isInitialMapLoad=true&shopFinderDatasourceId={2357A5BD-F3F1-483D-9ADA-1C883EF8EE54}"

respons = requests.get(apiurl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'})

data = respons.json()

def getallshopUrl(data):
    result=[]
    for a in data:
        result.append(a["shopUrl"])
    return result

def getalltitle(data):
    result=[]
    for a in data:
        a["DisplayTitle"]=a["DisplayTitle"].replace("\u3000"," ")
        result.append(a["DisplayTitle"])
    return result

def getalladdress(data):
    result=[]
    for a in data:
        a["searchText"]=a["searchText"].replace("\u3000"," ")
        result.append(a["searchText"])
    return result

test = ""

for a in getalladdress(data):
    test+=f"\n{a}"
print(test)
