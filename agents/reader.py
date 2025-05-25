from langgraph.prebuilt import create_react_agent
from tools import (
    get_customers,
    get_staff_appointments,
    get_customer_appointments,
    get_staff,
    get_services,
    get_available_slots,
    get_user_appointments,
    return_to_supervisor
)
from utils import llm, trim_agent_state
from prompts.reader_prompt import reader_prompt

reader_tools = [
    get_customers,
    get_staff_appointments,
    get_customer_appointments,
    get_staff,
    get_services,
    get_available_slots,
    get_user_appointments,
    return_to_supervisor
]

reader_agent = create_react_agent(
    model=llm,
    tools=reader_tools,
    prompt=reader_prompt,
    name="reader_assistant",
    pre_model_hook=trim_agent_state,
)
