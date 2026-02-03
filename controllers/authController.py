from models.authModel import RequestPostAuth, FirebaseAuth
from fastapi import HTTPException

modelo = FirebaseAuth()
    
class AuthController:
    '''
    Controla o que acontece nas requisições
    '''
    
    def criar(dados: RequestPostAuth):
        uid = modelo.criarConta(dados)

        return { "resultado": "Conta criada com sucesso!", "uid": uid }