from langchain.vectorstores import faiss
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from configuration import config
from constants import constant

def get_genai_embeddings():
    """
    Initializes a Google Generative AI Embeddings object.

    Handles API key loading and model configuration for text embedding tasks.

    Returns:
        GoogleGenerativeAIEmbeddings: An instance of GoogleGenerativeAIEmbeddings for generating embeddings.

    Raises:
        RuntimeError: If API key loading fails.
    """
    try:
        config.load_api_key()
    except Exception as e:
        raise RuntimeError("Failed to load API key: {}".format(e))
    
    embeddings = GoogleGenerativeAIEmbeddings(model=constant.GOOGLE_EMBEDDINGS_MODEL)
    return embeddings

def create_and_save_vector_store(text_chunks,vector_store_path):
    """
    Create a vector store using embeddings generated from text chunks and save it locally.

    Args:
        text_chunks (list): A list of text chunks to generate embeddings and create the vector store.

        vector_store_path (str): Path to save the vector store store

    Returns:
        None
    """
    embeddings = get_genai_embeddings()
    vector_store = faiss.FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local(vector_store_path)