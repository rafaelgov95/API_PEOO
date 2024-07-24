from classes import *
from api_client import *


def create_ong(token):
    ong = ONG('salve os bichos')
    projeto = Projeto('salve','todos animais','rafael','andamento')
    ong.adicionar_projeto(projeto)
    print(api_create(ong.to_json(),token))


def editar_ong(token):
   pass

def excluir_ong(token):
  pass

def listar_ongs():
    ongs = api_read()
    for ong in ongs:
        print(f'Nome: {ong['nome']}')
        for p in ong['projetos']:
            print(f'  Projeto ----> {p['nome']}')
        print('\n')