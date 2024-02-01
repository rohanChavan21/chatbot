from flask import Flask, request, jsonify
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate ,format_document
from utils.embeddings import embeddings

app = Flask(__name__)

db = FAISS.load_local("faiss-index", embeddings)

def similarity_search_from_vectorstore(query, k):
    """Retrieve documents from vectorstore by using similarity search"""

    documents = db.similarity_search_with_score(query=query, k=k+1)
    document_prompt = PromptTemplate.from_template("{page_content}")
    context = "\n".join(
        format_document(doc, document_prompt) for doc, _ in documents
    )

    return context


@app.route('/similarity_search', methods=['POST'])
def similarity_search():
    query = request.json.get('query', '')
    k = request.json.get('k', 4)
    n = k + 1
    context = similarity_search_from_vectorstore(query=query, k=k)
    response = {
        "query": query,
        "n": n,
        "context": context
    }
    print(f"Query to Vector DB: {query} \n Number of documents retrieved: {k}")

    return jsonify(response)

app.run(debug=True)