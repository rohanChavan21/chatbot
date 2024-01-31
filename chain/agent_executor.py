from langchain.agents import AgentExecutor
from callbacks.streaming_callback import callbacks
from utils.functions import get_conversation_history
from agents.chatbot_agent import initialize_agent
from tools.vector_similarity_search import get_vector_search_tool

def create_agent_executor_chain(model_name: str):
    """Create the Agent Executor Chain"""
    agent = initialize_agent(model_name=model_name)
    vector_search_tool = get_vector_search_tool()
    agent_executor = AgentExecutor(
        agent=agent,
        tools=[vector_search_tool],
        # verbose=True,
        max_iterations=5,
        max_execution_time=20.0,
        callbacks=callbacks
    )

    return agent_executor

def get_user_response(query: str, chain, conversation):
    """Querying the llm chatbot"""

    result = chain.invoke({
        "chat_history":get_conversation_history(conversation=conversation),
        "input": query
    })
    return result['output']
    