from pydantic import BaseModel
from firebase_admin import db
from typing import Optional

class RequestPostJovem(BaseModel):
    '''
    Essa classe é o modelo de como os dados devem ser mandados no POST
    '''
    nome: str
    idTribo: str
    idUsuario: str

class RequestPutJovem(BaseModel):
    '''
    Essa classe é o modelo de como os dados devem ser mandados PUT
    '''
    nome: Optional[str] = None
    idTribo: Optional[str] = None
    idUsuario: Optional[str] = None

referencia = db.reference('/jovens')

class FirebaseJovem:
    
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
        
    def criar(self, jovem: RequestPostJovem):
        '''
        Vamos criar dados no banco de dados aqui
        '''
        
        novaReferencia = referencia.push({ 
            "nome": jovem.nome,
            "id_tribo": jovem.idTribo,
            "id_usuario": jovem.idUsuario 
        })
        
        return novaReferencia.key
    
    def atualizar(self, id, jovem):
        '''
        Vamos atualizar os dados que já estão no banco de dados
        '''
        refFilho = referencia.child(id)
        refFilho.update(jovem)
    
    def deletar(self, id):
        '''
        Apagar os dados no banco de dados
        '''
        refFilho = referencia.child(id)
        refFilho.delete()