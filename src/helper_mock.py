import PyPDF2
import io
import os

from dotenv import load_dotenv
from openai import OpenAI
import openai
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai.api_key

client = OpenAI(api_key=openai.api_key)


def extract_text_from_pdf(uploaded_file):
    """
    extracts teh text from a pdf file

    args:
        pdf path (str): the path to the pdf file

    return:
        str: the extracted text
    """
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text
    

def ask_openai(prompt, max_tokens=500):
    """
    sends a prompt to openai and returns the response

    args:
        prompt (str): the prompt to send to openai
        model (str): the model to use

    return:
        str: the response from openai
    """
    # Mock response for testing - replace with real API call when quota is available
    if "summarize" in prompt.lower():
        return "Mock Summary: Experienced software developer with skills in Python, JavaScript, and cloud technologies. Strong background in web development and data analysis."
    elif "missing skills" in prompt.lower() or "skill gaps" in prompt.lower():
        return "Mock Skills Gap: Consider learning Docker, Kubernetes, and advanced machine learning frameworks like TensorFlow."
    elif "roadmap" in prompt.lower() or "future roadmap" in prompt.lower():
        return "Mock Roadmap: 1. Complete cloud certifications 2. Build portfolio projects 3. Contribute to open source 4. Network with industry professionals."
    elif "job titles" in prompt.lower():
        return "Mock Keywords: Senior Software Engineer, Backend Developer, Cloud Solutions Architect, DevOps Engineer, Technical Lead"
    else:
        return "Mock response for testing purposes."