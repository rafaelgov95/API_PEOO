import requests
import json
url = 'https://api.viana.dev/ongs'

def api_create(json_dict):
    json_= json.dumps(json_dict)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url,data=json_,headers=headers)
    return response

def api_read():
    headers = {'Content-type': 'application/json'}
    response = requests.get(url,headers=headers).json()
    return response

def api_update(ong):
    json_= json.dumps(ong)
    headers = {'Content-type': 'application/json'}
    response = requests.put(url,data=json_,headers=headers).json()
    return response

def api_delete(id):
    headers = {'Content-type': 'application/json'}
    response = requests.delete(f'{url}/{id}',headers=headers).json()
    return response


