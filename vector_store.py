from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, embedding_model):

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    vector_store.save_local("vector_db")

    return vector_store

from langchain_community.vectorstores import FAISS


def load_vector_store(embedding_model):

    return FAISS.load_local(
        "vector_db",
        embedding_model,
        allow_dangerous_deserialization=True
    )
