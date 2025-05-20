from prompts.cancel_prompt import cancel_appointment_prompt
from tools import get_user_appointments, cancel_appointment
from tools.complete_or_escalate import CompleteOrEscalate
from utils import llm, Assistant

cancel_appointment_safe_tools = [get_user_appointments]
cancel_appointment_sensitive_tools = [cancel_appointment]
cancel_appointment_tools = cancel_appointment_sensitive_tools + cancel_appointment_safe_tools
cancel_appointment_runnable = cancel_appointment_prompt | llm.bind_tools(
    cancel_appointment_tools + [CompleteOrEscalate]
)
cancel_appointment_assistant = Assistant(cancel_appointment_runnable)