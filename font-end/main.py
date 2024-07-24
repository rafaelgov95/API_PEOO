from menus import *
from crud import *
from login import *

def fluxo_principal():
    close = True
    while close:        
        print(menu_principal())
        op = input("Escolha uma opção: ")
        if op == '1': 
            jwt = login()
            token = jwt
            if token != None:
               fluxo_logado(token)
        elif op == '2':
            create_login()
        elif op == '3':
            listar_ongs()
            menu_ong()
        elif op == '0':
            close=False
        else:
            print("Opção Inválida")

def fluxo_logado(token):
    close = True
    print(menu_principal(True))
    while close:        
        op = input("Escolha uma opção: ")
        if op == '1': 
           listar_ongs()
           print(menu_principal(True,False))
        elif op == '2': 
           create_ong(token)
        elif op == '3': 
           editar_ong(token)
        elif op == '4': 
           excluir_ong(token)
        elif op == '0': 
           close = False
        else:
            print("Opção Inválida")

fluxo_principal()
