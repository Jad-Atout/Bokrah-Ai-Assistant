from pydantic import BaseModel,Field


class toBookAppointment(BaseModel):
    """Transfers work to a specialized assistant to handle appointment booking."""
    request: str = Field(description="User request or description of the appointment they want to book.")

    class Config:
        json_schema_extra = {
            "example": {
                "request": "I want to book a haircut and color session with Sam next week."
            }
        }


class toUpdateAppointment(BaseModel):
    """Transfers work to a specialized assistant to handle appointment updates."""
    request: str = Field(description="User intent or info about the appointment they want to change.")

    class Config:
        json_schema_extra = {
            "example": {
                "request": "Can I reschedule my facial appointment with Sarah to Friday?"
            }
        }


class toCancelAppointment(BaseModel):
    """Transfers work to a specialized assistant to handle appointment cancellation."""
    request: str = Field(description="What the user said about the appointment they want to cancel.")

    class Config:
        json_schema_extra = {
            "example": {
                "request": "Please cancel my massage appointment tomorrow."
            }
        }


class toReadData(BaseModel):
    """Transfers work to a specialized assistant to handle data reading or lookup requests."""
    request: str = Field(description="What the user is trying to check or view.")

    class Config:
        json_schema_extra = {
            "example": {
                "request": "Show me my appointments for this week."
            }
        }