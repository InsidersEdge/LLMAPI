from dotenv import load_dotenv
load_dotenv() # load all env variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(prompt,image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text


st.set_page_config(page_title="Gemini Pro", page_icon="🔮")
st.header("Gemini Pro")
input = st.text_input("Input: ",key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)


submit = st.button("Ask the question")
if submit:
    response = get_gemini_response(input,image)
    st.write("Response: ", response)