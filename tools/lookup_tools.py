from langchain_core.tools import tool
from tools.api_client import get
from utils.config import CLIENT_ID


@tool
def get_user_appointments():
    return get("/appointment")


@tool
def get_customer_appointments(customerId: str):
    return get(f"/appointment/customer/{customerId}")


@tool
def get_staff_appointments(staffId: str):
    return get(f"/appointment/staff/{staffId}")


@tool
def get_staff():
    return get(f"/staff/{CLIENT_ID}")


@tool
def get_services():
    return get(f"/service/{CLIENT_ID}")


@tool
def get_customers():
    return get("/customer")
