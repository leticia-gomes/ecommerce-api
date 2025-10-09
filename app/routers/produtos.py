from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.models import Produto
from app.schemas import ProdutoCreate, ProdutoRead
from app.database import get_session

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.post("/", response_model=ProdutoRead, status_code=status.HTTP_201_CREATED)
def criar_produto(produto: ProdutoCreate, session: Session = Depends(get_session)):
    novo_produto = Produto.from_orm(produto)
    session.add(novo_produto)
    session.commit()
    session.refresh(novo_produto)
    return novo_produto

@router.get("/", response_model=list[ProdutoRead])
def listar_produtos(session: Session = Depends(get_session)):
    produtos = session.exec(select(Produto)).all()
    return produtos

@router.get("/{id}", response_model=ProdutoRead)
def obter_produto(id: int, session: Session = Depends(get_session)):
    produto = session.get(Produto, id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.delete("/{id}")
def deletar_produto(id: int, session: Session = Depends(get_session)):
    produto = session.get(Produto, id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    session.delete(produto)
    session.commit()
    return {"mensagem": "Produto removido com sucesso!"}
