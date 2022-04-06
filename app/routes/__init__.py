# Seu código aqui
from app.routes.salgado_blueprint import bp_salgado
from flask import Flask

def init_app(app: Flask):
    app.register_blueprint(bp_salgado)
    