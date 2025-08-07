import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load .env (includes LANGCHAIN_API_KEY and tracing setup)
load_dotenv()

# Initialize TinyLlama via Ollama
llm = ChatOllama(model="tinyllama")

# Prompt template (no memory)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}")
])

# Chain prompt → model → output parser
chain = prompt | llm | StrOutputParser()

print("🤖 TinyLlama Chatbot is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    try:
        response = chain.invoke({"input": user_input})
        print("Bot:", response)

    except Exception as e:
        print("⚠️ Error:", e)
