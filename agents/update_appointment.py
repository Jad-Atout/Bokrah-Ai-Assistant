from prompts.update_prompt import update_appointment_prompt
from tools import (
    get_user_appointments,
    get_staff,
    get_customers,
    get_services,
    get_available_slots,
    update_appointment
)
from tools.complete_or_escalate import CompleteOrEscalate
from utils import llm
from langgraph.prebuilt import create_react_agent

update_appointment_tools = [
    get_user_appointments,
    get_staff,
    get_customers,
    get_services,
    get_available_slots,
    update_appointment,
    CompleteOrEscalate
]

update_appointment_agent = create_react_agent(
    model=llm,
    tools=update_appointment_tools,
    prompt=update_appointment_prompt,
    name="update_appointment_assistant"
)
