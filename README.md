# Classificação de Metas de Planos de Saúde

Esta é uma API desenvolvida com FastAPI para classificar metas de planos de saúde em positivas ou negativas. A API utiliza um modelo de aprendizado de máquina treinado para essa tarefa.

## Tecnologias Utilizadas

- Python 3
- FastAPI
- Pydantic
- Gradio Client

## Como Executar

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale as dependências:
   ```sh
   pip install fastapi uvicorn gradio_client pydantic
   ```

3. Inicie o servidor:
   ```sh
   uvicorn main:app --reload
   ```

4. Acesse a documentação interativa da API:
   - Swagger UI: [https://bert-base-portuguese-cased-finetuned.onrender.com/docs](https://bert-base-portuguese-cased-finetuned.onrender.com/docs)

## Uso da API

### Endpoint `/classificar-metas`

**Método:** `POST`  
**Descrição:** Classifica uma lista de metas de planos de saúde em positivas ou negativas.

**Requisição:**

```json
{
  "metas": [
    "Redução da taxa de mortalidade infantil",
    "Realizar exame de rastreamento do câncer de mama, no mínimo, de 50% da população alvo feminina de 50 a 69 anos anualmente"
  ]
}
```

**Resposta:**

```json
[
  {
    "texto": "Redução da taxa de mortalidade infantil",
    "polaridade": "Negativa"
  },
  {
    "texto": "Realizar exame de rastreamento do câncer de mama, no mínimo, de 50% da população alvo feminina de 50 a 69 anos anualmente",
    "polaridade": "Positiva"
  }
]
```


