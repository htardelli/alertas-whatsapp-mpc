from WPP_Whatsapp import connect

client = connect()
client.start()

# Mantém o processo rodando indefinidamente
import time
while True:
    time.sleep(60)
