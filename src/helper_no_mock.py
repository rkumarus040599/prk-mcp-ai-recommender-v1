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
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt},
        ],
        temperature=0.5,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content