from dotenv import load_dotenv
from chain.agent_executor import create_agent_executor_chain, get_user_response
# from utils.embeddings import embeddings
# from utils.text_splitter import get_split_docs
# from loader.textloader import documents
from vectorstore.vectorstore import *

load_dotenv()

#Initilize an empty list for simulation of chat memory
conversation = []

#Initializing the Huggingface sentence - transformers embeddings
# embeddings = embeddings

# #Loading the documents from the text file
# documents = documents

# #splitting the documents
# docs = get_split_docs(documents)

# #Loading the documents into the vectorstore
# db = load_documents_into_vectorstore(
#     documents=docs, 
#     embeddings=embeddings,
#     dimensions=384
# )

# #Saving the vector store to local directory
# save_to_local(db=db, index_name="faiss-index")

#Create the agent executor chain
chain = create_agent_executor_chain('gpt-3.5-turbo-1106')

#Generate function to answer user queries
def generate(query: str):
    """Function to query the llm with the agent executor chain"""

    response = get_user_response(query=query, chain=chain, conversation=conversation)

    conversation.append({'input': query, 'output': response})

    return response

#loop for conversation
while True:
    user_prompt = input("Enter a prompt:(Type 'exit' to end the conversation): ")
    if user_prompt.strip().lower() == 'exit':
        conversation = []
        break

    generate(user_prompt)
    print("\n\n")
    
