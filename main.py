from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API online"}

@app.post("/enviar-alerta")
async def enviar_alerta(request: Request):
    data = await request.json()
    mensagem = data.get("mensagem", "⚠️ Alerta sem conteúdo.")

    # Exemplo de payload para WPPConnect
    payload = {
        "phone": "120363167795908941@g.us",
        "message": mensagem
    }

    # Endpoint da sua instância do WPPConnect
    wpp_url = "http://localhost:21465/api/send-message"

    response = requests.post(wpp_url, json=payload)
    return {"status": "enviado", "resposta": response.json()}
