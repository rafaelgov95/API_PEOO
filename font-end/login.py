from api_client import *

def create_login():
    nome='rafael.viana'
    senha='12345'
    json_= {'nome':nome,'senha':senha}
    print(api_create_login(json_))


def login():
    nome='rafael.viana'
    senha='12345'
    json_= {'nome':nome,'senha':senha}
    response = api_login(json_)
    return json.loads(response.content)['token']


