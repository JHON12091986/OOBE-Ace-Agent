import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACE_API_KEY = os.getenv("ACE_API_KEY")
ACE_API_URL = "https://api.acedata.cloud/v1/chat/completions"

def research_market(token_name):
    print(f"[*] Investigando {token_name} usando Ace Data Cloud...")
    
    if not ACE_API_KEY or ACE_API_KEY == "tu_api_key_aqui":
        print("[-] ERROR: No has configurado tu ACE_API_KEY en el archivo .env")
        return False

    headers = {
        "Authorization": f"Bearer {ACE_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": f"Dame un resumen corto de las noticias más recientes sobre {token_name} en el mercado cripto."}
        ],
        "max_tokens": 200
    }

    try:
        response = requests.post(ACE_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            analysis = data['choices'][0]['message']['content']
            print(f"[+] Análisis de Ace Data Cloud:\n{analysis}")
            return True
        else:
            print(f"[-] Error en la API: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"[-] Error de conexión: {e}")
        return False

def execute_trade(token_name):
    print(f"\n[*] (Simulación OOBE) Conectando con Steve Capital para operar {token_name}...")
    print(f"[+] ¡Éxito! El agente ha decidido comprar {token_name} basado en el análisis.")
    print("[!] Recuerda hacer el post en X para reclamar el premio del track de Ace.")

if __name__ == "__main__":
    print("🦈 Iniciando Agente de Capital (Track: Ace Data Cloud) 🦈\n")
    
    # 1. Investigar el mercado usando la IA de Ace
    market_is_good = research_market("Solana")
    
    # 2. Si el análisis es exitoso, ejecutar la acción
    if market_is_good:
        execute_trade("SOL")