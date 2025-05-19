from langchain_core.runnables import Runnable, RunnableConfig
from langchain_openai import ChatOpenAI

from models import State


class Assistant:
    def __init__(self, runnable: Runnable):
        self.runnable = runnable

    def __call__(self, state: State, config: RunnableConfig):
        result = self.runnable.invoke(state)
        return {"messages": result}


llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
