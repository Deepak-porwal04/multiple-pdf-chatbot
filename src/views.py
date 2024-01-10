import streamlit as st
from src import pipeline

def create_app_ui():
    """
    Create a Streamlit user interface for chatting with multiple PDFs using Gemini Pro.

    The interface allows users to upload PDF files, submit and process them, and ask questions about the content.

    Returns:
        None
    """
    st.set_page_config("Chat with multiple PDFs")
    st.header("Chat with PDFs using Gemini Pro")

    with st.sidebar:
        st.title("Menu")
        pdf_docs = st.file_uploader("Upload your PDF files and click on the submit and process button", accept_multiple_files=True)

        if st.button("Submit and Process"):
            with st.spinner("Processing..."):
                pipeline.process_pdfs(pdf_docs)  # Call the process_pdfs function directly
                st.success("Done")

    user_question = st.text_input("Ask the query from the uploaded PDFs")
    if user_question:
        response = pipeline.answer_user_question(user_question)
        st.write("Reply: ", response)