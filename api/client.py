import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/haiku/invoke",
                             json={"input": {"topic": input_text}})
    
    return response.json()["output"]["content"]

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={"input": {"topic": input_text}})
    
    return response.json()["output"]

### Streamlit framework

st.title("LangChain Demo with OpenAI and LLAMA2 API")
input_text_haiku = st.text_input("Write a haiku on")
input_text_poem = st.text_input("Write a poem on")

if input_text_haiku:
    st.write(get_openai_response(input_text_haiku))

if input_text_poem:
    st.write(get_ollama_response(input_text_poem))