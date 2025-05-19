from typing import Annotated, Literal
from typing_extensions import TypedDict
from utils.dialog_reducer import update_dialog_stack
from langgraph.graph.message import AnyMessage, add_messages


class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    dialog_state: Annotated[
        list[
            Literal[
                "primary_assistant",
                "create_appointment",
                "cancel_appointment",
                "update_appointment",
                "read_data",
            ]
        ],
        update_dialog_stack,
    ]
    summery: str
