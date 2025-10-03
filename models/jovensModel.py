from pydantic import BaseModel

class Jovem(BaseModel):
    nome: str
    tribo: str