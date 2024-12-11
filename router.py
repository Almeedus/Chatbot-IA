from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import redis_db
from model import qa_chain
import json

# Inicializar FastAPI
app = FastAPI()

# Modelo de entrada
class QueryRequest(BaseModel):
    query: str

# Endpoint para responder perguntas
@app.post("/duvidas")
async def answer_query(request: QueryRequest):
    try:
        # Executar a query no chain
        response = qa_chain.run(request.query)

        # Salvar a pergunta e a resposta no Redis
        data = {"query": request.query, "response": response}
        redis_db.rpush("queries_responses", json.dumps(data))  # Adiciona ao final da lista

        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint de teste
@app.get("/")
async def root():
    return {"message": "API Funcionando!"}
