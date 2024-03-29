from langchain_openai import ChatOpenAI
from callbacks.streaming_callback import callbacks

def initialize_chat_model(model_name):
    """Initialize the OpenAI Chat Model with input model"""
    chat_model = ChatOpenAI(
        model=model_name,
        temperature=0,
        max_tokens=512,
        verbose=True,
        streaming=True,
        callbacks=callbacks
    )

    return chat_model