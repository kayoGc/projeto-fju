from pydantic import BaseModel
from firebase_admin import db
from typing import Optional

class RequestPostUsuario(BaseModel):
    nome: str
    funcao: str
    idTribo: str

class RequestPutUsuario(BaseModel):
    nome: Optional[str] = None
    funcao: Optional[str] = None
    idTribo: Optional[str] = None

referencia = db.reference('/usuarios')

class FirebaseUsuario:

    def ler(self):
        return referencia.get()
    
    def lerPorId(self, id):
        refFilho = referencia.child(id)
        return refFilho.get()
    
    def criar(self, usuario: RequestPostUsuario):
        novaReferencia = referencia.push({
            "nome": usuario.nome,
            "funcao": usuario.funcao,
            "idTribo": usuario.idTribo
        })
        return novaReferencia.key
    
    def atualizar(self, id, usuario):
        refFilho = referencia.child(id)
        refFilho.update(usuario)

    def deletar(self, id):
        refFilho = referencia.child(id)
        refFilho.delete()
