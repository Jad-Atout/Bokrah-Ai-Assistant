from langgraph.checkpoint.memory import InMemorySaver

from agents import cancel_appointment_agent, create_appointment_agent, reader_agent, update_appointment_agent
from prompts.primary_prompt import supervisor_agent_prompt
from tools import assign_to_create, assign_to_update, assign_to_cancel, assign_to_reader
from utils import llm
from langgraph_supervisor import create_supervisor
checkpointer = InMemorySaver()
supervisor_agent = create_supervisor(
    model=llm,
    agents=[cancel_appointment_agent,create_appointment_agent,reader_agent,update_appointment_agent],
    tools=[assign_to_create, assign_to_update, assign_to_cancel, assign_to_reader],
    prompt=supervisor_agent_prompt,
    include_agent_name="inline",
    output_mode="last_message",
    add_handoff_back_messages=True,

)
