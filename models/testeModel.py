from pydantic import BaseModel
from firebase_admin import db
from typing import Optional

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
        
    def criar(self, tribo):
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