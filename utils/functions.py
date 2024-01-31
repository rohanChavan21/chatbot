from langchain_core.messages import AIMessage, HumanMessage

def get_conversation_history(conversation):
    conversation_history = conversation[-5:] if len(conversation) >= 5 else conversation
    history = []
    for conv in conversation_history:
        history.append(HumanMessage(content=conv['input']))
        history.append(AIMessage(content=conv['output']))
    
    return history
