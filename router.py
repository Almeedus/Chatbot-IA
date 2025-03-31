from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from config import redis_db
from model import qa_chain
import json
import os


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
    
@app.get("/")
async def root():
    return {"message": "API Funcionando!"}

@app.post("/duvidas")
async def answer_query(request: QueryRequest):
    try:
        response = qa_chain.invoke(request.query)


        data = {
            "messages": [
                {
                    "role": "system",
                    "content": "Você é um atendente do Instituto Federal de São Paulo do Campus de Itapetininga."
                },
                {
                    "role": "user",
                    "content": request.query
                },
                {
                    "role": "assistant",
                    "content": response["result"]
                }
            ]
        }
        redis_db.rpush("queries_responses", json.dumps(data)) 

        return data
    except Exception as e:
        print("Erro no Backend:", str(e)) 
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download")
async def download():
    data = redis_db.lrange("queries_responses", 0, -1)
    
    if data:
        decoded_data = [json.loads(item) for item in data]
        
        with open("ArquivoFineTuning.jsonl", "w", encoding="utf-8") as file:
            for index, item in enumerate(decoded_data):
                json.dump(item, file, ensure_ascii=False)
                if index < len(decoded_data) - 1:
                    file.write("\n")