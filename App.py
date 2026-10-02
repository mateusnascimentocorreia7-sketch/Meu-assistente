
import streamlit as st
from google import genai

st.title("Meu Assistente Gemini")

# Configura a chave de API ou usa o ambiente
api_key = st.text_input("Insere a tua API Key do Gemini", type="password")

if api_key:
    client = genai.Client(api_key=api_key)
    prompt = st.text_area("O que queres perguntar ao assistente?")
    
    if st.button("Enviar"):
        if prompt:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            st.write(response.text)
        else:
            st.warning("Escreve uma pergunta primeiro.")
else:
    st.info("Por favor, insere a tua API Key para começar.")
