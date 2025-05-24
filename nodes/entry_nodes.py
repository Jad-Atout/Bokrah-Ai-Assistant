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
                        f"You are now the {assistant_name}. You must complete the task using the available tools. "
                        "Do not mark the task as complete without using a tool. "
                        "If the user’s request changes or you're unsure what to do next, call CompleteOrEscalate. "
                        "Don’t explain your role — just start helping the user naturally."
                    ),
                    tool_call_id=tool_call_id,
                )
            ],
            "dialog_state": new_dialog_state,
        }

    return entry_node

