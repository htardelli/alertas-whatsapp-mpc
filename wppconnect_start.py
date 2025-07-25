from wppconnect import enviar_alerta

if __name__ == "__main__":
    mensagem = "🚨 Teste de envio automático via WPPConnect"
    print(enviar_alerta(mensagem))

