from typing import Annotated
from langchain_core.tools import InjectedToolCallId, tool
from langgraph.graph import MessagesState
from langgraph.prebuilt import InjectedState
from langgraph.types import Command
from models import SupervisorRequest


@tool("return_to_supervisor", description="Return control to the supervisor for clarification, task delegation or "
                                          "getting user input",args_schema=SupervisorRequest)
def return_to_supervisor(
    request: SupervisorRequest,
    state: Annotated[MessagesState, InjectedState],
    tool_call_id: Annotated[str, InjectedToolCallId],
) -> Command:
    tool_message = {
        "role": "tool",
        "content": f"Agent requests supervisor intervention: {request.reason}",
        "name": "return_to_supervisor",
        "tool_call_id": tool_call_id,
    }
    return Command(
        goto="supervisor",
        update={**state, "messages": state["messages"] + [tool_message]},
        graph=Command.PARENT,
    )
