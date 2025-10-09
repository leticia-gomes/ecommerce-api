from fastapi import FastAPI
from app.routers import produtos
from app.database import create_db_and_tables

app = FastAPI(title="API de Produtos - FastAPI + Render")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(produtos.router)

@app.get("/")
def home():
    return {"message": "API de Produtos - FastAPI + PostgreSQL no Render"}
