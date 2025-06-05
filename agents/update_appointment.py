from prompts.update_prompt import update_appointment_prompt
from tools import (
    get_staff,
    get_customers,
    get_available_slots,
    update_appointment,
    return_to_supervisor, get_user_booked_appointments
)
from utils import llm, trim_agent_state
from langgraph.prebuilt import create_react_agent

update_appointment_tools = [
    get_user_booked_appointments,
    get_staff,
    get_customers,
    get_available_slots,
    update_appointment,
    return_to_supervisor
]

update_appointment_agent = create_react_agent(
    model=llm,
    tools=update_appointment_tools,
    prompt=update_appointment_prompt,
    name="update_appointment_assistant",
    pre_model_hook=trim_agent_state,
)
