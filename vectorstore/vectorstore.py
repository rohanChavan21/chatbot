from langchain.vectorstores import FAISS
from langchain.vectorstores.utils import DistanceStrategy
from utils.embeddings import embeddings
from langchain_core.prompts import PromptTemplate ,format_document
from langchain_community.docstore.in_memory import InMemoryDocstore
import faiss

index = ''

def initialize_vectorstore(embeddings, dimensions:int):
    """Initialize the FAISS Vectorstore"""
    db = FAISS(
        distance_strategy=DistanceStrategy.COSINE,
        index = faiss.IndexFlatIP(dimensions),
        embedding_function=embeddings,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={}
    )
    return db


def load_documents_into_vectorstore(documents, embeddings, dimensions):
    """Loading the chunked documents into the vectorstore"""
    db = initialize_vectorstore(embeddings=embeddings, dimensions=dimensions)
    db = db.from_documents(documents, embeddings)

    return db

def save_to_local(db, index_name):
    """Save the vectorstore index to local directory"""
    db.save_local(index_name)
    index = index_name

    return f"Vectorstore saved successfully at {index_name}"

def load_from_local(index_name, embeddings):
    """load vectorstore from local index file with matching index name"""
    db = FAISS.load_local(index_name, embeddings)
    index = index_name

    return db

def similarity_search_from_vectorstore(query, k):
    """Retrieve documents from vectorstore by using similarity search"""
    db = load_from_local(index_name="faiss-index", embeddings=embeddings)
    documents = db.similarity_search_with_score(query=query, k=k+1)
    print(f"Query to Vector DB: {query} \n Number of documents retrieved: {k}")
    document_prompt = PromptTemplate.from_template("{page_content}")
    context = "\n".join(
        format_document(doc, document_prompt) for doc, _ in documents
    )

    return context
