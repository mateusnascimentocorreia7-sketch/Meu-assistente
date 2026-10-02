import google.generativeai as genai
import streamlit as st

st.title("Meu Assistente Gemini")

api_key = st.text_input("Insira sua chave da API do Gemini", type="password")

if api_key:
    client = genai.Client(api_key=api_key)
    prompt = st.text_area("O que quer perguntar?")
    
    if st.button("Enviar"):
        if prompt:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            st.write(response.text)
