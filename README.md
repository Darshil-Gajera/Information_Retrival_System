# PDF Q&A Chatbot

A simple **Generative AI-powered PDF Question & Answer Chatbot** using the Gemini API. Users can upload PDF files and ask questions; the chatbot answers based on the PDF content.

---

## Features

- Upload a PDF document
- Extract text from PDF
- Chunk the text for context-aware answering
- Use Gemini API to answer questions based on PDF content
- Optional: Semantic search using embeddings (SentenceTransformer + FAISS)
- Supports multiple PDFs (stretch goal)

---

## Project Structure

pdf_qa_chatbot/<br>
├─ app.py &nbsp;&nbsp;&nbsp;# Main Streamlit app<br>
├─ requirements.txt &nbsp;&nbsp;&nbsp;# Python dependencies<br>
├─ .env &nbsp;&nbsp;&nbsp;# Store GEMINI_API_KEY (not shared)<br>
├─ pdfs/ &nbsp;&nbsp;&nbsp;# Uploaded PDFs (optional storage)<br>
├─ embeddings/ &nbsp;&nbsp;&nbsp;# Optional: store vector embeddings<br>
├─ utils/<br>
│&nbsp;&nbsp;&nbsp;├─ pdf_parser.py &nbsp;&nbsp;&nbsp;# PDF text extraction<br>
│&nbsp;&nbsp;&nbsp;├─ chunker.py &nbsp;&nbsp;&nbsp;# Text chunking logic<br>
│&nbsp;&nbsp;&nbsp;└─ qa_engine.py &nbsp;&nbsp;&nbsp;# Gemini API question-answer functions


---

## Setup & Installation

```bash
# Clone
git clone https://github.com/<your-username>/Information_Retrival_System.git
cd Information_Retrival_System

# Create virtual environment (Windows / Linux / macOS)
python -m venv venv

# Activate venv
# Windows (PowerShell):
.\venv\Scripts\Activate
# (If you see “execution policy” error, run as admin and set execution policy)
# Linux / macOS:
source venv/bin/activate

# Upgrade pip & install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple


