from dotenv import load_dotenv
load_dotenv() # load all env variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# FUNCTION to load gemini pro model and get responses

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_title="Gemini Pro", page_icon="🔮")
st.header("Gemini Pro")
input = st.text_input("Input: ",key="input")
submit = st.button("Ask the question")

#when submit is clicked

if submit:
    response = get_gemini_response(input)
    st.write("Response: ", response)