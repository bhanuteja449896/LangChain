from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="TinyLlama Chatbot API",
    description="A simple API for interacting with the TinyLlama chatbot using LangChain and Ollama.",
    version="1.0.0"
)

llm1 = ChatOllama(model="tinyllama")

add_routes(
    app,
    llm1,
    path="/tinyllama"
)

llm = Ollama(model = "tinyllama")
prompt1 = ChatPromptTemplate.from_template(
    "Write a essay about {topic} with a 100 words"
)

add_routes(
    app,
    prompt1 | llm,
    path="/essay"
)

if __name__ == "__main__":
    uvicorn.run(app,host="localhost", port=8000, log_level="info")