import requests
import json
import traceback

def createbox(os, cpu, memory, port):

    url = "http://localhost:8888/api/v2/superinspire/getOS"
    print(os, cpu, memory, port)
    querystring = {"os":os,"cpu":cpu,"mem":memory,"port":port}
    payload = ""
    headers = {
        'cache-control': "no-cache"}
    try:
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        print(response)
        response = json.loads(response.text)
        accessport = str(response["shareUrl"]).split("://")
        print(accessport)
        print(u'\u2713', "fetched linux machine ")
        print("container ID: ", response["containerId"])
        print("open port : ", response["openPort"])
        print("access port : ", "http://localhost" + accessport[1])
        print(response["containerId"])
        return response["containerId"], "http://localhost" + accessport[1]
    except Exception:
        print("something happend ", traceback.print_exc())
        # return "roll back" # TODO roll back
        return None, None




# createbox("instantbox/ubuntu:14.04", "1", "512", "10002")