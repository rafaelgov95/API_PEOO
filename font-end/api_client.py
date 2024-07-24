import requests
import json

url = 'https://api.viana.dev/'

def api_create_login(json_dict):
    json_= json.dumps(json_dict)
    print(json_)
    headers = {'Content-type': 'application/json'}
    response = requests.post(f'{url}/register',data=json_,headers=headers)
    return response

def api_login(json_dict):
    json_= json.dumps(json_dict)
    headers = {'Content-type': 'application/json'}
    response = requests.post(f'{url}/login',data=json_,headers=headers)
    return response

def api_create(json_dict,token):
    json_= json.dumps(json_dict)
    headers = {'Content-type': 'application/json',
               'x-auth-token':token}
    response = requests.post(f'{url}/ongs',data=json_,headers=headers)
    print(response.content)
    return response

def api_read():
    headers = {'Content-type': 'application/json'}
    response = requests.get(f'{url}/ongs',headers=headers).json()
    return response

def api_update(ong,token):
    json_= json.dumps(ong.to_json())
    headers = {'Content-type': 'application/json',
               'x-auth-token':token}
    response = requests.put(f'{url}/ongs/{ong.getId()}',data=json_,headers=headers)
    return response

def api_delete(id,token):
    headers = {'Content-type': 'application/json',
               'x-auth-token':token}
    response = requests.delete(f'{url}/ongs/{id}',headers=headers)
    print(response.content)
    return response
