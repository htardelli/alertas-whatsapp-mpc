from wpp_cliente import connect

def enviar_alerta(mensagem: str):
    try:
        creator = Create(session="milhaspracasal", headless=True)
        client = creator.start()

        grupo_id = "120363167795908941@g.us"
        client.sendText(grupo_id, mensagem)
        return "Mensagem enviada com sucesso"
    except Exception as e:
        return f"Erro ao enviar: {str(e)}"
