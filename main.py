'''
MVC

model - modelo
controller - controlador
view - telas
'''
from typing import Union
from fastapi import FastAPI
from config.db import config

# configura o banco
config()

# fastapi
app = FastAPI()

# modelos
from models.triboModel import Tribo

# controllers
from controllers.triboController import TriboController
tribo = TriboController

from controllers.jovemController import JovemController
jovem = JovemController

# views
# rotas - routes
@app.get("/")
def raiz():
    return { "messagem": "Servidor está funcionando" }

# vai devolver todas as tribos que estão no banco de dados
@app.get("/api/tribos")
def pegarTribos():
    return tribo.get()

@app.post("/api/tribos")
def colocarTribo(corpoTribo: Tribo):
    return tribo.post(corpoTribo)

@app.get("/api/jovens")
def pegarJovens():
    return jovem.get()