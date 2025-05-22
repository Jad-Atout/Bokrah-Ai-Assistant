from langchain_core.tools import tool
from tools.api_client import get
from utils.auth import extract_auth


@tool
def get_user_appointments(config: dict = None):
    """Fetch all appointments for the current authenticated user."""
    _, token = extract_auth(config)
    return get("/appointment", token=token)


@tool
def get_customer_appointments(customerId: str, config: dict = None):
    """Fetch all appointments for a specific customer by their ID."""
    _, token = extract_auth(config)
    return get(f"/appointment/customer/{customerId}", token=token)


@tool
def get_staff_appointments(staffId: str, config: dict = None):
    """Fetch all appointments assigned to a specific staff member by their ID."""
    _, token = extract_auth(config)
    return get(f"/appointment/staff/{staffId}", token=token)


@tool
def get_staff(config: dict = None):
    """Retrieve the list of staff members for the current client."""
    client_id, token = extract_auth(config)
    return get(f"/staff/{client_id}", token=token)


@tool
def get_services(config: dict = None):
    """Retrieve the list of available services for the current client."""
    client_id, token = extract_auth(config)
    return get(f"/service/{client_id}", token=token)


@tool
def get_customers(config: dict = None):
    """Retrieve the list of all customers in the system."""
    _, token = extract_auth(config)
    return get("/customer", token=token)
