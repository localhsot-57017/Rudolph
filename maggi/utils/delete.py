
import requests


def clean(containerid):
    url = "http://localhost:8888/api/v2/superinspire/rmOS"
    querystring = {"containerId":containerid}
    response = requests.request("GET", url, params=querystring)
    print("removed container and all local settings")
    return response.text