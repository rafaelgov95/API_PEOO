from classes import *
from api_client import *


def create_ong():
    ong = ONG('salve os bichos')
    projeto = Projeto('salve','todos animais','rafael','andamento')
    ong.adicionar_projeto(projeto)
    print(api_create(ong.to_json()))


def listar_ongs(ongs):
    for ong in ongs:
        print(f'Nome: {ong['nome']}')
        for p in ong['projetos']:
            print(f'  Projeto ----> {p['nome']}')
        print('\n')