import streamlit as st
import os
import PyPDF2 as pdf
import google.generativeai as genai
from dotenv import load_dotenv

#load the api key from env file
load_dotenv(".env")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#extract text from mutiple pdf pages of resume input

def pdf_to_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text=""
    for page in reader.pages:                               #(len(reader.pages)):
                                                             #page=reader.pages[page]
        text+=str(page.extract_text())

    return text


#prompt template used to format the pdf resume and jd in a way that LLM can understand, also define how we want our llm to respond

input_prompt="""
hey act like very experienced ats(apllication tracking system)
with a deep understanding of tech field, software engineering, data science , data analyst and big data enginner. your task is to evaluate the resume based on the given job description and you must consider the job market is very competative and you should provide vbest assistance for improving the resumes. assign the precentage matching based on JD and 
the missing keywords with high accuracy.

resume:{text}
description:{jd}

i want the %match, whether candidate is fit for the role or not , missing skills
in tabular format and profile summary separately as a paragraph

"""

#select the llm model which will be taking the prompt

def get_gemini_response(input):
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    response = model.generate_content(input)

    return response.text

#streamlit ui to display the contents

st.title("Resume ATS System")
st.text("Improve your ATS score")
uploaded_file =st.file_uploader("Upload your Resume",type="pdf",help="please upload the pdf")
jd = st.text_area("Paste Job Description of target company from Linkdin")


#submit buttom

submit =st.button("submit")

if submit:
    if uploaded_file is not None:
        text = pdf_to_text(uploaded_file)
        formatted_input = input_prompt.format(text=text , jd=jd)
        response =get_gemini_response(formatted_input)
        st.subheader(response)












