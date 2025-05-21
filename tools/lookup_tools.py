from langchain_core.tools import tool
from tools.api_client import get


@tool
def get_user_appointments(configurable=None):
    """Fetch all appointments for the current authenticated user."""
    token = configurable.get("user_token")
    return get("/appointment", token=token)


@tool
def get_customer_appointments(customerId: str, configurable=None):
    """Fetch all appointments for a specific customer by their ID."""
    token = configurable.get("user_token")
    return get(f"/appointment/customer/{customerId}", token=token)


@tool
def get_staff_appointments(staffId: str, configurable=None):
    """Fetch all appointments assigned to a specific staff member by their ID."""
    token = configurable.get("user_token")
    return get(f"/appointment/staff/{staffId}", token=token)


@tool
def get_staff(configurable=None):
    """Retrieve the list of staff members for the current client."""
    client_id = configurable.get("client_id")
    token = configurable.get("user_token")
    return get(f"/staff/{client_id}", token=token)


@tool
def get_services(configurable=None):
    """Retrieve the list of available services for the current client."""
    client_id = configurable.get("client_id")
    token = configurable.get("user_token")
    return get(f"/service/{client_id}", token=token)


@tool
def get_customers(configurable=None):
    """Retrieve the list of all customers in the system."""
    token = configurable.get("user_token")
    return get("/customer", token=token)
