import requests
import streamlit as st

def get_tinyllama_response(prompt):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={"input": {'topic':prompt}}
    )
    return response.json()['output']

st.title("TinyLlama Chatbot")
input_text = st.text_input("Enter a topic for the essay:")

if input_text:
    st.write(get_tinyllama_response(input_text))