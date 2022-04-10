# Seu código aqui
from flask import request, current_app
from itsdangerous import Serializer
from app.models.salgado_model import SalgadoModel


# Função com a lógica da rota
def criar_salgado():
    data = request.get_json()

    salgado = SalgadoModel(**data)

    current_app.db.session.add(salgado)
    current_app.db.session.commit()


    return {
        "id": salgado.id,
        "nome": salgado.nome,
        "preco": salgado.preco,
    }


# Criar multiplos salgados
def criar_multiplos_salgados():
    data = request.get_json()

    salgados = [SalgadoModel(**salgado) for salgado in data["salgados"]]

    current_app.db.session.add_all(salgados)
    current_app.db.session.commit()


    return {
        "salgados": [
            {
                "id": salgado.id,
                "nome": salgado.nome,
                "preco": salgado.preco
            } for salgado in salgados
        ]
    }


# Consultas com SQLAlchemy
def pegar_salgados():
    salgados = (
        SalgadoModel
        .query
        .all()
    )

    serializer = [
        {
            "id": salgado.id,
            "nome": salgado.nome,
            "preco": salgado.preco
        } for salgado in salgados
    ]

    return {"salgados": serializer}

    # Seleção com filtro por Primary Key
def salgados_por_id(salgado_id):
    salgado = (
        SalgadoModel
        .query
        .get(salgado_id)
    )

    return {
        "id": salgado.id,
        "nome": salgado.nome,
        "preco": salgado.preco
    }

# Seleções com SQLAlchemy .first()
def primeiro_salgado():
    salgado = (
      SalgadoModel
      .query.first()
    )

    return {
      "id": salgado.id,
      "nome": salgado.nome,
      "preco": salgado.preco
    }

# .filter() / .filter_by()

def filtro(salgado_nome):
    salgado = (
      SalgadoModel
      .query
      .filter(SalgadoModel.nome==salgado_nome)
      .first()
    )

    return {
      "id": salgado.id,
      "nome": salgado.nome,
      "preco": salgado.preco
    }


# .filter_by()

def filtro(salgado_nome):
    salgado = (
      SalgadoModel
      .query
      .filter_by(nome=salgado_nome)
      .first()
    )

    return {
      "id": salgado.id,
      "nome": salgado.nome,
      "preco": salgado.preco
    }

# .one()


def atualizar_salgado(id):
    data = request.get_json()

    # Capturamos o objeto desejado a partir do id
    salgado = SalgadoModel.query.get(id)

    # Iteramos sobre as chaves e valores da nossa request
    # recebida, atualizando os atributos do objeto
    # capturado um a um.
    for key, value in data.items():
        setattr(salgado, key, value)
    
    
    current_app.db.session.add(salgado)
    current_app.db.session.commit()

    return {
        "id": salgado.id,
        "nome": salgado.nome,
        "preco": salgado.preco
    }

def deletar_salgado(id):
