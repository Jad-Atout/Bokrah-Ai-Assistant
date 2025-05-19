from prompts.create_prompt import create_appointment_prompt
from tools import get_customers, get_staff, get_services, get_available_slots, create_appointment
from tools.control_flow import CompleteOrEscalate
from utils import llm, Assistant

create_appointment_safe_tools = [get_customers, get_staff, get_services, get_available_slots]
create_appointment_sensitive_tools = [create_appointment]
create_appointment_tools = create_appointment_sensitive_tools + create_appointment_safe_tools
create_appointment_runnable = create_appointment_prompt | llm.bind_tools(
    create_appointment_tools + [CompleteOrEscalate]
)

create_appointment_assistant = Assistant(create_appointment_runnable)