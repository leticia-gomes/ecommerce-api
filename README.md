
# 🐍 FastAPI + PostgreSQL + Docker + Render

Este projeto é uma **API RESTful** em **Python** desenvolvida com **FastAPI**, **PostgreSQL**, **SQLModel** e **Docker**, e está configurado para **deploy automático no Render**.

Foi desenvolvida para um webinar, ministrado por mim, para os alunos de ADS Ead da Toledo Prudente Centro Universitário na disciplina de Desenvolvimento de APIs e Microsserviços.

---

## 🚀 Tecnologias utilizadas

- **FastAPI**    – Framework moderno e performático para criação de APIs Python.
- **PostgreSQL** – Banco de dados relacional robusto.
- **SQLModel**   – ORM para integração com o banco.
- **Docker**     – Containerização e orquestração do ambiente.
- **Render**     – Hospedagem da aplicação e banco de dados em nuvem.
- **Uvicorn**    – Servidor ASGI rápido e leve.

---

## 📂 Estrutura do projeto

```
ecommerce-api/
├── app/
│   ├── main.py                   # Ponto de entrada da API
│   ├── database.py               # Conexão com o banco de dados PostgreSQL
│   ├── models.py                 # Modelos das tabelas (SQLModel)
│   ├── schemas.py                # Validações e contratos de dados (Pydantic)
│   ├── routers/
│   │   └── produto.py           # Rotas da API (CRUD de produto)
│
├── Dockerfile                    # Configuração para container Docker
├── .gitignore                    # Arquivos ignorados pelo Git
├── requirements.txt              # Dependências do projeto
├── render.yaml                   # Configuração de deploy no Render
├── .env                          # Variáveis de ambiente (não versionar!)
└── README.md                     # Este arquivo
```

---

## ⚙️ Como executar o projeto localmente

### 🔧 Pré-requisitos

- Python 3.10+
- PostgreSQL (caso queira rodar sem Docker)

### 📦 Clonar o repositório

```bash
git clone https://github.com/leticia-gomes/ecommerce-api.git
cd ecommerce-api
```

### 🔨 Criar o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # (Linux/Mac)
.venv\Scripts\activate     # (Windows)
```

### 📥 Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 🦄 Rodando o Projeto (usando Uvicorn)

```bash
uvicorn app.main:app --reload
```

A aplicação estará disponível em:
👉 **http://127.0.0.1:8000/**

---

## 🧭 Testando a API

Acesse a documentação interativa gerada automaticamente pelo FastAPI:

- **Swagger UI** → http://127.0.0.1:8000/docs  
- **ReDoc** → http://127.0.0.1:8000/redoc

---

## ☁️ Deploy no Render

1. Faça login no [Render](https://render.com)
2. Crie um novo serviço **Web Service**
3. Conecte seu repositório GitHub
4. Configure as variáveis de ambiente:
   ```env
   DATABASE_URL=postgresql+psycopg2://usuario:senha@host:port/dbname
   ```
5. Defina o comando de inicialização:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 10000
   ```
6. Deploy automático será configurado a cada novo commit.

---

## 🧩 Exemplo de endpoint

### **GET /api/produto**

Retorna todas os produtos cadastrados.

**Exemplo de resposta:**
```json
[
  {
    "id": 1,
    "nome": "Violino",
    "descricao": ""
  },
  {
    "id": 2,
    "nome": "Violão",
    "descricao": ""
  }
]
```

### **POST /api/produto**

Cadastra um novo produto.

```json
{
  "nome": "Guitarra",
  "descricao": ""
}
```

---

## 🛠️ Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql+psycopg2://usuario:senha@db:5432/fastapi_db
SECRET_KEY=sua_chave_secreta
DEBUG=True
```

---

## 👩‍💻 Autora

**Letícia Gomes Ribeiro**  
💻 Professora Universitária & Desenvolvedora Full Stack  
🔗 [LinkedIn](https://www.linkedin.com/in/leticia-gomes-ribeiro)

---

## 🪪 Licença

Este projeto está sob a licença **MIT** – sinta-se livre para usar e modificar.

---
