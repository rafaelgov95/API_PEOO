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
    while close:       
        print(menu_principal(True))
        op = input("Escolha uma opção: ")
        if op == '1': 
           ongs = listar_ongs()
           index_ong = int(input("Informe [index]:"))
           fluxo_ong(ongs[index_ong],token)
        elif op == '2':            
           create_ong(token)
        elif op == '0': 
           close = False
        else:
            print("Opção Inválida")


def fluxo_ong(ong:ONG, token):
    close = True
    while close: 
        print(menu_ong())
        op = input("Escolha uma opção: ")
        if op == '1': 
           editar_ong(ong,token)
        elif op == '2': 
           excluir_ong(ong,token)
        elif op == '0': 
           close = False
        else:
            print("Opção Inválida")


fluxo_principal()
