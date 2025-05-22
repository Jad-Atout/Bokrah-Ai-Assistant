from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph,END,START
from agents import create_appointment_assistant, update_appointment_assistant, cancel_appointment_assistant, \
    reader_assistant, primary_assistant
from agents.cancel_appointment import cancel_appointment_sensitive_tools, cancel_appointment_safe_tools
from agents.create_appointment import create_appointment_sensitive_tools, create_appointment_safe_tools
from agents.reader import reader_safe_tools
from agents.update_appointment import update_appointment_sensitive_tools, update_appointment_safe_tools
from graph.routes import route_create_appointment, route_update_appointment, route_cancel_appointment, route_read_data, \
    route_primary_assistant
from models import State
from nodes import create_entry_node, create_tool_node_with_fallback, pop_dialog_state

load_dotenv()

builder = StateGraph(State)

builder.add_node("leave_skill", pop_dialog_state)
builder.add_edge("leave_skill", "primary_assistant")

builder.add_node("enter_create_appointment", create_entry_node("Book Appointment Assistent", "create_appointment"))
builder.add_node("create_appointment_assistant", create_appointment_assistant)

builder.add_node("create_appointment_sensitive_tools",              create_tool_node_with_fallback(create_appointment_sensitive_tools))
builder.add_node("create_appointment_safe_tools",
                 create_tool_node_with_fallback(create_appointment_safe_tools))

builder.add_edge("enter_create_appointment","create_appointment_assistant")
builder.add_edge("create_appointment_sensitive_tools", "create_appointment_assistant")

builder.add_edge("create_appointment_safe_tools", "create_appointment_assistant")
builder.add_conditional_edges("create_appointment_assistant", route_create_appointment, [
    "create_appointment_sensitive_tools",
    "create_appointment_safe_tools",
    "leave_skill",
    END
])


builder.add_node("enter_update_appointment", create_entry_node("Update Appointment Assistent", "update_appointment"))
builder.add_node("update_appointment_assistant", update_appointment_assistant)

builder.add_node("update_appointment_sensitive_tools",
                 create_tool_node_with_fallback(update_appointment_sensitive_tools))
builder.add_node("update_appointment_safe_tools", create_tool_node_with_fallback(update_appointment_safe_tools))

builder.add_edge("enter_update_appointment", "update_appointment_assistant")
builder.add_edge("update_appointment_sensitive_tools", "update_appointment_assistant")

builder.add_edge("update_appointment_safe_tools", "update_appointment_assistant")
builder.add_conditional_edges(
    "update_appointment_assistant",
    route_update_appointment,
    ["update_appointment_sensitive_tools", "update_appointment_safe_tools", "leave_skill",END])


builder.add_node("enter_cancel_appointment", create_entry_node("Cancel Appointment Assistent", "cancel_appointment"))
builder.add_node("cancel_appointment_assistant", cancel_appointment_assistant)

builder.add_node("cancel_appointment_sensitive_tools",
                 create_tool_node_with_fallback(cancel_appointment_sensitive_tools)
                 )
builder.add_node("cancel_appointment_safe_tools",
                 create_tool_node_with_fallback(cancel_appointment_safe_tools)
                 )


builder.add_edge("enter_cancel_appointment", "cancel_appointment_assistant")
builder.add_edge("cancel_appointment_sensitive_tools", "cancel_appointment_assistant")
builder.add_edge("cancel_appointment_safe_tools", "cancel_appointment_assistant")
builder.add_conditional_edges("cancel_appointment_assistant", route_cancel_appointment,
                              ["cancel_appointment_safe_tools",
                               "cancel_appointment_sensitive_tools",
                               "leave_skill",
                               END])

builder.add_node("enter_reader", create_entry_node("Reader Assistant", "reader_assistant"))
builder.add_node("reader_assistant", reader_assistant)
builder.add_node("reader_tools", create_tool_node_with_fallback(reader_safe_tools))


builder.add_edge("enter_reader", "reader_assistant")
builder.add_edge("reader_tools", "reader_assistant")
builder.add_conditional_edges("reader_assistant", route_read_data, ["reader_tools", "leave_skill", END])

builder.add_node("primary_assistant", primary_assistant)
builder.add_edge(START, "primary_assistant")

#builder.add_node("summarize_conversation", RunnableLambda(summarize_conversation))

builder.add_conditional_edges(
    "primary_assistant",
    route_primary_assistant,
    [
        "enter_create_appointment",
        "enter_cancel_appointment",
        "enter_update_appointment",
        "enter_reader",
        END,
    ],
)

memory = MemorySaver()
graph = builder.compile(
    checkpointer=memory,
    interrupt_before=[
        "create_appointment_sensitive_tools",
        "update_appointment_sensitive_tools",
        "cancel_appointment_sensitive_tools",
    ],
)