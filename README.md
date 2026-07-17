# 📄 Smart Document Intelligence (RAG)

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask natural language questions. The application retrieves relevant document chunks using semantic search and generates context-aware answers using an LLM.

---

## 🚀 Features

- Upload one or multiple PDF documents
- AI-powered Question Answering
- Resume Summary Generator
- Semantic Search using FAISS
- Source Chunk Visualization
- Confidence Score for Answers
- Clean Streamlit Interface

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI / LLM
- LangChain
- Groq (Llama 3.3)

### Vector Database
- FAISS

### Embeddings
- HuggingFace Sentence Transformers

### PDF Processing
- PyPDF

---

## 📂 Project Structure

```
smart-document-rag/
│
├── app.py
├── llm.py
├── rag_pipeline.py
├── pdf_loader.py
├── embeddings.py
├── vector_store.py
├── text_splitter.py
├── prompts.py
├── utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Rithwik24J/smart-document-intelligence-rag.git
```

Move into the project

```bash
cd smart-document-intelligence-rag
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a .env file

```env
GROQ_API_KEY=your_api_key_here
```

Run

```bash
streamlit run app.py
```

---

## 💡 How it Works

1. Upload PDF
2. Extract Text
3. Split into Chunks
4. Generate Embeddings
5. Store in FAISS
6. Retrieve Relevant Chunks
7. Send Context to LLM
8. Generate Answer
9. Display Source Chunks

---

## 📸 Screenshots

Coming Soon

---

## 🔮 Future Improvements

- Chat History
- Multiple LLM Support
- OCR Support
- PDF Highlighting
- User Authentication
- Cloud Vector Database
- Dark/Light Theme

---

## 👨‍💻 Author

**Rithwik**

GitHub

https://github.com/Rithwik24J

---
