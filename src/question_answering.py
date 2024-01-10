from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

def initialize_conversational_chain():
    """
    Initialize a conversational chain for answering questions based on provided context and question.

    Returns:
        QAChain: A conversational chain for generating detailed answers to questions.
    """
    # Template for constructing the prompt

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.2)
    
    # Create a PromptTemplate with the specified template and input variables
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type='stuff', prompt=prompt)
    return chain

def generate_answer_from_conversational_chain(conversational_chain, documents, user_question):
    """
    Generate a detailed answer to a user's question using a conversational chain.

    Args:
        conversational_chain (QAChain): The conversational chain for generating answers.
        documents (list): A list of documents to provide context for answering the question.
        user_question (str): The user's question.

    Returns:
        str: The generated answer to the user's question.
    """
    response = conversational_chain(
        {"input_documents": documents, "question": user_question},
        return_only_outputs=True
    )
    return response["output_text"]
