from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from gradio_client import Client

app = FastAPI(
    title="Classificação de Metas de Planos de Saúde",
    description="API que classifica metas de planos de saúde em positivas ou negativas.",
    version="1.0.0",
    openapi_url="https://digisusgmp.saude.gov.br/v1.5/docs/api-docs.json",  # Altera a URL do JSON OpenAPI
    contact={
        "name": "Lucas Caetano",
        "url": "https://github.com/lucasmatias"
    },
    openapi_tags=[
        {"name": "Classificação Metas", "description": "Operações relacionadas à classificação de metas"}
    ],    
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
@app.post("/classificar-metas", response_model=List[MetaResponse])
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
