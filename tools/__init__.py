# tools/__init__.py
# -----------------
# Group all tool entrypoints under one namespace.
from .api_client import get, post, patch
from .appointment_tools import (
    create_appointment,
    update_appointment,
    cancel_appointment,
    get_available_slots,
)
from .lookup_tools import (
    get_user_appointments,
    get_customer_appointments,
    get_staff_appointments,
    get_staff,
    get_services,
    get_customers,
)

__all__ = [
    "get", "post", "patch",
    "create_appointment",
    "update_appointment",
    "cancel_appointment",
    "get_available_slots",
    "get_user_appointments",
    "get_customer_appointments",
    "get_staff_appointments",
    "get_staff",
    "get_services",
    "get_customers",
]
