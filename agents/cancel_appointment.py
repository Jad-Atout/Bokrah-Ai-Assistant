
from langgraph.prebuilt import create_react_agent
from prompts.cancel_prompt import cancel_appointment_prompt
from tools import get_staff_appointments, get_customer_appointments, get_user_appointments, cancel_appointment
from tools.complete_or_escalate import CompleteOrEscalate
from utils import llm

cancel_appointment_tools = [
    get_staff_appointments,
    get_customer_appointments,
    get_user_appointments,
    cancel_appointment,
    CompleteOrEscalate
]

cancel_appointment_agent = create_react_agent(
    model=llm,
    tools=cancel_appointment_tools,
    prompt=cancel_appointment_prompt,
    name="cancel_appointment_assistant"
)
