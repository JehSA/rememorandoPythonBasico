import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
modelo_ia = OpenAI(api_key=OPEN_AI_API_KEY)

st.write("# Estudo de Chatbot com IA")

if not "lista_mensagens" in st.session_state:
    #st.session_state.lista_mensagens = []
    '''st.session_state.lista_mensagens = [
        {"role": "system", "content": "Você é um assistente útil, mas não exagere nas respostas. Seja breve e objetivo."}
    ]'''


texto_usuario = st.chat_input("Digite sua mensagem aqui...")
#arquivo = st.file_uploader("Envie um arquivo para análise")
#arquivo = st.file_uploader("Envie um arquivo para análise").type("text/csv")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    menssagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state.lista_mensagens.append(menssagem_usuario)

    resposta_ia = modelo_ia.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state.lista_mensagens
    )
    print(resposta_ia.choices[0].message.content)

    texto_resposta_ia = resposta_ia.choices[0].message.content
    st.chat_message("assistant").write(texto_resposta_ia)
    menssagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state.lista_mensagens.append(menssagem_ia)

print(st.session_state["lista_mensagens"])
#print(st.session_state.lista_mensagens)