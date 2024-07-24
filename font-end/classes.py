class Projeto:
    _id:str
    nome:str
    descricao:str
    responsavel:str
    status:str
    def __init__(self, _id=None,nome=None, descricao=None, responsavel=None, status=None):
        self._id = _id
        self.nome = nome
        self.descricao = descricao
        self.responsavel = responsavel
        self.status = status
        
    def setId(self,id):
       self._id=id
    
    def getId(self):
       return self._id
    
    def setNome(self,nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def setDescricao(self,descricao):
        self.descricao=descricao

    def getDescricao(self):
        return self.descricao
    
    def setResposavel(self,resposavel):
        self.responsavel=resposavel

    def getResposavel(self):
        return self.responsavel
    
    def setStatus(self,status):
        self.status = status

    def getStatus(self):
        return self.status
    
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
    _id:str
    nome:str
    projetos:list

    def __init__(self,_id, nome):
        self._id = _id
        self.nome = nome
        self.projetos=[]

    def setId(self,id):
       self._id=id
    
    def getId(self):
       return self._id
    
    def setNome(self,nome):
       self.nome=nome
    
    def getNome(self):
       return self.nome
    
    def getProjetos(self):
       return self.projetos
    
    def buscar_projetos(self, nome):
        for projeto in self.getProjetos():
            posicao = projeto.nome.upper().find(nome.upper())
            if posicao != -1:
                return projeto
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
    