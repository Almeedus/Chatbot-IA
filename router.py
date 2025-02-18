from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from config import redis_db
from model import qa_chain
import json

# Inicializar FastAPI
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (ajuste conforme necessário)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Modelo de entrada
class QueryRequest(BaseModel):
    query: str

# Endpoint para responder perguntas
@app.post("/duvidas")
async def answer_query(request: QueryRequest):
    try:
        # Executar a query no chain
        print("Recebido:", request) 
        response = qa_chain.invoke(request.query)


        # Salvar a pergunta e a resposta no Redis
        data = {"query": request.query, "response": response}
        redis_db.rpush("queries_responses", json.dumps(data))  # Adiciona ao final da lista

        return data
    except Exception as e:
        print("Erro no Backend:", str(e))  # 🔹 Exibe o erro no terminal
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint de teste
@app.get("/")
async def root():
    return {"message": "API Funcionando!"}
