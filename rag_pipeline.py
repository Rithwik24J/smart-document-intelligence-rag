from langchain_core.prompts import PromptTemplate

from prompts import PROMPT_TEMPLATE
from llm import load_llm

# Load the LLM once
llm = load_llm()


def retrieve_chunks(question, vector_store):
    """
    Retrieve the top 5 most relevant chunks from the vector database.
    """
    results = vector_store.similarity_search_with_score(
        question,
        k=5
    )

    return results


def generate_answer(question, vector_store):
    """
    Retrieve relevant chunks and generate an answer using the LLM.
    """

    results = retrieve_chunks(
        question,
        vector_store
    )

    docs = [doc for doc, score in results]
    scores = [score for doc, score in results]

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = PromptTemplate.from_template(
        PROMPT_TEMPLATE
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    best_score = min(scores)

    confidence = round(
        (1 / (1 + best_score)) * 100
    )

    return {
        "answer": response.content,
        "sources": docs,
        "confidence": confidence
    }