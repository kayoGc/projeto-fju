from firebase_admin import db
from models.jovensModel import Jovem

jovensRef = db.reference("/jovens")

class JovemController:
    def get():
        return jovensRef.get()

    def post(jovem: Jovem):
        jovensRef.push({"nome": jovem.nome, "tribo": jovem.tribo})
        return {"message": "Boa garotooo"}