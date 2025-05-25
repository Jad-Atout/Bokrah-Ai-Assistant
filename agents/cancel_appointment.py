from langgraph.prebuilt import create_react_agent
from prompts.cancel_prompt import cancel_appointment_prompt
from tools import (
    get_staff_appointments,
    get_customer_appointments,
    get_user_appointments,
    cancel_appointment,
    return_to_supervisor
)
from utils import llm
from utils.state_management import trim_agent_state


cancel_appointment_tools = [
    get_staff_appointments,
    get_customer_appointments,
    get_user_appointments,
    cancel_appointment,
    return_to_supervisor
]

cancel_appointment_agent = create_react_agent(
    name="cancel_appointment_assistant",
    model=llm,
    tools=cancel_appointment_tools,
    prompt=cancel_appointment_prompt,
    pre_model_hook=trim_agent_state,
)
