from langgraph.graph.message import RemoveMessage


def trim_agent_state(state):
    messages = state["messages"]
    if len(messages) > 10:
        trimmed = [
            {"role": "system", "content": "Earlier messages trimmed for token efficiency."},
            *messages[-8:]
        ]
        return {
            "messages": [RemoveMessage(id="REMOVE_ALL_MESSAGES"), *trimmed]
        }
    return {}
