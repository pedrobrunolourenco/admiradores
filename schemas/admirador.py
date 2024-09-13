from pydantic import BaseModel, Field
from typing import List, Optional
from model.admirador import Admirador

class AdmiradorAddSchema(BaseModel):
    """ Define como um novo admirador
    """
    nome: str 
    email: str
    idade: int
    cep: str
    endereco: str
    complemento: str
    bairro: str
    cidade: str
    uf: str
    notavelId: int

class AdmiradorUpdSchema(BaseModel):
    """ Define como um novo notavel
    """
    id: int
    nome: str 
    email: str
    idade: int
    cep: str
    endereco: str
    complemento: str
    bairro: str
    cidade: str
    uf: str
    notavelId: int

class RetornoAdmiradorSchema(BaseModel):
    """ Retorno de um novo notavel
    """
    id: int
    nome: str 
    email: str
    idade: int
    cep: str
    endereco: str
    complemento: str
    bairro: str
    cidade: str
    uf: str
    notavelId: int

class AdmiradorTotais(BaseModel):
    """ Define como uma listagem de Notaveis será apresentada
    """
    nome: str
    count: int

class AdmiradorTotaisIdade(BaseModel):
    """ Define como uma listagem de Notaveis será apresentada
    """
    idade: str
    count: int

class ListaAdmiradorTotaisIdade(BaseModel):
    """ Define como uma listagem de Notaveis será apresentada
    """
    notaveis:List[AdmiradorTotaisIdade]



class ListaAdmiradorTotais(BaseModel):
    """ Define como uma listagem de Notaveis será apresentada
    """
    notaveis:List[AdmiradorTotais]


class ListagemAdmiradoresSchema(BaseModel):
    """ Define como uma listagem de Notaveis será apresentada
    """
    notaveis:List[RetornoAdmiradorSchema]

class AdmiradorGetAllSchema(BaseModel):
    """ faz busca paginada
    """
    offset: Optional[str] = None
    limit: Optional[str] = None
    busca: Optional[str] = None


class AdmiradoresGetPorIdSchema(BaseModel):
    """ faz busca por Id
    """
    id: int

class AdmiradoresGetPorNomeSchema(BaseModel):
    """ faz busca por Id
    """
    nome: str
    offset: str
    limit: str

class RetornoRemoveSchema(BaseModel):
    """ Retorno de exclusão de admirador
    """
    sucesso: bool
    mensagem: str

def apresenta_admirador(sucesso: bool, admirador: Admirador):
    """ Retorna uma representação de um notável 
    """
    return {
        "sucesso": sucesso,
        "id": admirador.id,
        "nome": admirador.nome,
        "email": admirador.email,
        "idade": admirador.idade,
        "cep": admirador.cep,
        "endereco": admirador.endereco,
        "complemento": admirador.complemento,
        "bairro": admirador.bairro,
        "cidade": admirador.cidade,
        "uf": admirador.uf,
        "notavelId": admirador.notavelId
    }


def apresenta_admiradores(sucesso: bool, admiradores: List[Admirador], totalCount):
    """ Retorna uma representação de uma lista de admiradores
    """
    result = []
    for admirador in admiradores:
        result.append({
            "id": admirador.id,
            "nome": admirador.nome,
            "email": admirador.email,
            "idade": admirador.idade,
            "cep": admirador.cep,
            "endereco": admirador.endereco,
            "complemento": admirador.complemento,
            "bairro": admirador.bairro,
            "cidade": admirador.cidade,
            "uf": admirador.uf,
            "notavelId": admirador.notavelId
        })

    return { 
        "sucesso": sucesso,
        "data": result,
        "totalCount": totalCount
    }

def apresenta_remove(sucesso: bool, msg: str):
    """ Retorna retorno de exclusão de admirador
    """
    return {
        "sucesso": sucesso,
        "mensagem": msg
    }
