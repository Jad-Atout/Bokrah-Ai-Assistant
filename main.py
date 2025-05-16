from dotenv import load_dotenv
from graph.build_graph import graph
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

memory = MemorySaver()

if __name__ == "__main__":
    # Example event loop - replace with your preferred runtime
    state = {"messages": [], "dialog_state": []}
    result = graph.invoke(state)
    print(result)
