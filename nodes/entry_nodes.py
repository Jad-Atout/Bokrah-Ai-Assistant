from typing import Callable

from langchain_core.messages import ToolMessage

from models import State


def create_entry_node(assistant_name: str, new_dialog_state: str) -> Callable:
    def entry_node(state: State) -> dict:
        tool_call_id = state["messages"][-1].tool_calls[0]["id"]
        return {
            "messages": [
                ToolMessage(
                    content=(
                        f"You are now the {assistant_name}. Help the user using the tools provided. "
                        "The task is not complete until the tool is called. "
                        "If the user changes their mind or needs something else, call CompleteOrEscalate. "
                        "Do not mention your role—just act."
                    ),
                    tool_call_id=tool_call_id,
                )
            ],
            "dialog_state": new_dialog_state,
        }

    return entry_node
