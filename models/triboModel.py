from pydantic import BaseModel
from firebase_admin import db
from typing import Optional

class RequestPostTribo(BaseModel):
    '''
    Essa classe é o modelo de como os dados da tribo devem ser mandados no POST
    '''
    nome: str
    
    # participantes aceita uma lista ex:
    # [ codigo_do_usuario_1, codigo_do_usuario_2, codigo_do_usuario_3 ] 
    participantes: list[str]    

class RequestPutTribo(BaseModel):
    '''
    Essa classe é o modelo de como os dados da tribo devem ser mandados PUT
    '''
    nome: Optional[str] = None
    participantes: Optional[list[str]] = None    

referencia = db.reference('/tribos')

class FirebaseTribo:
    
    def ler(self):
        '''
        Vamos pegar os dados nessa função
        '''        
        return referencia.get()
    
    def lerPorId(self, id):
        '''
        Vamos pegar dados de apenas um filho
        '''
        refFilho = referencia.child(id)
        return refFilho.get()
        
    def criar(self, tribo: RequestPostTribo):
        '''
        Vamos criar dados no banco de dados aqui
        '''
        
        novaReferencia = referencia.push({ 
            "nome": tribo.nome, 
            "participantes": tribo.participantes, 
        })
        
        return novaReferencia.key
    
    def atualizar(self, id, tribo):
        '''
        Vamos atualizar os dados que já estão no banco de dados
        '''
        refFilho = referencia.child(id)
        refFilho.update(tribo)
    
    def deletar(self, id):
        '''
        Apagar os dados no banco de dados
        '''
        refFilho = referencia.child(id)
        refFilho.delete()