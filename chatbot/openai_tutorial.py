import os
import streamlit as st

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
## for lansmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "openai_tutorial"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT")


## Prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

## Streamlit

st.title("Langchain Demo with OPENAI API")
input_text = st.text_input("Search the topic you want")

## openAI LLM

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

## chain
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
