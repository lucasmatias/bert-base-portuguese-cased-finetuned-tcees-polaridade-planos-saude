from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from gradio_client import Client

app = FastAPI(
    title="API para Classificação de Metas de Planos de Saúde",  # Novo título
    description="API que classifica metas de planos de saúde quanto a polaridade 'quanto maior, melhor'(positivas) ou 'quanto menor, melhor'(negativas)",  # Nova descrição
    version="1.0.0",
    contact={
        "name": "Lucas Caetano",
        "url": "https://github.com/lucasmatias"
    }    
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
