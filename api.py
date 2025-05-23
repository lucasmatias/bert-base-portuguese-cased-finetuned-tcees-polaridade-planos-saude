from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from gradio_client import Client

app = FastAPI(
    title="Classificação de Metas de Planos de Saúde",
    description="API que classifica metas de planos de saúde em positivas ou negativas.",
    version="1.0.0",
    openapi_url="/openapi.json",  # Mantém o JSON local da API
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc UI
    contact={
        "name": "Lucas Caetano",
        "url": "https://github.com/lucasmatias"
    },
    servers=[
        {"url": "https://bert-base-portuguese-cased-finetuned.onrender.com", "description": "Servidor de Produção"},
    ],
)


client = Client("lucasmatias1990/bert-base-portuguese-cased-finetuned-tcees-polaridade-planos-saude")

# Modelo da requisição
class MetaRequest(BaseModel):
    metas: List[str]

# Modelo da resposta
class MetaResponse(BaseModel):
    texto: str
    polaridade: str

# Endpoint da API
@app.post("/classificar-metas", response_model=List[MetaResponse], tags=["Classificação de Metas"])
async def classificar_metas(request: MetaRequest):

    dados = {
        "data": request.metas
    }

    resultados = client.predict(
        json_data=dados,
            api_name="/predict"
    )
    print(resultados)

    return resultados
