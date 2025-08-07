from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Simple Chatbot API",
    description="A simple API for interacting with the TinyLlama chatbot using LangChain and Ollama.",
    version="1.0.0"
)




llm1 = ChatOllama(model="tinyllama")
gemini = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)



prompt1 = ChatPromptTemplate.from_template(
    "You are a helpful assitant prompt : {topic}."
)
prompt2 = ChatPromptTemplate.from_template(
    "You are a helpful assistant prompt : {topic}."
)



add_routes(
    app,
    prompt1 | llm1,
    path="/ollama"
)

add_routes(
    app,
    prompt2 | gemini,
    path="/gemini"
)



if __name__ == "__main__":
    uvicorn.run(app,host="localhost", port=8000, log_level="info")