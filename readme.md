# Resume ATS using LLM

This project is a Resume Applicant Tracking System (ATS) that uses Large Language Models (LLM) to analyze and match resumes against job descriptions. The system is built with Streamlit for the front end and integrates with the Google Gemini-1.5-pro-latest 

## Features

- Upload resumes in PDF format
- Match resumes with job descriptions
- Display match percentage and highlight missing qualifications
- Simple drag-and-drop interface

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- I personally used python 3.12.2


### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Bikram9035/Gemini_pro_Resume_ATS.git
   cd Resume ats

2. python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    or conda create -p venv python==3.12.2 -y
    followed by - conda activate venv/

3. pip install -r requirements.txt

4. please refer to the screenshot for file structure

5. create your own .env file and add your  API_KEY=your_api_key_here   (get your own api key by signing up on https://ai.google.dev/ 
                                                                            followed by copying it from  https://aistudio.google.com/)

6. run the main file >>> streamlit run app.py

7. Open your web browser and go to http://localhost:8501.


Support:
If you like this project, please consider giving it a ⭐ on GitHub. It helps others discover the project and keeps me motivated to make further improvements.