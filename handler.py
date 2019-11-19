import json
import requests

def getdog(event, context):
    r = requests.get("https://dog.ceo/api/breeds/image/random")
    data = r.json()
    url = data["message"]

    response = {
        "statusCode": 200,
        "url": url
    }
    return response


def getcat(event, context):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    data = r.json()
    url = data[0]["url"]

    response = {
        "statusCode": 200,
        "url": url
    }
    return response
