from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from gradio_client import Client

app = FastAPI()
client = Client("lucasmatias1990/bert-base-portuguese-cased-finetuned-tcees-polaridade-planos-saude")

# Modelo da requisição
class MetaRequest(BaseModel):
    metas: List[str]

# Modelo da resposta
class MetaResponse(BaseModel):
    texto: str
    polaridade: str

# Simulação de classificação das metas
def classificar_polaridade(meta):
    palavras_positivas = ["aumentar", "melhorar", "expandir"]
    palavras_negativas = ["diminuir", "reduzir", "limitar"]

    for palavra in palavras_positivas:
        if palavra in meta.lower():
            return "positiva"
    
    for palavra in palavras_negativas:
        if palavra in meta.lower():
            return "negativa"

    return "neutra"

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
