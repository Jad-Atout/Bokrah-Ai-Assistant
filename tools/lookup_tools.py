from langchain_core.tools import tool
from tools.api_client import get
from utils.config import CLIENT_ID


@tool
def get_user_appointments():
    """Fetch all appointments for the current authenticated user."""
    return get("/appointment")


@tool
def get_customer_appointments(customerId: str):
    """Fetch all appointments for a specific customer by their ID."""
    return get(f"/appointment/customer/{customerId}")


@tool
def get_staff_appointments(staffId: str):
    """Fetch all appointments assigned to a specific staff member by their ID."""
    return get(f"/appointment/staff/{staffId}")


@tool
def get_staff():
    """Retrieve the list of staff members for the current client."""
    return get(f"/staff/{CLIENT_ID}")


@tool
def get_services():
    """Retrieve the list of available services for the current client."""
    return get(f"/service/{CLIENT_ID}")


@tool
def get_customers():
    """Retrieve the list of all customers in the system."""
    return get("/customer")