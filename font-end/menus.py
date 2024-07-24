from sys import platform
import os
def get_clear():
    if platform == "linux" or platform == "linux2":
        clear = lambda: os.system('clear')
    elif platform == "win32":
        clear = lambda: os.system('cls')
    return clear

clear = get_clear()

def menu_principal(logado=False,limpar=True):
    if limpar:
       clear()
    if logado == False:
        string = f"""
                        1 - Logar Usuário
                        2 - Registra Usuário
                        3 - Listar ONGs
                        0 - Sair
                 """
        return string

    else:
        string = f"""
                        1 - Listar ONGs
                        2 - Criar ONG
                        0 - Sair
                """
        return string


def menu_ong():
    string = f"""
               
                    1 - Editar ONG
                    2 - Editar Projetos ONG
                    3 - Save ONG
                    4 - Excluir ONG
                    0 - Sair

              """
    return string


def menu_editar_ong():
    clear()
    string = f"""
                    1 - Editar Nome
                    0 - Sair
              """
    return string


def menu_projeto():
    clear()
    string = f"""
                    1 - Editar Projeto
                    2 - Excluir Projeto
                    0 - Sair
              """
    return string

def menu_editar_projeto():
    clear()
    string = f"""
                    1 - Editar Nome
                    2 - Editar Descricao
                    3 - Editar Responsavel
                    4 - Editar Status
                    0 - Sair
              """
    return string
