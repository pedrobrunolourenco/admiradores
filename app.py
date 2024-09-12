from venv import logger
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from model.admirador import Admirador
from schemas.admirador import AdmiradorAddSchema, AdmiradorGetAllSchema, AdmiradorUpdSchema, AdmiradoresGetPorIdSchema, AdmiradoresGetPorNomeSchema, ListagemAdmiradoresSchema, RetornoAdmiradorSchema, RetornoRemoveSchema, apresenta_admirador, apresenta_admiradores, apresenta_remove
from schemas.error import ErrorSchema
from model import Session
from flask_cors import CORS
from sqlalchemy import update
from sqlalchemy.orm import aliased

info = Info(title="API Admiradores - Sprint-03", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

admirador_tag = Tag(name="Admirador", description="Adição, Edição, visualização e remoção de ADMIRADORES à base")

@app.get('/')
def home():
    return redirect('/openapi')

@app.post('/create', tags=[admirador_tag],
          responses={"200": RetornoAdmiradorSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_admirador(body: AdmiradorAddSchema):
    """Adiciona um novo notavel à base de dados"""
    admirador = Admirador(
        nome=body.nome,
        email=body.email,
        idade=body.idade,
        cep=body.cep,
        endereco=body.endereco,
        complemento=body.complemento,
        bairro=body.bairro,
        cidade=body.cidade,
        uf=body.uf,
        notavelId=body.notavelId
    )

    logger.debug(f"Adicionando um admirador à base: '{admirador.nome}'")
    try:
        session = Session()
        session.add(admirador)
        session.commit()
        return apresenta_admirador(True, admirador), 200
    except Exception as e:
        error_msg = "Não foi possível salvar o novo admirador :/"
        logger.warning(f"Erro ao adicionar um notável '{admirador.nome}', {error_msg}, erro: {e}")
        return {"sucesso": False, "message": error_msg}, 400

@app.get('/getall', tags=[admirador_tag],
          responses={"200": ListagemAdmiradoresSchema, "409": ErrorSchema, "400": ErrorSchema})
def get_adimiradores(query: AdmiradorGetAllSchema):
    """Obtém uma lista de admiradores"""
    try:
        limit = query.limit
        offset = query.offset
        busca = query.busca
        session = Session()
        if busca is None or busca.strip() == "":
           totalCount = session.query(Admirador).count()
           notaveis = session.query(Admirador).limit(limit).offset(offset).all()
        else:
           totalCount = session.query(Admirador).filter(Admirador.nome.ilike(f"%{busca}%")).count()
           notaveis = session.query(Admirador).filter(Admirador.nome.ilike(f"%{busca}%")).limit(limit).offset(offset).all()
        return apresenta_admiradores(True, notaveis, totalCount), 200
    except Exception as e:
        error_msg = "Não foi possível obter listagem de admiradores :/"
        logger.warning(f"Erro ao listar admiradores {error_msg}, erro: {e}")
        return {"sucesso": False, "message": error_msg}, 400

    
@app.get('/getbyid', tags=[admirador_tag],
          responses={"200": ListagemAdmiradoresSchema, "409": ErrorSchema, "400": ErrorSchema})
def get_por_id(query: AdmiradoresGetPorIdSchema):
    """Obtém um admirador por Id"""
    try:
        session = Session()
        admirador = session.query(Admirador).filter(Admirador.id == query.id).first()
        return apresenta_admirador(True, admirador), 200
    except Exception as e:
        error_msg = "Não foi possível obter o admirador :/"
        logger.warning(f"Erro ao pesquiar o admirador {error_msg}, erro: {e}")
        return {"sucesso": False, "message": error_msg}, 400

@app.put('/update', tags=[admirador_tag],
          responses={"200": RetornoAdmiradorSchema, "409": ErrorSchema, "400": ErrorSchema})
def update_admirador(body: AdmiradorUpdSchema):
    """Altera os dados do admirador na base de dados"""
    logger.debug(f"alterando um admirador '{body.nome}'")
    try:
        session = Session()
        stmt = update(Admirador).where(Admirador.id == body.id).values(
            nome=body.nome,
            email=body.email,
            idade=body.idade,
            cep=body.cep,
            endereco=body.endereco,
            complemento=body.complemento,
            bairro=body.bairro,
            cidade=body.cidade,
            uf=body.uf,
            notavelId=body.notavelId
        )

        result = session.execute(stmt)
        # Verificar se alguma linha foi afetada pela query
        if result.rowcount > 0:
            session.commit()
            return apresenta_admirador(True,body), 200
        else:
            session.rollback()
            return {"sucesso": False, "message": f"O admirador com código {body.id} não foi localizado"}, 400
    except Exception as e:
        error_msg = "Não foi possível alterar o admirador :/"
        logger.warning(f"Erro ao alterar um admirador '{body.nome}', {error_msg}, erro: {e}")
        return {"sucesso": False, "message": error_msg}, 400

@app.delete('/removebyid', tags=[admirador_tag],
          responses={"200": RetornoRemoveSchema, "409": RetornoRemoveSchema, "400": RetornoRemoveSchema})
def remove_po_id(query: AdmiradoresGetPorIdSchema):
    """Remove um admirador por Id"""
    try:
        session = Session()
        count = session.query(Admirador).filter(Admirador.id == query.id).delete()
        session.commit()
        if count:
           return apresenta_remove(True, f"Admirador de código {query.id} excluído com sucesso "), 200
        else:
           return apresenta_remove(False, f"Admirador de código {query.id} não encontrado "), 200
            
    except Exception as e:
        error_msg =  f"Admirador de código {query.id} => Erro na exclusão {e}"
        logger.warning(f"Erro ao excluir o admirador {error_msg}, erro: {e}")
        return {"sucesso": False, "message": error_msg}, 400

