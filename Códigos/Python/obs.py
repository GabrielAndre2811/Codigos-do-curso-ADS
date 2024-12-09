import time
from obswebsocket import obsws, requests

# Configurações do WebSocket
host = "localhost"
port = 4455  # Porta padrão do OBS WebSocket
password = "sua_senha"  # Defina a senha se necessário

def main():
    ws = obsws(host, port, password)
    
    try:
        # Conecta ao OBS
        ws.connect()
        print("Conectado ao OBS.")
        
        # Espera um pouco para garantir que o OBS esteja pronto
        time.sleep(2)

        # Ativar a câmera virtual
        ws.call(requests.SetVirtualCamEnabled(True))
        print("Câmera virtual ativada.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
    finally:
        ws.disconnect()
        print("Desconectado do OBS.")

if __name__ == "__main__":
    main()
