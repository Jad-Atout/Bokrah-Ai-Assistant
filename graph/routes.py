from langgraph.constants import END
from langgraph.prebuilt import tools_condition

from agents.create_appointment import create_appointment_safe_tools
from agents.update_appointment import update_appointment_safe_tools
from agents.cancel_appointment import cancel_appointment_safe_tools
from tools.complete_or_escalate import CompleteOrEscalate
from tools.primary_assistant_tools import (
    toBookAppointment,
    toCancelAppointment,
    toUpdateAppointment,
    toReadData,
)
from models import State


def _make_tool_router(safe_tools, safe_node, sensitive_node):
    safe_names = [t.name for t in safe_tools]

    def _route(state: State):
        route = tools_condition(state)
        if route == END:
            return END

        calls = state["messages"][-1].tool_calls
        if any(tc["name"] == CompleteOrEscalate.__name__ for tc in calls):
            return "leave_skill"
        if all(tc["name"] in safe_names for tc in calls):
            return safe_node
        return sensitive_node

    return _route


route_create_appointment = _make_tool_router(
    create_appointment_safe_tools,
    safe_node="create_appointment_safe_tools",
    sensitive_node="create_appointment_sensitive_tools",
)

route_update_appointment = _make_tool_router(
    update_appointment_safe_tools,
    safe_node="update_appointment_safe_tools",
    sensitive_node="update_appointment_sensitive_tools",
)

route_cancel_appointment = _make_tool_router(
    cancel_appointment_safe_tools,
    safe_node="cancel_appointment_safe_tools",
    sensitive_node="cancel_appointment_sensitive_tools",
)


def route_read_data(state: State):
    route = tools_condition(state)
    if route == END:
        return END
    calls = state["messages"][-1].tool_calls
    if any(tc["name"] == CompleteOrEscalate.__name__ for tc in calls):
        return "leave_skill"
    return "reader_tools"


_primary_map = {
    toBookAppointment.__name__: "enter_create_appointment",
    toCancelAppointment.__name__: "enter_cancel_appointment",
    toUpdateAppointment.__name__: "enter_update_appointment",
    toReadData.__name__: "enter_reader",
}


def route_primary_assistant(state: State):
    route = tools_condition(state)
    if route == END:
        return END

    calls = state["messages"][-1].tool_calls
    if calls:
        next_node = _primary_map.get(calls[0]["name"])
        if next_node:
            return next_node

    raise ValueError(f"Invalid route: {calls!r}")
