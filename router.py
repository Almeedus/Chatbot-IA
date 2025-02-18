from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from config import redis_db
from model import qa_chain
import json

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)


class QueryRequest(BaseModel):
    query: str

@app.post("/duvidas")
async def answer_query(request: QueryRequest):
    try:
        print("Recebido:", request) 
        response = qa_chain.invoke(request.query)


        data = {"query": request.query, "response": response}
        redis_db.rpush("queries_responses", json.dumps(data)) 

        return data
    except Exception as e:
        print("Erro no Backend:", str(e)) 
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "API Funcionando!"}
