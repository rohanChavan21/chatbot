from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, tool
from typing import Type, Optional
import requests, json
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

class SearchInput(BaseModel):
    query: str = Field(description="query to retrieve context from the knowledge base. should contain all the keywords to lookup in the knowledge base")
    num: int = Field(description="Number of entries to lookup. Consider one algo as one entry and determine requirement. Knowledge base contains 6 total algos. Avoid fetching all documents unless absolutely needed.")

class VectorSimilaritySearchTool(BaseTool):
    name = "context_search"
    description = "use when need to get context and to search about trading algorithms and parameters and look up information about Futures First. Don't use conversation history is sufficient enough."
    args_schema: Type[BaseModel] = SearchInput

    def _run(
            self, 
            query: str, 
            num: int, 
            run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool"""
        # return similarity_search_from_vectorstore(query=query, k=num)
        url = 'http://localhost:5000/similarity_search'
        payload = {'query': query, 'k': num}
        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, data=json.dumps(payload), headers=headers)
        final_response = response.json()
        print(f"Query to Vector DB: {final_response['query']} \n Number of documents retrieved: {final_response['n']}")
        if response.status_code == 200:
            return final_response["context"]
        else:
            print(f"Error: {response.status_code}")
            return "Cannot Fetch documents."
    
    async def _arun(
        self,
        a: int,
        b: int,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("Calculator does not support async")


def get_vector_search_tool():
    tool = VectorSimilaritySearchTool()
    return tool