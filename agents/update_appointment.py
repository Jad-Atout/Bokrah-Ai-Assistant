from prompts.update_prompt import update_appointment_prompt
from tools import get_user_appointments, get_staff, get_customers, get_services, get_available_slots, update_appointment
from tools.complete_or_escalate import CompleteOrEscalate
from utils import llm, Assistant

update_appointment_safe_tools = [get_user_appointments, get_staff, get_customers, get_services, get_available_slots]
update_appointment_sensitive_tools = [update_appointment]
update_appointment_tools = update_appointment_sensitive_tools + update_appointment_safe_tools
update_appointment_runnable = update_appointment_prompt | llm.bind_tools(
    update_appointment_tools + [CompleteOrEscalate]
)
update_appointment_assistant = Assistant(update_appointment_runnable)