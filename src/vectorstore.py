from langchain.vectorstores import faiss
from src.embeddings import get_genai_embeddings

def load_and_initialize_vector_store(vector_store_path):
    """
    Load and initialize a vector store from a local file using FAISS with embeddings.

    Args:
        vector_store_path (str): The path to the local vector store file.

    Returns:
        vector_sore: An instance of FAISS representing the loaded vector store.
    """
    
    return faiss.FAISS.load_local(vector_store_path,embeddings=get_genai_embeddings())

def search_vector_store(vector_store, query):
    """
    Retrieves documents most relevant to a query from a FAISS vector store.

    Args:
        vector_store (faiss.FAISS): A loaded FAISS vector store.
        query (str): The query text to search for relevant documents.

    Returns:
        list: A list of the most relevant documents, ranked by similarity.
    """
    return vector_store.similarity_search(query) 