class Projeto:
    def __init__(self, nome, descricao, responsavel, status):
        self._id = ''
        self.nome = nome
        self.descricao = descricao
        self.responsavel = responsavel
        self.status = status

    def to_json(self):
        json_ = { 'nome':self.nome,
                  'descricao':self.descricao,
                  'responsavel':self.responsavel,
                  'status':self.status
                }
        if self._id != '':
            json_['_id']=self._id
        return json_
    
class ONG:
    def __init__(self, nome):
        self._id = ''
        self.nome = nome
        self.projetos=[]
    def buscar_projetos(self, tit):
        for proj in self.projetos_ong:
            posicao = proj.nome.upper().find(tit.upper())
            if posicao != -1:
                return proj
            else:
                return None
 
    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)

    def to_json(self):
        json_ = {'nome':self.nome,'projetos':[]}
        for projeto in self.projetos:
            json_['projetos'].append(projeto.to_json())
        if self._id != '':
            json_['_id'] = self._id
        return json_
    



