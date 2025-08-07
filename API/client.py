import requests
import streamlit as st

def get_tinyllama_response(prompt):
    response = requests.post(
        "http://localhost:8000/ollama/invoke",
        json={"input": {'topic':prompt}}
    )
    return response.json()['output']

def get_gemini_response(prompt):
    response = requests.post(
        "http://localhost:8000/gemini/invoke",
        json={"input": {'topic':prompt}}
    )
    return response.json()['output']['content']

st.title("TinyLlama Chatbot")
input_text = st.text_input("Enter a prompt for TinyLlama:")

st.title("Gemini Chatbot")
input_text1 = st.text_input("Enter a prompt for Gemini:")

if input_text:
    st.write(get_tinyllama_response(input_text))

if input_text1:
    st.write(get_gemini_response(input_text1))