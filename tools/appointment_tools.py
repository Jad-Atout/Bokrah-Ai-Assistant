from langchain_core.tools import tool
from models.appointment import (
    CreateAppointmentInput, UpdateAppointmentInput,
    CancelAppointmentInput, GetAvailableSlotsInput
)
from tools.api_client import post, patch


@tool(args_schema=CreateAppointmentInput)
def create_appointment(customer_id, slot, notes=None, recurrence=None, configurable=None):
    """Create a new appointment for a customer with optional notes and recurrence."""
    client_id = configurable.get("client_id")
    token = configurable.get("user_token")

    payload = {"customerId": customer_id, "notes": notes, "slot": slot.model_dump()}
    if recurrence:
        payload["recurrence"] = recurrence.model_dump()

    return post(f"/appointment/{client_id}", payload, token=token)


@tool(args_schema=UpdateAppointmentInput)
def update_appointment(appointment_id, slot, configurable=None):
    """Update an existing appointment's slot."""
    token = configurable.get("user_token")

    return patch(
        f"/appointment/{appointment_id}",
        {"appointmentId": appointment_id, "slot": slot.model_dump()},
        token=token
    )


@tool(args_schema=CancelAppointmentInput)
def cancel_appointment(appointment_id, configurable=None):
    """Cancel an existing appointment for the current client."""
    client_id = configurable.get("client_id")
    token = configurable.get("user_token")

    return patch(
        f"/appointment/{client_id}/cancel",
        {"appointmentId": appointment_id},
        token=token
    )


@tool(args_schema=GetAvailableSlotsInput)
def get_available_slots(start_date, end_date, staffServices, recurrence=None, configurable=None):
    """Retrieve available time slots between start_date and end_date for the given staff/services and optional recurrence."""
    client_id = configurable.get("client_id")
    token = configurable.get("user_token")

    payload = {
        "startDate": start_date,
        "endDate": end_date,
        "staffsServices": [s.model_dump() for s in staffServices] if staffServices else []
    }
    if recurrence:
        payload["recurrence"] = recurrence.model_dump()

    return post(f"/appointment/slots/{client_id}", payload, token=token)
