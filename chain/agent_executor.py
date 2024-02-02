import os
from langchain.agents import AgentExecutor
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import UpstashRedisChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
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

    chain = RunnableWithMessageHistory(
        agent_executor,
        lambda session_id: UpstashRedisChatMessageHistory(
            session_id=session_id,
            url='https://eu2-simple-giraffe-31332.upstash.io',
            token=os.environ.get('UPSTASH_TOKEN'),
        ),
        input_messages_key='input',
        history_messages_key='chat_history'
    )


    return chain

def get_user_response(query: str, chain, config):
    """Querying the llm chatbot"""

    result = chain.invoke({
        "input": query,
    }, config=config)
    return result['output']
    