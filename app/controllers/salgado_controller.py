# Seu código aqui
from flask import request, current_app
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