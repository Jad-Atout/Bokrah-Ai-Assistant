from typing import Annotated
from langchain_core.tools import tool, InjectedToolCallId
from langgraph.prebuilt import InjectedState
from langgraph.types import Command
from langgraph.graph import MessagesState


def create_handoff_tool(agent_name: str, description: str = None):
    name = f"transfer_to_{agent_name}"
    description = description or f"Transfer control to {agent_name}"

    @tool(name, description=description)
    def handoff_tool(
            state: Annotated[MessagesState, InjectedState],
            tool_call_id: Annotated[str, InjectedToolCallId],
    ) -> Command:
        tool_message = {
            "role": "tool",
            "content": f"Successfully transferred to {agent_name}",
            "name": name,
            "tool_call_id": tool_call_id,
        }
        return Command(
            goto=agent_name,
            update={**state, "messages": state["messages"] + [tool_message]},
            graph=Command.PARENT,
        )

    return handoff_tool


assign_to_create = create_handoff_tool(agent_name="create_appointment_assistant")
assign_to_update = create_handoff_tool(agent_name="update_appointment_assistant")
assign_to_cancel = create_handoff_tool(agent_name="cancel_appointment_assistant")
assign_to_reader = create_handoff_tool(agent_name="reader_assistant")
