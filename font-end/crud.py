from classes import *
from api_client import *
from menus import *

def create_ong(token):
    ong = ONG('salve os bichos')
    projeto = Projeto('salve','todos animais','rafael','andamento')
    ong.adicionar_projeto(projeto)
    print(api_create(ong.to_json(),token))


def listar_projetos(projetos):
    for index,p in zip(range(len(projetos)),projetos):
        print(f'[{index}]: {p.nome}')
    

def listar_ongs():
    ongs = []
    api_data=api_read()
    for index, ong_ in zip(range(len(api_data)),api_data):
        ong = ONG(_id=ong_['_id'],nome=ong_['nome'])
        print(f'{index} : Nome: {ong_['nome']}')
        for p in ong_['projetos']:
            projeto = Projeto(p['_id'],p['nome'],p['descricao'],
                              p['responsavel'],p['status'])
            ong.adicionar_projeto(projeto)
            print(f'  Projeto ----> {p['nome']}')
        ongs.append(ong)
        print('\n')
    return ongs
    