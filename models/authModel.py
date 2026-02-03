from pydantic import BaseModel
from firebase_admin import auth
from typing import Optional

class RequestPostAuth(BaseModel):
    '''
    Essa classe é o modelo de como os dados da auth devem ser mandados no POST
    '''  
    email: str
    senha: str

# class RequestPutAuth(BaseModel):
#     '''
#     Essa classe é o modelo de como os dados da auth devem ser mandados PUT
#     '''

class FirebaseAuth:

    '''
    cria conta do usuário
    '''
    def criarConta(self, dados: RequestPostAuth):
        # create_user retorna algumas informações da criação do usuário
        usuario = auth.create_user(
            email = dados.email,
            password = dados.senha
        )

        # uid é o codigo de identificação gerado pelo firebase
        return usuario.uid