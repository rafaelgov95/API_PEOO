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
            fluxo_editar_ong(ong)
        elif op == '2': 
            fluxo_projeto(ong)
        elif op == '3': 
            api_update(ong,token)
        elif op == '4': 
            confirma = input("1-SIM/2-NÃO")
            if confirma == '1':
                api_delete(ong,token)
            elif confirma == '2':
                pass
        elif op == '0': 
           close = False
        else:
            print("Opção Inválida")



def fluxo_editar_ong(ong:ONG):
    close = True
    while close: 
        print(ong.getNome())
        ong.setNome(input("Digite novo nome: "))
        print(ong.to_json())
        close=False
    

def fluxo_projeto(ong:ONG):
    close = True
    while close: 
        projetos=ong.getProjetos()
        listar_projetos(projetos)
        print("-1 - Sair")
        op = int(input("Digite [index]:"))
        if op > -1 and op < len(projetos):
            print(projetos[op].getNome())
            fluxo_editar_projeto(projetos[op])
        elif op == -1:
             close=False
        else:
            print("Index Inválido")



def fluxo_editar_projeto(projeto:Projeto):
    close = True
    while close: 
        print(projeto.to_json())
        print(menu_editar_projeto())
        op = input("opção: ")
        if op == '1':
            projeto.setNome(input("Digite novo nome: "))
        elif op == '2':
            projeto.setDescricao(input("Digite novo Descricão: "))
        elif op == '3':
            projeto.setResposavel(input("Digite novo Responsavel: "))
        elif op == '4':
            projeto.setStatus(input("Digite novo Status: "))
        elif op == '0':
            close=False
        else:
            print("Opção Inválida")


fluxo_principal()
