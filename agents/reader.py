from prompts.reader_prompt import reader_prompt
from tools import get_customers, get_staff, get_services, get_available_slots
from tools.complete_or_escalate import CompleteOrEscalate
from utils import llm, Assistant

reader_safe_tools = [get_customers, get_staff, get_services, get_available_slots]
reader_runnable = reader_prompt | llm.bind_tools(
    reader_safe_tools + [CompleteOrEscalate]
)

reader_assistant = Assistant(reader_runnable)