from dotenv import load_dotenv
from chain.agent_executor import create_agent_executor_chain, get_user_response
from vectorstore.vectorstore import *
# from utils.embeddings import embeddings
# from utils.text_splitter import get_split_docs
# from loader.textloader import documents

load_dotenv()

#Initilize an empty list for simulation of chat memory
# conversation = []

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
config = {
    "configurable": {
        "session_id": "demo",
    }
}

chain = create_agent_executor_chain('gpt-3.5-turbo-1106')

#Generate function to answer user queries
def generate(query: str, config):
    """Function to query the llm with the agent executor chain"""
    response = get_user_response(
        query=query, 
        chain=chain, 
        config=config
    )

    # conversation.append({'input': query, 'output': response})

    return response

#loop for conversation
while True:
    user_prompt = input("Enter a prompt:(Type 'exit' to end the conversation): ")
    if user_prompt.strip().lower() == 'exit':
        break

    generate(user_prompt, config=config)
    print("\n\n")
    
