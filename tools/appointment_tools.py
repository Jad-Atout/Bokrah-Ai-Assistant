from typing import Annotated, Optional, List
from langchain_core.tools import tool
from models.appointment import (
    CreateAppointmentInput, UpdateAppointmentInput,
    CancelAppointmentInput, GetAvailableSlotsInput,
    AppointmentSlot, RecurrenceState, ServiceAssignment
)
from tools.api_client import post, patch
from utils.config import CLIENT_ID


@tool(args_schema=CreateAppointmentInput)
def create_appointment(
    customer_id: Annotated[str, "Unique customer ID"],
    slot: Annotated[AppointmentSlot, "Appointment slot object with start/end times and sub-slots"],
    notes: Annotated[Optional[str], "Optional notes for the appointment"] = None,
    recurrence: Annotated[Optional[RecurrenceState], "Optional recurrence pattern"] = None
):
    """Create a new appointment for a customer.

    Accepts a time slot, optional recurrence settings, and notes.
    """
    payload = {"customerId": customer_id, "notes": notes, "slot": slot.model_dump()}
    if recurrence:
        payload["recurrence"] = recurrence.model_dump()
    return post(f"/appointment/{CLIENT_ID}", payload)


@tool(args_schema=UpdateAppointmentInput)
def update_appointment(
    appointment_id: Annotated[str, "The ID of the appointment to update"],
    slot: Annotated[AppointmentSlot, "New slot details including start and end time"]
):
    """Update an existing appointment's scheduled slot."""
    return patch(f"/appointment/{appointment_id}", {
        "appointmentId": appointment_id,
        "slot": slot.model_dump()
    })


@tool(args_schema=CancelAppointmentInput)
def cancel_appointment(
    appointment_id: Annotated[str, "The ID of the appointment to cancel"]
):
    """Cancel an existing appointment for the current client."""
    return patch(f"/appointment/{CLIENT_ID}/cancel", {
        "appointmentId": appointment_id
    })


@tool(args_schema=GetAvailableSlotsInput)
def get_available_slots(
    start_date: Annotated[str, "Start date in YYYY-MM-DD format"],
    end_date: Annotated[str, "End date in YYYY-MM-DD format"],
    staffServices: Annotated[List[ServiceAssignment], "List of staff-service assignments"],
    recurrence: Annotated[Optional[RecurrenceState], "Optional recurrence settings"] = None
):
    """Retrieve available appointment slots between a date range.

    Includes optional recurrence and required staff-service mappings.
    """
    payload = {
        "startDate": start_date,
        "endDate": end_date,
        "staffsServices": [s.model_dump() for s in staffServices] if staffServices else []
    }
    if recurrence:
        payload["recurrence"] = recurrence.model_dump()
    return post(f"/appointment/slots/{CLIENT_ID}", payload)
