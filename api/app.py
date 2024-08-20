import os
import uvicorn

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.llms.ollama import Ollama
from langserve import add_routes
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API on LangServe exploring LLM models"
)


openai_llm = ChatOpenAI(model="gpt-3.5-turbo")
prompt1 = ChatPromptTemplate.from_template("Write me an haiku about {topic} with 20 words")

llama_llm = Ollama(model="llama2")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} with 20 words ")

add_routes(
    app,
    prompt1|openai_llm,
    path="/haiku"
)

add_routes(
    app,
    prompt2|llama_llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)