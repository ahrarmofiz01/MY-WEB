from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Project ke docs folder ka path
DOCS_DIR = Path(__file__).parent / "docs"


def load_documents():
    documents = []

    # docs folder ke andar .txt files read karo
    for file_path in DOCS_DIR.glob("*.txt"):

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        documents.append({
            "title": file_path.name,
            "content": content
        })

    return documents


def retrieve_context(query, top_k=2):

    # Documents load karo
    documents = load_documents()

    if not documents:
        return ""

    # Document content ki list
    document_texts = [
        document["content"]
        for document in documents
    ]

    # Query ko documents ke saath combine karo
    all_texts = document_texts + [query]

    # Text ko numerical vectors mein convert karo
    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform(all_texts)

    # Query vector
    query_vector = vectors[-1]

    # Document vectors
    document_vectors = vectors[:-1]

    # Query aur documents ki similarity calculate karo
    similarities = cosine_similarity(
        query_vector,
        document_vectors
    ).flatten()

    # Highest similarity wale documents ke indexes
    top_indexes = similarities.argsort()[::-1][:top_k]

    retrieved_context = ""

    for index in top_indexes:

        score = similarities[index]

        # Agar similarity zero hai to document relevant nahi hai
        if score <= 0:
            continue

        document = documents[index]

        retrieved_context += (
            f"\nSource: {document['title']}\n"
            f"Similarity: {score:.2f}\n"
            f"{document['content']}\n"
        )

    return retrieved_context
