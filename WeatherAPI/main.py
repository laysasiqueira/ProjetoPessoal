from fastapi import FastAPI
import requests

app = FastAPI()

@app.get('/clima/{cidade}')
def clima(cidade: str):
    #faz o pedido à api externa
    resposta = requests.get(f"https://wttr.in/{cidade}?format=j1")
    #converte a resposta para json
    dados = resposta.json()
    #devolve os dados para quem pediu
    return dados