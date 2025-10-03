# controller da tribo
from firebase_admin import db
from models.triboModel import Tribo

ref = db.reference("/tribos")

class TriboController:
    
    def get():
        return ref.get()
    
    
    def post(tribo: Tribo):
        ref.push({"nome": tribo.nome, "participantes": tribo.participantes})
        return { "message": "Deu tudo certo" }