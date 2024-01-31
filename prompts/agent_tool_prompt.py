from langchain import hub

prompt = hub.pull("hwchase17/openai-functions-agent")

prompt.messages[0].prompt.template = """You are a respectful and honest AI assistant called FFGenius. You have been made to help the traders at Futures First answer their queries about anything.
Always answer as truthfully as possible. Don't make up any false information. If you don't know the answer to a question just say so."""

def get_agent_prompt():
    """Get the prompt for the agent"""
    return prompt