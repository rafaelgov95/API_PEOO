import requests
import json
import http.client
url = 'https://api.viana.dev/ongs'

def api_create(json_dict):
    json_= json.dumps(json_dict)
    print(json_)
    response = requests.post(url,json=json_,headers={'Content-type','application/json'})
    return response

def api_read():
    response = requests.get(url).json()
    return response

def api_update(ong):
    json_= json.dumps(ong)
    response = requests.put(url=url_api_rest).json()
    return response

def api_delete(id):
    response = requests.delete(url=url_api_rest).json()
    return response


