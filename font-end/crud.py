from classes import *
from api_client import *


def create_ong(token):
    ong = ONG('salve os bichos')
    projeto = Projeto('salve','todos animais','rafael','andamento')
    ong.adicionar_projeto(projeto)
    print(api_create(ong.to_json(),token))


def editar_ong(ong:ONG,token):
    print(ong.getNome())
    ong.setNome(input("Digite novo nome: "))
    print(ong.to_json())

    result = api_update(ong,token)
    print(result.content)
    print(f'Novo Nome: {ong.getNome()}')

def excluir_ong(ong:ONG,token):
    print(ong.to_json())
    api_delete(ong._id,token)

def listar_ongs():
    ongs = []
    api_data=api_read()
    for index, ong_ in zip(range(len(api_data)),api_data):
        ong = ONG(_id=ong_['_id'],nome=ong_['nome'])
        print(f'{index} : Nome: {ong_['nome']}')
        for p in ong_['projetos']:
            print(p)
            projeto = Projeto(p['_id'],p['nome'],p['descricao'],
                              p['responsavel'],p['status'])
            ong.adicionar_projeto(projeto)
            print(f'  Projeto ----> {p['nome']}')
        ongs.append(ong)
        print('\n')
    return ongs
    