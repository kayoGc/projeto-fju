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
from models.triboModel import RequestPostTribo, RequestPutTribo
from models.jovensModel import RequestPostJovem, RequestPutJovem
from models.usuariosModel import RequestPostUsuario, RequestPutUsuario
from models.authModel import RequestPostAuth

# controllers
from controllers.triboController import TriboController
tribo = TriboController

from controllers.jovemController import JovemController
jovem = JovemController

from controllers.usuarioController import UsuarioController
usuario = UsuarioController

from controllers.authController import AuthController
auth = AuthController


# ---------------------------------------------------------------------
# rota raiz

@app.get("/")
def raiz():
    return { "messagem": "Servidor está funcionando" }

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# rotas tribos

# GET
@app.get("/api/tribos")
def pegarTribos():
    return tribo.ler()

@app.get("/api/tribos/{id}")
def pegarTriboPorId(id: str):
    return tribo.lerPorId(id)

# POST
@app.post("/api/tribos")
def colocarTribo(corpoTribo: RequestPostTribo):    
    return tribo.criar(corpoTribo)

# PUT /api/tribos/codigo_tribo_1
@app.put("/api/tribos/{id}")
def atualizarTribo(id: str, corpoTribo: RequestPutTribo):
    return tribo.atualizar(id, corpoTribo)

# DELETE
@app.delete("/api/tribos/{id}")
def deletarTribo(id: str):    
    return tribo.deletar(id)

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# rotas jovens

# GET
@app.get("/api/jovens")
def pegarJovens():
    return jovem.ler()

@app.get("/api/jovens/{id}")
def pegarJovemPorId(id: str):
    return jovem.lerPorId(id)

# POST
@app.post("/api/jovens")
def colocarJovem(corpoJovem: RequestPostJovem):    
    return jovem.criar(corpoJovem)

# PUT /api/jovens/codigo_tribo_1
@app.put("/api/jovens/{id}")
def atualizarJovem(id: str, corpoJovem: RequestPutJovem):
    return jovem.atualizar(id, corpoJovem)

# DELETE
@app.delete("/api/jovens/{id}")
def deletarJovem(id: str):    
    return jovem.deletar(id)

# ---------------------------------------------------------------------

# --------------------------------------------------
# rotas usuarios

# GET
@app.get("/api/usuarios")
def pegarUsuarios():
    return usuario.ler()

@app.get("/api/usuarios/{id}")
def pegarUsuariosPorId(id: str):
    return usuario.lerPorId(id)

# POST
@app.post("/api/usuarios")
def colocarUsuarios(corpoUsuarios: RequestPostUsuario):
    return usuario.criar(corpoUsuarios)

# PUT /api/usuarios
@app.put("/api/usuarios/{id}")
def atualizarUsuarios(id: str, corpoUsuarios: RequestPutUsuario):
    return usuario.atualizar(id, corpoUsuarios)

# DELETE
@app.delete("/api/usuarios/{id}")
def deletarUsuarios(id: str):
    return usuario.deletar(id)

# --------------------------------------------------


# --------------------------------------------------
# rotas auth (autenticação)

# POST
@app.post("/api/auth")
def criarUsuario(dados: RequestPostAuth):
    return auth.criar(dados)

# --------------------------------------------------