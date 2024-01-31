from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)

def get_split_docs(documents):
    """Used to chunk the documents"""
    return text_splitter.split_documents(documents=documents)