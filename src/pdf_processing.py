from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from constants import constant

def get_pdf_text(pdf_docs):
    """
    Extracts text from multiple PDF documents and concatenates it into a single string.

    Args:
        pdf_docs (list): A list of paths to the PDF documents to be processed.

    Returns:
        str: The extracted text from all the PDF documents, concatenated together.
    """
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    """Splits a text into overlapping chunks using a recursive character-based approach.

    Args:
        text (str): The text to be split into chunks.

    Returns:
        list: A list of overlapping text chunks.
    """
    # Create a text splitter object with specified chunk size and overlap from the constants
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=constant.SPLITTER_CHUNK_SIZE, chunk_overlap=constant.SPLITTER_CHUNK_OVERLAP)
    return text_splitter.split_text(text)