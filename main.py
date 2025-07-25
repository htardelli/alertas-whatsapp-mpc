from fastapi import FastAPI, Request
from wppconnect import enviar_alerta

app = FastAPI()

@app.post("/enviar-alerta")
async def receber_alerta(request: Request):
    dados = await request.json()
    mensagem = dados.get("mensagem")
    if not mensagem:
        return {"erro": "Mensagem não enviada"}
    
    status = enviar_alerta(mensagem)
    return {"status": status}
