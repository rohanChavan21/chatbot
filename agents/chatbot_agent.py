from langchain.agents import create_openai_functions_agent
from models.chat_model import initialize_chat_model
from tools.vector_similarity_search import get_vector_search_tool
from prompts.agent_tool_prompt import get_agent_prompt

def initialize_agent(model_name):
    """Initialize Langchain Agent"""

    #Load the chat-model
    llm = initialize_chat_model(
        model_name=model_name
    )
    #Load the vector search tool
    tool  = get_vector_search_tool()

    #Fetch the custom agent prompt
    prompt = get_agent_prompt()

    #Create an OpenAI Functions agent with custom tools
    agent = create_openai_functions_agent(
        llm=llm, 
        tools=[tool], 
        prompt=prompt
    )

    return agent