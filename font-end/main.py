from operacoes import *
from menus import *


close = True
while close:
    ongs = api_read()
    print(menu_principal())
    op = input("Escolha uma opção: ")
    if op == '1': 
        create_ong()
    elif op == '2':
        listar_ongs(ongs)
        menu_ong()
    elif op == '0':
        close=False
    else:
        print("Opção Inválida")