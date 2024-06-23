from dotenv import load_dotenv
import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai

# Initialize

import os
import PyPDF2
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model =  genai.GenerativeModel('gemini-pro')

def get_gemini_response(input):
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text

input_prompt="""
As an experienced ATS (Applicant Tracking System), proficient in the technical domain encopassing Software Engineering,
Data Science,Data Analysis,Big Data Engineering ,Web Developer,Mobile App Developer,DevOps Engineer , Machine Learning engineer, Cybersecurityanalyst,Cloud Solutions Architect,Database Administrator , Network ENgineer, AI Engineer , Systems Analyst,Full Stack Developer
UI/UX Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess
resumes agaisnt provided job descriptios. In a fiercely competitive job market , your expertise is crucial in offering top-notch guidance fro resume enhancement. Assign precise matching percentages based on the JD (Job Description) and meticuluoslyidentify any missing keywords with utmost accuracy.
resume:{text}
description:{jd}

I want the response in the following structure:
The first line indicates the percentage match with the job description (JD).
The second line presents a list of missing keywords.
The third section provides a profile summary.

Mention the tittle for all three sections.
while genrating the response put some space to separate all the three sections.

"""

st.set_page_config(page_title= "Resume ATS Tracker" , layout="wide")

avs.add_vertical_space(4)

col1, col2 = st.columns([3,2])
with col1:
    st.title("CareerCraft")
    st.header("Navigate the Job Market with Confidence!")
    st.markdown("""<p style-'text-align! justify;'>
                Introducing Careercraft, an ATS-optimized Resume analyzer - your ultimate solution for optimizing
                job applications and accelerating career growth. Our innovative platform leverages advanced ATS
                technology to provide job seekers with valuable insights into their resumes' compatibiltiy with 
                job descriptions. From resume optimization adm skill enhancement to career progression guidance,
                CareeerCraft empowers users to stand out in today's competitive job market. Streamline your job
                application progress, enhance your skills, amd navigate your  career path with confidence. Join
                CareerCraft today and unlock new opportunities for professional successs!
                </p>""" , unsafe_allow_html=True)
    
with col2:
    st.image("Images\Screenshot 2024-06-23 230719.png", use_column_width=True)
    
avs.add_vertical_space(10)

col1,col2 = st.columns([3 , 2])
with col2:
    st.header("Wide Range of Offerings")
    st.write('ATS-Optimized Resume Analysis')
    st.write('Resume Optimization')
    st.write('Skill Enhancement')
    st.write('Career Progression Guidance')
    st.write('Tailored Profile Summaries')
    st.write('Streamlined Application Process')
    st.write('Personal Recommenadations')
    st.write('Efficient Career Navigation')
with col1:
    img1 = Image.open("Images\Screenshot 2024-06-23 230346.png")
    st.image(img1, use_column_width=True)

avs.add_vertical_space(10)

col1, col2 = st.columns([3,2])
with col1:
    st.markdown("<h1 style='text-align: center;'>Embark on your Career Adventure</h>", unsafe_allow_html=True)
    jd=st.text_area("Paste the job Description")
    uploaded_file = st.file_uploader("Upload Your Resume",type="pdf",help="Please upload the pdf")

    submit = st.button("Submit")

    if submit:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response= get_gemini_response(input_prompt)
            st.subheader(response)

with col2:
    img2 = Image.open("Images\Screenshot 2024-06-23 230326.png")
    st.image(img2, use_column_width=True)

avs.add_vertical_space(10)



col1,col2 = st.columns([2,3])
with col2:
    st.markdown("<h1 style='text-align: center;'>FAQ</h1>", unsafe_allow_html=True)
    st.write("Questions: How does CareerCraft analyze resumes and job descriptions?")
    st.write("""Answer: CareerCraft uses advanced algorithms to anlalyze resumes and job description,
             identifying key keywords and asssessing compstibility betweeen the two.""")
    
    avs.add_vertical_space(3)

    st.write("Questions: Can CareerCraft suggest improvements for my resume?")
    st.write("""Answer: Yes,CareerCraft provides personalized recommendations to optimize your resume for specific job openings,
              including suggestions for missing keywords and alignmentswuth desired job roles.""")
    
    avs.add_vertical_space(3)

    st.write("Questions: Is CareerCraft suitable for both entry-level and experienced professionals?")
    st.write("""Answer: Absolutely! CareerCraft caters to to job seekers at all stages, offering tailored insights and 
             guidance to enhance theier resumeand advance their careers.""")
    
with col1:
    img3 = Image.open("Images\Screenshot 2024-06-23 230304.png")
    st.image(img3, use_column_width=True)



    