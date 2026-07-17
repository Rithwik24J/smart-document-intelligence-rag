from pdf_loader import load_pdf
from text_splitter import split_documents
from embeddings import get_embedding_model
from vector_store import create_vector_store

from rag_pipeline import generate_answer
from llm import load_llm

import os
import streamlit as st

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Smart Document Intelligence",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📄 Smart Document Intelligence (RAG)")

st.markdown("""
### 🤖 AI-Powered Resume & Document Assistant

Upload one or more PDF documents and ask questions using Retrieval-Augmented Generation (RAG).

**Features**
- 📄 Upload multiple PDFs
- 🔍 Semantic Search
- 🤖 AI-powered Answers
- 📚 Source Citations
- 📊 Confidence Score
""")

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

with st.sidebar:

    st.header("📂 Upload Documents")

    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )
st.markdown("---")

st.info("""
### 🚀 Built With

• Streamlit

• LangChain

• FAISS

• HuggingFace

• Groq Llama 3.3
""")
# -------------------------------------------------
# Upload Folder
# -------------------------------------------------

UPLOAD_FOLDER = "uploaded_docs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -------------------------------------------------
# Process PDFs
# -------------------------------------------------

if uploaded_files:

    all_chunks = []

    for uploaded_file in uploaded_files:

        save_path = os.path.join(
            UPLOAD_FOLDER,
            uploaded_file.name
        )

        with open(save_path, "wb") as file:
            file.write(uploaded_file.getbuffer())

        documents = load_pdf(save_path)

        chunks = split_documents(documents)

        all_chunks.extend(chunks)

    embedding_model = get_embedding_model()

    vector_store = create_vector_store(
        all_chunks,
        embedding_model
    )

    llm = load_llm()

    # -----------------------------
    # Success Messages
    # -----------------------------

    st.success("✅ Documents Loaded Successfully!")
    st.success("✅ Vector Database Created!")
    st.markdown("---")
    # -----------------------------
    # Quick Actions
    # -----------------------------

    st.subheader("📄 Quick Actions")

    if st.button("📝 Generate Resume Summary"):

        with st.spinner("Generating Summary..."):

            result = generate_answer(
                "Summarize the uploaded resume in a professional way.",
                vector_store
            )

        st.success("✅ Summary Generated!")

        st.subheader("📄 Resume Summary")
        st.write(result["answer"])

    # -----------------------------
    # Preview Chunks
    # -----------------------------

    st.write(f"### Total Chunks: {len(all_chunks)}")

    with st.expander("Preview Chunks"):

        for i, chunk in enumerate(all_chunks):

            st.markdown(f"#### Chunk {i+1}")
            st.write(chunk.page_content)
            st.divider()

    st.divider()

    # -----------------------------
    # Ask Questions
    # -----------------------------

    st.header("💬 Ask Questions")

    question = st.text_input(
    "💬 Ask a Question",
    placeholder="Example: What skills does the candidate have?"
)

    if question:

        with st.spinner("Generating answer..."):

            result = generate_answer(
                question,
                vector_store
            )

        st.success("✅ Answer Generated!")

        st.subheader("🤖 AI Answer")
        st.write(result["answer"])
        st.metric(
        "Confidence Score",
        f'{result["confidence"]}%'
    )

        st.divider()

        st.subheader("📚 Retrieved Source Chunks")

        for i, doc in enumerate(result["sources"], start=1):

            with st.expander(f"📄 Source Chunk {i}"):

                 st.markdown(doc.page_content)
                 st.markdown("---")

st.caption(
    "Built using ❤️ Streamlit • LangChain • FAISS • HuggingFace • Groq"
)


