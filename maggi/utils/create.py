import requests
import json

def createbox(os, cpu, memory, port):

    url = "http://localhost:8888/api/v2/superinspire/getOS"
    print(os, cpu, memory, port)
    querystring = {"os":os,"cpu":cpu,"mem":memory,"port":port}
    payload = ""
    headers = {
        'cache-control': "no-cache"}
    try:
        response = requests.request(method="GET", url=url, data=payload, headers=headers, params=querystring)
        response = json.loads(response.text)
        print(response)
        accessport = str(response["shareUrl"]).split("://")
        print(accessport)
        print(u'\u2713', "fetched linux machine...")
        print("container ID: ", response["containerId"])
        print("open port : ", response["openPort"])
        print("access port : ", "http://localhost:"+response["openPort"]+accessport[0])
        print(response["containerId"])
        return response["containerId"], "http://localhost:"+response["openPort"]+accessport[0]
    except Exception:
        print("something happend ", Exception)
        return "roll back" # TODO roll back





# createbox("instantbox/ubuntu:14.04", "1", "512", "10002")