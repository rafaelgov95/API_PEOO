from classes import *
from api_client import *
from menus import *

def create_ong():
    print("entrou")
    ong = ONG('salve os bichos')
    projeto = Projeto('salve','todos animais','rafael','andamento')
    ong.adicionar_projeto(projeto)
    print(ong.to_json())
    print(api_create(ong.to_json()))

close = True
while close:
    print(menu_principal())
    op = input("Escolha uma opção: ")
    if op == '1': 
        menu_criar_ong()
        create_ong()
    elif op == '2': 
        menu_listar_ongs()
        print(api_read())
    elif op == '0':
        close=False
    else:
        print("Opção Inválida")