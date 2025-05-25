from langgraph.prebuilt import create_react_agent
from tools import (
    get_customers,
    get_staff,
    get_services,
    get_available_slots,
    create_appointment,
    return_to_supervisor
)
from prompts.create_prompt import create_appointment_prompt
from utils import llm, trim_agent_state

create_appointment_tools = [
    get_customers,
    get_staff,
    get_services,
    get_available_slots,
    create_appointment,
    return_to_supervisor
]

create_appointment_agent = create_react_agent(
    model=llm,
    tools=create_appointment_tools,
    prompt=create_appointment_prompt,
    name="create_appointment_assistant",
    pre_model_hook=trim_agent_state,
)
