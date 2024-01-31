from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, tool
from typing import Type, Optional
from vectorstore.vectorstore import similarity_search_from_vectorstore
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

class SearchInput(BaseModel):
    query: str = Field(description="query to lookup from the knowledge base and get context. should contain all the keywords to lookup in the knowledge base")
    num: int = Field(description="Number of entries to lookup. Consider one algo as one entry and determine requirement. Knoeledge base contains 6 total algos")

class VectorSimilaritySearchTool(BaseTool):
    name = "context_search"
    description = "use only when need to get context and to search about trading algorithms and look up information about Futures First"
    args_schema: Type[BaseModel] = SearchInput

    def _run(
            self, query: str, num: int, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool"""
        return similarity_search_from_vectorstore(query=query, k=num)
    
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