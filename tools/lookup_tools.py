from typing import Annotated

from langchain_core.tools import tool
from tools.api_client import get
from utils.config import CLIENT_ID


@tool
def get_user_appointments():
    """Fetch all appointments for the current authenticated user.

     Returns:
        List of appointment objects.
     """
    return get("/appointment")


@tool
def get_customer_appointments(
        customerId: Annotated[
            str, "Customer ID whose appointments are to be fetched, e.g. '67d195dd3017f30d8042b03b'"]):
    """Fetch all appointments for a specific customer by their ID.

    Args:
        customerId: Unique identifier of the customer.

    Returns:
        List of appointment objects for the specified customer.
    """
    return get(f"/appointment/customer/{customerId}")


@tool
def get_staff_appointments(
        staffId: Annotated[str, "Staff ID whose appointments are to be fetched, e.g. '67d195dd3017f30d8042b03b'"]
):
    """Fetch all appointments assigned to a specific staff member by their ID.

    Args:
        staffId: Unique identifier of the staff member.

    Returns:
        List of appointments assigned to the staff member.
    """
    return get(f"/appointment/staff/{staffId}")


@tool
def get_staff():
    """Retrieve the list of staff members for the current client.

    Returns:
        List of staff profiles available for the client.
    """
    return get(f"/staff/{CLIENT_ID}")


@tool
def get_services():
    """Retrieve the list of available services for the current client.

    Returns:
        List of service offerings defined for the client.
    """
    return get(f"/service/{CLIENT_ID}")


@tool
def get_customers():
    """Retrieve the list of all customers in the system.

    Returns:
        List of customer profiles.
    """
    return get(f"/customer")
