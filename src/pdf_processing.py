from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from constants import constant

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=constant.SPLITTER_CHUNK_SIZE, chunk_overlap=constant.SPLITTER_CHUNK_OVERLAP)
    return text_splitter.split_text(text)