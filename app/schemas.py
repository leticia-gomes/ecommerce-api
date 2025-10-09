from pydantic import BaseModel
from typing import Optional

class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    descricao: Optional[str] = None

class ProdutoRead(ProdutoCreate):
    id: int

    class Config:
        orm_mode = True
