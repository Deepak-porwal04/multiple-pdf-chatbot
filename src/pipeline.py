from src import embeddings, pdf_processing, vectorstore, question_answering
from constants import constant
def process_pdfs(pdf_docs):
    """
    Process PDF documents to extract text, create text chunks, and generate a vector store.

    Args:
        pdf_docs (list): A list of paths to PDF documents for processing.

    Returns:
        None
    """
    # Extract raw text from PDF documents
    raw_text = pdf_processing.extract_text_from_pdfs(pdf_docs)
    # Split the raw text into manageable chunks
    text_chunks = pdf_processing.split_text_into_chunks(raw_text)
    # Create and save a vector store using the processed text chunks
    embeddings.create_and_save_vector_store(text_chunks,vector_store_path=constant.FAISS_STORE_PATH)

def answer_user_question(user_question):
    """Retrieves relevant text snippets and generates an answer to a user's question.

    Args:
    user_question (str): The question to be answered.

    Returns:
    str: The generated answer to the question.
    """
    # Load the vector store containing document embeddings
    vector_store = vectorstore.load_and_initialize_vector_store(vector_store_path=constant.FAISS_STORE_PATH)
    # Search for relevant documents in the vector store based on the user's question
    docs = vectorstore.search_vector_store(vector_store, user_question)
    # Initialize the conversational chain for answering questions
    chain = question_answering.initialize_conversational_chain()
    # Generate a detailed answer using the conversational chain and relevant documents
    response = question_answering.generate_answer_from_conversational_chain(chain, docs, user_question)
    return response