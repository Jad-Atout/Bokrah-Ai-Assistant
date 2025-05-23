from langchain_core.tools import tool
from langgraph.config import get_config
from models.appointment import (
    CreateAppointmentInput, UpdateAppointmentInput,
    CancelAppointmentInput, GetAvailableSlotsInput
)
from tools.api_client import post, patch


@tool(args_schema=CreateAppointmentInput)
def create_appointment(customer_id, slot, notes=None, recurrence=None):
    """Create a new appointment for a customer with optional notes and recurrence."""
    client_id = get_config()["configurable"].get("x-client-id")
    token = get_config()["configurable"].get("x-user-token")
    payload = {"customerId": customer_id, "notes": notes, "slot": slot.model_dump()}
    if recurrence:
        payload["recurrence"] = recurrence.model_dump()
    return post(f"/appointment/{client_id}", payload, token=token)


@tool(args_schema=UpdateAppointmentInput)
def update_appointment(appointment_id, slot):
    """Update an existing appointment's slot."""
    token = get_config()["configurable"].get("x-user-token")
    return patch(
        f"/appointment/{appointment_id}",
        {"appointmentId": appointment_id, "slot": slot.model_dump()},
        token=token
    )


@tool(args_schema=CancelAppointmentInput)
def cancel_appointment(appointment_id):
    """Cancel an existing appointment for the current client."""
    client_id = get_config()["configurable"].get("x-client-id")
    token = get_config()["configurable"].get("x-user-token")
    return patch(
        f"/appointment/{client_id}/cancel",
        {"appointmentId": appointment_id},
        token=token
    )


@tool(args_schema=GetAvailableSlotsInput)
def get_available_slots(start_date, end_date, staffServices, recurrence=None):
    """Retrieve available time slots between start_date and end_date for the given staff/services and optional
    recurrence."""
    client_id = get_config()["configurable"].get("x-client-id")
    token = get_config()["configurable"].get("x-user-token")
    payload = {
        "startDate": start_date,
        "endDate": end_date,
        "staffsServices": [s.model_dump() for s in staffServices] if staffServices else []
    }
    if recurrence:
        payload["recurrence"] = recurrence.model_dump()
    return post(f"/appointment/slots/{client_id}", payload, token=token)
