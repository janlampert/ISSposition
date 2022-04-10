import requests
import pyperclip

def getLocation():
    response = requests.get("http://api.open-notify.org/iss-now.json")

    responseJson = response.json()
    #responseJsonFormatted = json.dumps(responseJson, indent=4, sort_keys=True)

    position = responseJson["iss_position"]

    longitude = position["longitude"]
    latitude = position["latitude"]

    positionReturn = f"{latitude},{longitude}"

    return positionReturn

def copyToClipboard():
    position = getLocation()
    pyperclip.copy(position)

def run():
    copyToClipboard()

run()
