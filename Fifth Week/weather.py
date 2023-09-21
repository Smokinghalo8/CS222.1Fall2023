import json
import ssl  #Bypass

from urllib.request import urlopen

def CAAlert():
    url="https://api.weather.gov/alerts/active?area=CA"
    context = ssl._create_unverified_context    #DANGEROUS DO NOT DO THIS *EVER*
    response = urlopen(url,context=context)
    weatherData = json.loads(response.read())   #NOW A DICTORNARY THAT HOLDS ALL DATA
    return weatherData["features"][0]["properties"]["event"]


def main():

    url="https://api.weather.gov/alerts/active?area=CA"
    context = ssl._create_unverified_context    #DANGEROUS DO NOT DO THIS *EVER*
    response = urlopen(url,context=context)
    weatherData = json.loads(response.read())   #NOW A DICTORNARY THAT HOLDS ALL DATA

    for e in weatherData["featrues"]:
        print(e["properties"]["event"])
        print(e["properties"]["headline"])
        print(e["properties"]["description"])

main()