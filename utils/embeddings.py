from langchain.embeddings.huggingface import HuggingFaceEmbeddings

sentence_transformers_model = 'sentence-transformers/all-MiniLM-L6-v2'

#Using the huggingfaceembeddings to initialize the sentence-transformer model
embeddings = HuggingFaceEmbeddings(
    model_name=sentence_transformers_model
)