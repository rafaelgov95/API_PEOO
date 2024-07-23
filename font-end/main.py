from operacoes import *
from menus import *

def create_user_login():
    nome='rafael.viana'
    senha='12345'
    json_= {'nome':nome,'senha':senha}
    print(api_create_login(json_))

def login():
    nome='rafael.viana'
    senha='12345'
    json_= {'nome':nome,'senha':senha}
    response = api_login(json_)
    print( response.content)


token = {'x-auth-token':''}
close = True
while close:
    ongs = api_read()
    print(menu_principal())
    print('Token: ',token['x-auth-token'])
    op = input("Escolha uma opção: ")
    if op == '1': 
        jwt=login()
        token['x-auth-token']=jwt
    elif op == '2':
        create_user_login()
    elif op == '3':
        listar_ongs(ongs)
        menu_ong()
    elif op == '0':
        close=False
    else:
        print("Opção Inválida")