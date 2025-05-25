from langgraph.prebuilt import create_react_agent
from prompts.reader_prompt import reader_prompt
from tools import get_customers, get_staff, get_services, get_available_slots, get_staff_appointments, \
    get_customer_appointments, get_user_appointments
from tools.complete_or_escalate import CompleteOrEscalate
from utils import llm, Assistant
from prompts.reader_prompt import reader_prompt

reader_tools = [
    get_customers,
    get_staff_appointments,
    get_customer_appointments,
    get_staff,
    get_services,
    get_available_slots,
    get_user_appointments,
    CompleteOrEscalate
]

reader_agent = create_react_agent(
    model=llm,
    tools=reader_tools,
    prompt=reader_prompt,
    name="reader_assistant"
)
