from langchain_core.tools import tool
from models.appointment import (
    CreateAppointmentInput, UpdateAppointmentInput,
    CancelAppointmentInput, GetAvailableSlotsInput
)
from tools.api_client import post, patch
from utils.config import CLIENT_ID


@tool(args_schema=CreateAppointmentInput)
def create_appointment(customer_id, slot,notes=None, recurrence=None):
    payload = {"customerId": customer_id, "notes": notes, "slot": slot.model_dump()}
    if recurrence:
        payload["recurrence"] = recurrence.model_dump()
    return post(f"/appointment/{CLIENT_ID}", payload)


@tool(args_schema=UpdateAppointmentInput)
def update_appointment(appointment_id, slot):
    return patch(f"/appointment/{appointment_id}", {"appointmentId": appointment_id, "slot": slot.model_dump()})


@tool(args_schema=CancelAppointmentInput)
def cancel_appointment(appointment_id):
    return patch(f"/appointment/{CLIENT_ID}/cancel", {"appointmentId": appointment_id})


@tool(args_schema=GetAvailableSlotsInput)
def get_available_slots(start_date, end_date, staffServices, recurrence=None):
    payload = {
        "startDate": start_date,
        "endDate": end_date,
        "staffsServices": [s.model_dump() for s in staffServices] if staffServices else []
    }
    if recurrence:
        payload["recurrence"] = recurrence.model_dump()
    return post(f"/appointment/slots/{CLIENT_ID}", payload)
