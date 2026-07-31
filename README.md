# 🛒 E-commerce API

<div align="center">

API REST desenvolvida com **FastAPI**, **SQLModel** e **PostgreSQL**, criada como projeto prático do webinar de **Desenvolvimento de APIs e Microsserviços**.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-009688?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791?style=for-the-badge&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker)
![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?style=for-the-badge)

</div>

---

# 📖 Sobre o projeto

A **E-commerce API** é uma API REST desenvolvida para demonstrar a construção de aplicações backend modernas utilizando o ecossistema Python.

O projeto implementa operações de cadastro, consulta e remoção de produtos, utilizando o **SQLModel** como ORM para comunicação com um banco de dados **PostgreSQL**.

Além do desenvolvimento da API, o projeto demonstra práticas atuais de mercado, como containerização com Docker e publicação em ambiente de produção utilizando o Render.

---

# 🎓 Contexto acadêmico

Este projeto foi desenvolvido como material de apoio para um webinar da disciplina de **Desenvolvimento de APIs e Microsserviços**, do curso de **Análise e Desenvolvimento de Sistemas**.

Durante o webinar, os alunos acompanharam todas as etapas de criação de uma API REST utilizando **FastAPI**, desde a estruturação do projeto até sua integração com um banco de dados PostgreSQL, containerização com Docker e publicação em produção utilizando o Render.

O objetivo foi apresentar, de forma prática, tecnologias amplamente utilizadas no desenvolvimento de microsserviços e aplicações backend modernas.

---

# 🎯 Objetivos de aprendizagem

Ao longo do webinar foram abordados os seguintes conhecimentos:

## Desenvolvimento de APIs

- criação de APIs REST com FastAPI;
- organização de projetos backend;
- criação de endpoints;
- documentação automática utilizando Swagger e ReDoc;
- implementação das operações CRUD.

## Banco de dados

- integração com PostgreSQL;
- utilização do SQLModel como ORM;
- modelagem de entidades;
- persistência de dados.

## DevOps

- containerização utilizando Docker;
- configuração de variáveis de ambiente;
- deploy em ambiente de produção utilizando Render;
- integração com GitHub.

---

# ✨ Funcionalidades

- Cadastro de produtos
- Listagem de produtos
- Consulta por ID
- Exclusão de produtos
- Documentação automática da API
- Integração com PostgreSQL
- Deploy em produção

---

# 🏗 Arquitetura

```text
Cliente
      │
      ▼
 FastAPI
      │
      ▼
 Routers
      │
      ▼
 SQLModel
      │
      ▼
 PostgreSQL
```

---

# 📂 Estrutura do projeto

```text
ecommerce-api/

├── app/
│   ├── database/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   └── main.py
│
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

# 🔄 Fluxo da aplicação

```text
Cliente
      │
      ▼
Requisição HTTP
      │
      ▼
FastAPI
      │
      ▼
Router
      │
      ▼
SQLModel
      │
      ▼
PostgreSQL
      │
      ▼
Resposta JSON
```

---

# 🗄 Modelo de dados

A API possui atualmente a entidade **Produto**.

| Campo | Tipo |
|--------|------|
| id | Integer |
| nome | String |
| descricao | String |
| preco | Float |

---

# 🚀 Tecnologias

## Backend

- Python
- FastAPI
- SQLModel
- PostgreSQL
- Uvicorn

## DevOps

- Docker
- Docker Compose
- Render

## Ferramentas

- Swagger
- ReDoc
- Git
- GitHub

---

# ⚙ Como executar

## Pré-requisitos

- Python 3.13+
- PostgreSQL
- Docker (opcional)

---

## Clone o repositório

```bash
git clone https://github.com/leticia-gomes/fastapi-ecommerce-api.git
```

Entre na pasta:

```bash
cd ecommerce-api
```

---

## Crie o ambiente virtual

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux/macOS

```bash
python -m venv .venv

source .venv/bin/activate
```

---

## Instale as dependências

```bash
pip install -r requirements.txt
```

---

## Configure as variáveis de ambiente

Configure as informações de conexão com o PostgreSQL.

Exemplo:

```env
DATABASE_URL=postgresql://usuario:senha@localhost/ecommerce
```

---

## Execute a aplicação

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em:

```
http://localhost:8000
```

---

## Documentação

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# ☁ Deploy

O projeto foi preparado para execução em produção utilizando:

- Docker
- Render
- PostgreSQL

---

# 📚 Conceitos abordados

Durante o desenvolvimento deste projeto são explorados os seguintes conceitos:

- APIs REST
- FastAPI
- SQLModel
- ORM
- PostgreSQL
- CRUD
- Pydantic
- Docker
- Microsserviços
- Deploy
- Swagger
- ReDoc
- Versionamento com Git

---

# 🔮 Melhorias futuras

- Implementar atualização de produtos (PUT/PATCH)
- Autenticação JWT
- Controle de usuários
- Paginação
- Filtros
- Upload de imagens
- Testes unitários
- Testes de integração
- CI/CD com GitHub Actions
- Versionamento da API
- Logs estruturados
- Cache com Redis

---

# 👩‍🏫 Sobre o webinar

Este projeto foi desenvolvido como material de apoio para um webinar da disciplina de **Desenvolvimento de APIs e Microsserviços**.

Utilizando uma abordagem prática, os alunos acompanharam o desenvolvimento completo de uma API REST moderna, explorando desde a criação da estrutura do projeto até a publicação em ambiente de produção. Durante o webinar foram apresentados conceitos de arquitetura de APIs, integração com banco de dados, documentação automática, containerização com Docker e deploy utilizando o Render, aproximando os estudantes das práticas adotadas no mercado de desenvolvimento backend.

---

# 👩‍💻 Autora

**Letícia Gomes Ribeiro**

Desenvolvedora Full Stack • Professora Universitária

### Tecnologias

- Python
- FastAPI
- C#
- ASP.NET Core
- SQL Server
- React
- Angular
- Node.js

GitHub:

https://github.com/leticia-gomes

---

# ⭐ Apoie este projeto

Se este projeto foi útil para você, considere deixar uma ⭐ no repositório.
