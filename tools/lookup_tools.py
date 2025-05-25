from typing import Annotated
from pydantic import BaseModel
from langchain_core.tools import tool
from tools.api_client import get
from utils.config import CLIENT_ID


@tool("get_user_appointments")
def get_user_appointments():
    """Fetch all appointments for the currently authenticated user."""
    return get("/appointment")


class CustomerAppointmentsInput(BaseModel):
    customerId: Annotated[str, "Customer ID to retrieve appointments for."]


@tool("get_customer_appointments",args_schema=CustomerAppointmentsInput)
def get_customer_appointments(customerId: str):
    """Fetch all appointments for a specific customer using their customer ID."""
    return get(f"/appointment/customer/{customerId}")


class StaffAppointmentsInput(BaseModel):
    staffId: Annotated[str, "Staff ID to retrieve appointments for."]


@tool("get_staff_appointments",args_schema=StaffAppointmentsInput)
def get_staff_appointments(staffId: str):
    """Fetch all appointments for a specific staff member using their staff ID."""
    return get(f"/appointment/staff/{staffId}")


@tool("get_staff")
def get_staff():
    """Retrieve all staff members registered under the current client."""
    return get(f"/staff/{CLIENT_ID}")


@tool("get_services")
def get_services():
    """Retrieve all services offered by the current client."""
    return get(f"/service/{CLIENT_ID}")


@tool("get_customers")
def get_customers():
    """Retrieve all customers in the system."""
    return get(f"/customer")
