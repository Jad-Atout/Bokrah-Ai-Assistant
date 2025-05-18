from typing import Optional, List
from pydantic import BaseModel, Field
from .common import SlotSubBlock, RecurrenceState, ServiceAssignment


class AppointmentSlot(BaseModel):
    startTime: str = Field(
        description="Start time of the appointment slot in ISO8601 format, e.g. '2025-06-01T09:00:00Z'"
    )
    endTime: str = Field(
        description="End time of the appointment slot in ISO8601 format, e.g. '2025-06-01T10:30:00Z'"
    )
    subSlots: List[SlotSubBlock] = Field(
        description="List of sub-slots with staff-service assignments"
    )


class CreateAppointmentInput(BaseModel):
    customer_id: str = Field(
        description="Customer ID making the booking, e.g. '67d195dd3017f30d8042b03b'"
    )
    recurrence: Optional[RecurrenceState] = Field(
        default=None,
        description="Optional recurrence settings for the appointment, e.g. {'type': 'weekly', 'count': 4, 'interval': 1}"
    )
    notes: Optional[str] = Field(
        default=None,
        description="Notes about the booking, e.g. 'First-time visit'"
    )
    slot: AppointmentSlot = Field(
        description="Appointment slot information including timing and staff-service mapping"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "customer_id": "67d195dd3017f30d8042b03b",
                "notes": "First-time visit"
            }
        }


class GetAvailableSlotsInput(BaseModel):
    start_date: str = Field(
        description="Start date of the range in ISO format (YYYY-MM-DD), e.g. '2025-05-13'"
    )
    end_date: str = Field(
        description="End date of the range in ISO format (YYYY-MM-DD), e.g. '2025-05-20'"
    )
    recurrence: Optional[RecurrenceState] = Field(
        default=None,
        description="Optional recurrence configuration for the search"
    )
    staffServices: List[ServiceAssignment] = Field(
        description="List of staff-service assignments to check availability for"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "start_date": "2025-05-13",
                "end_date": "2025-05-20"
            }
        }


class UpdateAppointmentInput(BaseModel):
    appointment_id: str = Field(
        description="Appointment ID to be updated, e.g. '681d2887c7a45634a15bb659'"
    )
    slot: AppointmentSlot = Field(
        description="Updated slot for the appointment"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "appointment_id": "681d2887c7a45634a15bb659"
            }
        }


class CancelAppointmentInput(BaseModel):
    appointment_id: str = Field(
        description="Appointment ID to be cancelled, e.g. '681d2887c7a45634a15bb659'"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "appointment_id": "681d2887c7a45634a15bb659"
            }
        }
