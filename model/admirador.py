from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from typing import Union

from  model import Base

class Admirador(Base):
    __tablename__ = 'notavel'

    id = Column("pk_admirador", Integer, primary_key=True)
    nome = Column(String(80))
    email = Column(String(80))
    idade = Column(Integer)
    cep = Column(String(8))
    endereco = Column(String(80))
    complemento = Column(String(30))
    bairro = Column(String(50))
    cidade = Column(String(50))
    uf = Column(String(2))
    notavelId = Column(Integer)



    def __init__(self, nome:str, email:str, idade:Integer, cep:str, endereco:str, complemento:str, bairro:str, cidade:str, uf:str, notavelId:Integer):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.cep = cep
        self.endereco = endereco
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.notavelId = notavelId




