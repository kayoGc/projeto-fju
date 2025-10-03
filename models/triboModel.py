from pydantic import BaseModel

# composição da tribo
class Tribo(BaseModel):
    nome: str
    participantes: str