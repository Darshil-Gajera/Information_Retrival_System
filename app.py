import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.chunker import chunk_text
from utils.qa_engine import ask_question

st.title("PDF Q&A Chatbot")

# Upload PDF
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    chunks = chunk_text(text)
    st.session_state['chunks'] = chunks
    st.success("PDF processed!")

# Ask question
question = st.text_input("Ask a question")
if st.button("Get Answer") and question:
    if 'chunks' not in st.session_state:
        st.warning("Upload a PDF first!")
    else:
        # Combine top chunks as context (simple version)
        context = " ".join(st.session_state['chunks'][:5])
        answer = ask_question(question, context)
        st.write("Answer:", answer)