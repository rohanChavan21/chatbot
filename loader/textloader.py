from langchain_community.document_loaders import TextLoader

#Load the knowledge base from text file
loader = TextLoader('data/algos.txt')
documents = loader.load()