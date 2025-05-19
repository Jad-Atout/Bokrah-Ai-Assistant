from prompts.primary_prompt import primary_assistant_prompt
from tools.primary_assistant_tools import toCancelAppointment, toReadData, toUpdateAppointment, toBookAppointment
from utils import llm, Assistant

primary_assistant_runnable = primary_assistant_prompt | llm.bind_tools([
    toCancelAppointment,
    toReadData,
    toUpdateAppointment,
    toBookAppointment,
])
primary_assistant = Assistant(primary_assistant_runnable)