from langchain_core.tools import tool
from langgraph.config import get_config
from tools.api_client import get


@tool
def get_user_appointments():
    """Fetch all appointments for the current authenticated user."""
    token = get_config()["configurable"].get("x-user-token")
    return get("/appointment", token=token)


@tool
def get_customer_appointments(customerId: str):
    """Fetch all appointments for a specific customer by their ID."""
    token = get_config()["configurable"].get("x-user-token")
    return get(f"/appointment/customer/{customerId}", token=token)


@tool
def get_staff_appointments(staffId: str):
    """Fetch all appointments assigned to a specific staff member by their ID."""
    token = get_config()["configurable"].get("x-user-token")
    return get(f"/appointment/staff/{staffId}", token=token)


@tool
def get_staff():
    """Retrieve the list of staff members for the current client."""
    client_id = get_config()["configurable"].get("x-client-id")
    token = get_config()["configurable"].get("x-user-token")
    return get(f"/staff/{client_id}", token=token)


@tool
def get_services():
    """Retrieve the list of available services for the current client."""
    client_id = get_config()["configurable"].get("x-client-id")
    token = get_config()["configurable"].get("x-user-token")
    return get(f"/service/{client_id}", token=token)


@tool
def get_customers():
    """Retrieve the list of all customers in the system."""
    token = get_config()["configurable"].get("x-user-token")
    return get("/customer", token=token)
