import streamlit as st
import requests

st.title("Previsão do Tempo 🌦️")

# 1. Caixa de texto para a cidade
cidade = st.text_input("Digite o nome da cidade:")

# 2. Botão de pesquisa
if st.button("Pesquisar"):
    if cidade:
        # 3. O Streamlit faz um pedido GET ao nosso FastAPI
        url_api = f"http://127.0.0.1:8000/clima/{cidade}"
        resposta = requests.get(url_api)

        # 4. Converte e mostra os dados
        dados = resposta.json()
        st.write(dados)
    else:
        st.warning("Por favor, digite o nome de uma cidade primeiro.")